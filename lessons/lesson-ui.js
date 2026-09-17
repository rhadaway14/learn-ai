"use strict";

(function enhanceLessonUi(){
  const text=value=>value.replace(/\s+/g," ").trim();
  function rangeName(input){const label=input.closest("label");if(!label)return input.id||"Adjust value";const clone=label.cloneNode(true);clone.querySelectorAll("input, output, select").forEach(node=>node.remove());return text(clone.textContent)||input.id||"Adjust value";}
  function syncRange(input){const output=input.closest("label")?.querySelector("output");input.setAttribute("aria-label",input.getAttribute("aria-label")||rangeName(input));input.setAttribute("aria-valuetext",text(output?.value||output?.textContent||input.value));}
  document.querySelectorAll('input[type="range"]').forEach(input=>{syncRange(input);input.addEventListener("input",()=>setTimeout(()=>syncRange(input),0));});

  document.querySelectorAll(".micro-lab").forEach((lab,index)=>{const live=document.createElement("div");live.className="sr-only lab-announcer";live.setAttribute("aria-live","polite");live.setAttribute("aria-atomic","true");live.dataset.lab=String(index+1);lab.appendChild(live);let timer;new MutationObserver(()=>{clearTimeout(timer);timer=setTimeout(()=>{const values=[...lab.querySelectorAll("output, .observation-light, .feedback")].filter(node=>node!==live).map(node=>text(node.value||node.textContent)).filter(Boolean),announcement=values.slice(-6).join(". ");if(announcement&&live.textContent!==announcement)live.textContent=announcement;},60);}).observe(lab,{subtree:true,childList:true,characterData:true,attributes:true,attributeFilter:["value"]});});

  document.querySelectorAll("canvas").forEach((canvas,index)=>{canvas.setAttribute("role","img");if(!canvas.getAttribute("aria-label"))canvas.setAttribute("aria-label",`Interactive chart ${index+1}; the numeric results and interpretation are provided beside or below the chart.`);});

  document.querySelectorAll("button.active").forEach(active=>{const group=active.parentElement;if(!group)return;const buttons=[...group.querySelectorAll(":scope > button")];if(buttons.length<2)return;const sync=()=>buttons.forEach(button=>button.setAttribute("aria-pressed",String(button.classList.contains("active"))));sync();buttons.forEach(button=>button.addEventListener("click",()=>setTimeout(sync,0)));});

  document.querySelectorAll(".quiz").forEach((quiz,questionIndex)=>{const question=text(quiz.querySelector("h3")?.textContent||`Question ${questionIndex+1}`);const correct=quiz.querySelector(`button[data-choice="${quiz.dataset.answer}"]`);quiz.querySelectorAll("button").forEach(button=>button.addEventListener("click",()=>{if(button===correct)return;quiz.querySelector(".feedback").textContent=LessonUiLogic.diagnosticFeedback(question,button.textContent,correct?.textContent||"");}));});

  const lessonNumber=Number(document.querySelector(".progress-wrap span")?.textContent.match(/Lesson\s+(\d+)/)?.[1]);
  if(lessonNumber>1){document.querySelectorAll(".readiness-check button[data-correct=\"false\"]").forEach(button=>button.addEventListener("click",()=>{const feedback=button.closest(".readiness-check")?.querySelector(".feedback");if(feedback)feedback.insertAdjacentHTML("beforeend",` <a href="../${String(lessonNumber-1).padStart(2,"0")}_${["linear_regression","vectors_matrices_tensors","loss_functions_and_optimization","probability_and_statistics_for_ml","regression_and_classification","neural_network_anatomy","backpropagation_from_scratch","pytorch_and_autograd","train_and_evaluate_a_neural_network"][lessonNumber-2]}/index.html">Review the preceding lesson</a> and retry this prerequisite check.`);}));}
  const completion=document.querySelector(".completion");
  if(completion&&lessonNumber){const links=document.createElement("p");links.className="artifact-templates";links.innerHTML=`<strong>Artifact templates:</strong> <a href="../../templates/capstone-increment.md" target="_blank">capstone increment</a>${lessonNumber>=6?' · <a href="../../templates/model-evidence-card.md" target="_blank">model evidence card</a>':""}. Copy the prompts into your own Markdown file and preserve it for the next lesson.`;completion.querySelector(".completion-actions")?.before(links);}
})();
