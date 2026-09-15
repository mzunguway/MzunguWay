"""Build static locales and simplify the portfolio without changing its inventory."""
from pathlib import Path
from html import escape as e
from urllib.parse import quote
from datetime import date
import json, re, xml.etree.ElementTree as ET
import generate_domain_pages as base
from locales import LANGUAGES, UI, COPY, CATEGORIES
ROOT=base.ROOT
ORIGIN='https://mzunguway.com'
FEATURED=('arabicvoiceagent.com','agentpaymentrisk.com','citationreadiness.com')
ORDER=sorted(base.DOMAINS,key=lambda d:(d['name'] not in FEATURED,FEATURED.index(d['name']) if d['name'] in FEATURED else base.DOMAINS.index(d)))
BUNDLE_KEYS=[('pair_pay','pay_desc'),('pair_security','security_desc'),('pair_voice','voice_desc'),('pair_trust','trust_desc')]
COLLECTIONS={'agent-payment-domains':('pair_pay', ['agentpaymentid.com','agentpaymentrisk.com']), 'ai-security-domains':('pair_security',['agentsecurity.help','promptinjection.help']), 'arabic-ai-domains':('pair_voice',['arabicvoiceagent.com','arabicvoice.xyz']), 'digital-trust-domains':('pair_trust',['deepfakes.help','voicefraud.help','responsibleagents.org'])}
def path(lang,route=''):
    return ('/' if lang=='en' else '/'+lang+'/')+route

def cat(d,l):
    if l=='en': return d['category']
    fallback={'AI Governance':['Gouvernance IA','KI-Governance','Gobernanza de IA'], 'Fragrance & Lifestyle':['Parfumerie','Parfümerie','Perfumería'], 'Fintech & Payments':['Fintech et paiements','Fintech und Zahlungen','Fintech y pagos']}
    if d['category'] in CATEGORIES: return CATEGORIES[d['category']][list(LANGUAGES).index(l)]
    if d['category'] in fallback: return fallback[d['category']][['fr','de','es'].index(l)]
    raise ValueError('Missing category '+d['category'])

def copy(d,l):
    if l!='en': return COPY[l][d['name']]
    return dict(tagline=d['tagline'],concept=d['product'],why=' '.join(base.EDITORIAL[d['name']]['advantages']),tradeoff=base.EDITORIAL[d['name']]['tradeoff'],buyers=' · '.join(d['fits']))

def contact_url(l,name): return path(l,'contact/')+'?domain='+quote(name,safe='')

def actions(d,l):
    u=UI[l]; offer=f'<a class="btn {"" if d["afternic"] else "primary"}" href="{e(contact_url(l,d["name"]))}">{u["offer"]}</a>'
    market=f'<a class="btn primary" href="{e(d["afternic"])}" target="_blank" rel="noopener noreferrer">{u["market"]}</a>' if d['afternic'] else ''
    return '<div class="detail-actions">'+market+offer+'</div>'

def header(l,route):
    u=UI[l]
    links=''.join(f'<a href="{path(l)}#{key}">{u[key]}</a>' for key in ['domains','bundles','process'])+f'<a href="{path(l,"contact/")}">{u["contact"]}</a>'
    langs=''.join(f'<a href="{path(code,route)}" lang="{code}" hreflang="{code}" {"aria-current=page" if code==l else ""}>{label}</a>' for code,label in LANGUAGES.items())
    return f'''<header class="site-header"><div class="wrap"><nav class="navbar" aria-label="{u['menu']}"><a class="brand" href="{path(l)}" aria-label="MzunguWay"><span class="brand-window"><img src="/assets/mzunguway-original.jpg" alt="MzunguWay" width="1448" height="1086"></span></a><button class="menu-toggle" id="menuToggle" type="button" aria-expanded="false" aria-controls="mainNav" aria-label="{u['menu']}"><span></span><span></span><span></span></button><div class="navlinks" id="mainNav">{links}</div></nav><nav class="language-switch" aria-label="{u['language']}">{langs}</nav></div></header>'''

def alternates(route):
    return ''.join(f'<link rel="alternate" hreflang="{l}" href="{ORIGIN}{path(l,route)}">' for l in LANGUAGES)+f'<link rel="alternate" hreflang="x-default" href="{ORIGIN}/{route}">'

