---
name: arxiv-search
description: This skill should be used when the user wants to search for papers on arxiv, find academic papers, look up research by topic or author, or do a literature search. Trigger phrases include "search arxiv", "find papers on", "look up papers about", "recent papers on", "arxiv search".
version: 1.0.0
---

# Arxiv Search Skill

Search arxiv for academic papers using the public API.

## When to Use

Use this skill when the user wants to find papers on arxiv by topic, author, keyword, or any combination.

## How to Search

Run the search script with `uv run`:

```bash
uv run .claude-plugin/skills/arxiv-search/scripts/arxiv_search.py "<query>" [options]
```

### Options

| Flag | Description | Default |
|------|-------------|---------|
| `-n N` | Number of results | 10 |
| `-s relevance\|lastUpdatedDate\|submittedDate` | Sort order | relevance |
| `-a` | Show abstracts | off |

### Arxiv Query Syntax

The query supports full arxiv API syntax:
- `ti:attention` — search in title
- `au:vaswani` — search by author
- `abs:transformer` — search in abstract
- `cat:cs.LG` — filter by category
- `AND`, `OR`, `ANDNOT` — boolean operators

### Rules

- **Never combine `au:` with `cat:` filters.** Authors have at most ~200 papers, so the author filter is already tight enough. Adding a category filter causes papers to be silently missed when an author publishes across multiple categories.

### Examples

```bash
# Basic topic search
uv run .claude-plugin/skills/arxiv-search/scripts/arxiv_search.py "mechanistic interpretability" -n 5

# Recent papers with abstracts
uv run .claude-plugin/skills/arxiv-search/scripts/arxiv_search.py "sparse autoencoders" -s submittedDate -n 10 -a

# All papers by an author (no category filter)
uv run .claude-plugin/skills/arxiv-search/scripts/arxiv_search.py "au:geiger AND ti:causal" -n 50 -a

# Category filter only for topic searches (no author)
uv run .claude-plugin/skills/arxiv-search/scripts/arxiv_search.py "cat:cs.LG AND ti:attention" -s lastUpdatedDate -n 10
```

## After Searching

- Present results clearly with title, date, authors, and URL
- If the user wants to read a specific paper, use WebFetch on the arxiv abstract URL
- Offer to refine the search or search for related topics
