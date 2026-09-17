(function(root,factory){const api=factory();if(typeof module!=="undefined"&&module.exports)module.exports=api;else root.Lesson03Logic=api;})(typeof globalThis!=="undefined"?globalThis:this,function(){
  const probeLoss=weight=>(weight-4)**2+0.03*(weight-4)**4;
  const probeGradient=weight=>2*(weight-4)+0.12*(weight-4)**3;
  function finiteDifference(weight,epsilon){const left=probeLoss(weight-epsilon),right=probeLoss(weight+epsilon),estimate=(right-left)/(2*epsilon),exact=probeGradient(weight);return{left,right,estimate,exact,error:Math.abs(estimate-exact)};}
  return{finiteDifference,probeLoss,probeGradient};
});
