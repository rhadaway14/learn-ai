"use strict";
CourseProgress.visit(1);

const controls = {
  learningRate: document.querySelector("#learningRate"),
  epochs: document.querySelector("#epochs"),
  samples: document.querySelector("#samples"),
  noise: document.querySelector("#noise"),
  relationship: document.querySelector("#relationship"),
  outlier: document.querySelector("#outlier")
};

function seededRandom(seed = 42) {
  let state = seed >>> 0;
  return () => ((state = (1664525 * state + 1013904223) >>> 0) / 4294967296);
}

function normal(random) {
  const u = Math.max(random(), 1e-12);
  const v = random();
  return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
}

function dataset(count, noise, relationship, outlier) {
  return Lesson01Logic.dataset(count, noise, relationship, outlier);
}

function train(rows, learningRate, epochs) {
  const training = rows.filter(row => !row.test);
  let weight = 0;
  let bias = 0;
  const losses = [];
  let unstable = false;

  for (let step = 0; step < epochs; step += 1) {
    let squaredError = 0;
    let weightGradient = 0;
    let biasGradient = 0;
    for (const row of training) {
      const error = weight * row.x + bias - row.y;
      squaredError += error * error;
      weightGradient += error * row.x;
      biasGradient += error;
    }
    const loss = squaredError / training.length;
    if (!Number.isFinite(loss) || Math.abs(weight) > 1e8) {
      unstable = true;
      break;
    }
    losses.push(loss);
    weight -= learningRate * 2 * weightGradient / training.length;
    bias -= learningRate * 2 * biasGradient / training.length;
  }
  const mse = subset => subset.reduce((sum, row) => {
    const error = weight * row.x + bias - row.y;
    return sum + error * error;
  }, 0) / Math.max(1, subset.length);
  return {weight, bias, losses, unstable, trainLoss: mse(training), testLoss: mse(rows.filter(row => row.test))};
}

function chartFrame(canvas, xLabel, yLabel) {
  const context = canvas.getContext("2d");
  const width = canvas.width;
  const height = canvas.height;
  const pad = {left: 58, right: 22, top: 18, bottom: 45};
  context.clearRect(0, 0, width, height);
  context.fillStyle = "#fff";
  context.fillRect(0, 0, width, height);
  context.strokeStyle = "#dbe3ec";
  context.lineWidth = 1;
  context.font = "12px system-ui";
  context.fillStyle = "#637083";
  for (let index = 0; index <= 5; index += 1) {
    const x = pad.left + index * (width - pad.left - pad.right) / 5;
    const y = pad.top + index * (height - pad.top - pad.bottom) / 5;
    context.beginPath(); context.moveTo(x, pad.top); context.lineTo(x, height - pad.bottom); context.stroke();
    context.beginPath(); context.moveTo(pad.left, y); context.lineTo(width - pad.right, y); context.stroke();
  }
  context.textAlign = "center"; context.fillText(xLabel, width / 2, height - 9);
  context.save(); context.translate(15, height / 2); context.rotate(-Math.PI / 2); context.fillText(yLabel, 0, 0); context.restore();
  return {context, width, height, pad};
}

function drawFit(rows, result) {
  const {context, width, height, pad} = chartFrame(document.querySelector("#fitChart"), "input (x)", "label / prediction (y)");
  const values = rows.map(row => row.y);
  if (!result.unstable) values.push(result.bias, result.weight * 10 + result.bias);
  const minY = Math.min(0, ...values) - 5;
  const maxY = Math.max(40, ...values) + 5;
  const sx = value => pad.left + value / 10 * (width - pad.left - pad.right);
  const sy = value => height - pad.bottom - (value - minY) / (maxY - minY) * (height - pad.top - pad.bottom);
  for (const row of rows) {
    context.beginPath(); context.arc(sx(row.x), sy(row.y), row.test ? 4 : 3, 0, Math.PI * 2);
    context.fillStyle = row.test ? "#e27a2e" : "#2864dc"; context.globalAlpha = row.test ? .9 : .55; context.fill();
  }
  context.globalAlpha = 1;
  if (!result.unstable) {
    context.strokeStyle = "#d64b59"; context.lineWidth = 4; context.beginPath();
    context.moveTo(sx(0), sy(result.bias)); context.lineTo(sx(10), sy(result.weight * 10 + result.bias)); context.stroke();
  }
}

