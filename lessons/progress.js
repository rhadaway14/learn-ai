"use strict";

(function () {
  const key = "learn-ai-progress-v1";
  const embedded = window.parent !== window;
  const emptyState = () => ({ completed: [], visited: [], milestones: {} });
  let remoteState = null;
  let storageError = null;

  function normalize(value) {
    const state = value && typeof value === "object" ? value : emptyState();
    return {
      ...state,
      completed: Array.isArray(state.completed) ? state.completed : [],
      visited: Array.isArray(state.visited) ? state.visited : [],
      milestones:
        state.milestones && typeof state.milestones === "object"
          ? state.milestones
          : {},
    };
  }
  function reportStorageError(error) {
    storageError =
      "Progress cannot be saved in this browser. Your work remains available on this page until it is closed.";
    window.dispatchEvent(
      new CustomEvent("course-storage-error", {
        detail: { message: storageError, error },
      }),
    );
  }
  function read() {
    if (embedded && remoteState) return normalize(remoteState);
    if (storageError && remoteState) return normalize(remoteState);
    try {
      return normalize(JSON.parse(localStorage.getItem(key)));
    } catch (error) {
      reportStorageError(error);
      return emptyState();
    }
  }
  function publish(value, action, number) {
    const normalized = normalize(value);
    if (embedded)
      window.parent.postMessage(
        { type: "learn-ai-progress", action, number },
        "*",
      );
    else {
      try {
        localStorage.setItem(key, JSON.stringify(normalized));
      } catch (error) {
        reportStorageError(error);
      }
    }
    remoteState = normalized;
    window.dispatchEvent(
      new CustomEvent("course-progress", { detail: normalized }),
    );
  }
  function unique(values) {
    return [...new Set(values.map(Number))].sort((a, b) => a - b);
  }
  function visit(number) {
    const value = read();
    value.visited = unique([...value.visited, number]);
    value.lastVisited = number;
    publish(value, "visit", number);
    return value;
  }
  function complete(number) {
    const value = read();
    value.completed = unique([...value.completed, number]);
    value.visited = unique([...value.visited, number]);
    value.lastVisited = number;
    publish(value, "complete", number);
    return value;
  }
  function uncomplete(number) {
    const value = read();
    value.completed = value.completed.filter(
      (item) => Number(item) !== Number(number),
    );
    publish(value, "uncomplete", number);
    return value;
  }
  function isComplete(number) {
    return read().completed.map(Number).includes(Number(number));
  }
  function completeMilestone(id) {
    const value = read();
    value.milestones[id] = {
      completed: true,
      completedAt: new Date().toISOString(),
    };
    publish(value, "milestone", id);
    return value;
  }
  function isMilestoneComplete(id) {
    return Boolean(read().milestones[id]?.completed);
  }
  function clear() {
    const value = emptyState();
    publish(value, "clear");
    return value;
  }
  function getStorageError() {
    return storageError;
  }

  window.CourseProgress = {
    read,
    visit,
    complete,
    uncomplete,
    isComplete,
    completeMilestone,
    isMilestoneComplete,
    clear,
    getStorageError,
  };
  window.addEventListener("message", (event) => {
    if (event.data && event.data.type === "learn-ai-progress-state") {
      remoteState = normalize(event.data.state);
      window.dispatchEvent(
        new CustomEvent("course-progress", { detail: remoteState }),
      );
    }
  });
  if (embedded)
    window.parent.postMessage(
      { type: "learn-ai-progress", action: "read" },
      "*",
    );
})();
