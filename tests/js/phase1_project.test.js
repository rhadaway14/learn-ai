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
  normal_case: "Northstar predicts high delivery risk for a project, so operations sends it to review before the promised date. This action helps the team intervene early and avoid a late delivery for the customer.",
  failure_case: "Northstar produces a false negative when it misses a project that later arrives late. The customer bears the delay cost, so the team monitors recall by subgroup to reveal this failure.",
  limitations: "Northstar learned from an enterprise sample that may not represent the smaller customer population. The team should monitor calibration by subgroup because customer shift could increase uncertainty after launch."
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

test("Phase 1 rejects deliberately gamed keyword text", () => {
  const gamed = {
    normal_case: "Northstar project prediction risk review action operations late alpha beta gamma delta epsilon zeta eta theta iota kappa lambda.",
    failure_case: "Northstar false miss alert failure late review cost signal alpha beta gamma delta epsilon zeta eta theta iota kappa lambda.",
    limitations: "Northstar sample population customer calibration uncertainty subgroup shift enterprise small alpha beta gamma delta epsilon zeta eta theta."
  };
  const results = assessEvidence(gamed);
  assert.equal(Object.values(results).every((item) => item.complete === false), true);
});

test("Phase 1 requires every evidence category, case context, and reasoning", () => {
  const incomplete = {
    ...evidence,
    normal_case: "Northstar predicts project risk before the deadline because the score is high. The team records many additional distinct observations about schedules, owners, dates, customers, estimates, and planning."
  };
  const result = assessEvidence(incomplete).normal_case;
  assert.equal(result.complete, false);
  assert.deepEqual(result.missingGroups, ["response", "benefit"]);
});

test("Phase 1 accepts ordinary inflections instead of requiring magic keywords", () => {
  const natural = {
    ...evidence,
    normal_case: "Northstar's prediction marks a project as high risk, so operations reviews it before the promised date. That response helps the team intervene and avoid delivering late to the customer."
  };
  assert.equal(assessEvidence(natural).normal_case.complete, true);
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
