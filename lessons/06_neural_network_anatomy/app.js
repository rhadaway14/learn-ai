"use strict";

CourseProgress.visit(6);

const formatNumber=value=>Number(value).toFixed(2).replace("-","−");
const activationFunctions={
  relu:{value:z=>Math.max(0,z),slope:z=>z>0?1:0,label:"ReLU"},
  sigmoid:{value:z=>1/(1+Math.exp(-z)),slope:z=>{const value=1/(1+Math.exp(-z));return value*(1-value);},label:"sigmoid"},
  tanh:{value:z=>Math.tanh(z),slope:z=>1-Math.tanh(z)**2,label:"tanh"},
  linear:{value:z=>z,slope:()=>1,label:"linear"}
};

document.querySelectorAll(".readiness-choices button").forEach(button=>button.addEventListener("click",()=>{
  document.querySelectorAll(".readiness-choices button").forEach(item=>item.classList.remove("correct","wrong"));
  const correct=button.dataset.correct==="true";
  button.classList.add(correct?"correct":"wrong");
  document.querySelector("#readinessFeedback").textContent=correct
    ?"Correct. The first axis counts examples; the second counts features describing each example."
    :"Not quite. Return to Lesson 2's rule: name every axis before interpreting the numbers.";
}));

function updateNeuron(){
  const x1=Number(document.querySelector("#x1").value),w1=Number(document.querySelector("#w1").value),x2=Number(document.querySelector("#x2").value),w2=Number(document.querySelector("#w2").value),bias=Number(document.querySelector("#neuronBias").value),activationName=document.querySelector("#neuronActivation").value,z=x1*w1+x2*w2+bias,activation=activationFunctions[activationName],output=activation.value(z);
  [["x1Value",x1],["w1Value",w1],["x2Value",x2],["w2Value",w2],["biasValue",bias]].forEach(([id,value])=>document.querySelector(`#${id}`).value=Number(value).toFixed(1).replace("-","−"));
  document.querySelector("#neuronTerms").textContent=`(${x1.toFixed(1)} × ${w1.toFixed(1)}) + (${x2.toFixed(1)} × ${w2.toFixed(1)}) + ${bias.toFixed(1)}`.replaceAll("-","−");
  document.querySelector("#zValue").textContent=`z = ${formatNumber(z)}`;
  document.querySelector("#activationValue").textContent=`${activation.label}(z) = ${formatNumber(output)}`;
  document.querySelector("#neuronMeaning").textContent=activationName==="relu"&&z<=0
    ?"The weighted evidence is non-positive, so ReLU outputs zero. This neuron sends no positive signal onward for this example."
    :activationName==="sigmoid"&&Math.abs(z)>4
      ?"The sigmoid is near an extreme and locally flat. Its output is bounded, but its learning signal can become very small."
      :`The weights control how strongly and in which direction each input contributes. The bias shifts the response before ${activation.label} transforms it.`;
}
document.querySelectorAll("#x1, #w1, #x2, #w2, #neuronBias, #neuronActivation").forEach(input=>input.addEventListener("input",updateNeuron));

function updateShape(){
  const batch=Number(document.querySelector("#batchSize").value),inputs=Number(document.querySelector("#inputWidth").value),outputs=Number(document.querySelector("#outputWidth").value),parameters=inputs*outputs+outputs;
  document.querySelector("#batchValue").value=batch;
  document.querySelector("#inputWidthValue").value=inputs;
  document.querySelector("#outputWidthValue").value=outputs;
  document.querySelector("#inputShape").textContent=`(${batch}, ${inputs})`;
  document.querySelector("#weightShape").textContent=`(${inputs}, ${outputs})`;
  document.querySelector("#biasShape").textContent=`(${outputs})`;
  document.querySelector("#outputShape").textContent=`(${batch}, ${outputs})`;
  document.querySelector("#layerParameterCount").textContent=parameters.toLocaleString();
  document.querySelector("#shapeMeaning").textContent=`The batch size changes how many examples flow together, but not how many parameters the layer learns. Parameters = ${inputs} × ${outputs} weights + ${outputs} biases.`;
}
document.querySelectorAll("#batchSize, #inputWidth, #outputWidth").forEach(input=>input.addEventListener("input",updateShape));

