"use strict";

const test=require("node:test");
const assert=require("node:assert/strict");
const fs=require("node:fs");
const path=require("node:path");
const {feedbackFor}=require("../../lessons/lesson-ui-logic.js");

const root=path.resolve(__dirname,"../..");
const lessonDirs=fs.readdirSync(path.join(root,"lessons")).filter(name=>/^(0[1-9]|10)_/.test(name)).sort();
const plain=html=>html.replace(/<[^>]+>/g,"").replace(/&[^;]+;/g," ").replace(/\s+/g," ").trim();

test("all 140 distractors have specific authored feedback that does not reveal the answer",()=>{
  let questions=0,distractors=0;const allMessages=[];
  for(const directory of lessonDirs){
    const html=fs.readFileSync(path.join(root,"lessons",directory,"index.html"),"utf8"),messages=[];
    for(const match of html.matchAll(/<div class="quiz" data-answer="([^"]+)"([^>]*)>([\s\S]*?)<p class="feedback"><\/p>\s*<\/div>/g)){
      questions++;
      const answer=match[1],attributes=match[2],body=match[3];
      const buttons=[...body.matchAll(/<button data-choice="([^"]+)">([\s\S]*?)<\/button>/g)].map(item=>({choice:item[1],label:plain(item[2])})),correct=buttons.find(item=>item.choice===answer);
      for(const selected of buttons.filter(item=>item.choice!==answer)){distractors++;const encoded=attributes.match(new RegExp(`data-why-${selected.choice}="([^"]+)"`))?.[1]||"",explanation=plain(encoded.replace(/&quot;/g,'"'));assert.ok(explanation.length>=80,`${directory} ${selected.choice} needs substantive feedback`);assert.ok(!explanation.includes("tempting alternative"),`${directory} ${selected.choice} still uses the generic template`);assert.ok(explanation.split(/\s+/).length>=12,`${directory} ${selected.choice} needs a conceptual explanation`);const message=feedbackFor(explanation);assert.ok(!message.toLowerCase().includes(correct.label.toLowerCase()),`${directory} ${selected.choice} reveals the answer`);messages.push(message);allMessages.push(message);}
    }
    assert.equal(new Set(messages).size,messages.length,`${directory} has unique distractor feedback`);
  }
  assert.equal(questions,70);
  assert.equal(distractors,140);
  assert.equal(new Set(allMessages).size,140);
});
