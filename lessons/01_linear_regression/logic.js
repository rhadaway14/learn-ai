(function(root,factory){const api=factory();if(typeof module!=="undefined"&&module.exports)module.exports=api;else root.Lesson01Logic=api;})(typeof globalThis!=="undefined"?globalThis:this,function(){
  function seededRandom(seed=42){let state=seed>>>0;return()=>((state=(1664525*state+1013904223)>>>0)/4294967296);}
  function normal(random){const u=Math.max(random(),1e-12),v=random();return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);}
  function dataset(count,noise,relationship,outlier){const random=seededRandom(42),rows=Array.from({length:count},(_,index)=>{const x=random()*10,signal=relationship==="linear"?3.5*x+2:x*x+2;return{x,y:signal+normal(random)*noise,test:index%5===0};});if(outlier){const trainingIndex=rows.findIndex((row,index)=>!row.test&&index>=Math.floor(rows.length/2));rows[trainingIndex].y+=70;rows[trainingIndex].outlier=true;}return rows;}
  return{dataset};
});
