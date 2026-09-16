# Lesson 04 Reference Notes — Probability and Statistics for ML

Review these notes only after attempting the exercises. Exact wording can differ; the reasoning should not.

## Exercise 1

Both services have expected value 3 because outcomes balance around 3 with the same probabilities. Service B has greater spread: its outer outcomes are two days from the mean rather than one. It needs a larger reliability buffer. The mean alone is inadequate for setting a promised delivery window or safety stock.

## Exercise 2

Representative-sample means generally settle near 50 and interval width shrinks as sample size grows. Biased samples settle near the shifted value even while their intervals become narrow. More data improves precision about the process that was sampled; it does not prove that process represents the target population.

## Exercise 3

- Fraudulent: 50
- Legitimate: 9,950
- True positives: 45
- False positives: 199
- All flags: 244

The probability of real fraud after a flag is about $45\div244=18.4\%$. Sensitivity answers how often fraud is caught when fraud is already known to be present. The requested posterior asks how often fraud is present after a flag, which also depends on the base rate and false positives.

## Exercise 4

1. Invalid. The interval estimates a population mean, not the spread of individual request times.
2. Valid, assuming the data and method satisfy the procedure's conditions.
3. Invalid. Interval width does not detect every collection bias or coverage gap.
4. Approximately valid under comparable assumptions because standard error decreases with the square root of sample size.

## Exercise 5

The observed frequency is $1{,}200\div2{,}000=60\%$. An 80% forecast paired with 60% outcomes is overconfident by 20 percentage points in that band. Other probability bands may behave differently, and results may also vary across subgroups or over time.

## Exercise 6

Customers may contact support because they already have serious product problems, or frustrated customers may both contact support and cancel because of a third factor such as repeated outages. Contact count can still identify cancellation risk. Restricting support could worsen the underlying experience and does not follow from the correlation. A randomized or carefully controlled intervention, with ethical and operational safeguards, would provide stronger causal evidence.

## Capstone quality bar

A strong uncertainty and sampling contract:

- distinguishes the target population from the observed sample;
- names concrete selection, coverage, dependence, and drift risks;
- reports uncertainty alongside a point estimate;
- uses base rates when interpreting alerts;
- checks calibration by score range and meaningful subgroup;
- avoids causal language where only observational correlation exists; and
- connects every measurement to a real release or operating decision.
