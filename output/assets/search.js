
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
