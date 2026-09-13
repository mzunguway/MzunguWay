const PORTFOLIO = [
  {
    name: "agentsecurity.help",
    slug: "agentsecurity-help",
    category: "AI Security",
    description: "A direct, high-intent name for agentic AI security, secure deployment, governance, monitoring and incident support.",
    useCaseTitle: "Agent Security Operations & Support Hub",
    concept: "A customer-facing portal for permissions reviews, connector-risk checks, secure deployment guidance, incident intake and remediation playbooks.",
    idealFor: "AI-security vendors · Agent platforms · Enterprise security teams · MSSPs",
    featured: true,
    url: "https://www.afternic.com/domain/agentsecurity.help"
  },
  {
    name: "arabicvoiceagent.com",
    slug: "arabicvoiceagent-com",
    category: "Voice & AI",
    description: "A clear .com for Arabic voice agents, conversational AI, call automation, customer service and regional voice products.",
    useCaseTitle: "Arabic Voice Agent Platform for Customer Operations",
    concept: "A SaaS platform for building Arabic-speaking agents, choosing regional voices, connecting telephony and CRM systems and automating real customer workflows.",
    idealFor: "Contact-center platforms · Banks · Airlines · Clinics · Hospitality · MENA SaaS",
    featured: true,
    url: "https://www.afternic.com/domain/arabicvoiceagent.com"
  },
  {
    name: "arabicvoice.xyz",
    slug: "arabicvoice-xyz",
    category: "Voice & AI",
    description: "A flexible, developer-friendly name for Arabic speech technology, voice models, APIs, creator tools or experimental products.",
    useCaseTitle: "Arabic Voice Model Playground & API Marketplace",
    concept: "A developer platform to compare Arabic speech recognition and synthesis, test regional voices, benchmark quality and connect the chosen API.",
    idealFor: "Speech-tech labs · Developers · Voice marketplaces · Creator platforms · AI startups",
    featured: false,
    url: "https://www.afternic.com/domain/arabicvoice.xyz"
  },
  {
    name: "citationreadiness.com",
    slug: "citationreadiness-com",
    category: "AI Visibility",
    description: "A strong .com for AI-search readiness, structured authority, answer-engine visibility and content optimization.",
    useCaseTitle: "Citation Readiness Audit for AI Search & Answer Engines",
    concept: "A B2B audit platform that scores factual clarity, sourcing, entities, authorship, freshness and structured data, then prioritizes improvements.",
    idealFor: "AEO/GEO platforms · SEO agencies · Publishers · SaaS marketing · Brand intelligence",
    featured: true,
    url: "https://www.afternic.com/domain/citationreadiness.com"
  },
  {
    name: "deepfakes.help",
    slug: "deepfakes-help",
    category: "Trust & Safety",
    description: "A memorable help-oriented domain for deepfake incident response, victim support, verification, education and takedown guidance.",
    useCaseTitle: "Deepfake Incident Response & Victim Assistance Portal",
    concept: "A trusted first-response service for evidence preservation, authenticity triage, platform reporting, takedown guidance and specialist escalation.",
    idealFor: "Cybersecurity vendors · Trust & safety firms · Insurers · Media · Public-interest services",
    featured: true,
    url: "https://www.afternic.com/domain/deepfakes.help"
  },
  {
    name: "promptinjection.help",
    slug: "promptinjection-help",
    category: "AI Security",
    description: "A precise support domain for prompt-injection defense, secure LLM architecture, developer guidance and incident response.",
    useCaseTitle: "Prompt Injection Defense Center for LLM Teams",
    concept: "A defensive knowledge and response center with architecture checks, safe test cases, tool-boundary guidance, incident templates and mitigation playbooks.",
    idealFor: "AI-security companies · LLM platforms · Developer tools · Security teams · Training providers",
    featured: true,
    url: "https://www.afternic.com/domain/promptinjection.help"
  },
  {
    name: "responsibleagents.org",
    slug: "responsibleagents-org",
    category: "Responsible AI",
    description: "A mission-led .org for responsible agentic AI, standards, governance, research, benchmarks and industry collaboration.",
    useCaseTitle: "Responsible AI Agents Standards & Governance Initiative",
    concept: "An independent initiative publishing governance principles, templates, evaluation criteria, research, case studies and responsible-deployment commitments.",
    idealFor: "Research institutes · Standards initiatives · Nonprofits · Universities · Industry consortia",
    featured: false,
    url: "https://www.afternic.com/domain/responsibleagents.org"
  },
  {
    name: "voicefraud.help",
    slug: "voicefraud-help",
    category: "Voice & Fraud",
    description: "A high-intent domain for voice-cloning fraud, vishing response, impersonation defense, verification and customer protection.",
    useCaseTitle: "Voice Fraud Response Center for Banks & Telecoms",
    concept: "A branded response portal where users verify suspicious requests, preserve evidence, receive immediate safety guidance and reach the right fraud team.",
    idealFor: "Banks · Telecom operators · Fraud-prevention firms · Identity vendors · Insurers",
    featured: true,
    url: "https://www.afternic.com/domain/voicefraud.help"
  },
  {
    name: "dataorig.in",
    slug: "dataorig-in",
    category: "Data & Provenance",
    description: "A compact domain hack that reads as ‘data origin’, suited to provenance, lineage, traceability and AI-data authenticity.",
    useCaseTitle: "Data Provenance & Lineage Verification Layer",
    concept: "A platform that records where a dataset came from, how it changed, what permissions apply and whether its origin can be trusted before analytics or AI use.",
    idealFor: "Data-governance vendors · Lineage platforms · AI provenance startups · Dataset marketplaces",
    featured: true,
    url: null
  },
  {
    name: "choosethe.one",
    slug: "choosethe-one",
    category: "Brandable",
    description: "A memorable call-to-action domain for recommendation engines, matching platforms, premium curation and confident decision products.",
    useCaseTitle: "Curated Recommendation & Matching Platform",
    concept: "A product that reduces a crowded market to a small set of strong matches, then guides the user toward one confident final choice.",
    idealFor: "Recommendation engines · Matching platforms · Premium marketplaces · Recruitment · Curated commerce",
    featured: false,
    url: "https://www.afternic.com/domain/choosethe.one"
  }
];

