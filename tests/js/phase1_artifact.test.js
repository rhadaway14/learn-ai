"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const artifacts = require("../../projects/phase1/artifact.js");

const state = {
  answers: { q1: "a" },
  evidence: { normal_case: "evidence", failure_case: "evidence", limitations: "evidence" },
};
const evaluation = { score: 8, passed: true };

test("drafts carry and validate the current schema version", () => {
  const draft = artifacts.createDraft(state);
  assert.equal(draft.schema_version, "1.0");
  assert.equal(artifacts.validateDraft(draft).valid, true);
});

test("missing, stale, and malformed draft schemas are rejected", () => {
  assert.equal(artifacts.validateDraft(state).valid, false);
  assert.match(artifacts.validateDraft({ ...state, schema_version: "0.9" }).reason, /unsupported schema version/);
  assert.equal(artifacts.validateDraft({ ...state, schema_version: "1.0", evidence: [] }).valid, false);
});

test("attempt numbers are monotonic and recover safely from invalid storage", () => {
  assert.equal(artifacts.normalizeAttemptNumber("4"), 4);
  assert.equal(artifacts.nextAttemptNumber("4"), 5);
  assert.equal(artifacts.nextAttemptNumber("not-a-number"), 1);
  assert.equal(artifacts.nextAttemptNumber(-8), 1);
});

test("artifacts validate attempt identity and use non-overwriting filenames", () => {
  const first = artifacts.createArtifact(state, evaluation, 1, "2026-09-18T12:00:00.000Z");
  const second = artifacts.createArtifact(state, evaluation, 2, "2026-09-18T12:05:00.000Z");
  assert.equal(artifacts.validateArtifact(first).valid, true);
  assert.equal(first.attempt_number, 1);
  assert.equal(second.attempt_number, 2);
  assert.equal(artifacts.artifactFilename(first.attempt_number), "phase1-model-investigation-attempt-01.json");
  assert.equal(artifacts.artifactFilename(second.attempt_number), "phase1-model-investigation-attempt-02.json");
});

test("artifact validation rejects invalid attempt and schema metadata", () => {
  const artifact = artifacts.createArtifact(state, evaluation, 1, "2026-09-18T12:00:00.000Z");
  assert.equal(artifacts.validateArtifact({ ...artifact, attempt_number: 0 }).valid, false);
  assert.equal(artifacts.validateArtifact({ ...artifact, schema_version: "2.0" }).valid, false);
  assert.throws(() => artifacts.artifactFilename(0), /positive/);
});
