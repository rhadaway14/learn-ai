"use strict";

CourseProgress.visit(4);

document.querySelectorAll(".readiness-choices button").forEach(button=>button.addEventListener("click",()=>{
  document.querySelectorAll(".readiness-choices button").forEach(item=>item.classList.remove("correct","wrong"));
  const correct=button.dataset.correct==="true";
  button.classList.add(correct?"correct":"wrong");
  document.querySelector("#readinessFeedback").textContent=correct
    ?"Correct. A probability describes a pattern across comparable cases; either outcome can occur once."
    :"Not quite. A 70% forecast still allows a dry outcome 30% of the time. Judge it across many comparable forecasts.";
}));

const distributions={
  consistent:{probabilities:[.05,.20,.50,.20,.05],description:"Most deliveries cluster near 3 days. Planning is easier because extreme outcomes are uncommon."},
  variable:{probabilities:[.25,0,.50,0,.25],description:"The average is still 3 days, but half of deliveries land at an extreme. The mean alone hides that operational risk."}
};

function drawDistribution(name){
  const outcomes=[1,2,3,4,5],distribution=distributions[name],probabilities=distribution.probabilities;
  const mean=outcomes.reduce((sum,value,index)=>sum+value*probabilities[index],0);
  const variance=outcomes.reduce((sum,value,index)=>sum+((value-mean)**2)*probabilities[index],0);
  const canvas=document.querySelector("#distributionChart"),context=canvas.getContext("2d"),pad=46,width=canvas.width-pad*2,height=canvas.height-pad*2;
  context.clearRect(0,0,canvas.width,canvas.height);
  context.strokeStyle="#dbe3ec";context.lineWidth=1;context.beginPath();context.moveTo(pad,pad);context.lineTo(pad,pad+height);context.lineTo(pad+width,pad+height);context.stroke();
  const slot=width/outcomes.length,barWidth=slot*.58;
  probabilities.forEach((probability,index)=>{
    const x=pad+slot*index+(slot-barWidth)/2,barHeight=probability/.55*height,y=pad+height-barHeight;
    context.fillStyle=name==="consistent"?"#2864dc":"#d68c27";context.fillRect(x,y,barWidth,barHeight);
    context.fillStyle="#637083";context.font="13px system-ui";context.textAlign="center";context.fillText(`${Math.round(probability*100)}%`,x+barWidth/2,y-8);context.fillText(`${outcomes[index]} day${outcomes[index]===1?"":"s"}`,x+barWidth/2,pad+height+22);
  });
  context.textAlign="left";
  document.querySelector("#expectedValue").textContent=mean.toFixed(1);
  document.querySelector("#varianceValue").textContent=variance.toFixed(2)+" days²";
  document.querySelector("#stdValue").textContent=Math.sqrt(variance).toFixed(2)+" days";
  document.querySelector("#distributionMeaning").textContent=distribution.description;
}

document.querySelectorAll(".distribution-buttons button").forEach(button=>button.addEventListener("click",()=>{
  document.querySelectorAll(".distribution-buttons button").forEach(item=>item.classList.toggle("active",item===button));
  drawDistribution(button.dataset.distribution);
}));

function seededRandom(seed){let state=seed>>>0;return()=>{state=(1664525*state+1013904223)>>>0;return state/4294967296;};}
function normalSamples(count,bias){
  const random=seededRandom(4100+count+(bias?97:0)),samples=[];
  while(samples.length<count){const u=Math.max(random(),1e-12),v=random(),radius=Math.sqrt(-2*Math.log(u));samples.push(50+10*radius*Math.cos(2*Math.PI*v)+(bias?6:0));if(samples.length<count)samples.push(50+10*radius*Math.sin(2*Math.PI*v)+(bias?6:0));}
  return samples;
}

let selectedSampleSize=20;
function drawSample(){
  const biased=document.querySelector("#sampleBias").checked,samples=normalSamples(selectedSampleSize,biased),mean=samples.reduce((a,b)=>a+b,0)/samples.length;
  const variance=samples.reduce((sum,value)=>sum+(value-mean)**2,0)/(samples.length-1),standardDeviation=Math.sqrt(variance),standardError=standardDeviation/Math.sqrt(samples.length),margin=1.96*standardError,low=mean-margin,high=mean+margin;
  const bins=20,min=20,max=85,counts=Array(bins).fill(0),binWidth=(max-min)/bins;
  samples.forEach(value=>{const index=Math.max(0,Math.min(bins-1,Math.floor((value-min)/binWidth)));counts[index]+=1;});
  const canvas=document.querySelector("#sampleChart"),context=canvas.getContext("2d"),pad=48,width=canvas.width-pad*2,height=canvas.height-pad*2,maxCount=Math.max(...counts);
  context.clearRect(0,0,canvas.width,canvas.height);context.strokeStyle="#dbe3ec";context.beginPath();context.moveTo(pad,pad);context.lineTo(pad,pad+height);context.lineTo(pad+width,pad+height);context.stroke();
  counts.forEach((count,index)=>{const x=pad+index/bins*width,barWidth=width/bins-2,barHeight=count/maxCount*(height-25);context.fillStyle=biased?"#d68c27":"#2864dc";context.fillRect(x,pad+height-barHeight,barWidth,barHeight);});
  const mapX=value=>pad+(value-min)/(max-min)*width;
  [{value:50,color:"#0f9384",label:"population mean 50"},{value:mean,color:"#d64b59",label:`sample mean ${mean.toFixed(1)}`}].forEach(marker=>{context.strokeStyle=marker.color;context.lineWidth=3;context.beginPath();context.moveTo(mapX(marker.value),pad);context.lineTo(mapX(marker.value),pad+height);context.stroke();context.fillStyle=marker.color;context.font="12px system-ui";context.fillText(marker.label,Math.min(mapX(marker.value)+6,canvas.width-145),pad+14);});
  context.fillStyle="#637083";context.font="12px system-ui";context.textAlign="center";[20,30,40,50,60,70,80].forEach(value=>context.fillText(value,mapX(value),pad+height+22));context.textAlign="left";
  document.querySelector("#sampleMean").textContent=mean.toFixed(2);
  document.querySelector("#ciRange").textContent=`${low.toFixed(2)} to ${high.toFixed(2)}`;
  document.querySelector("#ciWidth").textContent=(high-low).toFixed(2);
  document.querySelector("#sampleDiagnosis").textContent=biased
    ?`The interval is based on ${selectedSampleSize.toLocaleString()} observations and may be narrow, but the collection process shifted the sample upward. Precision does not guarantee accuracy.`
    :`This representative sample centers near the population mean. Increasing size reduces the standard error and makes the interval narrower, though random variation never disappears completely.`;
}

