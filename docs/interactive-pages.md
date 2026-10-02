# Interactive pages for exploring assumptions

Use an interactive page when changing an input teaches something that a static explanation hides. [Karpathy's post](https://x.com/karpathy/status/2105819303471976479) recommends asking for HTML as an explanation format.

## Copyable prompt

```text
Explain [topic] in a self-contained HTML page.
Let the reader change [specific inputs] and see the resulting [outputs].
State the calculation, assumptions, units, and supported input range.
Use accessible labels and show the exact values alongside the visual.
Include a useful explanation when JavaScript is unavailable.
Use no external services, credentials, analytics, or network requests.
```

## Worked example

Download [the repeated-growth demo](../examples/repeated-growth/index.html) and open it in a browser. Change the number of steps to compare adding one with doubling. At six steps, the values are 7 and 64. The formulas and a numeric table remain visible beside the chart.

The demo is a local HTML file. It uses no external dependencies or services. GitHub's file view shows the source; opening a downloaded copy runs the interaction.

## Tradeoffs

An interface can imply more certainty than the underlying assumptions justify. Keep the model simple enough to inspect, name the supported range, and make invalid inputs visible. Prefer an interactive page when exploration changes understanding; a short answer may be enough for a single result.

Sources: [Karpathy's post](https://x.com/karpathy/status/2105819303471976479); [source register](../SOURCES.md). The demo is an original teaching example.
