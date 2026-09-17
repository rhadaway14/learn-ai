"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const { evaluate } = require("../../projects/phase1/logic.js");

const questions = Array.from({ length: 7 }, (_, index) => ({
  id: `q${index + 1}`,
  answer: "right",
  critical: index === 1 || index === 6,
  feedback: { right: "supported", wrong: "reconsider" }
}));
const evidence = {
  normal_case: "A normal case with useful action evidence.",
  failure_case: "A false negative delays an important intervention.",
  limitations: "The launch population differs from the sample."
};

test("Phase 1 passes only with score, critical decisions, and evidence", () => {
  const answers = Object.fromEntries(questions.map((question) => [question.id, "right"]));
  assert.equal(evaluate(answers, evidence, questions).passed, true);
  answers.q2 = "wrong";
  const failed = evaluate(answers, evidence, questions);
  assert.equal(failed.score, 6);
  assert.equal(failed.criticalPassed, false);
  assert.equal(failed.passed, false);
});

test("Phase 1 rejects unexplained answers even with a perfect score", () => {
  const answers = Object.fromEntries(questions.map((question) => [question.id, "right"]));
  const failed = evaluate(answers, { ...evidence, limitations: "too short" }, questions);
  assert.equal(failed.score, 7);
  assert.equal(failed.evidenceComplete, false);
  assert.equal(failed.passed, false);
});
