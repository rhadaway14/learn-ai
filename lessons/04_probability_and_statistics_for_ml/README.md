# Lesson 04 — Probability and Statistics for ML

## Start here

Open the [interactive lesson](index.html). It teaches the material in a browser and does not require Python or prior statistics coursework.

AI rarely produces certainty. A fraud detector estimates risk, a demand model estimates a range of future demand, and a language model assigns probabilities to possible next tokens. Probability gives us a language for possible outcomes. Statistics helps us learn from the limited outcomes we observed.

By the end of this lesson, you should be able to:

- distinguish probability from statistics;
- explain distributions, expected value, variance, and standard deviation;
- explain why a sample may or may not represent a population;
- reason through conditional probability and Bayes’ rule using counts;
- interpret a frequentist confidence interval correctly;
- recognize calibration, sampling bias, and base-rate neglect;
- separate predictive correlation from evidence of causation; and
- add an uncertainty and sampling contract to the course capstone.

## 1. Probability and statistics answer opposite questions

**Probability** begins with a model of an uncertain process and asks what data it could produce.

> If 20% of comparable support tickets escalate, what should we expect across the next 1,000 comparable tickets?

**Statistics** begins with observed data and asks what we can infer about the process that produced it.

> If 43 of 200 observed tickets escalated, what escalation rate is plausible for the wider ticket population?

A probability is between 0 and 1, or equivalently between 0% and 100%. It is not automatically a guarantee, confidence level, or frequency from one observation. It is always conditional on a model and information: probability of *what*, for *which cases*, during *what period*, given *which evidence*?

### Core vocabulary

| Term | Plain-language meaning | Example |
|---|---|---|
| Experiment | A repeatable process with an uncertain result | Route one incoming ticket |
| Outcome | One possible result | The ticket escalates |
| Event | One or more outcomes we care about | Escalation occurs within 24 hours |
| Random variable | A number assigned to an outcome | Resolution time in hours |
| Population | The full process or group of interest | All future tickets in production |
| Sample | The observations actually collected | Tickets from last month |
| Statistic | A number calculated from a sample | The sample escalation rate |

“Random variable” can sound stranger than it is. The rule assigning numbers is fixed; the value is uncertain before the outcome occurs. The number of minutes until a ticket is answered is a random variable because the next value is not known in advance.

## 2. A distribution is a map of uncertainty

A probability distribution describes the possible values of a random variable and how probability is allocated among them.

- A **discrete** variable has countable values, such as 0, 1, 2, or 3 failed servers.
- A **continuous** variable can take values across a range, such as latency or temperature.

Think of one unit of probability as inventory spread across outcome shelves. A shelf with more inventory represents a more likely outcome. For a discrete distribution, all shelf probabilities add to 1. For a continuous distribution, probability belongs to ranges rather than individual exact points.

### Expected value

The expected value is the probability-weighted center of a distribution. In words:

> Multiply each possible outcome by its probability, then add those products.

Suppose a delivery takes 1 day half the time and 5 days half the time. The expected duration is:

$$
(1 \times 0.5) + (5 \times 0.5) = 3\text{ days}
$$

This does **not** mean any delivery must take 3 days. Expected value is a long-run planning center, not a promise about the next outcome.

### Variance and standard deviation

The mean alone does not tell us how reliable a process is. A carrier that always takes about 3 days and one that alternates between 1 and 5 days can have the same mean.

Variance measures the average squared distance from the mean:

$$
\operatorname{Var}(X)=\sum_x P(X=x)(x-\mu)^2
$$

The square prevents positive and negative distances from cancelling and penalizes large distances strongly. Its units are squared, such as days squared. Standard deviation takes the square root:

$$
\sigma=\sqrt{\operatorname{Var}(X)}
$$

Standard deviation returns to the original units, so it is usually easier to communicate. In operations, expected value helps set a plan; spread helps set buffers and understand risk.

## 3. Samples are evidence, not miniature populations by default

