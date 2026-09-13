from __future__ import annotations

import html
import json
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]

DOMAINS = [
    {
        "name": "agentsecurity.help",
        "slug": "agentsecurity-help",
        "category": "AI Security",
        "description": "A direct, high-intent name for agentic AI security, secure deployment, governance, monitoring and incident support.",
        "concept": "Agent Security Operations & Support Hub",
        "opportunity": "Agentic AI is creating a new security surface: tools, permissions, identities, connectors and autonomous actions all need operational controls. This name immediately communicates a place to find practical help.",
        "problem": "Companies deploying autonomous AI agents need a clear way to assess permissions, control tool access, review risky integrations, document incidents and guide internal teams when an agent behaves unexpectedly.",
        "product": "A customer-facing security portal for an AI-security vendor or agent platform. It could centralize deployment checklists, connector-risk reviews, identity and authorization guidance, incident intake, policy templates and remediation playbooks.",
        "workflow": [
            "Select the agent, model, tools and connected systems.",
            "Run a permissions and integration risk review.",
            "Generate deployment controls and governance actions.",
            "Report suspicious agent behaviour or a security incident.",
            "Receive containment, remediation and audit guidance.",
        ],
        "fits": ["AI-security vendors", "Agent platforms", "Enterprise security teams", "MSSPs"],
        "afternic": "https://www.afternic.com/domain/agentsecurity.help",
    },
    {
        "name": "arabicvoiceagent.com",
        "slug": "arabicvoiceagent-com",
        "category": "Voice & AI",
        "description": "A clear .com for Arabic voice agents, conversational AI, call automation, customer service and regional voice products.",
        "concept": "Arabic Voice Agent Platform for Customer Operations",
        "opportunity": "The name combines a language, an interface and an explicit product category. Its .com ending gives a commercial platform a familiar address, and the words explain the focus before a visitor sees the product.",
        "problem": "Businesses across Arabic-speaking markets need voice automation that can handle real customer conversations, local language variants, business terminology and workflows such as booking, support, collections and lead qualification.",
        "product": "A SaaS platform where a company creates an Arabic-speaking voice agent, chooses the target locale and voice, connects telephony and CRM systems, defines business rules and deploys the agent to handle inbound or outbound calls.",
        "workflow": [
            "Choose the target market, Arabic locale and voice persona.",
            "Connect a phone number, CRM, calendar or booking system.",
            "Configure support, reservation, qualification or reminder intents.",
            "Test conversations and escalation rules with human handoff.",
            "Launch and monitor outcomes, containment and customer satisfaction.",
        ],
        "fits": ["Contact-center platforms", "Banks", "Airlines", "Clinics", "Hospitality groups", "MENA SaaS"],
        "afternic": "https://www.afternic.com/domain/arabicvoiceagent.com",
    },
    {
        "name": "arabicvoice.xyz",
        "slug": "arabicvoice-xyz",
        "category": "Voice & AI",
        "description": "A flexible, developer-friendly name for Arabic speech technology, voice models, APIs, creator tools or experimental products.",
        "concept": "Arabic Voice Model Playground & API Marketplace",
        "opportunity": "A short, category-level phrase gives this domain room to become a lab, API, model hub, creator tool or voice marketplace. The .xyz extension fits experimental and developer-led products.",
        "problem": "Developers and product teams often need to compare Arabic speech recognition, synthesis, accents, latency and voice quality before choosing a provider or building a production voice experience.",
        "product": "A developer playground and marketplace where users can test Arabic speech-to-text and text-to-speech engines, compare regional voices, benchmark output, generate sample audio and connect to APIs from one interface.",
        "workflow": [
            "Upload or record an Arabic speech sample.",
            "Choose the locale, accent and speech task.",
            "Compare transcription or synthesized outputs side by side.",
            "Review latency, quality and integration notes.",
            "Export the result or connect the selected API to a product.",
        ],
        "fits": ["Speech-tech labs", "Developers", "Voice marketplaces", "Creator platforms", "AI startups"],
        "afternic": "https://www.afternic.com/domain/arabicvoice.xyz",
    },
    {
        "name": "citationreadiness.com",
        "slug": "citationreadiness-com",
        "category": "AI Visibility",
        "description": "A strong .com for AI-search readiness, structured authority, answer-engine visibility and content optimization.",
        "concept": "Citation Readiness Audit for AI Search & Answer Engines",
        "opportunity": "As discovery shifts toward answer engines, brands need a useful way to assess whether their content is clear, structured, attributable and easy for machines to understand. The name can define that measurable category.",
        "problem": "Marketing teams can publish excellent content that is still difficult for search and answer systems to interpret because facts are buried, entities are unclear, sources are weak or page structure is inconsistent.",
        "product": "A B2B audit platform that scans a site and scores factual clarity, sources, entities, authorship, freshness, structured data and machine-readable information. It would identify what makes content easier to understand and reference without promising citations.",
        "workflow": [
            "Crawl the selected website or content library.",
            "Score factual clarity, sourcing, structure, entities and freshness.",
            "Detect missing or weak structured-data and authority signals.",
            "Generate a prioritized Citation Readiness action plan.",
            "Re-scan and track readiness improvements over time.",
        ],
        "fits": ["AEO/GEO platforms", "SEO agencies", "Publishers", "SaaS marketing teams", "Brand intelligence tools"],
        "afternic": "https://www.afternic.com/domain/citationreadiness.com",
    },
    {
        "name": "deepfakes.help",
        "slug": "deepfakes-help",
        "category": "Trust & Safety",
        "description": "A memorable help-oriented domain for deepfake incident response, victim support, verification, education and takedown guidance.",
        "concept": "Deepfake Incident Response & Victim Assistance Portal",
        "opportunity": "The .help extension turns a complex threat into a direct promise of assistance. The name suits a high-trust destination for people and organizations facing synthetic-media abuse.",
        "problem": "When a person or company discovers suspected synthetic audio, video or imagery, the first challenge is knowing what to preserve, how to verify it, where to report it and who can help before evidence disappears or harm spreads.",
        "product": "A trusted first-response portal that guides evidence preservation, accepts suspicious media for authenticity triage, generates reporting checklists, routes users toward platform takedown procedures and connects serious cases to cybersecurity or legal specialists.",
        "workflow": [
            "Choose the incident type: video, image, audio or impersonation.",
            "Preserve URLs, files, timestamps, screenshots and context.",
            "Submit material for technical triage or expert review.",
            "Receive platform-specific reporting and takedown guidance.",
            "Escalate high-risk cases to legal, fraud or cybersecurity support.",
        ],
        "fits": ["Cybersecurity vendors", "Trust & safety firms", "Insurers", "Media organizations", "Public-interest services"],
        "afternic": "https://www.afternic.com/domain/deepfakes.help",
    },
    {
        "name": "promptinjection.help",
        "slug": "promptinjection-help",
        "category": "AI Security",
        "description": "A precise support domain for prompt-injection defense, secure LLM architecture, developer guidance and incident response.",
        "concept": "Prompt Injection Defense Center for LLM Teams",
        "opportunity": "Prompt injection is a named and persistent security problem. This exact-match domain can anchor a specialist resource, product-support center or demand-generation property around the issue.",
        "problem": "Teams shipping copilots, RAG systems and AI agents need practical defensive guidance when untrusted content can manipulate model behavior, trigger unsafe tool use or override intended instructions.",
        "product": "A defensive knowledge and response center for developers with architecture checklists, safe test cases, input and tool-boundary guidance, incident templates, model-behavior monitoring advice and mitigation playbooks.",
        "workflow": [
            "Describe the application and where untrusted content enters.",
            "Map model permissions, tools, retrieval sources and sensitive actions.",
            "Run safe defensive tests against injection scenarios.",
            "Receive prioritized mitigations and architecture recommendations.",
            "Use an incident playbook if manipulation reaches production.",
        ],
        "fits": ["AI-security companies", "LLM platforms", "Developer tools", "Security teams", "Training providers"],
        "afternic": "https://www.afternic.com/domain/promptinjection.help",
    },
    {
        "name": "responsibleagents.org",
        "slug": "responsibleagents-org",
        "category": "Responsible AI",
        "description": "A mission-led .org for responsible agentic AI, standards, governance, research, benchmarks and industry collaboration.",
        "concept": "Responsible AI Agents Standards & Governance Initiative",
        "opportunity": "The phrase is broad enough to convene an ecosystem yet precise enough to own a clear mission. The .org extension supports a standards initiative, nonprofit, research coalition or industry consortium.",
        "problem": "Organizations adopting autonomous agents need shared language and practical governance around identity, authorization, human oversight, accountability, testing, transparency and safe deployment.",
        "product": "An independent initiative that publishes agent-governance principles, templates, evaluation criteria, research, case studies and a public registry of organizations committing to responsible agent deployment.",
        "workflow": [
            "Publish a practical Responsible Agent Framework.",
            "Release templates for identity, authorization, oversight and auditability.",
            "Maintain open benchmarks and implementation case studies.",
            "Invite organizations to self-assess against published criteria.",
            "Convene researchers, regulators, developers and enterprises.",
        ],
        "fits": ["Research institutes", "Standards initiatives", "Nonprofits", "Universities", "Industry consortia"],
        "afternic": "https://www.afternic.com/domain/responsibleagents.org",
    },
    {
        "name": "voicefraud.help",
        "slug": "voicefraud-help",
        "category": "Voice & Fraud",
        "description": "A high-intent domain for voice-cloning fraud, vishing response, impersonation defense, verification and customer protection.",
        "concept": "Voice Fraud Response Center for Banks & Telecoms",
        "opportunity": "Voice cloning and vishing create a problem people describe in plain language. This name pairs that category with an immediate help signal, making it well suited to customer protection and incident response.",
        "problem": "Customers and employees receiving suspicious calls or voice notes need a trusted way to verify the request, preserve evidence, avoid acting under urgency and reach the correct fraud team quickly.",
        "product": "A bank-, telecom- or fraud-vendor-branded response portal where users report a suspicious voice interaction, follow independent verification steps, preserve evidence, receive scam-specific guidance and escalate the case.",
        "workflow": [
            "Select the interaction: call, voicemail, voice note or executive request.",
            "Follow independent identity-verification steps before acting.",
            "Preserve the number, recording, timestamps and payment instructions.",
            "Classify the likely fraud pattern and receive immediate guidance.",
            "Escalate the case to fraud operations, security or support.",
        ],
        "fits": ["Banks", "Telecom operators", "Fraud-prevention firms", "Identity vendors", "Insurers"],
        "afternic": "https://www.afternic.com/domain/voicefraud.help",
    },
]

