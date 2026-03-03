# Literature Review

A Claude Code-assisted workspace for searching, reading, and summarizing academic papers.

This is just a scaffold for a claude code instance. In practice, I'll manually query a claude code instance to collect papers in `search_results/` and explain them to me, or search my notes for potential gaps and add clarifications. The literature review is a conversation with claude code. This repo contains skills to ease the process.


## Features

- **Arxiv search** — query papers by topic, author, or keyword via the arxiv API
- **Structured search results** — saved as markdown in `search_results/` with consistent formatting
- **Math rendering** — KaTeX math in markdown via the Markdown Preview Enhanced VS Code extension
- **Figure extraction** — crop figures from PDFs and embed them in notes

All Python tooling uses `uv`.

### Search arxiv

```bash
uv run .claude-plugin/skills/arxiv-search/scripts/arxiv_search.py "<query>" [options]
```

| Flag | Description | Default |
|------|-------------|---------|
| `-n N` | Number of results | 10 |
| `-s relevance\|lastUpdatedDate\|submittedDate` | Sort order | relevance |
| `-a` | Show abstracts | off |

**Examples:**

```bash
# Topic search, most recent first
uv run .claude-plugin/skills/arxiv-search/scripts/arxiv_search.py "sparse autoencoders" -s submittedDate -n 10 -a

# Author search (do not combine with cat: filter)
uv run .claude-plugin/skills/arxiv-search/scripts/arxiv_search.py "au:geiger AND ti:causal" -n 50 -a
```

### Save search results

Results go in `search_results/` as markdown files (excluded from git). See `.claude-plugin/skills/search-results/SKILL.md` for the file format.

## VS Code setup

- Install **Markdown Preview Enhanced** (`shd101wyy.markdown-preview-enhanced`) for KaTeX math rendering
- Open preview: command palette → "Markdown Preview Enhanced: Open Preview to the Side"
- Set `markdown-preview-enhanced.previewMode` to `"Multiple Previews"` so each file keeps its own pane

## Project structure

```
.claude-plugin/          # Claude Code skills
  skills/
    arxiv-search/        # Arxiv search script and instructions
    search-results/      # Format spec for saving results
search_results/          # Search output (gitignored)
CLAUDE.md                # Project rules for Claude
LEARNINGS.md             # Notes on tools and workflows
pyproject.toml           # Python project config (uv)
```
