(function(root,factory){const api=factory();if(typeof module!=="undefined"&&module.exports)module.exports=api;else root.LessonUiLogic=api;})(typeof globalThis!=="undefined"?globalThis:this,function(){
  const clean=value=>String(value).replace(/\s+/g," ").trim();
  function feedbackFor(explanation){const message=clean(explanation);if(!message)throw new Error("A distractor needs authored feedback");return`${message} Review the explanation above, then try again.`;}
  return{feedbackFor};
});
