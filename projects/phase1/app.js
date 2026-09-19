const STORAGE_KEY = "learn-ai-phase1-project-v1";
const ATTEMPT_KEY = "learn-ai-phase1-project-attempt-v1";
const questions = Array.from(document.querySelectorAll("[data-question]")).map(
  (card) => ({
    id: card.dataset.question,
    answer: card.dataset.answer,
    critical: card.dataset.critical === "true",
    feedback: Object.fromEntries(
      Array.from(card.querySelectorAll("input")).map((input) => [
        input.value,
        input.dataset.feedback,
      ]),
    ),
  }),
);
const form = document.querySelector("#assessmentForm");
const result = document.querySelector("#result");
const download = document.querySelector("#downloadArtifact");
const checkDecisions = document.querySelector("#checkDecisions");
const storageWarning = document.querySelector("#storageWarning");
let latestArtifact = null;
let attemptNumber = 0;

function showStorageWarning(
  message = "Your draft cannot be saved in this browser. Keep this page open and download your evidence artifact before leaving.",
) {
  storageWarning.textContent = message;
  storageWarning.hidden = false;
}

function readState() {
  const answers = {};
  new FormData(form).forEach((value, key) => {
    if (key.startsWith("q")) answers[key] = value;
  });
  const evidence = Object.fromEntries(
    ["normal_case", "failure_case", "limitations"].map((key) => [
      key,
      form.elements[key].value,
    ]),
  );
  return { answers, evidence };
}

function saveDraft() {
  try {
    localStorage.setItem(
      STORAGE_KEY,
      JSON.stringify(PhaseOneArtifacts.createDraft(readState())),
    );
  } catch (_) {
    showStorageWarning();
  }
}
function restoreDraft() {
  try {
    const state = JSON.parse(localStorage.getItem(STORAGE_KEY) || "null");
    if (!state) return;
    const validation = PhaseOneArtifacts.validateDraft(state);
    if (!validation.valid) {
      showStorageWarning(
        `The saved draft was not loaded because it uses ${validation.reason}. Start a new draft and download its evidence artifact before leaving.`,
      );
      return;
    }
    Object.entries(state.answers || {}).forEach(([key, value]) => {
      const input = form.querySelector(
        `input[name="${key}"][value="${value}"]`,
      );
      if (input) input.checked = true;
    });
    Object.entries(state.evidence || {}).forEach(([key, value]) => {
      if (form.elements[key]) form.elements[key].value = value;
    });
  } catch (_) {
    showStorageWarning(
      "The saved draft could not be read. A new draft is active; download your evidence artifact before leaving.",
    );
  }
}

function restoreAttemptNumber() {
  try {
    attemptNumber = PhaseOneArtifacts.normalizeAttemptNumber(
      localStorage.getItem(ATTEMPT_KEY),
    );
  } catch (_) {
    attemptNumber = 0;
    showStorageWarning();
  }
}

function beginAttempt() {
  attemptNumber = PhaseOneArtifacts.nextAttemptNumber(attemptNumber);
  try {
    localStorage.setItem(ATTEMPT_KEY, String(attemptNumber));
  } catch (_) {
    showStorageWarning(
      "This attempt is numbered for the current page, but its number cannot be saved in this browser. Download the artifact before leaving.",
    );
  }
  return attemptNumber;
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
  showDecisionFeedback(
    PhaseOneAssessment.checkAnswers(state.answers, questions),
  );
  document
    .querySelector("[data-question]")
    .scrollIntoView({ behavior: "smooth", block: "start" });
});
form.addEventListener("submit", (event) => {
  event.preventDefault();
  const state = readState();
  const evaluation = PhaseOneAssessment.evaluate(
    state.answers,
    state.evidence,
    questions,
  );
  showDecisionFeedback(evaluation.results);
  Object.entries(evaluation.evidenceResults).forEach(([key, item]) => {
    const status = form.querySelector(`[data-evidence-status="${key}"]`);
    const needs = [];
    if (item.distinctWords < item.minimumWords)
      needs.push(`${item.minimumWords} distinct words`);
    if (item.sentenceCount < 2) needs.push("two substantive sentences");
    if (!item.hasCaseContext) needs.push("the Northstar case name");
    if (!item.hasReasoning) needs.push("a because/when/so explanation");
    if (item.missingGroups.length)
      needs.push(`these ideas: ${item.missingGroups.join(", ")}`);
    status.textContent = item.complete
      ? "Evidence requirement met."
      : `Revise this note. Add ${needs.join("; ")}.`;
    status.className = `evidence-status ${item.complete ? "correct" : "incorrect"}`;
  });
  latestArtifact = PhaseOneArtifacts.createArtifact(
    state,
    evaluation,
    beginAttempt(),
  );
  if (evaluation.passed) CourseProgress.completeMilestone("phase1");
  result.hidden = false;
  result.className = evaluation.passed ? "result passed" : "result needs-work";
  result.innerHTML = `<h2>${evaluation.passed ? "Phase 1 gate passed" : "Evidence needs another pass"}</h2><p><strong>Attempt ${latestArtifact.attempt_number}:</strong> ${evaluation.score} of ${evaluation.total} decisions correct. Critical checks: ${evaluation.criticalPassed ? "passed" : "not yet"}. Evidence notes: ${evaluation.evidenceComplete ? "complete" : "need additional case-specific reasoning"}.</p><p>${evaluation.passed ? "Download the artifact and carry the accepted decision into Phase 2." : "Use the feedback beside each decision, revise, and assess again."}</p>`;
  download.disabled = false;
  result.scrollIntoView({ behavior: "smooth", block: "center" });
});

download.addEventListener("click", () => {
  if (!latestArtifact) return;
  const blob = new Blob([JSON.stringify(latestArtifact, null, 2)], {
    type: "application/json",
  });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = PhaseOneArtifacts.artifactFilename(
    latestArtifact.attempt_number,
  );
  link.click();
  URL.revokeObjectURL(link.href);
});
restoreAttemptNumber();
restoreDraft();
window.addEventListener("course-storage-error", (event) =>
  showStorageWarning(event.detail?.message),
);
if (CourseProgress.getStorageError())
  showStorageWarning(CourseProgress.getStorageError());