function drawLoss(losses, unstable) {
  const {context, width, height, pad} = chartFrame(document.querySelector("#lossChart"), "training step", "loss (log scale)");
  if (!losses.length) return;
  const logged = losses.map(value => Math.log10(Math.max(value, 1e-8)));
  const min = Math.min(...logged); const max = Math.max(...logged); const range = Math.max(max - min, 1);
  const sx = index => pad.left + index / Math.max(1, logged.length - 1) * (width - pad.left - pad.right);
  const sy = value => height - pad.bottom - (value - min) / range * (height - pad.top - pad.bottom);
  context.strokeStyle = unstable ? "#d64b59" : "#0f9384"; context.lineWidth = 3; context.beginPath();
  logged.forEach((value, index) => index ? context.lineTo(sx(index), sy(value)) : context.moveTo(sx(index), sy(value))); context.stroke();
}

function number(value) {
  return Number.isFinite(value) ? (Math.abs(value) >= 1000 ? value.toExponential(2) : value.toFixed(3)) : "unstable";
}

const scenarios = [
  {title: "Shipping fee by package weight", text: "The business has published exact weight brackets and prices.", answer: "rules", why: "The relationship is known, exact, and auditable. Writing the rules directly is clearer."},
  {title: "Estimate a home's sale price", text: "Past sales contain size, location, condition, and final price, but no complete pricing formula.", answer: "learn", why: "Examples can reveal a statistical relationship that would be difficult to specify as complete rules."},
  {title: "Block access outside business hours", text: "The security policy states that access is allowed only from 08:00 through 18:00.", answer: "rules", why: "This is an explicit policy boundary, not a relationship that should be estimated from past behavior."},
  {title: "Predict equipment failure", text: "Thousands of sensor histories are labeled with whether a component failed in the following week.", answer: "learn", why: "The examples may contain a predictive pattern across many interacting measurements."}
];
let scenarioIndex = 0;

function showScenario() {
  const scenario = scenarios[scenarioIndex];
  document.querySelector("#scenarioTitle").textContent = scenario.title;
  document.querySelector("#scenarioText").textContent = scenario.text;
  document.querySelector("#scenarioFeedback").textContent = "";
  document.querySelector("#nextScenario").hidden = true;
  document.querySelectorAll(".scenario-choice").forEach(button => button.disabled = false);
}

document.querySelectorAll(".scenario-choice").forEach(button => button.addEventListener("click", () => {
  const scenario = scenarios[scenarioIndex];
  const correct = button.dataset.answer === scenario.answer;
  document.querySelector("#scenarioFeedback").textContent = `${correct ? "Good choice." : "Consider the mechanism."} ${scenario.why}`;
  document.querySelectorAll(".scenario-choice").forEach(item => item.disabled = true);
  document.querySelector("#nextScenario").hidden = false;
}));
document.querySelector("#nextScenario").addEventListener("click", () => {scenarioIndex = (scenarioIndex + 1) % scenarios.length; showScenario();});

const roleSequence = ["feature", "label", "prediction"];
let roleIndex = 0;
document.querySelectorAll(".role-grid button").forEach(button => button.addEventListener("click", () => {
  const expected = roleSequence[roleIndex];
  if (button.dataset.role === expected) {
    button.classList.add("correct"); button.disabled = true; roleIndex += 1;
    if (roleIndex === roleSequence.length) {
      document.querySelector("#rolePrompt").textContent = "All three roles are identified.";
      document.querySelector("#roleFeedback").textContent = "The feature enters the model, the label supplies the known answer during training, and the prediction is the model's output.";
    } else {
      document.querySelector("#rolePrompt").innerHTML = `Now select the <strong>${roleSequence[roleIndex]}</strong>.`;
      document.querySelector("#roleFeedback").textContent = "Correct.";
    }
  } else document.querySelector("#roleFeedback").textContent = `That value is the ${button.dataset.role}. Try the ${expected}.`;
}));