def shell(l,route,title,desc,body):
    u=UI[l]; url=ORIGIN+path(l,route)
    schema=json.dumps({'@context':'https://schema.org','@type':'WebPage','name':title,'description':desc,'url':url,'inLanguage':l},ensure_ascii=False).replace('</','<\\/')
    return f'''<!doctype html><html lang="{l}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)} — MzunguWay</title><meta name="description" content="{e(desc)}"><meta name="robots" content="index,follow"><link rel="canonical" href="{url}">{alternates(route)}<meta property="og:title" content="{e(title)} — MzunguWay"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}"><meta property="og:type" content="website"><meta property="og:image" content="{ORIGIN}/og-card.png"><meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#F5F2EA"><link rel="icon" href="/brand-symbol.svg"><link rel="stylesheet" href="/styles.css?v=13"><link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&amp;family=Sora:wght@500;600;700&amp;display=swap" rel="stylesheet"><script type="application/ld+json">{schema}</script></head><body><a class="skip-link" href="#main">{u['skip']}</a>{header(l,route)}<main id="main">{body}</main><footer><div class="wrap foot"><span>© {date.today().year} MzunguWay. {u['rights']}</span><a href="mailto:hello@mzunguway.com">hello@mzunguway.com</a></div></footer><script src="/assets/ui.js?v=13" defer></script><script src="/app.js?v=13" defer></script></body></html>'''

def card(d,l):
    u=UI[l]; c=copy(d,l); badge=f'<span class="selection-badge">{u["featured"]}</span>' if d['name'] in FEATURED else ''
    return f'''<article class="domain" data-category="{e(cat(d,l))}" data-featured="{str(d['name'] in FEATURED).lower()}"><div class="domain-cat">{e(cat(d,l))} {badge}</div><h3 class="domain-name"><a href="{path(l,'domains/'+d['slug']+'/')}">{d['name']}</a></h3><p class="domain-desc">{e(c['tagline'])}</p><div class="domain-actions">{actions(d,l)}<a class="text-link" href="{path(l,'domains/'+d['slug']+'/')}">{u['view']} →</a></div></article>'''

def bundles(l):
    u=UI[l]; cards=[]
    for b,(key,desc) in zip(base.BUNDLES,BUNDLE_KEYS):
        names=[x[0] for x in b['members']]
        links=''.join(f'<li><a href="{path(l,"domains/"+next(d["slug"] for d in base.DOMAINS if d["name"]==n)+"/")}">{n}</a></li>' for n in names)
        cards.append(f'<article class="card bundle-card" id="bundle-{b["slug"]}"><h3>{u[key]}</h3><ul class="bundle-members">{links}</ul><p>{u[desc]}</p><a class="btn primary" href="{e(contact_url(l," + ".join(names)))}">{u["bundle_offer"]}</a></article>')
    return f'<section id="bundles"><div class="wrap"><div class="section-head"><h2>{u["bundle_title"]}</h2></div><div class="bundle-grid">{"".join(cards)}</div><p class="bundle-terms">{u["bundle_note"]}</p></div></section>'

def home(l):
    u=UI[l]
    body=f'''<section class="hero" id="top"><div class="wrap hero-grid"><div class="surface hero-copy"><div class="eyebrow">MzunguWay</div><h1>{u['hero']}</h1><p class="lead">{u['intro']}</p><a class="btn primary" href="#domains">{u['explore']}</a></div><div class="surface identity"><img class="identity-lockup original-lockup" src="/assets/mzunguway-original.jpg" alt="MzunguWay" width="1448" height="1086" fetchpriority="high"></div></div></section>
<section id="domains"><div class="wrap"><div class="section-head"><div><div class="kicker">{u['catalog']}</div><h2>{u['catalog_title']}</h2></div><p>{u['catalog_intro']}</p></div><div id="filters" class="filters" role="group" aria-label="{u['domains']}" hidden></div><p id="resultCount" class="result-count" aria-live="polite">11 {u['shown']}</p><div id="domainGrid" class="domain-grid">{''.join(card(d,l) for d in ORDER)}</div></div></section>'''
    body+=bundles(l)
    body+=f'<section id="process"><div class="wrap"><div class="section-head"><h2>{u["process_title"]}</h2></div><ol class="workflow-list">'+''.join(f'<li>{u["step"+str(i)]}</li>' for i in range(1,5))+'</ol></div></section>'
    body+=f'<section id="faq"><div class="wrap"><h2>{u["faq"]}</h2><div class="faq-list">'+''.join(f'<details><summary>{u[q]}</summary><p>{u[a]}</p></details>' for q,a in [('qprice','aprice'),('qinclude','boundary'),('qtime','atime'),('qbundle','bundle_note')])+'</div></div></section>'
    body+=f'<section id="studio"><div class="wrap"><h2>{u["studio"]}</h2><p class="lead">{u["studio_text"]}</p></div></section><section id="spirit"><div class="wrap"><div class="kicker">{u["spirit"]}</div><h2>{u["spirit_title"]}</h2><p class="lead">{u["spirit_text"]}</p></div></section><section id="contact" class="contact-section"><div class="wrap"><h2>{u["form_title"]}</h2><a class="btn primary" href="{path(l,"contact/")}">{u["offer"]}</a></div></section>'
    return shell(l,'',u['hero'],u['intro'],body)

