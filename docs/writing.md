# Writing that preserves meaning

Start with the [copyable instructions](../instructions/clear-writing.md). Use them when the reader needs to understand an explanation, make a decision, or follow a procedure.

The approach comes from [Karpathy's post](https://x.com/karpathy/status/2105819303471976479), which recommends trying ASD-STE100 and softening its constraints when useful. This project names the standard and then gives explicit adaptations. A percentage alone leaves the model to choose which rules to relax.

## How the adaptation relates to STE

These references use [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf), dated January 15, 2025.

| Principle | Relevant STE rules | Application here |
| --- | --- | --- |
| Accurate, connected sentences | 4.1, 4.2, 4.4 | Split independent ideas and preserve qualifications. |
| Conditions before procedural actions | 5.2, 5.4 | Make prerequisites visible before the reader acts. |
| Direct actions and consistent names | 1.11, 3.6, 3.7 | Name the actor, action, and affected item when known. |
| Accessible terminology | 1.9, 1.10 | Prefer familiar words and explain necessary unfamiliar terms. |
| Focused paragraphs | 6.4, 6.5 | Keep each paragraph about one topic. |

Matching detail to the question and stating material dates are practical additions. Explaining a necessary unfamiliar term is an adaptation of the terminology principles, rather than an exact numbered STE rule.

## Worked examples

All examples below are synthetic teaching examples, not transcript quotations.

| Less clear | Clearer | Why |
| --- | --- | --- |
| Updated the ranking and details. | I updated the comparison PDF. The shared directory is unchanged. | Names the affected artifact and resolves a plausible scope ambiguity. |
| The release is pending activation. | The update is installed. We have not verified that the running application loaded it. | Explains the state in terms the reader can act on. |
| Configure access, run the transfer, and verify the output once the key has the necessary permissions. | If the key has the required permissions, configure access. Then run the transfer and verify the output. | Places the condition before the governed actions. |
| Here are twenty additional questions for the initial pricing discussion. | For the initial discussion, ask these four pricing questions. | Controls answer scope as well as sentence length. |
| Your booking covers the selected weekdays. | Your booking covers Monday through Thursday. Friday is excluded. | Makes a material boundary explicit. |

## Tradeoffs

STE has strict procedural and descriptive sentence limits. This adaptation uses the idea of short, clear sentences without enforcing those limits mechanically. Splitting a sentence can add words or separate a condition from its consequence. Readability depends on meaning and structure as well as length.

A known actor often makes a sentence clearer. An unknown actor must stay unknown. Define essential terms without turning every answer into a glossary. Include dates and exclusions when they affect interpretation; omit repeated routine details when context is clear.

The [review](../research/session-review.md) supports these choices as useful opportunities. It did not test these rewritten responses with users.

Reference image: [STE overview attached to Karpathy's post](https://x.com/karpathy/status/2105819303471976479/photo/1). Source details and licensing boundaries are in [SOURCES.md](../SOURCES.md).