DOMAINS.extend([
    dict(name="dataorig.in", slug="dataorig-in", category="Data & Provenance",
         description="A compact data-origin identity for dataset provenance, lineage and traceability.",
         concept="Data Provenance & Lineage Layer",
         opportunity="Read across the dot, dataorig.in suggests data origin. It gives provenance a compact identity, while the .in ending requires explaining the domain hack when spoken.",
         problem="Data teams need to understand where a dataset came from, what changed and which usage permissions are recorded.",
         product="A provenance workspace connecting source records, transformation histories and permission documentation before a dataset is used in analytics or AI.",
         workflow=["Register a dataset and its source.", "Document permissions and transformations.", "Trace lineage back to the source.", "Export an evidence record for review."],
         fits=["Data-governance vendors", "Lineage platforms", "AI-data startups", "Dataset marketplaces"], afternic=None),
    dict(name="choosethe.one", slug="choosethe-one", category="Brandable",
         description="A memorable call-to-action name for curated recommendations, matching and confident choices.",
         concept="Curated Recommendation & Matching Platform",
         opportunity="The words and extension form one complete invitation: choose the one. It is easy to remember and flexible enough for a focused recommendation brand.",
         problem="Buyers faced with too many similar options need a shortlist grounded in their own requirements.",
         product="A curated recommendation service that gathers a customer's priorities, explains a small set of matches and helps them choose a product or service.",
         workflow=["Define the customer's priorities.", "Create a relevant shortlist.", "Explain each match and its trade-offs.", "Help the customer choose."],
         fits=["Recommendation startups", "Recruitment platforms", "Curated commerce", "Matching services"],
         afternic="https://www.afternic.com/domain/choosethe.one"),
])