We usually cannot observe every future customer, transaction, or model request. We collect a sample and use a statistic—such as its mean—to estimate an unknown population quantity.

Think of tasting soup. One spoonful can represent the pot only if the soup was mixed and the spoon reached a representative location. A larger spoon from an unmixed salty corner gives a more precise measurement of the wrong region.

Two different problems matter:

- **Sampling variation:** representative samples differ by chance. Larger samples usually reduce this random variation.
- **Sampling bias:** the collection method systematically over- or under-represents part of the population. More observations from the same biased process do not repair it.

For independent representative observations, the sample mean tends to settle near the population mean as sample size grows. This is the practical idea behind the law of large numbers. It does not say every larger sample is closer, and it does not rescue selection bias, drift, duplicated observations, or a badly defined target population.

The standard error estimates how much a statistic such as the sample mean would vary across repeated samples. For a sample mean, an often-used estimate is:

$$
\text{standard error} = \frac{\text{sample standard deviation}}{\sqrt{\text{sample size}}}
$$

Because sample size is under a square root, cutting standard error in half generally requires about four times as many representative observations.

## 4. Conditional probability changes the question

Conditional probability means probability after restricting attention to cases where some evidence is known.

$$
P(A\mid B)
$$

Read this as “the probability of A given B.” The order matters. The probability that a sensor flags an item **given that it is defective** is not the same as the probability that an item is defective **given that the sensor flagged it**.

That reversed interpretation causes the base-rate fallacy.

### Bayes’ rule using natural counts

Imagine 10,000 manufactured components:

- 1% are defective, so 100 are defective and 9,900 are good.
- The sensor catches 95% of defects, producing 95 true positives.
- It falsely flags 5% of good components, producing 495 false positives.
- It produces 590 positive flags in total.

Among flagged components, only 95 of 590 are actually defective:

$$
95 \div 590 \approx 16.1\%
$$

The sensor can have 95% sensitivity while a positive flag has only about a 16% chance of indicating a real defect. The defect was rare enough that a small false-positive rate acted on a much larger group.

The compact Bayes formula expresses the same update:

$$
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}
$$

Here, $P(A)$ is the prior or base rate, $P(B\mid A)$ describes how likely the evidence is when A is true, and $P(A\mid B)$ is the posterior after observing B. When a formula feels abstract, rebuild it with a population of 1,000 or 10,000 and count the cases.

## 5. Confidence intervals describe a repeated procedure

A point estimate such as “the mean is 50” conceals sampling uncertainty. A confidence interval pairs the estimate with a range constructed by a procedure.

For a representative sample with mean 50, standard deviation 10, and size 100:

1. Standard error is $10\div\sqrt{100}=1$.
2. An approximate 95% margin is $1.96\times1=1.96$.
3. The interval is approximately $50\pm1.96$, or $[48.04,51.96]$.

The careful frequentist interpretation is:

> If we repeatedly collected valid samples and constructed intervals with this procedure, about 95% of those intervals would contain the fixed population value.

It does not mean 95% of individual observations are inside the interval. It also does not assign a 95% frequentist probability to the fixed parameter after this one interval has been produced.

Intervals rely on assumptions. Dependence between observations, selection bias, distribution mismatch, drift, or an incorrect standard-error formula can make a narrow interval misleading.

### Bootstrap intervals

When a statistic is difficult to analyze directly, the bootstrap repeatedly resamples the observed data **with replacement**, recalculates the statistic, and uses the resulting empirical spread to estimate uncertainty. It asks: “If this sample approximates the population, how much would the statistic vary under repeated sampling?”

The bootstrap is powerful, but it cannot create missing populations or remove collection bias. If the original sample omits an important group, every bootstrap resample inherits that omission.

## 6. Calibration tests whether confidence is honest

A model is calibrated when predicted probabilities match observed frequencies across comparable cases. Among many predictions near 80%, the event should occur about 80% of the time.

Calibration is not the same as:

- **accuracy:** the fraction of hard decisions that are correct;
- **discrimination:** how well a score ranks positives above negatives; or
- **usefulness:** whether decisions made from the probabilities create value at an acceptable cost.