function drawConceptLine() {
  const weight = Number(document.querySelector("#lineWeight").value);
  const bias = Number(document.querySelector("#lineBias").value);
  document.querySelector("#lineWeightValue").value = weight.toFixed(1);
  document.querySelector("#lineBiasValue").value = bias.toFixed(1);
  document.querySelector("#linePrediction").textContent = (weight * 4 + bias).toFixed(1);
  const canvas = document.querySelector("#lineConceptChart"), context = canvas.getContext("2d");
  const width = canvas.width, height = canvas.height, pad = 35;
  context.clearRect(0, 0, width, height); context.fillStyle = "#fff"; context.fillRect(0, 0, width, height);
  context.strokeStyle = "#dbe3ec"; context.lineWidth = 1;
  const sx = x => pad + x / 10 * (width - 2 * pad); const sy = y => height - pad - (y + 20) / 100 * (height - 2 * pad);
  context.beginPath(); context.moveTo(sx(0), sy(0)); context.lineTo(sx(10), sy(0)); context.stroke();
  context.beginPath(); context.moveTo(sx(0), sy(-20)); context.lineTo(sx(0), sy(80)); context.stroke();
  context.strokeStyle = "#2864dc"; context.lineWidth = 4; context.beginPath(); context.moveTo(sx(0), sy(bias)); context.lineTo(sx(10), sy(weight * 10 + bias)); context.stroke();
  context.fillStyle = "#d64b59"; context.beginPath(); context.arc(sx(4), sy(weight * 4 + bias), 6, 0, Math.PI * 2); context.fill();
  const tilt = weight > 0 ? "upward" : weight < 0 ? "downward" : "not at all";
  document.querySelector("#lineExplanation").textContent = `The weight tilts the line ${tilt}. The bias makes it cross the vertical axis at ${bias.toFixed(1)}.`;
}
document.querySelector("#lineWeight").addEventListener("input", drawConceptLine);
document.querySelector("#lineBias").addEventListener("input", drawConceptLine);

const mseLabels = [10, 20, 30];
const msePredictions = [8, 23, 30];
function drawMse() {
  const body = document.querySelector("#mseRows"); body.innerHTML = "";
  const sliderArea = document.querySelector("#mseSliders"); sliderArea.innerHTML = "";
  let sum = 0;
  mseLabels.forEach((label, index) => {
    const residual = msePredictions[index] - label, squared = residual * residual; sum += squared;
    body.insertAdjacentHTML("beforeend", `<tr><td>${index + 1}</td><td>${label}</td><td>${msePredictions[index]}</td><td>${residual}</td><td>${squared}</td></tr>`);
    const control = document.createElement("label"); control.innerHTML = `Prediction ${index + 1}: <output>${msePredictions[index]}</output><input type="range" min="0" max="50" step="1" value="${msePredictions[index]}">`;
    control.querySelector("input").addEventListener("input", event => {msePredictions[index] = Number(event.target.value); drawMse();}); sliderArea.appendChild(control);
  });
  const mse = sum / mseLabels.length; document.querySelector("#mseValue").textContent = mse.toFixed(2);
  const largest = mseLabels.map((label, index) => (msePredictions[index] - label) ** 2).indexOf(Math.max(...mseLabels.map((label, index) => (msePredictions[index] - label) ** 2)));
  document.querySelector("#mseExplanation").textContent = `Example ${largest + 1} contributes the most squared error. MSE is ${mse.toFixed(2)}; moving that prediction toward its label will have the largest immediate effect.`;
}

let stepWeight = 0;
function updateStep(message) {
  const prediction = stepWeight * 2, error = prediction - 10, loss = error ** 2, gradient = 2 * error * 2;
  document.querySelector("#stepWeight").textContent = stepWeight.toFixed(2); document.querySelector("#stepPrediction").textContent = prediction.toFixed(2);
  document.querySelector("#stepLoss").textContent = loss.toFixed(2); document.querySelector("#stepGradient").textContent = gradient.toFixed(2);
  if (message) document.querySelector("#stepExplanation").textContent = message;
}
document.querySelector("#stepRate").addEventListener("input", event => document.querySelector("#stepRateValue").value = Number(event.target.value).toFixed(3));
document.querySelector("#takeStep").addEventListener("click", () => {
  const beforePrediction = stepWeight * 2, beforeError = beforePrediction - 10, beforeLoss = beforeError ** 2, gradient = 4 * beforeError;
  const change = Number(document.querySelector("#stepRate").value) * gradient; stepWeight -= change;
  const afterLoss = (stepWeight * 2 - 10) ** 2;
  updateStep(`The update subtracted ${change.toFixed(2)} from the weight. Loss moved from ${beforeLoss.toFixed(2)} to ${afterLoss.toFixed(2)}${afterLoss < beforeLoss ? ", so this step helped." : ", so this step was too large and hurt."}`);
});
document.querySelector("#resetStep").addEventListener("click", () => {stepWeight = 0; updateStep("The gradient is negative, so subtracting it will increase the weight and move the prediction toward 10.");});

