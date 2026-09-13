// Progressive enhancement: inventory and links are rendered at build time.
document.querySelectorAll('[data-current-year], #year').forEach(node => {
  node.textContent = new Date().getFullYear();
});
const menuToggle = document.getElementById('menuToggle');
const mainNav = document.getElementById('mainNav');
function closeMenu() {
  if (!menuToggle || !mainNav) return;
  menuToggle.setAttribute('aria-expanded', 'false');
  menuToggle.setAttribute('aria-label', 'Open navigation menu');
  mainNav.classList.remove('open');
  document.body.classList.remove('menu-open');
}
if (menuToggle && mainNav) {
  menuToggle.addEventListener('click', () => {
    const opening = menuToggle.getAttribute('aria-expanded') !== 'true';
    menuToggle.setAttribute('aria-expanded', String(opening));
    menuToggle.setAttribute('aria-label', opening ? 'Close navigation menu' : 'Open navigation menu');
    mainNav.classList.toggle('open', opening);
    document.body.classList.toggle('menu-open', opening);
  });
  mainNav.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menuToggle.getAttribute('aria-expanded') === 'true') {
      closeMenu();
      menuToggle.focus();
    }
  });
  window.addEventListener('resize', () => { if (window.innerWidth > 820) closeMenu(); });
}
const grid = document.getElementById('domainGrid');
const filters = document.getElementById('filters');
const resultCount = document.getElementById('resultCount');
if (grid && filters) {
  const cards = [...grid.querySelectorAll('[data-category]')];
  const categories = ['All', 'Featured', ...new Set(cards.map(card => card.dataset.category))];
  categories.forEach((category, index) => {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'filter' + (index === 0 ? ' active' : '');
    button.textContent = category;
    button.setAttribute('aria-pressed', String(index === 0));
    button.addEventListener('click', () => {
      filters.querySelectorAll('button').forEach(item => {
        item.classList.toggle('active', item === button);
        item.setAttribute('aria-pressed', String(item === button));
      });
      cards.forEach(card => {
        card.hidden = !(category === 'All' || card.dataset.category === category ||
          (category === 'Featured' && card.dataset.featured === 'true'));
      });
      const count = cards.filter(card => !card.hidden).length;
      resultCount.textContent = count + (count === 1 ? ' domain shown' : ' domains shown');
    });
    filters.appendChild(button);
  });
  filters.hidden = false;
}
