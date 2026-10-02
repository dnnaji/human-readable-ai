# What the session review supports

This note reports a private exploratory review that informed the writing instructions. It is a qualitative account of opportunities for clearer communication.

## Coverage

The review started with 10 randomly selected interactive Codex sessions from one week. It then added 100 distinct Codex threads and 50 distinct Amp threads. The expanded sample excluded the original 10 and used all available history to obtain enough eligible interactive threads.

| Expanded sample | Threads | Visible assistant messages screened |
| --- | ---: | ---: |
| Codex | 100 | 4,068 |
| Amp | 50 | 1,709 |
| Total | 150 | 5,777 |

The original 10 sessions are separate from these totals. Platform names describe the corpus sources; they do not establish which underlying models produced every response.

## Method

Eligibility required distinct human turns with intervening visible assistant prose. Automated or delegated tasks, probes, repeated prompt payloads, and tool-result messages masquerading as user turns were excluded where detected. Random draws used saved local seeds. Candidates found ineligible during provenance review were replaced with draws from the remaining candidates.

Automated screening examined extracted visible assistant prose. Manual assessment covered candidate passages and user follow-ups from each sampled thread. Material cases received fuller context review. The initial inventory included one Amp export that timed out; it was unavailable for eligibility assessment. Eligibility depends on heuristics and manual provenance checks.

A separate Amp ultra consultation critiqued proposed wording. It did not independently review the corpus. The resulting recommendations were assessed against the evidence rather than adopted automatically.

## Findings

Observed clarification requests supported four recurring opportunities:

- Name the exact artifact affected by an update.
- Explain unfamiliar terms used to communicate a result or state.
- Match detail to the question and decision stage.
- State material dates, boundaries, and exclusions.

Requests for simpler comparisons also supported direct wording and an appropriate table. A counterexample favored removing redundant dates from routine receipts. These findings argue for conditional guidance that follows the reader's needs.

Splitting chains of actions and putting prerequisites first appeared useful in additional passages. Those benefits are inferred. The public [examples](../docs/writing.md) are newly constructed teaching examples, not quotations or de-identified transcript excerpts.

## Limits

The review did not measure comprehension, task time, clarification rates, or causal improvements. It did not compare the standard's name with an anonymous rule list. It did not establish the best wording experimentally.

Sentence screening used heuristic whitespace counts rather than STE's formal counting rules. Quoted prose was not always separated from authored prose. Task mix, conversation length, dates, and model versions differ across sources, so platform comparisons would be unsupported.

Raw transcripts, thread identifiers, seeds, source locators, and personal context are retained privately. This public summary cannot reproduce the private sample. Readers can inspect the published guidance and synthetic examples, then test them on their own tasks.

## How to test the guidance next

Compare the same explanation request with a neutral prompt, a bare STE reference, and the explicit adaptation. Record whether the reader can identify the result, condition, affected item, and uncertainty. Include counterexamples where compression loses meaning. Report the model, task, evaluation method, and limits for any claimed improvement.

Sources: [Karpathy's original post](https://x.com/karpathy/status/2105819303471976479); [ASD-STE100](https://www.asd-ste100.org/). These sources motivated the adaptation; they do not validate the private review's conclusions.
