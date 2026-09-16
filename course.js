"use strict";
const phases=[
  ["Foundations","Lessons 01–05",["How machines learn","Vectors, matrices, and tensors","Loss functions and optimization","Probability and statistics","Regression and classification"]],
  ["Neural networks","Lessons 06–10",["Neural-network anatomy","Backpropagation from scratch","PyTorch and autograd","Train and evaluate a neural network","Regularization and generalization"]],
  ["Language-model mechanics","Lessons 11–16",["Tokenization","Embeddings and semantic similarity","Attention from scratch","Transformer blocks","Build a tiny GPT","LLM inference and decoding"]],
  ["AI applications","Lessons 17–23",["Prompt and context engineering","Structured output and tool calling","RAG fundamentals","Hybrid retrieval and reranking","Agents, loops, state, and memory","MCP and tool ecosystems","Multi-agent systems"]],
  ["Production and specialization","Lessons 24–30",["Evaluation and regression testing","Fine-tuning, LoRA, and QLoRA","AI security and red teaming","Multimodal AI","Production AI serving","MLOps and LLMOps","Distributed AI"]],
  ["Advanced architecture","Lessons 31–35",["Advanced model architectures","Advanced reasoning and verification","Research literacy and reproduction","Enterprise AI architecture","Capstone agentic AI platform"]]
];
const slugs=["01_linear_regression","02_vectors_matrices_tensors","03_loss_functions_and_optimization","04_probability_and_statistics_for_ml","05_regression_and_classification","06_neural_network_anatomy","07_backpropagation_from_scratch","08_pytorch_and_autograd","09_train_and_evaluate_a_neural_network","10_regularization_and_generalization","11_tokenization","12_embeddings_and_semantic_similarity","13_attention_from_scratch","14_transformer_blocks","15_build_a_tiny_gpt","16_llm_inference_and_decoding","17_prompt_and_context_engineering","18_structured_output_and_tool_calling","19_rag_fundamentals","20_hybrid_retrieval_and_reranking","21_agents_loops_state_and_memory","22_mcp_and_tool_ecosystems","23_multi_agent_systems","24_evaluation_and_regression_testing","25_fine_tuning_lora_and_qlora","26_ai_security_and_red_teaming","27_multimodal_ai","28_production_ai_serving","29_mlops_and_llmops","30_distributed_ai","31_advanced_model_architectures","32_advanced_reasoning_and_verification","33_research_literacy_and_reproduction","34_enterprise_ai_architecture","35_capstone_production_grade_agentic_ai_platform"];
function lessonPath(number){return number<=5?`course.html?lesson=${number}`:`lessons/${slugs[number-1]}/README.md`;}
function render(){const state=CourseProgress.read(),completed=new Set((state.completed||[]).map(Number));let number=1;const host=document.querySelector("#coursePhases");host.innerHTML="";for(const [name,range,titles] of phases){const section=document.createElement("section");section.className="phase";section.innerHTML=`<div class="phase-heading"><h2>${name}</h2><span>${range}</span></div><div class="lesson-grid"></div>`;const grid=section.querySelector(".lesson-grid");for(const title of titles){const n=number++,interactive=n<=5;const card=document.createElement("a");card.className=`lesson${completed.has(n)?" complete":""}${state.lastVisited===n?" current":""}`;card.href=lessonPath(n);card.innerHTML=`<span class="number">LESSON ${String(n).padStart(2,"0")}</span><h3>${title}</h3><small>${completed.has(n)?"Completed":interactive?"Interactive lesson":"Instructional review pending"}</small>`;grid.appendChild(card);}host.appendChild(section);}const count=completed.size,percent=Math.round(count/35*100);document.querySelector("#completedCount").textContent=count;document.querySelector("#progressPercent").textContent=`${percent}% complete`;document.querySelector("#progressBar").style.width=`${percent}%`;const next=Math.min(35,[...Array(35)].map((_,i)=>i+1).find(n=>!completed.has(n))||35);document.querySelector("#continueLink").href=lessonPath(next);}

const viewer=document.querySelector("#lessonViewer");
const frame=document.querySelector("#lessonFrame");
const requestedLesson=Number(new URLSearchParams(window.location.search).get("lesson"));

function sendProgress(target){target.postMessage({type:"learn-ai-progress-state",state:CourseProgress.read()},"*");}
window.addEventListener("message",event=>{
  if(event.source!==frame.contentWindow||!event.data||event.data.type!=="learn-ai-progress")return;
  const action=event.data.action,number=Number(event.data.number);
  if(action==="visit"&&number>=1&&number<=35)CourseProgress.visit(number);
  else if(action==="complete"&&number>=1&&number<=35)CourseProgress.complete(number);
  else if(action==="uncomplete"&&number>=1&&number<=35)CourseProgress.uncomplete(number);
  else if(action==="clear")CourseProgress.clear();
  sendProgress(event.source);
});

if(requestedLesson>=1&&requestedLesson<=5){
  viewer.hidden=false;
  document.querySelector("#viewerTitle").textContent=`Lesson ${requestedLesson} · ${phases[0][2][requestedLesson-1]}`;
  frame.title=`Lesson ${requestedLesson}: ${phases[0][2][requestedLesson-1]}`;
  frame.src=`lessons/${slugs[requestedLesson-1]}/index.html`;
  frame.addEventListener("load",()=>sendProgress(frame.contentWindow));
}

document.querySelector("#resetProgress").addEventListener("click",()=>{if(confirm("Clear completed and visited lessons on this browser?")){CourseProgress.clear();render();}});window.addEventListener("course-progress",render);render();