# Editorial positioning lives alongside the inventory: no runtime portfolio copy.
POSITIONING = {
 "agentsecurity.help": ("A clear home for safer AI agents.", ["Security knowledge base", "Permissions reviews", "Incident documentation", "Developer resources"], ["Tool access and permissions need understandable controls.", "A dedicated support destination can complement an existing security product."], ["Review permissions", "Map tool access", "Document incidents"]),
 "arabicvoiceagent.com": ("An explicit name for Arabic conversational AI.", ["Contact centers", "Banking", "Healthcare", "Hospitality", "Telecom"], ["Language and product category are clear in the name.", "Bookings and support provide concrete workflows to design around.", "Regional language testing and human handoff can become product differentiators."], ["Choose a locale", "Connect a workflow", "Plan human handoff"]),
 "arabicvoice.xyz": ("A place to explore the possibilities of Arabic speech.", ["Speech APIs", "Voice model demos", "Creator tools", "Developer benchmarks"], ["Speech recognition and synthesis share a coherent brand umbrella.", "A focused playground could help developers evaluate integration choices."], ["Speech to text", "Text to speech", "Compare outputs"]),
 "citationreadiness.com": ("Is your brand ready to be cited by AI?", ["Content audits", "Source reviews", "Structured-data checks", "Agency reporting"], ["Clear sourcing and structure give teams actionable audit criteria.", "Agencies could package readiness reviews as a repeatable service.", "Readiness does not guarantee indexing, ranking or AI citations."], ["Review sources", "Clarify entities", "Prioritize improvements"]),
 "deepfakes.help": ("Is this video real? Start with the right questions.", ["Evidence preservation", "Verification guidance", "Reporting resources", "Victim support"], ["People facing suspected synthetic media need a clear next step.", "Verification guidance and incident support can serve different audiences.", "Authenticity assessment must communicate uncertainty, not absolute detection claims."], ["Preserve", "Assess", "Learn", "Report"]),
 "promptinjection.help": ("Practical guidance at the boundary of trust.", ["Defense knowledge base", "Red-team resources", "Mitigation library", "Developer education"], ["The name matches a specific problem developers can recognize.", "Defensive examples and mitigation guidance can support a security platform."], ["Identify untrusted input", "Review boundaries", "Document mitigations"]),
 "responsibleagents.org": ("A shared home for responsible AI agents.", ["Governance research", "Policy templates", "Industry collaboration", "Nonprofit initiatives"], ["The .org ending suits an initiative with a public-interest mission.", "Governance templates and research can bring multiple disciplines together.", "The domain itself confers no standards authority or certification."], ["Principles", "Research", "Deployment guidance"]),
 "voicefraud.help": ("Think before you trust the voice.", ["Scam education", "Independent verification", "Fraud reporting", "Customer protection"], ["The name connects a recognizable risk with practical assistance.", "A bank or telecom could use it as a focused customer-education destination."], ["Pause", "Verify independently", "Preserve evidence", "Report"]),
 "dataorig.in": ("Every dataset has a story. Make its origin traceable.", ["Data lineage", "Provenance records", "Permission documentation", "Dataset reviews"], ["Source and transformation records support informed data-use decisions.", "The concept fits a standalone workspace or an existing governance suite."], ["Source", "Transformations", "Permissions"]),
 "choosethe.one": ("From endless options to one considered choice.", ["Curated commerce", "Matching services", "Recommendation tools", "Recruitment"], ["The complete phrase gives a product a natural call to action.", "A focused niche can make recommendations more useful than a general catalog."], ["Your priorities", "A considered shortlist", "Your choice"]),
}
for domain in DOMAINS:
    domain["tagline"], domain["uses"], domain["reasons"], domain["preview"] = POSITIONING[domain["name"]]
    domain["featured"] = domain["name"] in {"arabicvoiceagent.com", "agentsecurity.help", "citationreadiness.com", "deepfakes.help"}


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def offer_url(domain: str) -> str:
    subject = quote(f"Private offer for {domain} — MzunguWay")
    body = quote(
        "Hello MzunguWay,\n\n"
        f"I would like to discuss a private offer for {domain}.\n\n"
        "Name:\n"
        "Company:\n"
        "Offer or budget range:\n"
        "Intended use:\n"
        "Acquisition timeline:\n\n"
        "Thank you."
    )
    return f"mailto:hello@mzunguway.com?subject={subject}&body={body}"