function updateActivation(){
  const z=Number(document.querySelector("#activationInput").value),canvas=document.querySelector("#activationChart"),context=canvas.getContext("2d"),pad=48,width=canvas.width-pad*2,height=canvas.height-pad*2,mapX=x=>pad+(x+6)/12*width,mapY=y=>pad+height-(y+1.5)/8*height,colors={relu:"#2864dc",sigmoid:"#d68c27",tanh:"#0f9384",linear:"#9b61c8"};
  document.querySelector("#activationInputValue").value=z.toFixed(1).replace("-","−");
  context.clearRect(0,0,canvas.width,canvas.height);
  context.strokeStyle="#dbe3ec";context.lineWidth=1;context.beginPath();context.moveTo(mapX(-6),mapY(0));context.lineTo(mapX(6),mapY(0));context.moveTo(mapX(0),mapY(-1.5));context.lineTo(mapX(0),mapY(6.5));context.stroke();
  Object.entries(activationFunctions).forEach(([name,activation])=>{context.strokeStyle=colors[name];context.lineWidth=3;context.beginPath();for(let step=0;step<=120;step++){const x=-6+step/10,y=activation.value(x);if(step===0)context.moveTo(mapX(x),mapY(y));else context.lineTo(mapX(x),mapY(y));}context.stroke();context.fillStyle=colors[name];context.beginPath();context.arc(mapX(z),mapY(activation.value(z)),5,0,Math.PI*2);context.fill();});
  context.font="12px system-ui";context.textAlign="left";let labelX=pad+8;Object.entries(colors).forEach(([name,color])=>{context.fillStyle=color;context.fillText(`● ${activationFunctions[name].label}`,labelX,pad+14);labelX+=name==="sigmoid"?90:78;});context.fillStyle="#637083";context.fillText("z",pad+width+9,mapY(0)+4);
  const values={relu:activationFunctions.relu.value(z),sigmoid:activationFunctions.sigmoid.value(z),tanh:activationFunctions.tanh.value(z),linear:z};
  Object.keys(values).forEach(name=>{document.querySelector(`#${name}Output`).textContent=formatNumber(values[name]);document.querySelector(`#${name}Slope`).textContent=`local slope ${formatNumber(activationFunctions[name].slope(z))}`;});
  document.querySelector("#activationMeaning").textContent=Math.abs(z)>=4
    ?"At this extreme input, sigmoid and tanh are close to their limits and their slopes are small. ReLU still passes positive inputs with slope 1, while negative ReLU inputs produce zero."
    :z<0
      ?"Negative inputs show the major contrast: ReLU becomes zero, sigmoid remains between 0 and 0.5, tanh remains negative, and linear passes the value unchanged."
      :"Near the center, sigmoid and tanh respond most strongly. ReLU passes positive values directly, and linear never bends the representation.";
}
document.querySelector("#activationInput").addEventListener("input",updateActivation);

let xorMode="linear";
function drawXor(){
  const canvas=document.querySelector("#xorChart"),context=canvas.getContext("2d"),pad=58,size=280,mapX=x=>pad+x*size,mapY=y=>pad+size-y*size,points=[{x:0,y:0,p:0},{x:0,y:1,p:1},{x:1,y:0,p:1},{x:1,y:1,p:0}];
  context.clearRect(0,0,canvas.width,canvas.height);
  if(xorMode==="relu"){context.fillStyle="#edf3ff";context.fillRect(mapX(0),mapY(1),size/2,size/2);context.fillRect(mapX(.5),mapY(.5),size/2,size/2);}
  context.strokeStyle="#dbe3ec";context.strokeRect(mapX(0),mapY(1),size,size);context.beginPath();context.moveTo(mapX(.5),mapY(1));context.lineTo(mapX(.5),mapY(0));context.moveTo(mapX(0),mapY(.5));context.lineTo(mapX(1),mapY(.5));context.stroke();
  if(xorMode==="linear"){context.strokeStyle="#d64b59";context.setLineDash([7,6]);context.lineWidth=3;context.beginPath();context.moveTo(mapX(0),mapY(.65));context.lineTo(mapX(1),mapY(.35));context.stroke();context.setLineDash([]);}
  points.forEach(point=>{context.fillStyle=point.p?"#2864dc":"#8290a4";context.beginPath();context.arc(mapX(point.x),mapY(point.y),12,0,Math.PI*2);context.fill();context.fillStyle="white";context.font="bold 11px system-ui";context.textAlign="center";context.fillText(point.p?"1":"0",mapX(point.x),mapY(point.y)+4);});
  context.fillStyle="#637083";context.font="13px system-ui";context.fillText("x₁",mapX(1)+25,mapY(0)+4);context.fillText("x₂",mapX(0),mapY(1)-25);
  document.querySelector("#xorMeaning").textContent=xorMode==="linear"
    ?"Any single straight line leaves at least one corner on the wrong side. Additional linear-only layers still reduce to one straight boundary."
    :"The hidden ReLU units measure disagreement in both directions. Their sum is 1 for the two unequal-input corners and 0 for the equal-input corners.";
  document.querySelector("#xorTable").innerHTML=points.map(point=>{const h1=Math.max(0,point.x-point.y),h2=Math.max(0,point.y-point.x);return `<span>(${point.x}, ${point.y}) → h = (${h1}, ${h2}) → ${h1+h2}</span>`;}).join("");
}
document.querySelectorAll(".xor-buttons button").forEach(button=>button.addEventListener("click",()=>{xorMode=button.dataset.xor;document.querySelectorAll(".xor-buttons button").forEach(item=>item.classList.toggle("active",item===button));drawXor();}));

