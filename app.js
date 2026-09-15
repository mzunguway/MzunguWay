// Localized progressive enhancement. Inventory and translated content are static HTML.
const lang = document.documentElement.lang || 'en';
const ui = (window.MW_UI || {})[lang] || {};
document.querySelectorAll('[data-current-year], #year').forEach(n => { n.textContent = new Date().getFullYear(); });
const toggle = document.getElementById('menuToggle');
const nav = document.getElementById('mainNav');
function closeMenu() {
  if (!toggle || !nav) return;
  toggle.setAttribute('aria-expanded', 'false');
  toggle.setAttribute('aria-label', ui.menu || 'Open menu');
  nav.classList.remove('open'); document.body.classList.remove('menu-open');
}
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? ui.close : ui.menu);
    nav.classList.toggle('open', open); document.body.classList.toggle('menu-open', open);
  });
  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));
  document.addEventListener('keydown', e => { if(e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true'){closeMenu();toggle.focus();} });
  window.addEventListener('resize', () => { if(window.innerWidth > 820) closeMenu(); });
}

// Visual and acquisition improvements are isolated in a small override stylesheet.
if (!document.querySelector('link[data-mw-improvements]')) {
  const improvementStyles = document.createElement('link');
  improvementStyles.rel = 'stylesheet';
  improvementStyles.href = '/improvements.css?v=1';
  improvementStyles.dataset.mwImprovements = 'true';
  document.head.appendChild(improvementStyles);
}

const grid = document.getElementById('domainGrid');
const filters = document.getElementById('filters');

// Newly acquired domains. Kept here as a minimal additive layer so the validated static pages remain untouched.
const newDomains = {
  en: [
    {name:'glucosehack.com',category:'Health & Wellness',desc:'A memorable name for glucose-aware habits and metabolic insight.',uses:'Glucose education · Meal experiments · Habit tracking · Metabolic wellness',concept:'A consumer platform that helps users organize glucose readings, meals, activity and notes into understandable experiments and trends, without replacing medical advice.'},
    {name:'instantpaylayer.com',category:'Payments Infrastructure',desc:'A strong infrastructure name for instant-payment orchestration.',uses:'Instant payments · API orchestration · Routing · Settlement workflows',concept:'An API layer that connects apps to multiple instant-payment rails and normalizes requests, routing, status updates and operational controls.'},
    {name:'kychuman.com',category:'Identity & Trust',desc:'A direct name for human verification in KYC workflows.',uses:'Human verification · KYC review · Identity checks · Compliance workflows',concept:'An identity-verification layer that helps teams confirm a real human is behind an onboarding or high-risk action, combining checks, review queues and audit trails.'}
  ],
  fr: [
    {name:'glucosehack.com',category:'Santé & bien-être',desc:'Un nom mémorable pour les habitudes liées au glucose et les données métaboliques.',uses:'Éducation au glucose · Expériences alimentaires · Suivi des habitudes · Bien-être métabolique',concept:'Une plateforme grand public pour organiser mesures de glucose, repas, activité et notes en expériences et tendances compréhensibles, sans se substituer à un avis médical.'},
    {name:'instantpaylayer.com',category:'Infrastructure de paiement',desc:'Un nom d’infrastructure clair pour l’orchestration des paiements instantanés.',uses:'Paiements instantanés · Orchestration API · Routage · Flux de règlement',concept:'Une couche API reliant des applications à plusieurs rails de paiement instantané, avec normalisation des requêtes, du routage, des statuts et des contrôles opérationnels.'},
    {name:'kychuman.com',category:'Identité & confiance',desc:'Un nom direct pour la vérification humaine dans les parcours KYC.',uses:'Vérification humaine · Revue KYC · Contrôles d’identité · Conformité',concept:'Une couche de vérification d’identité aidant les équipes à confirmer qu’une personne réelle se trouve derrière une inscription ou une action sensible, avec contrôles, files de revue et piste d’audit.'}
  ],
  de: [
    {name:'glucosehack.com',category:'Gesundheit & Wellness',desc:'Ein einprägsamer Name für glucosebewusste Gewohnheiten und metabolische Einblicke.',uses:'Glukose-Wissen · Mahlzeiten-Experimente · Gewohnheitstracking · Metabolisches Wohlbefinden',concept:'Eine Verbraucherplattform, die Glukosewerte, Mahlzeiten, Aktivität und Notizen zu verständlichen Experimenten und Trends zusammenführt, ohne medizinische Beratung zu ersetzen.'},
    {name:'instantpaylayer.com',category:'Zahlungsinfrastruktur',desc:'Ein klarer Infrastrukturname für die Orchestrierung von Echtzeitzahlungen.',uses:'Echtzeitzahlungen · API-Orchestrierung · Routing · Abwicklungsprozesse',concept:'Eine API-Schicht, die Anwendungen mit mehreren Echtzeit-Zahlungswegen verbindet und Anfragen, Routing, Statusmeldungen und operative Kontrollen vereinheitlicht.'},
    {name:'kychuman.com',category:'Identität & Vertrauen',desc:'Ein direkter Name für menschliche Verifikation in KYC-Prozessen.',uses:'Menschliche Verifikation · KYC-Prüfung · Identitätschecks · Compliance-Workflows',concept:'Eine Identitätsprüfungsschicht, mit der Teams bestätigen können, dass hinter einem Onboarding oder einer risikoreichen Aktion eine reale Person steht, inklusive Prüfungen, Review-Warteschlangen und Audit-Trail.'}
  ],
  es: [
    {name:'glucosehack.com',category:'Salud & bienestar',desc:'Un nombre memorable para hábitos conscientes de la glucosa y conocimiento metabólico.',uses:'Educación sobre glucosa · Experimentos con comidas · Seguimiento de hábitos · Bienestar metabólico',concept:'Una plataforma de consumo que organiza lecturas de glucosa, comidas, actividad y notas en experimentos y tendencias comprensibles, sin sustituir el consejo médico.'},
    {name:'instantpaylayer.com',category:'Infraestructura de pagos',desc:'Un nombre de infraestructura sólido para orquestar pagos instantáneos.',uses:'Pagos instantáneos · Orquestación API · Enrutamiento · Flujos de liquidación',concept:'Una capa API que conecta aplicaciones con múltiples redes de pago instantáneo y normaliza solicitudes, enrutamiento, estados y controles operativos.'},
    {name:'kychuman.com',category:'Identidad & confianza',desc:'Un nombre directo para la verificación humana en flujos KYC.',uses:'Verificación humana · Revisión KYC · Controles de identidad · Cumplimiento',concept:'Una capa de verificación de identidad que ayuda a confirmar que una persona real está detrás de un alta o una acción de alto riesgo, combinando controles, colas de revisión y trazabilidad.'}
  ]
};

const featuredDomainNames = new Set(['glucosehack.com', 'instantpaylayer.com', 'kychuman.com']);
const afternicListings = {
  'agentsecurity.help': 'https://www.afternic.com/domain/agentsecurity.help',
  'arabicvoiceagent.com': 'https://www.afternic.com/domain/arabicvoiceagent.com',
  'arabicvoice.xyz': 'https://www.afternic.com/domain/arabicvoice.xyz',
  'citationreadiness.com': 'https://www.afternic.com/domain/citationreadiness.com',
  'deepfakes.help': 'https://www.afternic.com/domain/deepfakes.help',
  'promptinjection.help': 'https://www.afternic.com/domain/promptinjection.help',
  'responsibleagents.org': 'https://www.afternic.com/domain/responsibleagents.org',
  'voicefraud.help': 'https://www.afternic.com/domain/voicefraud.help'
};
function afternicUrl(domainName) {
  return afternicListings[domainName.toLowerCase()] || `https://www.afternic.com/search?q=${encodeURIComponent(domainName)}`;
}
function domainOfferUrl(domainName) {
  return `/contact/?domain=${encodeURIComponent(domainName)}`;
}
function addFeaturedBadge(card, domainName) {
  card.querySelectorAll('.selection-badge, .badge-featured').forEach(node => node.remove());
  card.dataset.featured = featuredDomainNames.has(domainName.toLowerCase()) ? 'true' : 'false';
  if (!featuredDomainNames.has(domainName.toLowerCase())) return;
  const category = card.querySelector('.domain-cat');
  if (!category) return;
  const badge = document.createElement('span');
  badge.className = 'badge-featured';
  badge.textContent = 'Featured';
  category.after(badge);
}
function normalizeActionSet(container, domainName) {
  if (!container || !domainName) return;
  let offer = [...container.querySelectorAll('a')].find(a => a.href.includes('/contact/?domain='));
  if (!offer) {
    offer = document.createElement('a');
    offer.href = domainOfferUrl(domainName);
    offer.textContent = lang === 'en' ? 'Make an offer' : (ui.offer || 'Make an offer');
    container.appendChild(offer);
  }
  offer.classList.add('btn', 'btn-outline');
  offer.classList.remove('primary', 'btn-primary', 'marketplace');

  let marketplace = [...container.querySelectorAll('a')].find(a => a.href.includes('afternic.com'));
  if (!marketplace) {
    marketplace = document.createElement('a');
    container.insertBefore(marketplace, offer);
  }
  marketplace.href = afternicUrl(domainName);
  marketplace.target = '_blank';
  marketplace.rel = 'noopener noreferrer';
  marketplace.textContent = 'View on Afternic';
  marketplace.classList.add('btn', 'btn-primary');
  marketplace.classList.remove('primary', 'btn-outline', 'marketplace');
  if (marketplace !== container.firstElementChild) container.insertBefore(marketplace, container.firstElementChild);
}

if (grid) {
  (newDomains[lang] || newDomains.en).forEach(d => {
    if (grid.querySelector(`[data-domain="${d.name}"]`)) return;
    const card = document.createElement('article');
    card.className = 'domain';
    card.dataset.category = d.category;
    card.dataset.sector = d.category;
    card.dataset.featured = 'true';
    card.dataset.domain = d.name;
    card.innerHTML = `<div class="domain-cat">${d.category}</div><span class="badge-featured">Featured</span><h3 class="domain-name">${d.name}</h3><p class="domain-desc">${d.desc}</p><div class="card-usecase"><strong>${ui.use_cases || 'Use cases'}</strong><p>${d.uses}</p></div><details class="card-concept"><summary>${ui.concept || 'What you could build'}</summary><p>${d.concept}</p></details><div class="domain-actions"><div class="detail-actions"><a class="btn btn-primary" href="${afternicUrl(d.name)}" target="_blank" rel="noopener noreferrer">View on Afternic</a><a class="btn btn-outline" href="${domainOfferUrl(d.name)}">${lang === 'en' ? 'Make an offer' : (ui.offer || 'Make an offer')}</a></div></div>`;
    grid.appendChild(card);
  });

  const cards = [...grid.querySelectorAll('.domain[data-category]')];
  cards.forEach(card => {
    const name = (card.dataset.domain || card.querySelector('.domain-name')?.textContent || '').trim().toLowerCase();
    card.dataset.domain = name;
    card.dataset.sector = card.dataset.category || card.dataset.sector || '';
    addFeaturedBadge(card, name);
    normalizeActionSet(card.querySelector('.domain-actions .detail-actions'), name);
    const detail = card.querySelector('.domain-actions > .text-link, .domain-actions > a:not(.btn)');
    if (detail) detail.classList.add('btn-link');
  });

  const total = cards.length;
  const badge = document.querySelector('.portfolio-badge');
  if (badge) badge.textContent = badge.textContent.replace(/^\d+/, String(total));
  const count = document.getElementById('resultCount');
  if (count) count.textContent = total + ' ' + (ui.shown || 'domains shown');
}

if (grid && filters) {
  const cards = [...grid.querySelectorAll('.domain[data-sector]')];
  const sectors = [...new Set(cards.map(card => card.dataset.sector).filter(Boolean))];
  filters.replaceChildren();
  const groups = [{key:'all', label:ui.all || 'All'}, ...sectors.map(sector => ({key:sector, label:sector}))];
  groups.forEach((group, i) => {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'filter' + (i === 0 ? ' active' : '');
    button.textContent = group.label;
    button.dataset.sectorFilter = group.key;
    button.setAttribute('aria-pressed', String(i === 0));
    button.addEventListener('click', () => {
      filters.querySelectorAll('button').forEach(node => {
        const active = node === button;
        node.classList.toggle('active', active);
        node.setAttribute('aria-pressed', String(active));
      });
      cards.forEach(card => { card.hidden = !(group.key === 'all' || card.dataset.sector === group.key); });
      const shown = cards.filter(card => !card.hidden).length;
      document.getElementById('resultCount').textContent = shown + ' ' + (ui.shown || 'domains shown');
    });
    filters.append(button);
  });
  filters.hidden = false;
}

// Keep the studio numbering but make it visually premium without changing its content structure.
document.querySelectorAll('#studio .index').forEach(index => index.classList.add('studio-index'));

// Standardize domain-page acquisition CTAs and add lightweight Product structured data.
const domainDisplay = document.querySelector('.domain-display');
if (domainDisplay) {
  const domainName = domainDisplay.textContent.trim().toLowerCase();
  const primaryActions = [
    document.querySelector('.domain-page-copy .detail-actions'),
    document.querySelector('.domain-closing .detail-actions'),
    document.querySelector('.mobile-acquire .detail-actions')
  ].filter(Boolean);
  primaryActions.forEach(actions => normalizeActionSet(actions, domainName));

  const category = document.querySelector('.domain-kicker-row .kicker')?.textContent.trim() || 'Premium';
  const pageDescription = document.querySelector('.domain-page-desc')?.textContent.trim() || `${domainName} is available for acquisition through MzunguWay.`;
  document.title = `${domainName} – ${category} Domain for Sale | MzunguWay`;
  const metaDescription = document.querySelector('meta[name="description"]');
  if (metaDescription) metaDescription.content = pageDescription.slice(0, 154);

  if (!document.querySelector('script[data-mw-product-schema]')) {
    const canonical = document.querySelector('link[rel="canonical"]')?.href || location.href;
    const productSchema = document.createElement('script');
    productSchema.type = 'application/ld+json';
    productSchema.dataset.mwProductSchema = 'true';
    productSchema.textContent = JSON.stringify({
      '@context': 'https://schema.org',
      '@type': 'Product',
      name: domainName,
      description: pageDescription.slice(0, 154),
      url: canonical,
      brand: {'@type': 'Brand', name: 'MzunguWay'},
      offers: {
        '@type': 'Offer',
        url: afternicUrl(domainName),
        availability: 'https://schema.org/InStock',
        itemCondition: 'https://schema.org/NewCondition'
      }
    });
    document.head.appendChild(productSchema);
  }
}

// Preserve intrinsic image dimensions where known and lazy-load only non-critical images.
document.querySelectorAll('img').forEach(img => {
  if (img.getAttribute('src')?.includes('/assets/mzunguway-original.jpg')) {
    if (!img.hasAttribute('width')) img.setAttribute('width', '1448');
    if (!img.hasAttribute('height')) img.setAttribute('height', '1086');
  }
  const critical = img.closest('.site-header, .hero, .domain-page-hero');
  if (!critical && !img.hasAttribute('loading')) img.loading = 'lazy';
  if (!img.hasAttribute('decoding')) img.decoding = 'async';
});

// Carry a draft's selected domain when switching languages; never carry personal data.
const selected = new URLSearchParams(location.search).get('domain');
if (selected) document.querySelectorAll('.language-switch a').forEach(a=>{const url=new URL(a.href);url.searchParams.set('domain',selected.slice(0,250));a.href=url.href;});
const form=document.getElementById('enquiryForm');
if(form) {
  form.hidden=false;
  if(selected) document.getElementById('enquiryDomain').value=selected.slice(0,250);
  form.addEventListener('submit',e=>{
    e.preventDefault(); if(!form.reportValidity())return;
    const data=new FormData(form);
    const fields=['domain','email','budget','message'];
    const labels={domain:ui.domain_label,email:ui.email,budget:ui.budget,message:ui.message};
    const message=fields.map(k=>labels[k]+': '+String(data.get(k)||'').trim()).join('\n\n');
    const subject=String(data.get('domain')).replace(/[\r\n]/g,' ').slice(0,250)+' — MzunguWay';
    document.getElementById('preparedMessage').value=message;
    document.getElementById('sendEnquiry').href='mailto:hello@mzunguway.com?subject='+encodeURIComponent(subject)+'&body='+encodeURIComponent(message);
    document.getElementById('enquiryResult').hidden=false;
    document.getElementById('enquiryStatus').textContent=ui.ready;
    document.getElementById('enquiryResult').scrollIntoView({behavior:'smooth',block:'nearest'});
  });
  document.getElementById('copyEnquiry').addEventListener('click',async()=>{
    const text=document.getElementById('preparedMessage');
    try {await navigator.clipboard.writeText(text.value);document.getElementById('enquiryStatus').textContent=ui.copied;}
    catch {text.focus();text.select();document.getElementById('enquiryStatus').textContent=ui.copy_fail;}
  });
}