def page_schema(domain: dict[str, object]) -> str:
    url = f"https://mzunguway.com/domains/{domain['slug']}/"
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": f"{url}#webpage",
                "url": url,
                "name": f"{domain['name']} — Domain acquisition and business concept",
                "description": domain["description"],
                "isPartOf": {"@id": "https://mzunguway.com/#website"},
                "about": {
                    "@type": "Thing",
                    "name": domain["name"],
                    "description": domain["concept"],
                },
                "inLanguage": "en",
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "MzunguWay",
                        "item": "https://mzunguway.com/",
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Domains",
                        "item": "https://mzunguway.com/#domains",
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": domain["name"],
                        "item": url,
                    },
                ],
            },
        ],
    }
    return json.dumps(schema, ensure_ascii=False, separators=(",", ":")).replace("</", r"<\/")


def actions(domain):
    marketplace = domain['afternic']
    href = marketplace or offer_url(domain['name'])
    attrs = ' target="_blank" rel="noopener noreferrer"' if marketplace else ''
    label = 'Acquire Domain' if marketplace else 'Discuss Acquisition'
    return f'<div class="detail-actions"><a class="btn primary" href="{esc(href)}"{attrs}>{label}</a><a class="btn" href="{esc(offer_url(domain["name"]))}">Make an Offer</a></div>'