def detail(d,l):
    u=UI[l]; c=copy(d,l); route='domains/'+d['slug']+'/'
    body=f'''<section class="domain-page-hero"><div class="wrap"><a class="text-link" href="{path(l)}#domains">← {u['back']}</a><div class="kicker">{e(cat(d,l))}</div><h1 class="domain-display">{d['name']}</h1><p class="lead">{e(c['tagline'])}</p>{actions(d,l)}<p class="market-note">{u['market_note'] if d['afternic'] else u['private_note']}</p></div></section><section class="detail-body"><div class="wrap"><div class="detail-content-grid"><div class="detail-stack"><article class="detail-section"><h2>{u['why']}</h2><p>{e(c['why'])}</p><h3>{u['tradeoff']}</h3><p>{e(c['tradeoff'])}</p></article><article class="detail-section"><h2>{u['buyers']}</h2><p>{e(c['buyers'])}</p></article></div><div class="detail-stack"><article class="detail-section"><h2>{u['concept']}</h2><p>{e(c['concept'])}</p><h3>{u['only']}</h3><p>{u['boundary']}</p></article></div></div><div class="domain-closing"><h2>{u['form_title']}</h2>{actions(d,l)}</div></div></section>'''
    relevant=[(b,k) for b,k in zip(base.BUNDLES,BUNDLE_KEYS) if d['name'] in dict(b['members'])]
    if relevant: body+=f'<div class="wrap"><a class="text-link" href="{path(l)}#bundle-{relevant[0][0]["slug"]}">{u["bundles"]} →</a></div>'
    return shell(l,route,d['name']+' | '+u['only'],c['tagline'],body)

def contact(l):
    u=UI[l]; opts=''.join(f'<option value="{e(d["name"])}"></option>' for d in base.DOMAINS)
    body=f'''<section class="contact-page"><div class="wrap contact-wrap"><h1>{u['form_title']}</h1><p class="lead">{u['form_intro']}</p><form id="enquiryForm" hidden><label for="enquiryDomain">{u['domain_label']}</label><input id="enquiryDomain" name="domain" list="domainOptions" required maxlength="250" autocomplete="off"><datalist id="domainOptions">{opts}</datalist><label for="enquiryEmail">{u['email']}</label><input id="enquiryEmail" type="email" name="email" required maxlength="254" autocomplete="email"><label for="enquiryBudget">{u['budget']}</label><input id="enquiryBudget" name="budget" maxlength="100"><label for="enquiryMessage">{u['message']}</label><textarea id="enquiryMessage" name="message" rows="5" maxlength="4000" required></textarea><button class="btn primary" type="submit">{u['prepare']}</button><p class="market-note">{u['privacy']}</p></form><div id="enquiryResult" hidden><p id="enquiryStatus" role="status"></p><textarea id="preparedMessage" rows="10" readonly aria-label="{u['message']}"></textarea><div class="detail-actions"><a id="sendEnquiry" class="btn primary">{u['send']}</a><button class="btn" id="copyEnquiry" type="button">{u['copy']}</button></div></div><noscript><p>{u['nojs']}</p></noscript><p><a href="mailto:hello@mzunguway.com">hello@mzunguway.com</a></p></div></section>'''
    return shell(l,'contact/',u['form_title'],u['form_intro'],body)

