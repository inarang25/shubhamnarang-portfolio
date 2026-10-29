# shubhamnarang.in — roadmap

Working notes for growing this site from a portfolio into a full personal home (a "digital twin"): ideas, projects, writing, images, all in one place.

## Where it is now

| URL | File | What it is |
|---|---|---|
| `/` | `index.html` | Main site. Minimal, warm-paper design with small Indian line-art touches (kolam, toran, jharokha arch, Warli figures). |
| `/builder` | `builder.html` | "Comic edition" — the pop-art take, kept as a playful second view. |
| anything else | `404.html` | Not-found page. |

### Information structure (main site)

1. **Intro** — one sentence on what I do, one on the background.
2. **Now** — what has my attention this season (work, side project, learning).
3. **Selected work** — only two: demand.ai & Project Vihan (enterprise), nurchur.in (my own product).
4. **The path** — career and education, one line each, plus certifications.
5. **Lab** — capstone studies as a compact list, honestly labelled as early work in progress.
6. **Writing** — placeholder until the first essays exist.
7. **Contact.**

### Design language

- Ground: handmade-paper cream `#F5EFE3`; ink `#1F1A14`; muted `#6A5E50`; one accent, sindoor `#A8381F`.
- Type: Instrument Serif (headings), Manrope (body), Tiro Devanagari Hindi (name in Devanagari).
- Art, used sparingly: kolam dot motif (section markers, hero), toran line under the header, jharokha arch around the portrait, a Warli scene above the footer.

## The bigger picture: a personal twin

Sections the site can grow into, each a page of its own:

| Section | What goes there |
|---|---|
| `/work/<project>` | A full case study per project (problem → approach → outcome, screenshots, live dashboards). |
| `/lab` | Capstones and experiments, each with a short write-up as it matures. |
| `/writing` | Essays and longer posts. RSS feed. |
| `/ideas` | Short notes and half-formed thoughts — a "digital garden" that's allowed to be unfinished. |
| `/gallery` | Photos, sketches, images. |
| `/now` | A dated "what I'm doing now" page. |
| `/ask` | **The twin itself**: a chat that answers questions about my work and thinking, grounded only in what's published on this site, and says so when it doesn't know. |

Examples researched: digital gardens (personal wikis where notes grow over time) and "AI twin" portfolios such as Twinfolio — open-source, answers from your own work and admits gaps.

## Suggested order

1. ✅ Restructure the main page and give it its own minimal identity.
2. Move to **Astro** (a static-site tool built for content sites, first-class on Vercel). One content folder feeds every page, so nothing is written twice; posts and notes become simple Markdown files.
3. Add `/writing` and `/ideas`, then project pages under `/work`.
4. Add `/gallery` and `/now`.
5. Build `/ask` — a small serverless function on Vercel that calls an LLM with the site's own content as its only source.

## Open questions

- Who are the essays for, and what are the first 3 topics?
- How do you want to write — Markdown files, a simple web editor, or dictating to Claude?
- Which photos/images should the gallery start with?
- For `/ask`: is it OK for visitors' questions to be logged so you can see what people ask?
