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
