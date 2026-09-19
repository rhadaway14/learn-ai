(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  root.PhaseOneAssessment = api;
})(typeof globalThis !== "undefined" ? globalThis : this, function () {
  const evidenceRules = {
    normal_case: {
      minimumWords: 18,
      requiredGroups: {
        prediction: ["predict", "predicted", "prediction", "probability", "score", "risk"],
        response: ["action", "escalate", "investigate", "prioritize", "review"],
        benefit: ["avoid", "benefit", "deliver", "delivery", "help", "intervene", "late", "operations"]
      }
    },
    failure_case: {
      minimumWords: 18,
      requiredGroups: {
        error: ["false", "miss", "missed", "negative", "positive"],
        impact: ["cost", "customer", "delay", "late", "overload", "waste"],
        signal: ["alert", "metric", "monitor", "precision", "rate", "recall", "signal"]
      }
    },
    limitations: {
      minimumWords: 18,
      requiredGroups: {
        evidence: ["customer", "enterprise", "population", "sample", "subgroup"],
        uncertainty: ["calibration", "confidence", "drift", "representative", "shift", "uncertainty"],
        response: ["collect", "compare", "monitor", "recalibrate", "review", "segment", "validate"]
      }
    }
  };
  const reasoningWords = new Set(["because", "causing", "could", "if", "may", "means", "reveals", "so", "therefore", "when", "which", "while", "would"]);
  function words(value) { return String(value || "").toLowerCase().match(/[a-z0-9]+(?:[-'][a-z0-9]+)*/g) || []; }
  function substantiveSentences(value) {
    return String(value || "").split(/[.!?]+/).map((part) => words(part)).filter((tokens) => tokens.length >= 5).length;
  }
  function assessEvidence(evidence) {
    return Object.fromEntries(Object.entries(evidenceRules).map(([key, rule]) => {
      const tokens = words(evidence[key]);
      const unique = new Set(tokens);
      const groupHits = Object.fromEntries(Object.entries(rule.requiredGroups).map(([group, concepts]) => [group, concepts.filter((concept) => tokens.some((token) => token === concept || (concept.length >= 5 && token.startsWith(concept))))]));
      const missingGroups = Object.entries(groupHits).filter(([, hits]) => hits.length === 0).map(([group]) => group);
      const sentenceCount = substantiveSentences(evidence[key]);
      const hasCaseContext = tokens.some((token) => token === "northstar" || token.startsWith("northstar'"));
      const hasReasoning = tokens.some((token) => reasoningWords.has(token));
      const complete = unique.size >= rule.minimumWords && sentenceCount >= 2 && hasCaseContext && hasReasoning && missingGroups.length === 0;
      return [key, { complete, distinctWords: unique.size, minimumWords: rule.minimumWords, sentenceCount, hasCaseContext, hasReasoning, groupHits, missingGroups }];
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