document.querySelectorAll(".size-buttons button").forEach(button=>button.addEventListener("click",()=>{
  selectedSampleSize=Number(button.dataset.size);document.querySelectorAll(".size-buttons button").forEach(item=>item.classList.toggle("active",item===button));drawSample();
}));
document.querySelector("#sampleBias").addEventListener("change",drawSample);

function updateBayes(){
  const population=10000,prevalence=Number(document.querySelector("#prevalence").value)/100,sensitivity=Number(document.querySelector("#sensitivity").value)/100,falsePositiveRate=Number(document.querySelector("#falsePositive").value)/100;
  const defective=population*prevalence,good=population-defective,truePositives=defective*sensitivity,falsePositives=good*falsePositiveRate,totalPositives=truePositives+falsePositives,posterior=totalPositives?truePositives/totalPositives:0;
  document.querySelector("#prevalenceValue").value=`${(prevalence*100).toFixed(1).replace(".0","")}%`;document.querySelector("#sensitivityValue").value=`${Math.round(sensitivity*100)}%`;document.querySelector("#falsePositiveValue").value=`${Math.round(falsePositiveRate*100)}%`;
  document.querySelector("#truePositiveCount").textContent=Math.round(truePositives).toLocaleString();document.querySelector("#falsePositiveCount").textContent=Math.round(falsePositives).toLocaleString();document.querySelector("#positiveCount").textContent=Math.round(totalPositives).toLocaleString();document.querySelector("#posteriorValue").textContent=`${(posterior*100).toFixed(1)}%`;
  document.querySelector("#bayesMeaning").textContent=`Among flagged components, about ${Math.round(posterior*100)} in 100 are actually defective. The rest are false alarms. Changing the base rate can change this result dramatically without changing sensor sensitivity.`;
}
document.querySelectorAll("#prevalence, #sensitivity, #falsePositive").forEach(input=>input.addEventListener("input",updateBayes));

function updateCalibration(){
  const forecast=Number(document.querySelector("#forecastProbability").value),observed=Number(document.querySelector("#observedOutcomes").value),gap=observed-forecast,absoluteGap=Math.abs(gap);
  document.querySelector("#forecastValue").value=`${forecast}%`;document.querySelector("#observedValue").value=`${observed} of 100`;document.querySelector("#forecastBar").style.width=`${forecast}%`;document.querySelector("#observedBar").style.width=`${observed}%`;document.querySelector("#calibrationGap").textContent=`${gap>0?"+":""}${gap} points`;
  document.querySelector("#calibrationMeaning").textContent=absoluteGap<=5
    ?"Roughly calibrated in this cohort: forecast confidence and observed frequency are close. A real audit would need many more cases and several probability ranges."
    :gap<0?"Overconfident: the predicted probability is higher than the observed frequency. Decisions may take more risk than results justify.":"Underconfident: the event occurs more often than predicted. The model systematically understates this outcome's probability.";
}
document.querySelectorAll("#forecastProbability, #observedOutcomes").forEach(input=>input.addEventListener("input",updateCalibration));

document.querySelectorAll(".quiz").forEach(quiz=>quiz.querySelectorAll("button").forEach(button=>button.addEventListener("click",()=>{
  quiz.querySelectorAll("button").forEach(item=>item.classList.remove("correct","wrong"));const correct=button.dataset.choice===quiz.dataset.answer;button.classList.add(correct?"correct":"wrong");quiz.querySelector(".feedback").textContent=correct?"Correct — you can connect the idea to a decision.":"Not quite. Revisit the related example, then try again.";
})));

function completionState(){const done=CourseProgress.isComplete(4);document.querySelector("#completeLesson").textContent=done?"Lesson 4 completed ✓":"Mark Lesson 4 complete";document.querySelector("#completionStatus").textContent=done?"Your course dashboard has been updated.":"Completion is stored in this browser.";}
document.querySelector("#completeLesson").addEventListener("click",()=>{CourseProgress.complete(4);completionState();});window.addEventListener("course-progress",completionState);

drawDistribution("consistent");drawSample();updateBayes();updateCalibration();completionState();
