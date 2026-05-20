# rasa.io Legacy KB — Archive Site

A self-contained static site preserving the legacy rasa.io HubSpot KB. **144 articles across 11 categories**, hosted independently so the HubSpot KB can be repurposed for the new Send dashboard documentation.

## Folder structure

```
rasa-kb-site/
├── content/                   ← THE EDITABLE SOURCE
│   ├── account/
│   │   ├── _category.json
│   │   ├── anti-spam-email-requirements....md
│   │   ├── billing-updating-payment....md
│   │   └── ...
│   ├── analytics/
│   ├── contacts/
│   └── ... (11 categories total)
├── output/                    ← THE BUILT SITE (do not edit by hand)
│   ├── index.html
│   ├── categories/
│   ├── articles/
│   ├── assets/
│   └── search-index.json
├── build.py                   ← rebuild output/ from content/
└── README.md
```

## Editing an article

Every article is a single markdown file at `content/<category>/<article-slug>.md` with this structure:

```markdown
---
title: Anti-Spam Email Requirements and Deliverability Considerations
source: https://help.rasa.io/anti-spam-email-requirements-and-deliverability-considerations
keywords: security, deliverability, CAN-SPAM, ...
---

At rasa.io, we take anti-spam email requirements...
```

- The block between the `---` lines is the article's metadata. Don't break that format.
- Everything below is the body, in standard markdown (headings with `#`, lists with `-`, links as `[text](url)`, etc.).
- The filename becomes part of the URL — leave it alone unless you want to break existing links.

After editing, rebuild:

```bash
python3 build.py
```

That regenerates the entire `output/` folder. Then redeploy (or, if hosting on Netlify with auto-deploy, just push the edited markdown to GitHub and it rebuilds automatically).

## Adding a new article

1. Pick the right category folder under `content/`.
2. Create a new `.md` file. Filename should be lowercase, hyphens for spaces (e.g. `how-to-do-the-thing.md`).
3. Include the frontmatter block at the top with at least `title:`.
4. Write the body.
5. Run `python3 build.py`.

## Deleting an article

Delete the `.md` file. Run `python3 build.py`. Done.

## Hosting

This is pure static HTML/CSS/JS. The most painless setup:

1. Put this whole folder in a GitHub repo
2. Connect the repo to [Netlify](https://netlify.com) (free)
3. Set the build command to `python3 build.py` and the publish directory to `output`
4. Every time you (or anyone with repo access) edits a file in GitHub's web interface, Netlify rebuilds and redeploys automatically

GitHub's web editor lets you click any `.md` file, hit the pencil icon, edit in the browser, click "Commit." No terminal required for routine edits.

Alternative: skip the GitHub auto-deploy and just drag the `output/` folder onto [app.netlify.com/drop](https://app.netlify.com/drop) whenever you rebuild. Less automated but zero setup.

## What's not included

- **Visitor analytics** (Google Analytics, etc.) — not added because no service was specified. To add, edit the `page_template` function in `build.py` and put your tracking snippet in the `<head>`.
- **A real logo** — the topbar shows a placeholder "r" tile. Drop the rasa.io PNG in `output/assets/` and update the brand markup in `build.py` when ready.
- **Redirects from old HubSpot URLs** — once this lives at a real domain, you'll want `help.rasa.io/old-article-url` → `kb-archive.rasa.io/articles/category--article.html`. Each article preserves its original URL in the `source:` frontmatter field, which gives you the full mapping.

## Notes

- Drafts from the original export (7 articles) are not included — they were placeholders for content that was never finished.
- The Dashboard Walkthrough and Videos category has 2 articles; Video Overviews dropped out entirely since all 6 of its entries were drafts.
