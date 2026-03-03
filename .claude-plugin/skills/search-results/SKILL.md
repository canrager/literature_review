---
name: search-results
description: This skill should be used when saving, writing, or recording the results of an arxiv or literature search. Trigger phrases include "save search results", "write up the search", "record these papers", "save to search results".
version: 1.0.0
---

# Search Results Skill

Save literature search results to `search_results/` as structured markdown files for future reference.

## File Naming

Use descriptive kebab-case filenames that capture the author and/or topic:

```
search_results/
├── geiger_causal_abstraction.md
├── vaswani_attention.md
├── sparse_autoencoders_2024.md
└── ...
```

## File Format

Every search result file must follow this structure:

```markdown
# <Author> — <Topic> (or just <Topic> for topical searches)

**Search date:** YYYY-MM-DD
**Query:** `<exact arxiv query used>` (n=<num>, sort=<sort>)
**Total papers found:** <N>
**Filtered to:** <M> papers related to <topic>

---

## <Category 1>

| Year | Title | arxiv |
|------|-------|-------|
| YYYY | **Title** — one-line description of relevance | [XXXXXXX](https://arxiv.org/abs/XXXXXXX) |

## <Category 2>
...

---

## Excluded papers (not related to <topic>)

Brief note on what was excluded and why.
```

## Guidelines

- Group papers into meaningful categories (e.g. Core Theory, Methods, Tooling, Evaluation, Applied)
- Write a one-line description of relevance for each paper — not just the title
- Always record the exact query used so searches can be reproduced or refined
- Always note excluded papers so it's clear the filtering was intentional
- Use the search date so staleness is visible
