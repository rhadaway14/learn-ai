"use strict";

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
  const random = seededRandom(42);
  const rows = Array.from({length: count}, (_, index) => {
    const x = random() * 10;
    const signal = relationship === "linear" ? 3.5 * x + 2 : x * x + 2;
    return {x, y: signal + normal(random) * noise, test: index % 5 === 0};
  });
  if (outlier) rows[Math.floor(rows.length / 2)].y += 70;
  return rows;
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