document.querySelectorAll(".leak-scenarios button").forEach(button => button.addEventListener("click", () => {
  document.querySelectorAll(".leak-scenarios button").forEach(item => item.classList.remove("correct", "wrong"));
  const leak = button.dataset.leak === "yes"; button.classList.add(leak ? "wrong" : "correct");
  document.querySelector("#leakFeedback").textContent = leak ? "Leakage: information from the intended test population influenced training or model selection, so the final score is no longer independent." : "Trustworthy design: validation supports choices while the untouched test set remains an independent final check.";
}));

function updateLabels() {
  const rate = 10 ** Number(controls.learningRate.value);
  document.querySelector("#learningRateValue").value = rate.toFixed(rate < .001 ? 5 : 3);
  document.querySelector("#epochsValue").value = controls.epochs.value;
  document.querySelector("#samplesValue").value = controls.samples.value;
  document.querySelector("#noiseValue").value = controls.noise.value;
}

function run() {
  const rate = 10 ** Number(controls.learningRate.value);
  const rows = dataset(Number(controls.samples.value), Number(controls.noise.value), controls.relationship.value, controls.outlier.checked);
  const result = train(rows, rate, Number(controls.epochs.value));
  document.querySelector("#weightMetric").textContent = number(result.weight);
  document.querySelector("#biasMetric").textContent = number(result.bias);
  document.querySelector("#trainLossMetric").textContent = number(result.trainLoss);
  document.querySelector("#testLossMetric").textContent = number(result.testLoss);
  drawFit(rows, result); drawLoss(result.losses, result.unstable);
  const observation = document.querySelector("#observation");
  if (result.unstable) observation.innerHTML = "<strong>The training became unstable.</strong> The steps were so large that the model moved farther away on each update. Lower the learning rate and try again.";
  else if (controls.relationship.value === "quadratic") observation.innerHTML = "<strong>The model found its best straight-line compromise, but the pattern is curved.</strong> This is limited model capacity: more steps cannot turn a line into a curve.";
  else if (controls.outlier.checked) { const baseline=train(dataset(Number(controls.samples.value),Number(controls.noise.value),controls.relationship.value,false),rate,Number(controls.epochs.value)); observation.innerHTML=`<strong>One unusual training label pulled the fitted line.</strong> Adding 70 to that label contributes roughly 4,900 squared-error units before refitting. The learned weight moved from ${number(baseline.weight)} without the outlier to ${number(result.weight)} with it.`; }
  else if (Number(controls.noise.value) >= 5) observation.innerHTML = "<strong>The trend is learnable, but considerable uncertainty remains.</strong> Noise represents variation this single input cannot explain.";
  else observation.innerHTML = `<strong>The line learned from examples.</strong> Its weight is ${number(result.weight)}; the hidden relationship used to create the baseline data has a weight of 3.5.`;
}

Object.values(controls).forEach(control => control.addEventListener("input", updateLabels));
document.querySelector("#trainButton").addEventListener("click", run);
document.querySelector("#resetButton").addEventListener("click", () => {
  controls.learningRate.value = -2; controls.epochs.value = 500; controls.samples.value = 100;
  controls.noise.value = 1.5; controls.relationship.value = "linear"; controls.outlier.checked = false;
  updateLabels(); run();
});
document.querySelectorAll(".quiz").forEach(quiz => quiz.querySelectorAll("button").forEach(button => button.addEventListener("click", () => {
  quiz.querySelectorAll("button").forEach(item => item.classList.remove("correct", "wrong"));
  const correct = button.dataset.choice === quiz.dataset.answer;
  button.classList.add(correct ? "correct" : "wrong");
  quiz.querySelector(".feedback").textContent = correct ? "Correct — you have the idea." : "Not quite. Revisit the explanation above and try again.";
})));
updateLabels(); run();
showScenario(); drawConceptLine(); drawMse(); updateStep();

function completionState() {
  const done = CourseProgress.isComplete(1);
  document.querySelector("#completeLesson").textContent = done ? "Lesson 1 completed ✓" : "Mark Lesson 1 complete";
  document.querySelector("#completionStatus").textContent = done ? "Your course dashboard has been updated." : "Completion is stored in this browser.";
}
document.querySelector("#completeLesson").addEventListener("click", () => { CourseProgress.complete(1); completionState(); });
window.addEventListener("course-progress", completionState);
completionState();
