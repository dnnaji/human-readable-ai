# Diagrams for relationships and flow

Use a diagram when the question is about how parts connect, who owns a step, or how information moves. [Karpathy's original post](https://x.com/karpathy/status/2105819303471976479) suggests diagrams as a way to make explanations easier to process.

## Copyable prompt

```text
Explain [topic] with a diagram and a short accompanying explanation.
Use named parts and label the important relationships.
Show direction only when it has meaning.
Distinguish known relationships from assumptions.
Include a text equivalent so the diagram can be read without the image.
Keep evidence and uncertainty visible.
```

## Worked example

The [repeated-growth example](../examples/repeated-growth/README.md) includes a diagram and a text equivalent. Its two rows show the same starting value under two different rules. The arrows mean one step, rather than an unspecified relationship.

## Tradeoffs

A diagram can make an unsupported connection look established. Labels and arrows need the same verification as prose. A small diagram with one clear job is often easier to inspect than a comprehensive map. Use symbols and line styles consistently, and pair color with labels.

Sources: [Karpathy's post](https://x.com/karpathy/status/2105819303471976479); [source register](../SOURCES.md). The prompts and examples here are this project's adaptations.