def route_note(domain):
    if domain['afternic']:
        return 'Acquisition opens the existing Afternic listing. Confirm availability, pricing and any payment options there before proceeding. MzunguWay is not an official marketplace partner.'
    return 'Private enquiry only. Confirm current availability, registrar eligibility, transaction method and transfer terms before any payment.'


def mockup(domain):
    steps = ''.join(f'<li><span class="concept-number">0{i + 1}</span><span>{esc(step)}</span></li>' for i, step in enumerate(domain['preview']))
    return f'<figure class="concept-preview"><div class="concept-chrome"><span aria-hidden="true">○ ○ ○</span><span>Brand concept</span></div><div class="concept-canvas"><p class="concept-name">{esc(domain["name"])}</p><h3>{esc(domain["tagline"])}</h3><ol class="concept-steps">{steps}</ol></div><figcaption>Illustrative concept only — not a working product. The domain name is the asset offered.</figcaption></figure>'


def card(domain, featured=False):
    url = f'/domains/{domain["slug"]}/'
    return f'''<article class="domain" data-category="{esc(domain['category'])}" data-featured="{str(domain['featured']).lower()}">
      <div class="domain-cat">{esc(domain['category'])}</div>
      <h3 class="domain-name"><a href="{url}">{esc(domain['name'])}</a></h3>
      <p class="domain-desc">{esc(domain['tagline'])}</p>
      <p class="card-usecase"><strong>Build on this name</strong>{esc(domain['concept'])}</p>
      <details class="card-concept"><summary>Preview the business concept</summary><p>{esc(domain['product'])}</p><p><strong>Ideal for:</strong> {esc(' · '.join(domain['fits']))}</p></details>
      <div class="domain-actions"><a class="btn" href="{url}">View Opportunity <span aria-hidden="true">→</span></a>{actions(domain)}</div>
    </article>'''


def related(domain):
    candidates = sorted((d for d in DOMAINS if d != domain), key=lambda d: d['category'] != domain['category'])[:3]
    return ''.join(f'<a class="card" href="/domains/{d["slug"]}/"><span class="kicker">{esc(d["category"])}</span><strong>{esc(d["name"])}</strong><p>{esc(d["tagline"])}</p></a>' for d in candidates)


