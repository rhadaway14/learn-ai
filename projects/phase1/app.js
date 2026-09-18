const STORAGE_KEY = "learn-ai-phase1-project-v1";
const questions = Array.from(document.querySelectorAll("[data-question]")).map((card) => ({
  id: card.dataset.question,
  answer: card.dataset.answer,
  critical: card.dataset.critical === "true",
  feedback: Object.fromEntries(Array.from(card.querySelectorAll("input")).map((input) => [input.value, input.dataset.feedback]))
}));
const form = document.querySelector("#assessmentForm");
const result = document.querySelector("#result");
const download = document.querySelector("#downloadArtifact");
const checkDecisions = document.querySelector("#checkDecisions");
let latestArtifact = null;

function readState() {
  const answers = {};
  new FormData(form).forEach((value, key) => { if (key.startsWith("q")) answers[key] = value; });
  const evidence = Object.fromEntries(["normal_case", "failure_case", "limitations"].map((key) => [key, form.elements[key].value]));
  return { answers, evidence };
}

function saveDraft() { localStorage.setItem(STORAGE_KEY, JSON.stringify(readState())); }
function restoreDraft() {
  try {
    const state = JSON.parse(localStorage.getItem(STORAGE_KEY) || "null");
    if (!state) return;
    Object.entries(state.answers || {}).forEach(([key, value]) => { const input = form.querySelector(`input[name="${key}"][value="${value}"]`); if (input) input.checked = true; });
    Object.entries(state.evidence || {}).forEach(([key, value]) => { if (form.elements[key]) form.elements[key].value = value; });
  } catch (_) { localStorage.removeItem(STORAGE_KEY); }
}

form.addEventListener("input", saveDraft);
function showDecisionFeedback(results) {
  results.forEach((item) => {
    const card = form.querySelector(`[data-question="${item.id}"]`);
    const feedback = card.querySelector(".feedback");
    feedback.textContent = `${item.correct ? "Strong decision." : "Revisit this decision."} ${item.feedback}`;
    feedback.className = `feedback ${item.correct ? "correct" : "incorrect"}`;
  });
}
checkDecisions.addEventListener("click", () => {
  const state = readState();
  showDecisionFeedback(PhaseOneAssessment.checkAnswers(state.answers, questions));
  document.querySelector("[data-question]").scrollIntoView({ behavior: "smooth", block: "start" });
});
form.addEventListener("submit", (event) => {
  event.preventDefault();
  const state = readState();
  const evaluation = PhaseOneAssessment.evaluate(state.answers, state.evidence, questions);
  showDecisionFeedback(evaluation.results);
  Object.entries(evaluation.evidenceResults).forEach(([key, item]) => {
    const status = form.querySelector(`[data-evidence-status="${key}"]`);
    status.textContent = item.complete ? "Evidence requirement met." : `Add detail: use at least ${item.minimumWords} distinct words and connect the answer to a named case concept.`;
    status.className = `evidence-status ${item.complete ? "correct" : "incorrect"}`;
  });
  latestArtifact = { schema_version: "1.0", project_id: "phase1-model-investigation", completed_at: new Date().toISOString(), ...state, evaluation };
  result.hidden = false;
  result.className = evaluation.passed ? "result passed" : "result needs-work";
  result.innerHTML = `<h2>${evaluation.passed ? "Phase 1 gate passed" : "Evidence needs another pass"}</h2><p><strong>${evaluation.score} of ${evaluation.total}</strong> decisions correct. Critical checks: ${evaluation.criticalPassed ? "passed" : "not yet"}. Evidence notes: ${evaluation.evidenceComplete ? "complete" : "need additional case-specific reasoning"}.</p><p>${evaluation.passed ? "Download the artifact and carry the accepted decision into Phase 2." : "Use the feedback beside each decision, revise, and assess again."}</p>`;
  download.disabled = false;
  result.scrollIntoView({ behavior: "smooth", block: "center" });
});

download.addEventListener("click", () => {
  if (!latestArtifact) return;
  const blob = new Blob([JSON.stringify(latestArtifact, null, 2)], { type: "application/json" });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = "phase1-model-investigation.json";
  link.click();
  URL.revokeObjectURL(link.href);
});
restoreDraft();
