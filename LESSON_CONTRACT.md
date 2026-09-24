# Reusable Lesson Contract

Every student-ready lesson uses one structure while supporting two depths of study. The core path must stand alone. The advanced path may deepen the same topic, but it may not repair missing explanations in the core path.

This structure is delivered inside the persistent course UI described in [INTEGRATED_COURSE_EXPERIENCE.md](INTEGRATED_COURSE_EXPERIENCE.md). The table below describes required content, not separate pages. Content and project interaction are interleaved in concept-sized learning loops.

## Required learner journey

| Component | Purpose | Required evidence |
|---|---|---|
| Orientation | State the problem, outcomes, prerequisites, and estimated effort | Learner knows why the topic matters and what prior knowledge is assumed |
| Core explanation | Teach the mental model, vocabulary, layered math, and guided example | Learner can explain the mechanism without framework jargon |
| Interactive exploration | Let the learner predict and change controlled inputs | Visible observation and interpretation, including one failure |
| AI story | Connect prior capability, this lesson's contribution, and a modern use case | Learner can locate the primitive in a larger AI system |
| Advanced engineering | Add derivation, implementation mechanics, tradeoffs, scale, and production diagnosis | Experienced learner can defend an engineering decision |
| Hands-on activity | Progress through guided, challenge, and engineer-extension work | Saved activity artifact with hypothesis, evidence, and reflection |
| Phase-project increment | Add one accepted capability to the current phase project | Versioned artifact that is explicitly reused later |
| Assessment and completion | Check recall, interpretation, prediction, and application | Feedback, remediation, and an explicit definition of done |

## Required concept loop

Every major concept uses the following sequence when each beat is meaningful:

1. **Learn** — problem, intuition, vocabulary, and layered math.
2. **Locate** — highlight the real project component, input, and output.
3. **Predict** — choose the expected result before it is revealed.
4. **Manipulate** — change one bounded causal control.
5. **Observe** — see the real state and evidence change.
6. **Interpret** — select the explanation supported by the evidence and receive specific feedback.
7. **Apply** — save a decision or capability used by the cumulative project.

The required path must not send the learner to a different lesson page or lab guide between these steps.

## Two-depth rule

### Core path

- Assumes only explicitly listed prerequisites.
- Uses plain language, realistic examples, bounded metaphors, and visual interactions.
- Never requires source-code editing before Engineering Lab A.
- Contains everything needed to complete the required activity and phase increment.

### Advanced engineering

- Is labeled **Engineer deep dive** and remains optional for course progression.
- Starts from the same scenario and vocabulary as the core path.
- Covers mathematical derivation, implementation mechanics, performance, failure diagnosis, and architecture tradeoffs.
- States any additional prerequisites and provides a bridge or marks the work as post–Engineering Lab A.
- Ends with a design question, diagnostic task, or implementation extension—not additional trivia.

## Standard component markup

The shared stylesheet and script recognize the following components.

```html
<aside class="ai-story" data-current="New capability">
  <p class="tag">WHERE THIS FITS</p>
  <div class="story-steps">
    <article data-story-step="before"><strong>Before</strong><p>Existing capability</p></article>
    <article data-story-step="now"><strong>This lesson</strong><p>New capability</p></article>
    <article data-story-step="next"><strong>Next</strong><p>Capability unlocked later</p></article>
  </div>
  <p><strong>Modern use case:</strong> A concrete application.</p>
</aside>

<details class="advanced-section">
  <summary>Engineer deep dive: topic</summary>
  <div class="advanced-content">
    <p class="advanced-prerequisites"><strong>Additional prerequisites:</strong> ...</p>
    <!-- derivation, mechanics, tradeoffs, scale, failure diagnosis -->
  </div>
</details>

<section class="hands-on-activity" data-activity-id="LNN-A1">
  <p class="tag">HANDS-ON ACTIVITY</p>
  <h3>Activity mission</h3>
  <ol class="activity-levels">
    <li data-level="guided"><strong>Guided</strong><p>Exact steps and expected evidence.</p></li>
    <li data-level="challenge"><strong>Challenge</strong><p>Goal with reduced support.</p></li>
    <li data-level="extension"><strong>Engineer extension</strong><p>Optional implementation or diagnosis.</p></li>
  </ol>
  <p class="activity-artifact"><strong>Save:</strong> named artifact and acceptance evidence.</p>
</section>

<section class="phase-increment" data-phase="phase-id" data-increment="increment-id">
  <p class="tag">PHASE PROJECT</p>
  <h3>Capability added</h3>
  <p><strong>Reused in:</strong> later lesson or phase project.</p>
  <ul class="acceptance-criteria"><li>Observable acceptance criterion</li></ul>
</section>
```

## Hands-on activity contract

Every required activity declares:

- a mission tied to one lesson outcome;
- a working starting state;
- the controlled decisions the learner owns;
- expected evidence and at least one failure experiment;
- guided, challenge, and optional engineer-extension levels;
- an artifact path or browser-download name;
- acceptance criteria and recovery instructions;
- the phase-project capability it feeds.

Infrastructure is introduced only when it teaches something. Browser-only activities remain browser-only. Docker Compose is reserved for labs that genuinely need persistent data, a runtime service, a model server, a database, or multi-service observability.

The hands-on activity is part of the lesson's concept loop, not a detached exercise at the bottom of a reading page. Its controls, evidence, interpretation, and saved project state must remain visible from the same course shell.

## Phase-project increment contract

Every increment records the capability added, its upstream lesson evidence, inputs and outputs, interfaces, acceptance criteria, failure behavior, verification steps, and the later increment that consumes it. Replacing an earlier design preserves the decision record explaining why.

After five lesson increments, a phase integration checkpoint combines them in the same UI. It may recap, compare, fail, recover, verify, promote, and export. It may not teach a missing prerequisite or introduce a second navigation model.

## Author review gate

- [ ] Core path is complete without opening the advanced section.
- [ ] Advanced content deepens rather than repeats the core explanation.
- [ ] The AI-story component names a prior capability, new capability, next capability, and modern use case.
- [ ] Activity support fades from guided to challenge.
- [ ] Activity produces a saved artifact with reproducible evidence.
- [ ] Phase increment has observable acceptance criteria and a named downstream consumer.
- [ ] Every major concept is visibly located in the cumulative project.
- [ ] Teaching, interaction, evidence, and interpretation occur in one continuous UI sequence.
- [ ] Each meaningful visual exposes cause and effect and has an accessible data equivalent.
- [ ] Environment requirements are no larger than the lesson needs.
- [ ] Completion can be verified without relying on learner confidence alone.
