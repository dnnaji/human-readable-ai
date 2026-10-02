# Explainer videos for change over time

Use a short video when motion, timing, or a guided sequence makes an explanation easier to follow. [Karpathy's post](https://x.com/karpathy/status/2105819303471976479) proposes custom explainer videos as another output format.

## Copyable prompt

```text
Create a short explainer about [topic] for [audience].
First produce a script and a scene-by-scene storyboard.
For each scene, specify what appears, what changes, and the narration.
Check the factual claims and calculations before rendering.
Provide captions and a transcript.
Use original visuals and authorized assets.
State any tools, costs, or credentials needed before using them.
```

## Worked example

The [repeated-growth storyboard](../examples/repeated-growth/storyboard.md) walks through two rules with the same starting value. It includes narration and a transcript. It is a production plan, not a rendered video.

Start with a verified script. A rendered demonstration can be added later with its source files, rendering instructions, captions, and asset credits. Speech services are optional; keep credentials outside the repository.

## Tradeoffs

Video gives the creator control over pacing, while a reader may prefer to jump directly to a result. Provide a transcript and a still summary. Smooth animation does not verify a claim, and a memorable visual can make an error harder to notice. Check the substance before refining presentation.

Sources: [Karpathy's post](https://x.com/karpathy/status/2105819303471976479); [source register](../SOURCES.md). The prompt and storyboard are original adaptations.
