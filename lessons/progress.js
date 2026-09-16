"use strict";

(function () {
  const key = "learn-ai-progress-v1";
  const embedded = window.parent !== window;
  let remoteState = null;
  function read() {
    if (embedded && remoteState) return remoteState;
    try { return JSON.parse(localStorage.getItem(key)) || {completed: [], visited: []}; }
    catch (_) { return {completed: [], visited: []}; }
  }
  function publish(value, action, number) {
    if (embedded) window.parent.postMessage({type: "learn-ai-progress", action, number}, "*");
    else localStorage.setItem(key, JSON.stringify(value));
    remoteState = value;
    window.dispatchEvent(new CustomEvent("course-progress", {detail: value}));
  }
  function unique(values) { return [...new Set(values.map(Number))].sort((a, b) => a - b); }
  function visit(number) { const value = read(); value.visited = unique([...(value.visited || []), number]); value.lastVisited = number; publish(value, "visit", number); return value; }
  function complete(number) { const value = read(); value.completed = unique([...(value.completed || []), number]); value.visited = unique([...(value.visited || []), number]); value.lastVisited = number; publish(value, "complete", number); return value; }
  function uncomplete(number) { const value = read(); value.completed = (value.completed || []).filter(item => Number(item) !== Number(number)); publish(value, "uncomplete", number); return value; }
  function isComplete(number) { return (read().completed || []).map(Number).includes(Number(number)); }
  function clear() { const value = {completed: [], visited: []}; publish(value, "clear"); return value; }
  window.CourseProgress = {read, visit, complete, uncomplete, isComplete, clear};
  window.addEventListener("message", event => {
    if (event.data && event.data.type === "learn-ai-progress-state") {
      remoteState = event.data.state;
      window.dispatchEvent(new CustomEvent("course-progress", {detail: remoteState}));
    }
  });
  if (embedded) window.parent.postMessage({type: "learn-ai-progress", action: "read"}, "*");
})();