document.querySelectorAll("[data-current-year], #year").forEach(function (node) {
  node.textContent = new Date().getFullYear();
});

const menuToggle = document.getElementById("menuToggle");
const mainNav = document.getElementById("mainNav");

function closeMenu() {
  if (!menuToggle || !mainNav) return;
  menuToggle.setAttribute("aria-expanded", "false");
  menuToggle.setAttribute("aria-label", "Open navigation menu");
  mainNav.classList.remove("open");
  document.body.classList.remove("menu-open");
}

if (menuToggle && mainNav) {
  menuToggle.addEventListener("click", function () {
    const opening = menuToggle.getAttribute("aria-expanded") !== "true";
    menuToggle.setAttribute("aria-expanded", String(opening));
    menuToggle.setAttribute("aria-label", opening ? "Close navigation menu" : "Open navigation menu");
    mainNav.classList.toggle("open", opening);
    document.body.classList.toggle("menu-open", opening);
  });

  mainNav.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", closeMenu);
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") closeMenu();
  });

  window.addEventListener("resize", function () {
    if (window.innerWidth > 820) closeMenu();
  });
}

function privateOfferUrl(domain) {
  const subject = encodeURIComponent("Private offer for " + domain + " — MzunguWay");
  const body = encodeURIComponent(
    "Hello MzunguWay,\n\n" +
    "I would like to discuss a private offer for " + domain + ".\n\n" +
    "Name:\n" +
    "Company:\n" +
    "Offer or budget range:\n" +
    "Intended use:\n" +
    "Acquisition timeline:\n\n" +
    "Thank you."
  );
  return "mailto:hello@mzunguway.com?subject=" + subject + "&body=" + body;
}