def render(domain: dict[str, object]) -> str:
    name = str(domain["name"])
    slug = str(domain["slug"])
    category = str(domain["category"])
    description = str(domain["description"])
    concept = str(domain["concept"])
    opportunity = str(domain["opportunity"])
    problem = str(domain["problem"])
    product = str(domain["product"])
    afternic = domain["afternic"] or offer_url(name)
    transaction = "Afternic marketplace" if domain["afternic"] else "Private enquiry — confirm eligibility and transfer terms"
    workflow = list(domain["workflow"])
    fits = list(domain["fits"])
    url = f"https://mzunguway.com/domains/{slug}/"
    extension = "." + name.rsplit(".", 1)[-1]
    fit_html = "\n".join(f'                <span>{esc(str(item))}</span>' for item in fits)
    workflow_html = "\n".join(f"              <li>{esc(str(item))}</li>" for item in workflow)

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(name)} for Sale | {esc(category)} Opportunity — MzunguWay</title>
  <meta name="description" content="{esc(description)}">
  <meta name="theme-color" content="#F5F2EA">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <link rel="canonical" href="{url}">
  <link rel="icon" href="/brand-symbol.svg?v=7" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&amp;family=Sora:wght@500;600;700&amp;display=swap" rel="stylesheet">

  <meta property="og:title" content="{esc(name)} — MzunguWay">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:site_name" content="MzunguWay">
  <meta property="og:image" content="https://mzunguway.com/og-card.png?v=7">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="MzunguWay Domain Naming Studio">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(name)} — MzunguWay">
  <meta name="twitter:description" content="{esc(description)}">
  <meta name="twitter:image" content="https://mzunguway.com/og-card.png?v=7">

  <link rel="stylesheet" href="/styles.css?v=7">
  <script type="application/ld+json">{page_schema(domain)}</script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>

  <header class="site-header">
    <div class="wrap">
      <nav class="navbar" aria-label="Primary navigation">
        <a class="brand" href="/#top" aria-label="MzunguWay home">
          <span class="brand-window"><img src="/assets/mzunguway-original.jpg" alt="MzunguWay — Domain Naming Studio" width="1448" height="1086"></span>
        </a>
        <button class="menu-toggle" id="menuToggle" type="button" aria-expanded="false" aria-controls="mainNav" aria-label="Open navigation menu">
          <span></span><span></span><span></span>
        </button>
        <div class="navlinks" id="mainNav">
          <a href="/#studio">Studio</a>
          <a href="/#spirit">Spirit</a>
          <a href="/#domains">Domains</a>
          <a href="/#process">How it works</a>
          <a href="/#faq">FAQ</a>
          <a href="/#contact">Contact</a>
        </div>
        <a class="btn header-cta" href="/#domains">All domains</a>
      </nav>
    </div>
  </header>

  <main id="main" class="detail-main">
    <div class="wrap">
      <nav class="breadcrumb" aria-label="Breadcrumb">
        <a href="/">MzunguWay</a><span aria-hidden="true">/</span>
        <a href="/#domains">Domains</a><span aria-hidden="true">/</span>
        <span aria-current="page">{esc(name)}</span>
      </nav>
    </div>

    <section class="domain-page-hero">
      <div class="wrap domain-page-grid">
        <div class="domain-page-copy">
          <div class="domain-kicker-row">
            <div class="kicker">{esc(category)}</div>
            <span class="status-chip">Listed for acquisition</span>
          </div>
          <h1 class="domain-display">{esc(name)}</h1>
          <p class="opportunity-tagline">{esc(domain['tagline'])}</p>
          <p class="domain-page-desc">{esc(description)}</p>
          {actions(domain)}
          <p class="market-note">{route_note(domain)}</p>
        </div>

        <aside class="domain-page-aside" aria-labelledby="identity-title">
          <div>
            <div class="kicker">The identity</div>
            <h2 id="identity-title">{esc(concept)}</h2>
            <dl class="fact-list">
              <div class="fact"><dt>Category</dt><dd>{esc(category)}</dd></div>
              <div class="fact"><dt>Extension</dt><dd>{esc(extension)}</dd></div>
              <div class="fact"><dt>Asset</dt><dd>Domain name only</dd></div>
              <div class="fact"><dt>Transaction</dt><dd>{esc(transaction)}</dd></div>
            </dl>
          </div>
          <p class="aside-disclaimer">Concepts are illustrative positioning ideas. No operating business, website, traffic, trademark or content is included unless separately agreed in writing.</p>
        </aside>
      </div>
    </section>

    <section class="detail-body">
      <div class="wrap">
        <div class="detail-content-grid">
          <div class="detail-stack">
            <article class="detail-section">
              <div class="kicker">Why this domain</div>
              <h2>The opportunity</h2>
              <p>{esc(opportunity)}</p>
            </article>
            <article class="detail-section">
              <div class="kicker">Ideal for</div>
              <h2>Who could build on it</h2>
              <div class="fit-tags">
{fit_html}
              </div>
            </article>
            <article class="detail-section">
              <div class="kicker">Built for</div><h2>Choose a focused use case.</h2>
              <div class="fit-tags">{''.join('<span>' + esc(x) + '</span>' for x in domain['uses'])}</div>
            </article>
            <article class="detail-section">
              <div class="kicker">Why it matters</div><h2>A practical commercial angle.</h2>
              <ul class="commercial-reasons">{''.join('<li>' + esc(x) + '</li>' for x in domain['reasons'])}</ul>
            </article>
          </div>

          <div class="detail-stack">
            <article class="detail-section">
              <div class="kicker">Imagine</div>
              <h2>{esc(concept)}</h2>
              <h3>The problem</h3>
              <p>{esc(problem)}</p>
              <h3 class="section-subhead">What someone could build</h3>
              <p>Imagine {esc(product[0].lower() + product[1:])}</p>
              {mockup(domain)}
              {actions(domain)}
            </article>
            <article class="detail-section">
              <div class="kicker">Illustrative workflow</div>
              <h2>How the concept could work</h2>
              <ol class="workflow-list">
{workflow_html}
              </ol>
            </article>
          </div>
        </div>

        <div class="domain-closing">
          <div>
            <h2>Could this be your next identity?</h2>
            <p>{route_note(domain)}</p>
          </div>
          {actions(domain)}
        </div>

        <section class="related-opportunities" aria-label="Related opportunities"><div class="kicker">Explore another direction</div><h2>Related opportunities</h2><div class="related-grid">{related(domain)}</div></section>

        <a class="text-link back-link" href="/#domains"><span aria-hidden="true">←</span> Return to all domains</a>
      </div>
    </section>
  </main>
  <div class="mobile-acquire" aria-label="Acquisition shortcuts">{actions(domain)}</div>

  <footer>
    <div class="wrap foot">
      <span>© <span data-current-year></span> MzunguWay. All rights reserved.</span>
      <span><a href="mailto:hello@mzunguway.com">hello@mzunguway.com</a> · Domain Naming Studio</span>
    </div>
  </footer>

  <script src="/app.js?v=7" defer></script>
