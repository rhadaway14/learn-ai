# Lesson 04 Exercises — Probability and Statistics for ML

Complete these exercises after the [interactive lesson](index.html). No programming is required.

## Exercise 1 — Distribution and operational risk

Two delivery services both average 3 days:

- Service A takes 2 days 25% of the time, 3 days 50% of the time, and 4 days 25% of the time.
- Service B takes 1 day 25% of the time, 3 days 50% of the time, and 5 days 25% of the time.

Answer:

1. Why is the expected value identical?
2. Which service has greater variance?
3. Which would require a larger customer-expectation buffer, and why?
4. Name a decision for which the mean alone would be inadequate.

## Exercise 2 — Sample size and bias

Use the sample-size interaction with 20, 100, 1,000, and 10,000 observations. Record what happens first with representative sampling and then with biased collection.

| Sample size | Representative mean | Representative interval width | Biased mean | Biased interval width |
|---:|---:|---:|---:|---:|
| 20 | | | | |
| 100 | | | | |
| 1,000 | | | | |
| 10,000 | | | | |

Explain why the 10,000-observation biased result can look convincing while remaining wrong.

## Exercise 3 — Base rates from counts

A review system examines 10,000 transactions:

- 0.5% are fraudulent.
- It catches 90% of fraudulent transactions.
- It falsely flags 2% of legitimate transactions.

Fill in the counts before calculating a percentage:

| Quantity | Count |
|---|---:|
| Fraudulent transactions | |
| Legitimate transactions | |
| True positives | |
| False positives | |
| All positive flags | |

Then calculate the probability that a flagged transaction is actually fraudulent. Explain why “90% sensitivity” is not the answer.

## Exercise 4 — Interpret an interval

A team reports: “Mean response time is 420 ms, with a 95% confidence interval from 405 ms to 435 ms.”

For each claim, mark valid or invalid and explain:

1. 95% of individual requests took between 405 and 435 ms.
2. This interval came from a procedure designed for 95% long-run coverage under its assumptions.
3. The narrow interval proves the traffic sample represents every production region.
4. Repeating the study with four times as many comparable independent observations should make the interval roughly half as wide.

## Exercise 5 — Calibration diagnosis

A risk model places 2,000 cases into its “about 80%” probability band. Only 1,200 cases have the predicted outcome.

1. What observed frequency did the cohort produce?
2. Is the model overconfident or underconfident in this band?
3. Why can you not diagnose the entire model from this band alone?
4. Name one subgroup and one later time period you would audit.

## Exercise 6 — Prediction versus intervention

A company observes that customers who contact support more often are more likely to cancel.

1. Give two plausible explanations other than “contacting support causes cancellation.”
2. Explain how support-contact count could still be useful for prediction.
3. Explain why intentionally reducing access to support is not justified by the correlation.
4. What stronger evidence would help evaluate a causal intervention?

## Capstone worksheet — Uncertainty and sampling contract

For the AI delivery advisor, complete:

| Decision item | Your answer |
|---|---|
| Target population | |
| Available evaluation sample | |
| Important ways the sample might differ from production | |
| Base rate required to interpret an alert | |
| Point estimate to report | |
| Uncertainty interval to report with it | |
| Calibration check | |
| Important subgroup check | |
| Correlation that must not be presented as causal | |
| Signal that the data distribution has changed | |

Finish with a four-sentence review: what is estimated, where the evidence came from, what uncertainty remains, and what decision the estimate can safely support.
