(function(root,factory){const api=factory();if(typeof module!=="undefined"&&module.exports)module.exports=api;else root.LessonUiLogic=api;})(typeof globalThis!=="undefined"?globalThis:this,function(){
  const clean=value=>String(value).replace(/\s+/g," ").trim();
  function diagnosticFeedback(question,selected,correct){return`Not quite. “${clean(selected)}” reflects the wrong distinction for ${clean(question).replace(/^\d+\.\s*/,"").toLowerCase()} The deciding idea is: “${clean(correct)}”.`;}
  return{diagnosticFeedback};
});
