(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  root.PhaseOneAssessment = api;
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
  const evidenceRules = {
    normal_case: { minimumWords: 12, concepts: ["project", "prediction", "risk", "review", "action", "operations", "late"] },
    failure_case: { minimumWords: 12, concepts: ["false", "miss", "alert", "failure", "late", "review", "cost", "signal"] },
    limitations: { minimumWords: 12, concepts: ["sample", "population", "customer", "calibration", "uncertainty", "subgroup", "shift", "enterprise", "small"] }
  };
  function words(value) { return String(value || "").toLowerCase().match(/[a-z0-9]+(?:[-'][a-z0-9]+)*/g) || []; }
  function assessEvidence(evidence) {
    return Object.fromEntries(Object.entries(evidenceRules).map(([key, rule]) => {
      const tokens = words(evidence[key]);
      const unique = new Set(tokens);
      const conceptHits = rule.concepts.filter((concept) => unique.has(concept));
      return [key, { complete: unique.size >= rule.minimumWords && conceptHits.length >= 1, distinctWords: unique.size, minimumWords: rule.minimumWords, conceptHits }];
    }));
  }
  function evaluate(answers, evidence, questions) {
    const results = questions.map((question) => {
      const selected = answers[question.id] || "";
      return {
        id: question.id,
        selected,
        correct: selected === question.answer,
        critical: Boolean(question.critical),
        feedback: selected ? (question.feedback[selected] || "Review this decision.") : "Choose an answer before submitting."
      };
    });
    const score = results.filter((result) => result.correct).length;
    const criticalPassed = results.filter((result) => result.critical).every((result) => result.correct);
    const evidenceResults = assessEvidence(evidence);
    const evidenceComplete = Object.values(evidenceResults).every((item) => item.complete);
    return { score, total: questions.length, criticalPassed, evidenceComplete, evidenceResults, passed: score >= 7 && criticalPassed && evidenceComplete, results };
  }
  function checkAnswers(answers, questions) { return evaluate(answers, {}, questions).results; }
  return { evaluate, checkAnswers, assessEvidence, evidenceRules };
});
