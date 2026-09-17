"use strict";

const test=require("node:test");
const assert=require("node:assert/strict");
const fs=require("node:fs");
const path=require("node:path");
const {diagnosticFeedback}=require("../../lessons/lesson-ui-logic.js");

const root=path.resolve(__dirname,"../..");
const lessonDirs=fs.readdirSync(path.join(root,"lessons")).filter(name=>/^(0[1-9]|10)_/.test(name)).sort();
const plain=html=>html.replace(/<[^>]+>/g,"").replace(/&[^;]+;/g," ").replace(/\s+/g," ").trim();

test("all 70 quiz distractors receive specific, distinct feedback",()=>{
  let questions=0;
  for(const directory of lessonDirs){
    const html=fs.readFileSync(path.join(root,"lessons",directory,"index.html"),"utf8"),messages=[];
    for(const match of html.matchAll(/<div class="quiz" data-answer="([^"]+)">([\s\S]*?)<p class="feedback"><\/p>\s*<\/div>/g)){
      questions++;
      const answer=match[1],body=match[2],question=plain(body.match(/<h3>([\s\S]*?)<\/h3>/)?.[1]||"");
      const buttons=[...body.matchAll(/<button data-choice="([^"]+)">([\s\S]*?)<\/button>/g)].map(item=>({choice:item[1],label:plain(item[2])})),correct=buttons.find(item=>item.choice===answer);
      for(const selected of buttons.filter(item=>item.choice!==answer)){const message=diagnosticFeedback(question,selected.label,correct.label);assert.ok(message.includes(selected.label));assert.ok(message.includes(correct.label));messages.push(message);}
    }
    assert.equal(new Set(messages).size,messages.length,`${directory} has unique distractor feedback`);
  }
  assert.equal(questions,70);
});