def collection(l,slug=None):
    u=UI[l]; title=u['collections'] if slug is None else u[COLLECTIONS[slug][0]]
    selected=ORDER if slug is None else [d for d in ORDER if d['name'] in COLLECTIONS[slug][1]]
    body=f'<section><div class="wrap"><h1>{title}</h1><p class="lead">{u["catalog_intro"]}</p><div class="domain-grid">'+''.join(card(d,l) for d in selected)+'</div></div></section>'
    return shell(l,'collections/'+(slug+'/' if slug else ''),title,u['catalog_intro'],body)

def write(route,source):
    dest=ROOT/route/'index.html';dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(source,encoding='utf8')

def patch_en(source,route):
    source=re.sub(r'<header\b.*?</header>',lambda m:header('en',route),source,flags=re.S)
    source=re.sub(r'<link rel="alternate"[^>]*>','',source)
    source=source.replace('</head>',alternates(route)+'</head>')
    source=re.sub(r'<script src="/assets/ui.js[^"]*" defer></script>', '', source)
    if '/app.js' not in source: source=source.replace('</body>', '<script src="/app.js?v=13" defer></script></body>')
    source=source.replace('<script src="/app.js', '<script src="/assets/ui.js?v=13" defer></script><script src="/app.js')
    source=re.sub(r'(/(?:styles.css|app.js))\?v=\d+',r'\1?v=13',source)
    return source

def main():
    # English long-form pages remain generated by the existing editorial source.
    base.main()
    source=(ROOT/'index.html').read_text()
    source=re.sub(r'\s*<section id="featured">.*?</section>','',source,flags=re.S)
    catalog=re.search(r'<section id="domains">.*?</section>',source,re.S).group()
    catalog=re.sub(r'(<div id="domainGrid" class="domain-grid">).*?(</div>\s*</div>\s*</section>)',lambda m:m[1]+''.join(card(d,'en') for d in ORDER)+m[2],catalog,flags=re.S)
    source=re.sub(r'<section id="domains">.*?</section>','',source,flags=re.S)
    hero_end=source.index('</section>',source.index('<section class="hero"'))+len('</section>')
    source=source[:hero_end]+catalog+source[hero_end:]
    # Keep the studio and full brand story after the buying journey.
    story=[]
    for sec in ['studio','spirit']:
        m=re.search(r'<section id="'+sec+r'".*?</section>',source,re.S);story.append(m[0]);source=source.replace(m[0],'')
    source=source.replace('<section id="contact"',''.join(story)+'<section id="contact"')
    source=re.sub(r'href="mailto:hello@mzunguway.com\?subject=Domain%20enquiry[^\"]*"','href="/contact/"',source)
    source=source.replace('Start a private enquiry','Make an offer')
    (ROOT/'index.html').write_text(source,encoding='utf8')
    english=[ROOT/'index.html',*ROOT.glob('domains/*/index.html'),*ROOT.glob('collections/**/index.html')]
    for file in english:
        route=str(file.parent.relative_to(ROOT)).replace('.','')
        if route: route+='/'
        file.write_text(patch_en(file.read_text(),route),encoding='utf8')
    write('contact',contact('en'))
    for l in ['fr','de','es']:
        write(l,home(l));write(l+'/contact',contact(l));write(l+'/collections',collection(l))
        for slug in COLLECTIONS: write(l+'/collections/'+slug,collection(l,slug))
        for d in base.DOMAINS: write(l+'/domains/'+d['slug'],detail(d,l))
    # UI strings are local, versioned assets; no tracking or translation API.
    (ROOT/'assets/ui.js').write_text('window.MW_UI = '+json.dumps(UI,ensure_ascii=False)+';',encoding='utf8')
    routes=['','contact/','collections/',*('collections/'+s+'/' for s in COLLECTIONS),*('domains/'+d['slug']+'/' for d in base.DOMAINS)]
    urls=[ORIGIN+path(l,r) for l in LANGUAGES for r in routes]
    ns='http://www.sitemaps.org/schemas/sitemap/0.9'; ET.register_namespace('',ns)
    root=ET.Element('{'+ns+'}urlset')
    for url in urls:
        item=ET.SubElement(root,'{'+ns+'}url');ET.SubElement(item,'{'+ns+'}loc').text=url;ET.SubElement(item,'{'+ns+'}lastmod').text=date.today().isoformat()
    ET.ElementTree(root).write(ROOT/'sitemap.xml',encoding='utf-8',xml_declaration=True)
    print(f'Built {len(urls)} pages in four languages; 11 domains unchanged.')
if __name__=='__main__': main()
