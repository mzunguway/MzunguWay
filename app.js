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

if (grid) {
  (newDomains[lang] || newDomains.en).forEach(d => {
    if (grid.querySelector(`[data-domain="${d.name}"]`)) return;
    const card = document.createElement('article');
    card.className = 'domain';
    card.dataset.category = d.category;
    card.dataset.featured = 'false';
    card.dataset.domain = d.name;
    card.innerHTML = `<div class="domain-cat">${d.category}</div><h3 class="domain-name">${d.name}</h3><p class="domain-desc">${d.desc}</p><div class="card-usecase"><strong>${ui.use_cases || 'Use cases'}</strong><p>${d.uses}</p></div><details class="card-concept"><summary>${ui.concept || 'What you could build'}</summary><p>${d.concept}</p></details><div class="domain-actions"><div class="detail-actions"><a class="btn primary" href="/contact/?domain=${encodeURIComponent(d.name)}">${ui.offer || 'Make an offer'}</a></div></div>`;
    grid.appendChild(card);
  });
  const total = grid.querySelectorAll('[data-category]').length;
  const badge = document.querySelector('.portfolio-badge');
  if (badge) badge.textContent = badge.textContent.replace(/^\d+/, String(total));
  const count = document.getElementById('resultCount');
  if (count) count.textContent = total + ' ' + (ui.shown || 'domains shown');
}

if (grid && filters) {
  const cards = [...grid.querySelectorAll('[data-category]')];
  const groups = [{key:'all',label:ui.all},{key:'featured',label:ui.featured}, ...[...new Set(cards.map(c=>c.dataset.category))].map(label=>({key:label,label}))];
  groups.forEach((group,i) => {
    const b=document.createElement('button'); b.type='button'; b.className='filter'+(i===0?' active':''); b.textContent=group.label; b.setAttribute('aria-pressed',String(i===0));
    b.addEventListener('click',()=>{
      filters.querySelectorAll('button').forEach(n=>{n.classList.toggle('active',n===b);n.setAttribute('aria-pressed',String(n===b));});
      cards.forEach(c=>{c.hidden=!(group.key==='all'||(group.key==='featured'?c.dataset.featured==='true':c.dataset.category===group.key));});
      document.getElementById('resultCount').textContent=cards.filter(c=>!c.hidden).length+' '+ui.shown;
    }); filters.append(b);
  }); filters.hidden=false;
}
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
