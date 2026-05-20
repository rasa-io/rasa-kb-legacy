"""Build the legacy rasa.io KB archive site from per-article markdown files.

Directory structure expected:
    content/
        <category-slug>/
            _category.json       (optional, sets display name)
            <article-slug>.md    (one per article, with frontmatter)

Article frontmatter (between --- lines at top of file):
    ---
    title: Article title
    source: https://help.rasa.io/original-url
    keywords: kw1, kw2, kw3
    ---
    Article body in markdown...
"""
import json
import re
import shutil
from pathlib import Path

import markdown as md

ROOT = Path(__file__).parent.resolve()
CONTENT = ROOT / "content"
OUT = ROOT / "output"

BRAND = {
    "teal_dark": "#0e4f5c", "teal": "#1a7d8f", "teal_light": "#e6f3f5",
    "accent": "#00b8d4", "ink": "#1a1f2e", "ink_soft": "#4a5568",
    "muted": "#718096", "bg": "#ffffff", "bg_soft": "#f7fafc", "border": "#e2e8f0",
}

CATEGORY_ICONS = {
    "account": "👤", "analytics": "📊", "contacts": "👥", "content": "📰",
    "dashboard-walkthrough-and-videos": "🎬", "design": "🎨", "faqs": "❓",
    "general": "📘", "integrations": "🔌", "schedule": "📅", "support": "💬",
}

CATEGORY_ORDER = [
    "account", "analytics", "contacts", "content",
    "dashboard-walkthrough-and-videos", "design", "faqs",
    "general", "integrations", "schedule", "support",
]

def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw_fm = text[3:end].strip()
    body = text[end + 4:].lstrip("\n")
    meta = {}
    for line in raw_fm.split("\n"):
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        meta[key.strip()] = val.strip()
    return meta, body

