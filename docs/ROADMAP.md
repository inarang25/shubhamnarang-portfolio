# Portfolio roadmap & brainstorm

Working notes for the next round of work on the site. Pick up from **Open questions** and **Next up**.

## Where the site is today

| URL | File | Design |
|---|---|---|
| `/` | `index.html` | Boardroom — Apple-style "Keynote" (Option C from the design canvas) |
| `/builder` | `builder.html` | Builder — comic-book "Issue #01" (Option A) |
| anything else | `404.html` | Boardroom-styled not-found page |

Plain static HTML, deployed by Vercel from `main`. `vercel.json` turns on clean URLs (`/builder` instead of `/builder.html`).

## What's not working well yet

1. **Content got thinner in the redesign.** The old page had full case studies (problem → approach → outcome), dashboard screenshots, "View live" Power BI / Tableau embeds, a logo strip, and clickable side projects (Streamlit app, notebooks, Celonis post). The new designs only have one-liners. Images for all of it are still in `images/` and the old page is in git history (commit `0b11d11`).
2. **Everything is written twice.** Both pages hold their own copy of the same career, stats and projects, so every update means editing two files and they will drift.
3. **The two pages don't have distinct jobs.** The Builder page still leads with Mahindra and "Boardroom + Builder"; the Boardroom page leads with nurchur.in. Each lens should tell its own story.
4. **Hard to edit by hand.** The HTML came out of a design tool, so styling is inline on every element.
5. **No place for writing**, so no blog yet.
6. **Social previews are half-done.** `og:image` is a relative path; LinkedIn/WhatsApp want a full URL (needs the final domain).

## Proposed structure

```
/                    Boardroom: enterprise data & AI strategy, career, outcomes
/builder             Builder: products shipped, side projects, stack
/work/<slug>         One page per case study (nurchur, demand.ai & Vihan, EV market, dashboards)
/blog                Writing — list, tags, RSS
/blog/<slug>         One post
/about               Longer story, photo, résumé PDF download
/now   (optional)    What I'm focused on this month
```

Both lenses link into the same `/work` and `/blog` pages, each styled in its own theme.

## Tech options for the blog

| Option | Writing a post | Effort | Notes |
|---|---|---|---|
| **Astro** (recommended) | Add a Markdown file (from GitHub's web editor, VS Code, Obsidian, or ask Claude) | Medium, one-time migration | Static and fast, built for content sites, first-class on Vercel. One data file feeds both lenses, fixing the "written twice" problem. |
| Astro + a CMS (Decap / Tina / Notion) | Write in a web editor, no Git | Medium+ | Add later if Markdown feels awkward. |
| Next.js | Markdown / MDX | Higher | More than a portfolio needs unless app features come. |
| Stay plain HTML | Hand-write HTML per post | Low now, painful later | Fine for 1–2 posts, not for a habit. |
| External (Substack / Medium / Hashnode) | Their editor | Lowest | Posts live off-site; only list/link them here. |

Migration note: Astro needs a build step, so the Vercel project's framework preset changes from "Other" to "Astro". Do it on a branch and check the preview URL before merging.

## Feature ideas (not committed)

- **Case study pages** with screenshots and click-to-load live dashboards.
- **Dashboard gallery** — filterable by domain (manufacturing, hospitality, FMCG, aviation, SaaS).
- **Résumé PDF** download.
- **Contact form** (Formspree or a Vercel function) besides email.
- **Vercel Web Analytics** — which lens people pick, which projects get opened.
- **Newsletter signup** for the blog (Buttondown / Substack embed).
- **Remember the lens** a visitor last picked.
- **Dark mode** for the Boardroom page.
- **sitemap.xml + robots.txt** and per-page social images.
- **Testimonials / recommendations** from LinkedIn.

## Next up (suggested order)

1. **Restore the lost depth** in the current static pages: project links, screenshots, live embeds, logo strip. Quick, no tooling change.
2. **Give each lens its own story** — Builder leads with products, Boardroom with enterprise outcomes.
3. **Migrate to Astro** with a single content file feeding both themes.
4. **Add the blog** (`/blog`, Markdown posts, RSS, tags), then the extras above.

## Open questions

- What's the live domain? (Needed for social previews, sitemap, RSS.)
- Who is the blog for, and what topics? (Data/AI strategy for leaders? Build logs from side projects? Both, tagged by lens?)
- How do you want to write — Markdown files, a web editor/CMS, or posting elsewhere and linking?
- Should `/` stay Boardroom-first, or become a small landing page where visitors pick a lens?
- Keep the comic style for Builder long-term, or explore the Blueprint / Material options from the canvas?
- Résumé PDF to add? Any testimonials?

## Done

- 2026-10-27 — Rebuilt as Boardroom (Keynote) + Builder (Comic) pages (PR #1).
- 2026-10-28 — Clean URLs, 404 page, favicon, social meta, portrait compressed 889 KB → 83 KB (WebP), this roadmap.