</body>
</html>
"""


def main() -> None:
    for domain in DOMAINS:
        output_dir = ROOT / "domains" / str(domain["slug"])
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "index.html").write_text(render(domain).replace('?v=7', '?v=10'), encoding="utf-8")
    template = (ROOT / "templates/home.html").read_text(encoding="utf-8")
    cards = '\n'.join(card(d) for d in DOMAINS)
    featured = '\n'.join(card(d, True) for d in DOMAINS if d['featured'])
    items = [{"@type": "ListItem", "position": i + 1, "url": f"https://mzunguway.com/domains/{d['slug']}/", "name": d['name']} for i, d in enumerate(DOMAINS)]
    template = template.replace('@@PORTFOLIO@@', cards).replace('@@FEATURED@@', featured).replace('@@ITEMS@@', json.dumps(items)).replace('@@COUNT@@', str(len(DOMAINS))).replace('?v=9', '?v=10')
    (ROOT / 'index.html').write_text(template, encoding='utf-8')
    urls = ['https://mzunguway.com/'] + [f"https://mzunguway.com/domains/{d['slug']}/" for d in DOMAINS]
    (ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + '\n'.join(f'<url><loc>{u}</loc></url>' for u in urls) + '\n</urlset>\n', encoding='utf-8')


if __name__ == "__main__":
    main()
