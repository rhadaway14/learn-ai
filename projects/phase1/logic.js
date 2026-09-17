(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  root.PhaseOneAssessment = api;
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
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
    const evidenceComplete = ["normal_case", "failure_case", "limitations"].every((key) => String(evidence[key] || "").trim().length >= 20);
    return { score, total: questions.length, criticalPassed, evidenceComplete, passed: score >= 6 && criticalPassed && evidenceComplete, results };
  }
  return { evaluate };
});