const grid = document.getElementById("domainGrid");
const filters = document.getElementById("filters");
const resultCount = document.getElementById("resultCount");

if (grid && filters) {
  const categories = ["All", "Featured"].concat(
    Array.from(new Set(PORTFOLIO.map(function (item) { return item.category; })))
  );

  function renderFilters() {
    filters.innerHTML = "";

    categories.forEach(function (category, index) {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "filter" + (index === 0 ? " active" : "");
      button.textContent = category;
      button.setAttribute("aria-pressed", String(index === 0));

      button.addEventListener("click", function () {
        filters.querySelectorAll(".filter").forEach(function (item) {
          item.classList.remove("active");
          item.setAttribute("aria-pressed", "false");
        });
        button.classList.add("active");
        button.setAttribute("aria-pressed", "true");
        renderDomains(category);
      });

      filters.appendChild(button);
    });
  }

  function renderDomains(filter) {
    const activeFilter = filter || "All";
    const list = PORTFOLIO.filter(function (item) {
      return activeFilter === "All" ||
        (activeFilter === "Featured" && item.featured) ||
        item.category === activeFilter;
    });

    grid.innerHTML = "";
    if (resultCount) {
      resultCount.textContent = list.length + (list.length === 1 ? " domain shown" : " domains shown");
    }

    list.forEach(function (item) {
      const article = document.createElement("article");
      const panelId = "usecase-" + item.slug;
      const acquisitionHref = item.url || privateOfferUrl(item.name);
      const acquisitionLabel = item.url ? "View acquisition options" : "Request acquisition route";
      const targetAttrs = item.url ? ' target="_blank" rel="noopener noreferrer"' : '';
      const statusLabel = item.url ? "Listed" : "Private enquiry";
      article.className = "domain";
      article.id = item.slug;

      article.innerHTML =
        '<div class="domain-topline">' +
          '<div class="domain-cat">' + item.category + '</div>' +
          '<span class="status-chip">' + statusLabel + '</span>' +
        '</div>' +
        '<h3 class="domain-name"><a href="/domains/' + item.slug + '/">' + item.name + '</a></h3>' +
        '<div class="domain-desc">' + item.description + '</div>' +
        '<button class="usecase-toggle" type="button" aria-expanded="false" aria-controls="' + panelId + '">' +
          '<span>Preview the business concept</span><span class="usecase-plus" aria-hidden="true">+</span>' +
        '</button>' +
        '<div class="usecase-panel" id="' + panelId + '" hidden>' +
          '<div class="usecase-label">Real-world concept</div>' +
          '<div class="usecase-title">' + item.useCaseTitle + '</div>' +
          '<div class="usecase-block"><strong>Product angle</strong><p>' + item.concept + '</p></div>' +
          '<div class="ideal-for"><strong>Best fit</strong><span>' + item.idealFor + '</span></div>' +
        '</div>' +
        '<div class="domain-actions">' +
          '<a class="btn marketplace" href="' + acquisitionHref + '"' + targetAttrs + ' aria-label="' + acquisitionLabel + ' for ' + item.name + '">' + acquisitionLabel + (item.url ? ' <span aria-hidden="true">↗</span>' : '') + '</a>' +
          '<div class="domain-secondary">' +
            '<a href="' + privateOfferUrl(item.name) + '">Make a private offer</a>' +
            '<a href="/domains/' + item.slug + '/">Full concept <span aria-hidden="true">→</span></a>' +
          '</div>' +
        '</div>';

      const toggle = article.querySelector(".usecase-toggle");
      const panel = article.querySelector(".usecase-panel");

      toggle.addEventListener("click", function () {
        const isOpen = toggle.getAttribute("aria-expanded") === "true";
        toggle.setAttribute("aria-expanded", String(!isOpen));
        panel.hidden = isOpen;
        toggle.querySelector(".usecase-plus").textContent = isOpen ? "+" : "−";
      });

      grid.appendChild(article);
    });
  }

  renderFilters();
  renderDomains("All");
}
