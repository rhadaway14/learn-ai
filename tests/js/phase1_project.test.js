"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const { evaluate, checkAnswers, assessEvidence } = require("../../projects/phase1/logic.js");

const questions = Array.from({ length: 9 }, (_, index) => ({
  id: `q${index + 1}`,
  answer: "right",
  critical: index === 1 || index === 6,
  feedback: { right: "supported", wrong: "reconsider" }
}));
const evidence = {
  normal_case: "A project with high predicted risk enters operations review before its promised delivery date, enabling a useful action.",
  failure_case: "A false negative misses a late project, increases customer cost, and appears when recall falls for that subgroup.",
  limitations: "The enterprise sample may not represent the smaller customer population, causing calibration shift and greater uncertainty after launch."
};

test("Phase 1 passes only with score, critical decisions, and evidence", () => {
  const answers = Object.fromEntries(questions.map((question) => [question.id, "right"]));
  assert.equal(evaluate(answers, evidence, questions).passed, true);
  answers.q2 = "wrong";
  const failed = evaluate(answers, evidence, questions);
  assert.equal(failed.score, 8);
  assert.equal(failed.criticalPassed, false);
  assert.equal(failed.passed, false);
});

test("Phase 1 rejects unexplained answers even with a perfect score", () => {
  const answers = Object.fromEntries(questions.map((question) => [question.id, "right"]));
  const failed = evaluate(answers, { ...evidence, limitations: "too short" }, questions);
  assert.equal(failed.score, 9);
  assert.equal(failed.evidenceComplete, false);
  assert.equal(failed.passed, false);
});

test("Phase 1 rejects long filler and repeated words", () => {
  const filler = { normal_case: "x".repeat(200), failure_case: "failure ".repeat(30), limitations: "...............!!!!!!!!" };
  const results = assessEvidence(filler);
  assert.equal(Object.values(results).some((item) => item.complete), false);
});

test("formative checking returns feedback without evaluating evidence", () => {
  const answers = { q1: "right", q2: "wrong" };
  const results = checkAnswers(answers, questions);
  assert.equal(results.length, 9);
  assert.equal(results[0].correct, true);
  assert.equal(results[1].correct, false);
  assert.equal(Object.hasOwn(results[0], "passed"), false);
});

test("blind-guess pass rate remains below one percent", () => {
  let passing = 0;
  const choices = ["right", "wrong-a", "wrong-b"];
  for (let value = 0; value < 3 ** questions.length; value++) {
    let cursor = value;
    const answers = {};
    for (const question of questions) { answers[question.id] = choices[cursor % 3]; cursor = Math.floor(cursor / 3); }
    if (evaluate(answers, evidence, questions).passed) passing++;
  }
  assert.ok(passing / (3 ** questions.length) < .01);
});
