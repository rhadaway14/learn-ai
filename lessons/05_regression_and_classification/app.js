"use strict";

CourseProgress.visit(5);

document.querySelectorAll(".readiness-choices button").forEach(button=>button.addEventListener("click",()=>{
  document.querySelectorAll(".readiness-choices button").forEach(item=>item.classList.remove("correct","wrong"));
  const correct=button.dataset.correct==="true";button.classList.add(correct?"correct":"wrong");
  document.querySelector("#readinessFeedback").textContent=correct
    ?"Correct. Planned integrations exist at intake; the completion date and final delay code are future information."
    :"That field is created after intake, so using it would let the model peek into the future. Try the information genuinely available before delivery begins.";
}));

function bindChoiceCards(selector,labels){
  document.querySelectorAll(selector).forEach(card=>card.querySelectorAll("button").forEach(button=>button.addEventListener("click",()=>{
    card.querySelectorAll("button").forEach(item=>item.classList.remove("correct","wrong"));
    const correct=button.dataset.choice===card.dataset.answer;button.classList.add(correct?"correct":"wrong");
    card.querySelector(".feedback").textContent=correct?labels[card.dataset.answer]:"Not quite. Focus on the required output and what information exists at prediction time.";
  })));
}
bindChoiceCards(".task-grid article",{regression:"Correct — the requested output is a numeric amount.",classification:"Correct — the requested output is a category or decision class."});
bindChoiceCards(".leak-grid article",{safe:"Correct — validation remains separated from label and test information.",leak:"Correct — this design exposes future, repeated-entity, or test-tuning information."});

const train=[{x:1,y:2},{x:2,y:4.4},{x:3,y:4.2},{x:4,y:7.2},{x:5,y:7.0},{x:6,y:9.5}];
const test=[{x:1.5,y:2.8},{x:2.5,y:3.9},{x:3.5,y:5.2},{x:4.5,y:6.4},{x:5.5,y:7.8}];
const trainMean=train.reduce((sum,point)=>sum+point.y,0)/train.length;
const xMean=train.reduce((sum,point)=>sum+point.x,0)/train.length;
const slope=train.reduce((sum,point)=>sum+(point.x-xMean)*(point.y-trainMean),0)/train.reduce((sum,point)=>sum+(point.x-xMean)**2,0);
const intercept=trainMean-slope*xMean;
function polynomialPrediction(x){return train.reduce((sum,point,index)=>sum+point.y*train.reduce((product,other,otherIndex)=>index===otherIndex?product:product*(x-other.x)/(point.x-other.x),1),0);}
const models={
  baseline:{predict:()=>trainMean,color:"#8290a4",description:"The mean baseline ignores every feature. It is intentionally simple: a useful model must beat it on unseen projects."},
  linear:{predict:x=>slope*x+intercept,color:"#2864dc",description:"The linear trend accepts some training error but captures the stable relationship. Its lower test error is evidence of generalization."},
  overfit:{predict:polynomialPrediction,color:"#d64b59",description:"The flexible curve passes through every training point, producing zero training error. Between those points it bends toward noise and performs worse on unseen projects."}
};
function regressionMetrics(points,predict){
  const errors=points.map(point=>predict(point.x)-point.y),mae=errors.reduce((sum,error)=>sum+Math.abs(error),0)/errors.length,rmse=Math.sqrt(errors.reduce((sum,error)=>sum+error**2,0)/errors.length),targetMean=points.reduce((sum,point)=>sum+point.y,0)/points.length,total=points.reduce((sum,point)=>sum+(point.y-targetMean)**2,0),residual=errors.reduce((sum,error)=>sum+error**2,0);
  return {mae,rmse,r2:1-residual/total};
}
function drawRegression(name){
  const model=models[name],trainMetrics=regressionMetrics(train,model.predict),testMetrics=regressionMetrics(test,model.predict),canvas=document.querySelector("#regressionChart"),context=canvas.getContext("2d"),pad=48,width=canvas.width-pad*2,height=canvas.height-pad*2,mapX=x=>pad+(x-.5)/6*width,mapY=y=>pad+height-Math.max(0,Math.min(11,y))/11*height;
  context.clearRect(0,0,canvas.width,canvas.height);context.strokeStyle="#dbe3ec";context.lineWidth=1;context.beginPath();context.moveTo(pad,pad);context.lineTo(pad,pad+height);context.lineTo(pad+width,pad+height);context.stroke();
  context.fillStyle="#637083";context.font="12px system-ui";context.textAlign="center";for(let x=1;x<=6;x++)context.fillText(`${x}`,mapX(x),pad+height+22);context.save();context.translate(15,pad+height/2);context.rotate(-Math.PI/2);context.fillText("effort units",0,0);context.restore();context.fillText("project complexity",pad+width/2,canvas.height-8);
  context.strokeStyle=model.color;context.lineWidth=3;context.beginPath();for(let step=0;step<=120;step++){const x=.5+step/20,y=model.predict(x);if(step===0)context.moveTo(mapX(x),mapY(y));else context.lineTo(mapX(x),mapY(y));}context.stroke();
  [{points:train,color:"#2864dc",label:"train"},{points:test,color:"#e27a2e",label:"test"}].forEach(group=>group.points.forEach(point=>{context.fillStyle=group.color;context.beginPath();context.arc(mapX(point.x),mapY(point.y),6,0,Math.PI*2);context.fill();}));context.textAlign="left";context.fillStyle="#2864dc";context.fillText("● training",pad+8,pad+14);context.fillStyle="#e27a2e";context.fillText("● unseen test",pad+95,pad+14);
  document.querySelector("#trainMae").textContent=trainMetrics.mae.toFixed(2);document.querySelector("#testMae").textContent=testMetrics.mae.toFixed(2);document.querySelector("#testRmse").textContent=testMetrics.rmse.toFixed(2);document.querySelector("#testR2").textContent=testMetrics.r2.toFixed(2);document.querySelector("#regressionMeaning").textContent=model.description;
}
document.querySelectorAll(".model-buttons button").forEach(button=>button.addEventListener("click",()=>{document.querySelectorAll(".model-buttons button").forEach(item=>item.classList.toggle("active",item===button));drawRegression(button.dataset.model);}));

