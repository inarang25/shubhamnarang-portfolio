# shubhamnarang.in — roadmap

Working notes for growing this site from a portfolio into a full personal home (a "digital twin"): ideas, projects, writing, images, all in one place.

## Where it is now

| URL | File | What it is |
|---|---|---|
| `/` | `index.html` | **Executive view** — the main site, built for a boardroom audience. |
| `/builder` | `builder.html` | **Builder view** — the pop-art take on the same story. |
| anything else | `404.html` | Not-found page. |

Both views share one header: name, section links (Work · Career · Lab · Contact) and an **Executive view / Builder view** switch.

### Information structure (Executive view)

1. **Intro** — one sentence on what I do, one on the background.
2. **Now** — what has my attention this season (work, side project, learning).
3. **Selected work** — only two: demand.ai & Project Vihan (enterprise), nurchur.in (my own product).
4. **The path** — career and education, one line each, plus certifications.
5. **Lab** — capstone studies as a compact list, honestly labelled as early work in progress.
6. **Writing** — placeholder until the first essays exist.
7. **Contact.**

### Design language (Executive view)

- Restrained and boardroom-grade; Indian character comes through craft details, not decoration.
- Colour: porcelain white `#F7F6F2`, ink green `#13201B` text, deep bottle green `#1E4535` buttons, antique gold `#7E5F1C` labels and `#A7853A` hairlines.
- Type: Cormorant Garamond (headings), Hanken Grotesk (body), Tiro Devanagari Hindi for the name in Devanagari.
- Detail: a fine gold Mughal jaali (eight-pointed star lattice) fading in behind the hero and contact; the portrait as a monochrome engraving set in an arched (jharokha) frame; an eight-pointed star as the only ornament.

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
