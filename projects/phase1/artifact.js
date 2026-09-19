(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  root.PhaseOneArtifacts = api;
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
  const SCHEMA_VERSION = "1.0";
  const PROJECT_ID = "phase1-model-investigation";

  function isRecord(value) {
    return Boolean(value) && typeof value === "object" && !Array.isArray(value);
  }

  function validateDraft(value) {
    if (!isRecord(value)) return { valid: false, reason: "not an object" };
    if (value.schema_version !== SCHEMA_VERSION)
      return {
        valid: false,
        reason: `unsupported schema version ${String(value.schema_version || "missing")}`,
      };
    if (!isRecord(value.answers) || !isRecord(value.evidence))
      return { valid: false, reason: "answers or evidence are missing" };
    return { valid: true, reason: "current schema" };
  }

  function createDraft(state) {
    const draft = { schema_version: SCHEMA_VERSION, ...state };
    const validation = validateDraft(draft);
    if (!validation.valid) throw new TypeError(validation.reason);
    return draft;
  }

  function normalizeAttemptNumber(value) {
    const attempt = Number(value);
    return Number.isSafeInteger(attempt) && attempt >= 0 ? attempt : 0;
  }

  function nextAttemptNumber(previous) {
    return normalizeAttemptNumber(previous) + 1;
  }

  function validateArtifact(value) {
    const draft = validateDraft(value);
    if (!draft.valid) return draft;
    if (value.project_id !== PROJECT_ID)
      return { valid: false, reason: "unexpected project id" };
    if (!Number.isSafeInteger(value.attempt_number) || value.attempt_number < 1)
      return { valid: false, reason: "attempt number must be a positive integer" };
    if (typeof value.completed_at !== "string" || Number.isNaN(Date.parse(value.completed_at)))
      return { valid: false, reason: "completion timestamp is invalid" };
    if (!isRecord(value.evaluation))
      return { valid: false, reason: "evaluation is missing" };
    return { valid: true, reason: "current schema" };
  }

  function createArtifact(state, evaluation, attemptNumber, completedAt = new Date().toISOString()) {
    const artifact = {
      schema_version: SCHEMA_VERSION,
      project_id: PROJECT_ID,
      attempt_number: attemptNumber,
      completed_at: completedAt,
      ...state,
      evaluation,
    };
    const validation = validateArtifact(artifact);
    if (!validation.valid) throw new TypeError(validation.reason);
    return artifact;
  }

  function artifactFilename(attemptNumber) {
    const attempt = normalizeAttemptNumber(attemptNumber);
    if (attempt < 1) throw new RangeError("attempt number must be positive");
    return `${PROJECT_ID}-attempt-${String(attempt).padStart(2, "0")}.json`;
  }

  return {
    SCHEMA_VERSION,
    PROJECT_ID,
    validateDraft,
    createDraft,
    normalizeAttemptNumber,
    nextAttemptNumber,
    validateArtifact,
    createArtifact,
    artifactFilename,
  };
});
