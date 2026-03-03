# Project Rules

## Python
- Always use `uv` for package management and running scripts
- Run scripts with `uv run <script>`, install packages with `uv add <package>`
- Never use `pip`, `python`, or `python3` directly

## Search Results
- Save literature search results to `search_results/` as markdown files
- Follow the format defined in `.claude-plugin/skills/search-results/SKILL.md`

## Math in Markdown
- Use `$...$` (inline) and `$$...$$` (display) for KaTeX math in markdown files
- Extension **Markdown Preview Enhanced** (`shd101wyy.markdown-preview-enhanced`) is installed and renders KaTeX
- Open math preview via command palette: "Markdown Preview Enhanced: Open Preview to the Side"
- The built-in VS Code markdown preview does NOT render math

## Inserting Figures from Papers into Markdown

- Render PDF pages with `pdftoppm` via Bash (installed at `/opt/homebrew/bin/pdftoppm`; the Read tool cannot find it and will error):
  `pdftoppm -r 200 -png -f <page> -l <page> <file.pdf> /tmp/prefix`
- Preview the rendered page with the Read tool to identify which page contains the figure
- Crop to just the figure + caption using PIL (Pillow is installed):
  1. Detect the bottom boundary: scan rows for whitespace gaps, pick the largest gap below the figure
  2. Auto-crop all four sides using `mask.getbbox()` on a thresholded grayscale image (white > 240 → 0, else 255), then add a small padding (e.g. 10px)
  - Prefer PIL over `sips` — sips `-c` crops from center which is counterintuitive
- Save the final crop into the same folder as the markdown file
- Embed with `![Figure N from Paper X](filename.png)` — no separate caption in the markdown, the figure's own caption is already in the image

## Opening Files in VS Code
- To open PDFs (or any files) in the current VS Code window, use `code <file>` (not `code --reuse-window <url>`)
- Never pass URLs to `code` — it creates text files instead of opening them