A model can be calibrated but poor at separating cases, or good at ranking while systematically overconfident. Production evaluation often needs all three perspectives.

Calibration must also be checked across time, probability ranges, and relevant subgroups. A global average can conceal severe local failures.

## 7. Correlation supports prediction, not automatic causal claims

Correlation means two variables vary together. It does not identify why.

Ice-cream sales and drownings may both rise during hot weather. Temperature is a **confounder** affecting both. Other traps include reverse causation and selection effects.

This distinction matters because prediction and intervention ask different questions:

- Prediction: “Given what I observe, what is likely next?”
- Causation: “If I deliberately change this factor, what outcome will change because of it?”

An AI model can exploit a stable non-causal correlation for prediction. But when the environment changes—or when someone acts on the prediction—the correlation may break. Policies, treatments, and product interventions require experimental or carefully justified causal evidence.

## 8. Connections to modern AI

| AI task | Probability/statistics role |
|---|---|
| Language generation | The model outputs a probability distribution over the next token |
| Classification | Scores may be interpreted as class probabilities only when the model and calibration justify it |
| RAG evaluation | Samples of questions estimate performance on a larger usage population |
| Agent monitoring | Base rates determine how to interpret alerts and rare failures |
| A/B testing | Sampling uncertainty separates plausible effects from noise |
| Model governance | Intervals, subgroup checks, drift, and calibration expose uncertainty hidden by a single metric |

## Common failure modes

- Treating one probabilistic miss as proof that the probability was wrong.
- Reporting a mean without the distribution or spread.
- Assuming a large biased dataset is representative.
- Confusing $P(A\mid B)$ with $P(B\mid A)$.
- Ignoring a rare base rate when interpreting a positive alert.
- Treating model confidence as calibrated probability without testing it.
- Reading a confidence interval as a range containing 95% of observations.
- Turning correlation into an intervention claim.

## Interactive learning sequence

In [index.html](index.html):

1. Answer the readiness question about a 70% forecast.
2. Compare two delivery distributions with the same expected value.
3. Increase sample size and observe interval width.
4. Turn on biased collection and notice that precision can increase around a wrong value.
5. Change defect prevalence, sensitivity, and false-positive rate in the Bayes lab.
6. Compare forecast probability with observed frequency in the calibration lab.
7. Complete all seven knowledge checks.

## Capstone increment: uncertainty and sampling contract

Extend the AI delivery advisor design with:

- the target population and available evaluation sample;
- ways the sample could differ from production traffic;
- at least one base rate required to interpret an alert;
- a point estimate reported with an uncertainty interval;
- a calibration check by score range and important subgroup; and
- one observed correlation that must not be described as causal.

This artifact will support Lesson 5’s model-selection and evaluation work. Later capstone lessons will turn it into executable evaluations and production monitoring.

## Knowledge checkpoint

You are ready to continue when you can explain, without relying on a formula alone:

1. Why two processes with the same mean can pose different operational risks.
2. Why more observations reduce random error but not systematic bias.
3. Why sensitivity is not the same as the probability of a true defect after a flag.
4. What a 95% confidence procedure means across repeated samples.
5. What calibrated 80% predictions should look like over many comparable cases.
6. Why correlation can be useful for prediction but insufficient for intervention.

## Definition of done

- [ ] Complete the browser lesson and all interactions.
- [ ] Explain expectation, spread, sampling, Bayes, intervals, and calibration in plain language.
- [ ] Diagnose the biased large-sample experiment.
- [ ] Explain the 10,000-component base-rate example from counts.
- [ ] Complete the seven knowledge checks.
- [ ] Produce the capstone uncertainty and sampling contract.
- [ ] Mark Lesson 4 complete on the course dashboard.

## Instructor and maintainer note

The repository retains `lab.py` and the reusable course-lab implementation for automated verification and optional instructor demonstrations. They are not part of the learner path. A student can complete Lesson 4 without reading or editing Python.
