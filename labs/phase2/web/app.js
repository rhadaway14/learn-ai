"use strict";

const $ = (selector) => document.querySelector(selector);
const samplePhase1 = {
  schema_version: "1.0",
  project_id: "phase1-model-investigation",
  attempt_number: 1,
  completed_at: "2026-09-18T00:00:00.000Z",
  answers: {},
  evidence: {},
  evaluation: { passed: true, score: 9, total: 9 },
};
let latestRun = null;
let latestArtifact = null;
let failureObserved = false;

function setFeedback(selector, message, ok) {
  const target = $(selector);
  target.textContent = message;
  target.className = `feedback ${ok ? "ok" : "error"}`;
}

function completeStep(number) {
  const item = document.querySelector(`[data-step="${number}"]`);
  document.querySelectorAll("[data-step]").forEach((step) => step.classList.remove("current"));
  item.classList.add("complete");
  const next = document.querySelector(`[data-step="${number + 1}"]`);
  if (next) next.classList.add("current");
}

function evidence(id, text) {
  const target = $(id);
  target.textContent = text;
  target.className = "complete";
}

async function request(path, options = {}) {
  const response = await fetch(path, {
    ...options,
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
  });
  const body = await response.json().catch(() => ({}));
  if (!response.ok) {
    const detail = typeof body.detail === "string" ? body.detail : body.detail?.failure_signal || "Request failed";
    throw new Error(detail);
  }
  return body;
}

async function checkStack() {
  try {
    const [health, status] = await Promise.all([request("/health"), request("/api/phase2/status")]);
    $("#apiStatus").textContent = "connected";
    $("#apiStatus").className = "status ok";
    $("#apiHealth").textContent = health.status === "ok" ? "Ready" : "Unavailable";
    $("#dbHealth").textContent = "Ready";
    setFeedback("#stackFeedback", "Web, API, and database boundaries are responding.", true);
    completeStep(1);
    if (status.phase1_imported) {
      evidence("#evidencePhase1", status.phase1_evidence_id);
      completeStep(2);
    }
    if (status.current_model) {
      completeStep(3);
      showRun(status.current_model);
    }
    if (status.failure_observed) evidence("#evidenceFailure", "Explosive run failed closed");
    if (status.recovered_after_failure) completeStep(5);
    if (status.prediction_made) {
      evidence("#evidenceUse", "New project scored");
      completeStep(6);
    }
  } catch (error) {
    $("#apiStatus").textContent = "unavailable";
    $("#apiStatus").className = "status error";
    $("#apiHealth").textContent = "Unavailable";
    $("#dbHealth").textContent = "Unknown";
    setFeedback("#stackFeedback", `${error.message}. Run make phase2-status and use the recovery guide.`, false);
  }
}

async function importPhase1(artifact) {
  try {
    const result = await request("/api/phase2/phase1", { method: "POST", body: JSON.stringify(artifact) });
    setFeedback("#importFeedback", `Imported ${result.phase1_evidence_id}.`, true);
    evidence("#evidencePhase1", result.phase1_evidence_id);
    completeStep(2);
  } catch (error) {
    setFeedback("#importFeedback", error.message, false);
  }
}

function config(overrides = {}) {
  return {
    prediction: $("#trainingPrediction").value.trim(),
    seed: Number($("#seed").value),
    epochs: Number($("#epochs").value),
    learning_rate: Number($("#learningRate").value),
    hidden_width: Number($("#hiddenWidth").value),
    patience: 30,
    ...overrides,
  };
}

function percent(value) { return `${(Number(value) * 100).toFixed(1)}%`; }

function drawHistory(history) {
  const canvas = $("#trainingChart"), context = canvas.getContext("2d");
  const width = canvas.width, height = canvas.height, pad = 38;
  context.clearRect(0, 0, width, height);
  context.strokeStyle = "#c7d0dc";
  context.strokeRect(pad, 15, width - pad - 12, height - pad - 15);
  const maximum = Math.max(...history.flatMap((row) => [row.train_loss, row.validation_loss]));
  const minimum = Math.min(...history.flatMap((row) => [row.train_loss, row.validation_loss]));
  const plot = (key, color) => {
    context.beginPath(); context.strokeStyle = color; context.lineWidth = 3;
    history.forEach((row, index) => {
      const x = pad + (index / Math.max(1, history.length - 1)) * (width - pad - 12);
      const y = 15 + ((maximum - row[key]) / Math.max(.0001, maximum - minimum)) * (height - pad - 15);
      if (index === 0) context.moveTo(x, y); else context.lineTo(x, y);
    });
    context.stroke();
  };
  plot("train_loss", "#255fd0"); plot("validation_loss", "#a12b35");
  context.fillStyle = "#17233b"; context.font = "14px system-ui";
  context.fillText("Blue: training · Red: validation", pad, height - 8);
  const sampled = history.filter((_, index) => index === 0 || index === history.length - 1 || index % Math.max(1, Math.floor(history.length / 12)) === 0);
  $("#historyTable").innerHTML = sampled.map((row) => `<tr><td>${row.epoch}</td><td>${row.train_loss.toFixed(4)}</td><td>${row.validation_loss.toFixed(4)}</td><td>${row.gradient_norm.toFixed(4)}</td></tr>`).join("");
}

