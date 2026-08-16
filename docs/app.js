const state = { skills: [], categories: [], activeCategory: 'All domains', query: '', visible: 36 };
const els = {};

const formatNumber = (value) => new Intl.NumberFormat('en-US').format(value);
const escapeHtml = (value) => String(value).replace(/[&<>'"]/g, (char) => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', "'":'&#039;', '"':'&quot;' }[char]));

function cacheElements() {
  els.categoryList = document.querySelector('#category-list');
  els.grid = document.querySelector('#skill-grid');
  els.search = document.querySelector('#search-input');
  els.clear = document.querySelector('#clear-button');
  els.resultCount = document.querySelector('#result-count');
  els.activeFilter = document.querySelector('#active-filter');
  els.loadMore = document.querySelector('#load-more');
  els.empty = document.querySelector('#empty-state');
  els.heroTotal = document.querySelector('#hero-total');
  els.heroCategories = document.querySelector('#hero-categories');
}

function renderCategories() {
  const all = [{ name: 'All domains', count: state.skills.length }, ...state.categories];
  els.categoryList.innerHTML = all.map((category) => `
    <button class="category-button ${category.name === state.activeCategory ? 'active' : ''}" type="button" data-category="${escapeHtml(category.name)}">
      <span>${escapeHtml(category.name)}</span><span>${formatNumber(category.count)}</span>
    </button>`).join('');
  els.categoryList.querySelectorAll('[data-category]').forEach((button) => {
    button.addEventListener('click', () => {
      state.activeCategory = button.dataset.category;
      state.visible = 36;
      renderCategories();
      renderResults();
    });
  });
}

function filteredSkills() {
  const query = state.query.trim().toLowerCase();
  return state.skills.filter((skill) => {
    const inCategory = state.activeCategory === 'All domains' || skill.category === state.activeCategory;
    if (!inCategory) return false;
    if (!query) return true;
    return `${skill.name} ${skill.description} ${skill.category}`.toLowerCase().includes(query);
  });
}

function renderCard(skill) {
  return `<article class="skill-card">
    <div>
      <div class="skill-top"><div class="skill-name">${escapeHtml(skill.name)}</div><span class="skill-index">${String(skill.index).padStart(3, '0')}</span></div>
      <p class="skill-description">${escapeHtml(skill.description || 'Capability definition available in the upstream source.')}</p>
    </div>
    <div class="skill-bottom"><span class="skill-category">${escapeHtml(skill.category)}</span><a class="skill-link" href="${escapeHtml(skill.url)}" target="_blank" rel="noreferrer">Open source ↗</a></div>
  </article>`;
}

function renderResults() {
  const results = filteredSkills();
  const visible = results.slice(0, state.visible);
  els.grid.innerHTML = visible.map(renderCard).join('');
  els.empty.hidden = results.length !== 0;
  els.grid.hidden = results.length === 0;
  els.resultCount.textContent = `${formatNumber(results.length)} result${results.length === 1 ? '' : 's'} indexed`;
  els.activeFilter.textContent = state.activeCategory === 'All domains' ? '' : `· ${state.activeCategory}`;
  els.loadMore.hidden = visible.length >= results.length || results.length === 0;
  if (!els.loadMore.hidden) els.loadMore.innerHTML = `Load more results <span>↓</span> <small>(${formatNumber(results.length - visible.length)} remaining)</small>`;
}

function bindInteractions() {
  els.search.addEventListener('input', (event) => {
    state.query = event.target.value;
    state.visible = 36;
    renderResults();
  });
  els.clear.addEventListener('click', () => {
    els.search.value = '';
    state.query = '';
    state.activeCategory = 'All domains';
    state.visible = 36;
    renderCategories();
    renderResults();
    els.search.focus();
  });
  els.loadMore.addEventListener('click', () => {
    state.visible += 36;
    renderResults();
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === '/' && document.activeElement !== els.search) {
      event.preventDefault();
      els.search.focus();
    }
    if (event.key === 'Escape' && document.activeElement === els.search) els.search.blur();
  });
}

async function init() {
  cacheElements();
  try {
    const response = await fetch('data/skills.json');
    if (!response.ok) throw new Error(`Catalog request failed: ${response.status}`);
    const payload = await response.json();
    state.skills = payload.skills || [];
    state.categories = payload.categories || [];
    els.heroTotal.textContent = formatNumber(payload.total || state.skills.length);
    els.heroCategories.textContent = formatNumber(state.categories.length);
    renderCategories();
    renderResults();
    bindInteractions();
  } catch (error) {
    els.resultCount.textContent = 'Catalog unavailable';
    els.empty.hidden = false;
    els.empty.querySelector('h3').textContent = 'The catalog is offline.';
    els.empty.querySelector('p').textContent = 'Run the repository build script to regenerate docs/data/skills.json.';
    console.error(error);
  }
}

init();
