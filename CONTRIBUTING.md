# Contributing

Start with a concrete problem: what does the reader need to understand, and where does the current explanation fail?

For a new example, include the request, the proposed format, a worked result, and its limitations. Label synthetic examples. For factual claims, link the supporting source near the claim. Attribute the original idea and distinguish your adaptation.

Preserve exactness when simplifying. Keep a condition connected to its action. Name material assumptions and unknowns. A shorter response is useful when it remains complete for the task.

Before publishing, run:

```sh
python3 scripts/check_publication.py
gitleaks dir . --redact
gitleaks git . --redact
```

Install or select a supported Gitleaks version if the command is unavailable. Review all tracked files and commit metadata as well. The checks catch a subset of risks; they do not determine whether a person's information is authorized for publication.

Keep conversations, identifying details, credentials, and machine configuration outside the repository. Use synthetic examples and publicly sourced facts. See [PRIVACY.md](PRIVACY.md).