function showRun(run) {
  latestRun = run;
  $("#results").hidden = false;
  $("#baselineAccuracy").textContent = percent(run.baseline.accuracy);
  $("#modelAccuracy").textContent = percent(run.sealed_test.accuracy);
  $("#modelPrecision").textContent = percent(run.sealed_test.precision);
  $("#modelRecall").textContent = percent(run.sealed_test.recall);
  $("#selectedEpoch").textContent = `${run.training.selected_epoch} / ${run.configuration.epochs}`;
  $("#acceptanceChecks").innerHTML = Object.entries(run.acceptance.checks).map(([name, passed]) => `<li class="${passed ? "pass" : ""}">${passed ? "Passed" : "Not passed"}: ${name.replaceAll("_", " ")}</li>`).join("");
  drawHistory(run.training.history);
  evidence("#evidenceRun", run.acceptance.passed ? "Acceptance gate passed" : "Gate needs work");
  completeStep(4);
}

async function train(overrides = {}) {
  if (config().prediction.length < 20) {
    setFeedback("#trainFeedback", "Record a specific prediction of at least 20 characters before observing training.", false);
    return;
  }
  completeStep(3);
  evidence("#evidencePrediction", "Recorded before training");
  $("#trainModel").disabled = true;
  setFeedback("#trainFeedback", "Training on CPU; the sealed test remains unavailable until checkpoint selection.", true);
  try {
    const result = await request("/api/phase2/train", { method: "POST", body: JSON.stringify(config(overrides)) });
    showRun(result);
    setFeedback("#trainFeedback", result.acceptance.passed ? "Known-good run passed every automated gate." : "Training completed, but the model is not eligible for promotion.", result.acceptance.passed);
  } catch (error) {
    setFeedback("#trainFeedback", error.message, false);
    throw error;
  } finally {
    $("#trainModel").disabled = false;
  }
}

$("#checkStack").addEventListener("click", checkStack);
$("#useSample").addEventListener("click", () => importPhase1(samplePhase1));
$("#phase1File").addEventListener("change", async (event) => {
  try { await importPhase1(JSON.parse(await event.target.files[0].text())); }
  catch (error) { setFeedback("#importFeedback", `The selected file is not valid JSON: ${error.message}`, false); }
});
$("#hiddenWidth").addEventListener("input", () => { $("#hiddenShape").textContent = `(batch, ${$("#hiddenWidth").value})`; });
$("#trainModel").addEventListener("click", () => train().catch(() => {}));
$("#runFailure").addEventListener("click", async () => {
  try {
    await train({ learning_rate: 1000000, epochs: 40 });
    setFeedback("#failureSignal", "The run unexpectedly remained stable; do not accept this as the required failure evidence.", false);
  } catch (error) {
    failureObserved = true;
    setFeedback("#failureSignal", `Expected failure observed: ${error.message}. No checkpoint was promoted.`, true);
    evidence("#evidenceFailure", "Explosive run failed closed");
  }
});
$("#recoverModel").addEventListener("click", async () => {
  $("#learningRate").value = "0.05"; $("#epochs").value = "300"; $("#seed").value = "17";
  try { await train(); if (failureObserved) completeStep(5); } catch (_) { /* feedback already visible */ }
});
$("#predictionForm").addEventListener("submit", async (event) => {
  event.preventDefault();
  const values = Object.fromEntries(new FormData(event.target).entries());
  try {
    const result = await request("/api/phase2/predict", { method: "POST", body: JSON.stringify(Object.fromEntries(Object.entries(values).map(([key, value]) => [key, Number(value)]))) });
    $("#predictionResult").hidden = false;
    $("#predictionResult").innerHTML = `<strong>${percent(result.probability)} late-delivery risk</strong><p>Decision: ${result.decision} at threshold ${result.threshold.toFixed(2)}.</p>`;
    evidence("#evidenceUse", "New project scored"); completeStep(6);
  } catch (error) { $("#predictionResult").hidden = false; $("#predictionResult").textContent = error.message; }
});
$("#createArtifact").addEventListener("click", async () => {
  const reasoning = {
    observation: $("#observation").value,
    failure_diagnosis: $("#failureDiagnosis").value,
    recovery: $("#recovery").value,
    promotion_rationale: $("#promotionRationale").value,
    limitation: $("#limitation").value,
  };
  try {
    latestArtifact = await request("/api/phase2/artifact", { method: "POST", body: JSON.stringify(reasoning) });
    setFeedback("#artifactFeedback", `Created ${latestArtifact.filename}.`, true);
    $("#downloadArtifact").disabled = false;
    evidence("#evidenceArtifact", latestArtifact.filename); completeStep(7);
  } catch (error) { setFeedback("#artifactFeedback", error.message, false); }
});
$("#downloadArtifact").addEventListener("click", () => {
  if (!latestArtifact) return;
  const link = document.createElement("a");
  link.href = URL.createObjectURL(new Blob([JSON.stringify(latestArtifact.artifact, null, 2)], { type: "application/json" }));
  link.download = latestArtifact.filename; link.click(); URL.revokeObjectURL(link.href);
});
$("#resetView").addEventListener("click", () => location.reload());
checkStack();
