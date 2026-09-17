"use strict";

const test=require("node:test");
const assert=require("node:assert/strict");
const lesson01=require("../../lessons/01_linear_regression/logic.js");
const lesson03=require("../../lessons/03_loss_functions_and_optimization/logic.js");
const lesson09=require("../../lessons/09_train_and_evaluate_a_neural_network/logic.js");
const lesson10=require("../../lessons/10_regularization_and_generalization/logic.js");

test("Lesson 1 outlier belongs to training evidence",()=>{
  const rows=lesson01.dataset(100,1.5,"linear",true),outlier=rows.find(row=>row.outlier);
  assert.ok(outlier,"an outlier is identified");
  assert.equal(outlier.test,false,"the outlier can influence fitted parameters");
});

test("Lesson 3 epsilon changes finite-difference error",()=>{
  const coarse=lesson03.finiteDifference(1,1),fine=lesson03.finiteDifference(1,.05);
  assert.ok(coarse.error>.01);
  assert.ok(fine.error<coarse.error);
});

test("Lesson 9 curves encode distinct optimization behavior",()=>{
  const seeds=[11,23,47],bestEpochs=seeds.map(seed=>{const s=lesson09.trainingSeries("good",seed);return s.validation.indexOf(Math.min(...s.validation))+1;});
  assert.ok(new Set(bestEpochs).size>1,"seeds change the selected checkpoint");
  const slow=lesson09.trainingSeries("slow",11),secondDifferences=slow.train.slice(2).map((v,i)=>v-2*slow.train[i+1]+slow.train[i]);
  assert.ok(secondDifferences.some(value=>Math.abs(value)>1e-4),"slow training is not a straight line");
  const good=lesson09.trainingSeries("good",11),high=lesson09.trainingSeries("high",11);
  assert.ok(Math.min(...high.validation)>Math.min(...good.validation)+.08,"unstable rate is visibly worse");
});

test("Lesson 9 precision and recall answer different questions",()=>{
  const metrics=lesson09.matrixMetrics([[630,45,25],[55,150,25],[12,28,30]]);
  assert.equal(metrics.total,1000);
  assert.equal(metrics.accuracy,.81);
  assert.equal(metrics.severeRecall,30/70);
  assert.equal(metrics.severePrecision,30/80);
  assert.notEqual(metrics.severeRecall,metrics.severePrecision);
});

test("Lesson 10 errors are calculated from the displayed fitted model",()=>{
  const flexible=lesson10.fitModel(10,10,2,0),constrained=lesson10.fitModel(10,10,2,4);
  assert.ok(flexible.trainError<1e-10,"high capacity tracks the training observations");
  assert.ok(flexible.validationError>flexible.trainError+.1,"separate validation evidence exposes overfit");
  assert.ok(constrained.trainError>flexible.trainError,"regularization changes the fitted model and its measured error");
});

test("Lesson 10 capacity control can demonstrate all three fit diagnoses",()=>{
  const evidence=18,noise=1,regularization=0;
  const reference=lesson10.fitModel(10,evidence,noise,regularization).trainError;
  const diagnoses=new Set(Array.from({length:10},(_,i)=>lesson10.diagnoseFit(lesson10.fitModel(i+1,evidence,noise,regularization),reference)));
  assert.deepEqual([...diagnoses].sort(),["Overfitting risk","Underfitting","Useful balance"].sort());
});