def load_category(cat_dir: Path) -> dict | None:
    cat_slug = cat_dir.name
    meta_file = cat_dir / "_category.json"
    if meta_file.exists():
        meta = json.loads(meta_file.read_text(encoding="utf-8"))
        cat_name = meta.get("name", cat_slug.replace("-", " ").title())
    else:
        cat_name = cat_slug.replace("-", " ").title()
    articles = []
    for md_file in sorted(cat_dir.glob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        articles.append({
            "title": fm.get("title", md_file.stem),
            "slug": md_file.stem,
            "source": fm.get("source", ""),
            "keywords": fm.get("keywords", ""),
            "body_md": body,
            "file": md_file.name,
        })
    return {"name": cat_name, "slug": cat_slug, "articles": articles}

def load_content() -> list[dict]:
    categories = []
    seen = set()
    for cat_slug in CATEGORY_ORDER:
        cat_dir = CONTENT / cat_slug
        if not cat_dir.is_dir():
            continue
        cat = load_category(cat_dir)
        if cat and cat["articles"]:
            categories.append(cat); seen.add(cat_slug)
    for cat_dir in sorted(CONTENT.iterdir()):
        if not cat_dir.is_dir() or cat_dir.name in seen:
            continue
        cat = load_category(cat_dir)
        if cat and cat["articles"]:
            categories.append(cat)
    return categories

def escape_html(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;").replace("'", "&#39;"))

def render_md(text: str) -> str:
    return md.markdown(text, extensions=["extra", "sane_lists", "nl2br"], output_format="html5")

def base_css() -> str:
    return f""":root {{
    --teal-dark: {BRAND['teal_dark']}; --teal: {BRAND['teal']}; --teal-light: {BRAND['teal_light']};
    --accent: {BRAND['accent']}; --ink: {BRAND['ink']}; --ink-soft: {BRAND['ink_soft']};
    --muted: {BRAND['muted']}; --bg: {BRAND['bg']}; --bg-soft: {BRAND['bg_soft']}; --border: {BRAND['border']};
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: var(--ink); background: var(--bg); line-height: 1.6; font-size: 16px; -webkit-font-smoothing: antialiased; }}
a {{ color: var(--teal); text-decoration: none; }}
a:hover {{ color: var(--teal-dark); text-decoration: underline; }}
.topbar {{ position: sticky; top: 0; z-index: 100; background: var(--bg);
    border-bottom: 1px solid var(--border); padding: 14px 32px;
    display: flex; align-items: center; gap: 24px; }}
.topbar .brand {{ display: flex; align-items: center; }}
.topbar .brand-logo {{ height: 28px; width: auto; display: block; }}
.topbar .kb-tag {{ background: var(--teal-light); color: var(--teal-dark);
    padding: 3px 10px; border-radius: 12px; font-size: 12px; font-weight: 600; letter-spacing: 0.3px; }}
.topbar .spacer {{ flex: 1; }}
.topbar .search-wrap {{ position: relative; width: 360px; max-width: 100%; }}
.topbar input[type=search] {{ width: 100%; padding: 8px 12px 8px 36px;
    border: 1px solid var(--border); border-radius: 8px; font-size: 14px;
    background: var(--bg-soft) url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23718096' stroke-width='2'><circle cx='11' cy='11' r='8'/><line x1='21' y1='21' x2='16.65' y2='16.65'/></svg>") no-repeat 12px center;
    transition: border-color 0.15s, background 0.15s; }}
.topbar input[type=search]:focus {{ outline: none; border-color: var(--teal); background-color: var(--bg); }}
.search-results {{ position: absolute; top: calc(100% + 6px); left: 0; right: 0;
    background: var(--bg); border: 1px solid var(--border); border-radius: 8px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08); max-height: 420px; overflow-y: auto; display: none; }}
.search-results.show {{ display: block; }}
.search-results .sr-item {{ padding: 10px 14px; border-bottom: 1px solid var(--border);
    cursor: pointer; display: block; color: var(--ink); }}
.search-results .sr-item:last-child {{ border-bottom: none; }}
.search-results .sr-item:hover {{ background: var(--bg-soft); text-decoration: none; }}
.search-results .sr-title {{ font-weight: 600; font-size: 14px; color: var(--ink); }}
.search-results .sr-cat {{ font-size: 12px; color: var(--muted); margin-top: 2px; }}
.search-results .sr-empty {{ padding: 16px; color: var(--muted); font-size: 14px; text-align: center; }}
.layout {{ display: grid; grid-template-columns: 280px 1fr; min-height: calc(100vh - 60px); }}
.sidebar {{ background: var(--bg-soft); border-right: 1px solid var(--border);
    padding: 24px 0; overflow-y: auto; max-height: calc(100vh - 60px); position: sticky; top: 60px; }}
.sidebar h4 {{ text-transform: uppercase; font-size: 11px; letter-spacing: 0.6px;
    color: var(--muted); margin: 18px 24px 8px; font-weight: 700; }}
.sidebar a.cat-link {{ display: flex; align-items: center; gap: 10px;
    padding: 8px 24px; color: var(--ink-soft); font-size: 14px;
    border-left: 3px solid transparent; transition: background 0.12s, color 0.12s, border-color 0.12s; }}
.sidebar a.cat-link:hover {{ background: var(--teal-light); color: var(--teal-dark); text-decoration: none; }}
.sidebar a.cat-link.active {{ background: var(--teal-light); color: var(--teal-dark);
    border-left-color: var(--teal); font-weight: 600; }}
.sidebar .cat-icon {{ font-size: 16px; width: 20px; }}
.sidebar .cat-count {{ margin-left: auto; font-size: 12px; color: var(--muted);
    background: var(--bg); padding: 1px 8px; border-radius: 10px; }}
.main {{ padding: 40px 56px; max-width: 1100px; }}
.main.article-main {{ max-width: 820px; }}
.crumbs {{ font-size: 13px; color: var(--muted); margin-bottom: 18px;
    display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }}
.crumbs a {{ color: var(--muted); }}
.crumbs a:hover {{ color: var(--teal); }}
.crumbs .sep {{ color: var(--border); }}
.hero {{ background: linear-gradient(135deg, var(--teal-dark) 0%, var(--teal) 100%);
    color: white; padding: 56px 56px 48px; margin: -40px -56px 40px; }}
.hero h1 {{ font-size: 36px; margin-bottom: 12px; line-height: 1.2; }}
.hero p {{ font-size: 17px; opacity: 0.92; max-width: 640px; }}
.hero .hero-search {{ margin-top: 28px; max-width: 560px; position: relative; }}
.hero .hero-search input {{ width: 100%; padding: 14px 18px 14px 46px;
    border: none; border-radius: 10px; font-size: 15px;
    background: white url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='%230e4f5c' stroke-width='2'><circle cx='11' cy='11' r='8'/><line x1='21' y1='21' x2='16.65' y2='16.65'/></svg>") no-repeat 16px center;
    box-shadow: 0 4px 16px rgba(0,0,0,0.12); }}
.hero .hero-search input:focus {{ outline: 2px solid var(--accent); }}
.hero .hero-search .search-results {{ color: var(--ink); }}
.cat-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 18px; margin-top: 12px; }}
.cat-card {{ border: 1px solid var(--border); border-radius: 12px;
    padding: 22px; background: white;
    transition: transform 0.15s, box-shadow 0.15s, border-color 0.15s;
    display: block; color: inherit; }}
.cat-card:hover {{ transform: translateY(-2px); box-shadow: 0 8px 20px rgba(14, 79, 92, 0.10);
    border-color: var(--teal); text-decoration: none; }}
.cat-card .icon {{ font-size: 28px; margin-bottom: 10px; }}
.cat-card h3 {{ font-size: 17px; color: var(--ink); margin-bottom: 6px; }}
.cat-card .count {{ color: var(--muted); font-size: 13px; }}
.article-list {{ display: grid; grid-template-columns: 1fr; gap: 4px; margin-top: 8px; }}
.article-list a.art-item {{ display: flex; align-items: center; gap: 12px;
    padding: 14px 18px; border: 1px solid var(--border); border-radius: 8px;
    color: var(--ink); background: white;
    transition: border-color 0.12s, background 0.12s, transform 0.12s; }}
.article-list a.art-item:hover {{ border-color: var(--teal); background: var(--teal-light);
    text-decoration: none; transform: translateX(2px); }}
.article-list .art-arrow {{ margin-left: auto; color: var(--muted); }}
.article-list a.art-item:hover .art-arrow {{ color: var(--teal-dark); }}
.page-title {{ font-size: 30px; margin-bottom: 8px; color: var(--ink); }}
.page-desc {{ color: var(--muted); margin-bottom: 28px; }}
.article-header {{ margin-bottom: 28px; padding-bottom: 20px; border-bottom: 1px solid var(--border); }}
.article-header h1 {{ font-size: 32px; color: var(--ink); margin-bottom: 12px; line-height: 1.25; }}
.article-meta {{ display: flex; flex-wrap: wrap; gap: 14px; align-items: center;
    font-size: 13px; color: var(--muted); }}
.article-meta .src-link {{ color: var(--teal); }}
.keywords {{ display: flex; flex-wrap: wrap; gap: 6px; margin-top: 14px; }}
.keywords .kw {{ background: var(--bg-soft); color: var(--ink-soft);
    padding: 3px 9px; border-radius: 10px; font-size: 11px; border: 1px solid var(--border); }}
.article-body {{ font-size: 16px; color: var(--ink); }}
.article-body h1, .article-body h2, .article-body h3, .article-body h4 {{
    margin-top: 28px; margin-bottom: 12px; line-height: 1.3; color: var(--ink); }}
.article-body h1 {{ font-size: 24px; }}
.article-body h2 {{ font-size: 21px; }}
.article-body h3 {{ font-size: 18px; }}
.article-body h4 {{ font-size: 16px; }}
.article-body p {{ margin-bottom: 14px; }}
.article-body ul, .article-body ol {{ margin: 0 0 16px 22px; }}
.article-body li {{ margin-bottom: 6px; }}
.article-body code {{ background: var(--bg-soft); padding: 1px 6px; border-radius: 4px;
    font-size: 0.92em; border: 1px solid var(--border); }}
.article-body pre {{ background: var(--bg-soft); padding: 14px 16px; border-radius: 8px;
    overflow-x: auto; border: 1px solid var(--border); margin-bottom: 16px; }}
.article-body pre code {{ border: none; padding: 0; background: transparent; }}
.article-body blockquote {{ border-left: 3px solid var(--teal); padding: 6px 14px;
    background: var(--teal-light); color: var(--ink-soft); margin-bottom: 16px; border-radius: 0 6px 6px 0; }}
.article-body img {{ max-width: 100%; height: auto; border-radius: 6px; margin: 10px 0; }}
.article-body a {{ word-break: break-word; }}
.article-body table {{ border-collapse: collapse; margin: 14px 0; width: 100%; }}
.article-body th, .article-body td {{ border: 1px solid var(--border); padding: 8px 12px; text-align: left; }}
.article-body th {{ background: var(--bg-soft); font-weight: 600; }}
.article-nav {{ margin-top: 40px; padding-top: 24px; border-top: 1px solid var(--border);
    display: flex; gap: 12px; flex-wrap: wrap; }}
.article-nav a {{ flex: 1; min-width: 200px; border: 1px solid var(--border);
    border-radius: 8px; padding: 14px 16px; color: var(--ink);
    transition: border-color 0.12s, background 0.12s; }}
.article-nav a:hover {{ border-color: var(--teal); background: var(--teal-light); text-decoration: none; }}
.article-nav .label {{ font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.5px; }}
.article-nav .title {{ font-weight: 600; margin-top: 4px; color: var(--ink); }}
.article-nav .next {{ text-align: right; }}
.footer {{ border-top: 1px solid var(--border); padding: 28px 56px;
    color: var(--muted); font-size: 13px; background: var(--bg-soft); text-align: center; }}
@media (max-width: 900px) {{
    .layout {{ grid-template-columns: 1fr; }}
    .sidebar {{ position: static; max-height: none; border-right: none; border-bottom: 1px solid var(--border); }}
    .main {{ padding: 24px; }}
    .hero {{ padding: 36px 24px; margin: -24px -24px 24px; }}
    .hero h1 {{ font-size: 26px; }}
    .topbar {{ padding: 12px 16px; gap: 12px; }}
    .topbar .search-wrap {{ width: auto; flex: 1; }}
    .topbar .kb-tag {{ display: none; }}
    .footer {{ padding: 20px 24px; }}
}}
"""

def js_search() -> str:
    return r"""
(function() {
    let INDEX = null; let indexPromise = null;
    function loadIndex() {
        if (indexPromise) return indexPromise;
        indexPromise = fetch(window.KB_ROOT + 'search-index.json')
            .then(r => r.json()).then(data => { INDEX = data; return data; });
        return indexPromise;
    }
    function escapeHtml(s) {
        return s.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
    }
    function attachSearch(inputId, resultsId) {
        const input = document.getElementById(inputId);
        const results = document.getElementById(resultsId);
        if (!input || !results) return;
        input.addEventListener('focus', loadIndex);
        let cur = -1;
        function render(query) {
            if (!INDEX || !query.trim()) {
                results.classList.remove('show'); results.innerHTML = ''; cur = -1; return;
            }
            const q = query.toLowerCase().trim();
            const tokens = q.split(/\s+/).filter(Boolean);
            const scored = [];
            for (const item of INDEX.articles) {
                let score = 0;
                const titleLow = item.title.toLowerCase();
                const haystack = (item.title + ' ' + item.category + ' ' + item.keywords + ' ' + item.preview).toLowerCase();
                for (const tok of tokens) {
                    if (titleLow.includes(tok)) score += 5;
                    if (haystack.includes(tok)) score += 1;
                }
                if (score > 0) scored.push({item, score});
            }
            scored.sort((a, b) => b.score - a.score);
            const top = scored.slice(0, 12);
            if (!top.length) {
                results.innerHTML = '<div class="sr-empty">No matches</div>';
            } else {
                results.innerHTML = top.map(s => `
                    <a class="sr-item" href="${window.KB_ROOT}${s.item.url}">
                        <div class="sr-title">${escapeHtml(s.item.title)}</div>
                        <div class="sr-cat">${escapeHtml(s.item.category)}</div>
                    </a>
                `).join('');
            }
            results.classList.add('show'); cur = -1;
        }
        input.addEventListener('input', e => {
            loadIndex().then(() => render(e.target.value));
        });
        input.addEventListener('keydown', e => {
            const items = results.querySelectorAll('.sr-item');
            if (e.key === 'ArrowDown') {
                e.preventDefault(); cur = Math.min(cur + 1, items.length - 1);
                items.forEach((el, i) => el.style.background = i === cur ? 'var(--bg-soft)' : '');
                if (items[cur]) items[cur].scrollIntoView({block: 'nearest'});
            } else if (e.key === 'ArrowUp') {
                e.preventDefault(); cur = Math.max(cur - 1, 0);
                items.forEach((el, i) => el.style.background = i === cur ? 'var(--bg-soft)' : '');
                if (items[cur]) items[cur].scrollIntoView({block: 'nearest'});
            } else if (e.key === 'Enter') {
                if (cur >= 0 && items[cur]) { e.preventDefault(); window.location = items[cur].href; }
            } else if (e.key === 'Escape') {
                results.classList.remove('show'); input.blur();
            }
        });
        document.addEventListener('click', e => {
            if (!input.contains(e.target) && !results.contains(e.target)) {
                results.classList.remove('show');
            }
        });
    }
    window.attachKBSearch = attachSearch;
})();
"""

def page_template(title: str, body: str, root_rel: str, sidebar_html: str, body_class: str = "") -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · rasa.io Knowledge Base</title>
<link rel="stylesheet" href="{root_rel}assets/style.css">
<link rel="icon" type="image/png" href="{root_rel}assets/favicon.png">
<link rel="apple-touch-icon" href="{root_rel}assets/favicon.png">
<script>window.KB_ROOT = "{root_rel}";</script>
</head>
<body class="{body_class}">
<header class="topbar">
    <a href="{root_rel}index.html" class="brand">
        <img src="{root_rel}assets/rasa-logo.png" alt="rasa.io" class="brand-logo">
    </a>
    <span class="kb-tag">Knowledge Base</span>
    <span class="spacer"></span>
    <div class="search-wrap">
        <input type="search" id="topbar-search" placeholder="Search the knowledge base…" autocomplete="off">
        <div class="search-results" id="topbar-search-results"></div>
    </div>
</header>
<div class="layout">
    {sidebar_html}
    <main class="main {body_class}">
        {body}
    </main>
</div>
<footer class="footer">rasa.io Knowledge Base </footer>
<script src="{root_rel}assets/search.js"></script>
<script>
    window.attachKBSearch('topbar-search', 'topbar-search-results');
    const hs = document.getElementById('hero-search');
    if (hs) window.attachKBSearch('hero-search', 'hero-search-results');
</script>
</body>
</html>
"""

def render_sidebar(categories, current_slug, root_rel):
    items = ['<aside class="sidebar"><h4>Browse by category</h4>']
    items.append(f'<a class="cat-link {"active" if current_slug == "__home__" else ""}" href="{root_rel}index.html"><span class="cat-icon">🏠</span><span>Home</span></a>')
    for cat in categories:
        active = "active" if current_slug == cat["slug"] else ""
        icon = CATEGORY_ICONS.get(cat["slug"], "📄")
        items.append(
            f'<a class="cat-link {active}" href="{root_rel}categories/{cat["slug"]}.html">'
            f'<span class="cat-icon">{icon}</span>'
            f'<span>{escape_html(cat["name"])}</span>'
            f'<span class="cat-count">{len(cat["articles"])}</span>'
            f'</a>'
        )
    items.append("</aside>")
    return "\n".join(items)

def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    (OUT / "assets").mkdir()
    (OUT / "categories").mkdir()
    (OUT / "articles").mkdir()
    (OUT / "assets" / "style.css").write_text(base_css(), encoding="utf-8")
    (OUT / "assets" / "search.js").write_text(js_search(), encoding="utf-8")
    # copy static assets (logo, etc.) if the assets_static dir exists
    static_src = ROOT / "assets_static"
    if static_src.is_dir():
        for f in static_src.iterdir():
            if f.is_file():
                shutil.copy2(f, OUT / "assets" / f.name)
    categories = load_content()
    total_articles = sum(len(c["articles"]) for c in categories)
    print(f"Loaded {len(categories)} categories, {total_articles} articles")
    index_articles = []
    for cat in categories:
        for art in cat["articles"]:
            preview_raw = re.sub(r"[#*`>\-\[\]()]", " ", art["body_md"])
            preview_raw = re.sub(r"\s+", " ", preview_raw).strip()
            index_articles.append({
                "title": art["title"], "category": cat["name"],
                "url": f"articles/{cat['slug']}--{art['slug']}.html",
                "keywords": art["keywords"], "preview": preview_raw[:280],
            })
    (OUT / "search-index.json").write_text(
        json.dumps({"articles": index_articles}, ensure_ascii=False), encoding="utf-8")
    home_sidebar = render_sidebar(categories, "__home__", "")
    cat_cards = []
    for cat in categories:
        icon = CATEGORY_ICONS.get(cat["slug"], "📄")
        cat_cards.append(
            f'<a class="cat-card" href="categories/{cat["slug"]}.html">'
            f'<div class="icon">{icon}</div>'
            f'<h3>{escape_html(cat["name"])}</h3>'
            f'<div class="count">{len(cat["articles"])} article{"s" if len(cat["articles"]) != 1 else ""}</div>'
            f'</a>'
        )
    home_body = f"""
<section class="hero">
    <h1>How can we help?</h1>
    <p>Find answers, walkthroughs, and best practices for getting the most out of rasa.io.</p>
    <div class="hero-search">
        <input type="search" id="hero-search" placeholder="Search articles, features, topics…" autocomplete="off">
        <div class="search-results" id="hero-search-results"></div>
    </div>
</section>
<h2 style="margin: 8px 0 18px; font-size: 22px;">Browse by category</h2>
<div class="cat-grid">{''.join(cat_cards)}</div>
<p style="margin-top: 32px; color: var(--muted); font-size: 14px;">
    {total_articles} articles across {len(categories)} categories.
</p>
"""
    (OUT / "index.html").write_text(
        page_template("Home", home_body, "", home_sidebar, body_class="home"), encoding="utf-8")
    for cat in categories:
        sidebar = render_sidebar(categories, cat["slug"], "../")
        items_html = []
        for art in sorted(cat["articles"], key=lambda a: a["title"].lower()):
            items_html.append(
                f'<a class="art-item" href="../articles/{cat["slug"]}--{art["slug"]}.html">'
                f'<span>{escape_html(art["title"])}</span>'
                f'<span class="art-arrow">→</span></a>'
            )
        icon = CATEGORY_ICONS.get(cat["slug"], "📄")
        body = f"""
<nav class="crumbs">
    <a href="../index.html">Home</a><span class="sep">/</span>
    <span>{escape_html(cat["name"])}</span>
</nav>
<h1 class="page-title">{icon} {escape_html(cat["name"])}</h1>
<p class="page-desc">{len(cat["articles"])} article{"s" if len(cat["articles"]) != 1 else ""} in this category.</p>
<div class="article-list">{''.join(items_html)}</div>
"""
        (OUT / "categories" / f"{cat['slug']}.html").write_text(
            page_template(cat["name"], body, "../", sidebar), encoding="utf-8")
    for cat in categories:
        sidebar = render_sidebar(categories, cat["slug"], "../")
        cat_articles = cat["articles"]
        for cat_idx, art in enumerate(cat_articles):
            body_html = render_md(art["body_md"])
            kw_html = ""
            if art["keywords"]:
                chips = [f'<span class="kw">{escape_html(k.strip())}</span>'
                         for k in art["keywords"].split(",") if k.strip()]
                kw_html = f'<div class="keywords">{"".join(chips)}</div>'
            source_html = ""
            if art["source"]:
                source_html = f'<a class="src-link" href="{escape_html(art["source"])}" target="_blank" rel="noopener">View original ↗</a>'
            prev_art = cat_articles[cat_idx - 1] if cat_idx > 0 else None
            next_art = cat_articles[cat_idx + 1] if cat_idx < len(cat_articles) - 1 else None
            nav_parts = []
            if prev_art:
                nav_parts.append(
                    f'<a href="{cat["slug"]}--{prev_art["slug"]}.html">'
                    f'<div class="label">← Previous</div>'
                    f'<div class="title">{escape_html(prev_art["title"])}</div></a>'
                )
            if next_art:
                nav_parts.append(
                    f'<a class="next" href="{cat["slug"]}--{next_art["slug"]}.html">'
                    f'<div class="label">Next →</div>'
                    f'<div class="title">{escape_html(next_art["title"])}</div></a>'
                )
            body = f"""
<nav class="crumbs">
    <a href="../index.html">Home</a><span class="sep">/</span>
    <a href="../categories/{cat["slug"]}.html">{escape_html(cat["name"])}</a>
    <span class="sep">/</span><span>{escape_html(art["title"])}</span>
</nav>
<article>
    <header class="article-header">
        <h1>{escape_html(art["title"])}</h1>
        <div class="article-meta">
            <span>📁 <a href="../categories/{cat["slug"]}.html">{escape_html(cat["name"])}</a></span>
            {f'<span>{source_html}</span>' if source_html else ''}
        </div>
        {kw_html}
    </header>
    <div class="article-body">{body_html}</div>
    <nav class="article-nav">{''.join(nav_parts)}</nav>
</article>
"""
            (OUT / "articles" / f"{cat['slug']}--{art['slug']}.html").write_text(
                page_template(art["title"], body, "../", sidebar, body_class="article-main"),
                encoding="utf-8")
    print(f"Built site in {OUT}")
    print(f"  Pages: 1 home + {len(categories)} category + {total_articles} article = {1 + len(categories) + total_articles} total")

if __name__ == "__main__":
    build()