const cases=[
  {id:"P1",score:.92,positive:true},{id:"P2",score:.81,positive:true},{id:"P3",score:.75,positive:false},{id:"P4",score:.72,positive:true},{id:"P5",score:.66,positive:false},{id:"P6",score:.61,positive:true},{id:"P7",score:.54,positive:false},{id:"P8",score:.48,positive:false},{id:"P9",score:.43,positive:true},{id:"P10",score:.39,positive:false},{id:"P11",score:.35,positive:false},{id:"P12",score:.30,positive:false},{id:"P13",score:.28,positive:true},{id:"P14",score:.25,positive:false},{id:"P15",score:.20,positive:false},{id:"P16",score:.15,positive:false},{id:"P17",score:.12,positive:false},{id:"P18",score:.08,positive:false},{id:"P19",score:.05,positive:false},{id:"P20",score:.03,positive:false}
];
function outcomesAt(threshold){
  return cases.reduce((counts,item)=>{const predicted=item.score>=threshold;if(predicted&&item.positive)counts.tp++;else if(predicted)counts.fp++;else if(item.positive)counts.fn++;else counts.tn++;return counts;},{tp:0,fp:0,fn:0,tn:0});
}
function safeDivide(numerator,denominator){return denominator?numerator/denominator:0;}
function updateThreshold(){
  const threshold=Number(document.querySelector("#classificationThreshold").value),fpCost=Number(document.querySelector("#falsePositiveCost").value),fnCost=Number(document.querySelector("#falseNegativeCost").value),counts=outcomesAt(threshold),precision=safeDivide(counts.tp,counts.tp+counts.fp),recall=safeDivide(counts.tp,counts.tp+counts.fn),accuracy=(counts.tp+counts.tn)/cases.length,specificity=safeDivide(counts.tn,counts.tn+counts.fp),f1=safeDivide(2*precision*recall,precision+recall),cost=counts.fp*fpCost+counts.fn*fnCost;
  document.querySelector("#thresholdValue").value=threshold.toFixed(2);document.querySelector("#falsePositiveCostValue").value=fpCost;document.querySelector("#falseNegativeCostValue").value=fnCost;
  document.querySelector("#scoreRows").innerHTML=cases.map(item=>{const predicted=item.score>=threshold;return `<li class="score-item ${predicted?"predicted":""} ${item.positive?"actual-positive":"actual-negative"}" aria-label="${item.id}: score ${item.score.toFixed(2)}, actually ${item.positive?"late":"on time"}, predicted ${predicted?"escalate":"do not escalate"}"><strong>${item.score.toFixed(2)}</strong><small>${predicted?"Escalate":"No action"} · actual ${item.positive?"late":"on time"}</small></li>`;}).join("");
  for(const [key,value] of Object.entries(counts))document.querySelector(`#${key}Count`).textContent=value;
  const percent=value=>`${Math.round(value*100)}%`;document.querySelector("#accuracyValue").textContent=percent(accuracy);document.querySelector("#precisionValue").textContent=percent(precision);document.querySelector("#recallValue").textContent=percent(recall);document.querySelector("#f1Value").textContent=percent(f1);document.querySelector("#specificityValue").textContent=percent(specificity);document.querySelector("#costValue").textContent=cost;
  const candidates=Array.from({length:17},(_,index)=>Number((.1+index*.05).toFixed(2))).map(value=>{const c=outcomesAt(value);return {threshold:value,cost:c.fp*fpCost+c.fn*fnCost};}),best=candidates.reduce((winner,item)=>item.cost<winner.cost?item:winner);
  document.querySelector("#thresholdMeaning").textContent=Math.abs(best.threshold-threshold)<.001
    ?`This is the lowest-cost tested operating point under the current assumptions: ${counts.fp} false alarms × ${fpCost} plus ${counts.fn} misses × ${fnCost} = ${cost}. Validate it on untouched data before release.`
    :`Current error cost is ${cost}. Under these simplified costs, threshold ${best.threshold.toFixed(2)} has a lower tested cost of ${best.cost}. Change the costs and the preferred operating point may move.`;
}
document.querySelectorAll("#classificationThreshold, #falsePositiveCost, #falseNegativeCost").forEach(input=>input.addEventListener("input",updateThreshold));

document.querySelectorAll(".quiz").forEach(quiz=>quiz.querySelectorAll("button").forEach(button=>button.addEventListener("click",()=>{
  quiz.querySelectorAll("button").forEach(item=>item.classList.remove("correct","wrong"));const correct=button.dataset.choice===quiz.dataset.answer;button.classList.add(correct?"correct":"wrong");quiz.querySelector(".feedback").textContent=correct?"Correct — you can connect the metric to the decision.":"Not quite. Revisit the related example and try again.";
})));

function completionState(){const done=CourseProgress.isComplete(5);document.querySelector("#completeLesson").textContent=done?"Lesson 5 completed ✓":"Mark Lesson 5 complete";document.querySelector("#completionStatus").textContent=done?"Foundation Gate A is recorded on your course dashboard.":"Completion is stored in this browser.";}
document.querySelector("#completeLesson").addEventListener("click",()=>{CourseProgress.complete(5);completionState();});window.addEventListener("course-progress",completionState);

drawRegression("baseline");updateThreshold();completionState();