function updateArchitecture(){
  const batch=Number(document.querySelector("#networkBatch").value),hidden1=Number(document.querySelector("#hidden1").value),hidden2=Number(document.querySelector("#hidden2").value),layers=[
    {name:"Input",shape:`(${batch}, 10)`,detail:"No learned parameters"},
    {name:"Dense + ReLU",shape:`(${batch}, ${hidden1})`,detail:`W (10, ${hidden1}) · b (${hidden1})`},
    {name:"Dense + ReLU",shape:`(${batch}, ${hidden2})`,detail:`W (${hidden1}, ${hidden2}) · b (${hidden2})`},
    {name:"Output logits",shape:`(${batch}, 3)`,detail:`W (${hidden2}, 3) · b (3)`}
  ],parameters=(10*hidden1+hidden1)+(hidden1*hidden2+hidden2)+(hidden2*3+3),largest=Math.max(batch*10,batch*hidden1,batch*hidden2,batch*3);
  document.querySelector("#networkBatchValue").value=batch;
  document.querySelector("#hidden1Value").value=hidden1;
  document.querySelector("#hidden2Value").value=hidden2;
  document.querySelector("#architectureVisual").innerHTML=layers.map((layer,index)=>`${index?'<span class="architecture-arrow">→</span>':""}<article class="architecture-layer"><small>${layer.name}</small><strong>${layer.shape}</strong><small>${layer.detail}</small></article>`).join("");
  document.querySelector("#networkParameterCount").textContent=parameters.toLocaleString();
  document.querySelector("#largestActivation").textContent=`${largest.toLocaleString()} values`;
  document.querySelector("#capacityMeaning").textContent=parameters<1000
    ?"A relatively narrow candidate. It is inexpensive, but must still prove it can beat the Lesson 5 baseline."
    :parameters>5000
      ?"A higher-capacity candidate. It may represent richer interactions, but needs stronger generalization evidence and regularization checks."
      :"A moderate candidate architecture. Parameter count describes size, not whether the learned function will generalize.";
}
document.querySelectorAll("#networkBatch, #hidden1, #hidden2").forEach(input=>input.addEventListener("input",updateArchitecture));

document.querySelectorAll(".quiz").forEach(quiz=>quiz.querySelectorAll("button").forEach(button=>button.addEventListener("click",()=>{
  quiz.querySelectorAll("button").forEach(item=>item.classList.remove("correct","wrong"));const correct=button.dataset.choice===quiz.dataset.answer;button.classList.add(correct?"correct":"wrong");quiz.querySelector(".feedback").textContent=correct?"Correct — you can trace the mechanism.":"Not quite. Revisit the related interaction and try again.";
})));
function completionState(){const done=CourseProgress.isComplete(6);document.querySelector("#completeLesson").textContent=done?"Lesson 6 completed ✓":"Mark Lesson 6 complete";document.querySelector("#completionStatus").textContent=done?"Your neural architecture contract is ready for Lesson 7.":"Completion is stored in this browser.";}
document.querySelector("#completeLesson").addEventListener("click",()=>{CourseProgress.complete(6);completionState();});window.addEventListener("course-progress",completionState);

updateNeuron();updateShape();updateActivation();drawXor();updateArchitecture();completionState();
