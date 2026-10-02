# Human-readable AI

Practical ways to make AI outputs easier to understand, inspect, and act on.

This project starts with [Andrej Karpathy's October 1, 2026 post](https://x.com/karpathy/status/2105819303471976479) about understanding language-model outputs. It develops his suggestions into reusable guidance for writing, diagrams, interactive pages, and explainer videos.

The writing guidance draws on [ASD-STE100 Simplified Technical English](https://www.asd-ste100.org/). Naming the standard gives a recognizable writing target. The explicit rules define how this project adapts it for conversations. That prompting benefit is a hypothesis, rather than a measured result.

## Start here

- Copy the [clear-writing instructions](instructions/clear-writing.md) into the instruction file or prompt you use with your assistant.
- Read the [writing guide](docs/writing.md) for examples and tradeoffs.
- Choose an output format using the table below.
- Explore [one topic in four formats](examples/repeated-growth/README.md).

| What you need to understand | Useful format | Guide |
| --- | --- | --- |
| A result, decision, or sequence of actions | Clear prose | [Writing](docs/writing.md) |
| Relationships, ownership, or flow | A diagram | [Diagrams](docs/diagrams.md) |
| How changing an assumption affects an outcome | An interactive page | [Interactive pages](docs/interactive-pages.md) |
| A process that benefits from motion and narration | A short explainer video | [Explainer videos](docs/explainer-videos.md) |

Choose the format that reduces the reader's effort. More elaborate output is useful when it improves understanding. Evidence and uncertainty still need to be visible in every format.

## What the review found

A private review examined an initial 10 interactive sessions, then 150 additional threads across Codex and Amp. The clearest opportunities were naming the affected artifact, explaining unfamiliar terms, matching detail to the question, and stating material scope or exclusions.

The [research note](research/session-review.md) describes the method and its limits. The public examples are synthetic. Raw conversations and identifying details remain private. The review does not establish causal effects or compare model quality.

## Contents and reuse

The [source register](SOURCES.md) credits the original post, its [attached STE overview image](https://x.com/karpathy/status/2105819303471976479/photo/1), and the underlying standard. The linked image remains with its source; it is not included in this repository's licenses.

Original prose and diagrams are licensed under [CC BY 4.0](LICENSE). Original code, including the HTML demo and check script, is licensed under [MIT](LICENSE-CODE). The adaptations and demonstrations here are independent work.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for the example format and publication checks. Suggested improvements should explain what becomes easier to understand and what evidence supports that claim.
