const PORTFOLIO = [
  {
    "name": "humancheck.in",
    "category": "Identity & Trust",
    "tag": "Featured",
    "description": "A crisp, memorable name for identity verification, trust layers, human-in-the-loop AI, or anti-bot products.",
    "featured": true,
    "url": "https://www.afternic.com/domain/humancheck.in"
  },
  {
    "name": "agentsecurity.help",
    "category": "AI Security",
    "tag": "Featured",
    "description": "A direct fit for agentic-AI safety, secure agents, enterprise AI governance, or security support.",
    "featured": true,
    "url": "https://www.afternic.com/domain/agentsecurity.help"
  },
  {
    "name": "voicefraud.help",
    "category": "Voice & Fraud",
    "tag": "Featured",
    "description": "Built for voice-fraud prevention, deepfake protection, authentication, awareness, or customer support.",
    "featured": true,
    "url": "https://www.afternic.com/domain/voicefraud.help"
  },
  {
    "name": "arabicvoice.xyz",
    "category": "Voice & AI",
    "tag": "Featured",
    "description": "A broad, expressive name for Arabic voice AI, speech products, conversational interfaces, or creator tools.",
    "featured": true,
    "url": "https://www.afternic.com/domain/arabicvoice.xyz"
  },
  {
    "name": "llmcheck.in",
    "category": "AI & Evaluation",
    "tag": "Featured",
    "description": "A compact name for LLM testing, evaluation, guardrails, observability, QA, or model verification.",
    "featured": true,
    "url": "https://www.afternic.com/domain/llmcheck.in"
  },
  {
    "name": "botcheck.in",
    "category": "Identity & Trust",
    "tag": "Featured",
    "description": "Short and functional for bot detection, fraud prevention, traffic integrity, or trust infrastructure.",
    "featured": true,
    "url": "https://www.afternic.com/domain/botcheck.in"
  },
  {
    "name": "agentcheck.in",
    "category": "AI & Agents",
    "tag": "Selected",
    "description": "A straightforward name for agent verification, monitoring, evaluation, compliance, or performance checks.",
    "featured": false,
    "url": "https://www.afternic.com/domain/agentcheck.in"
  },
  {
    "name": "responsibleagents.org",
    "category": "Responsible AI",
    "tag": "Selected",
    "description": "A mission-led name for responsible agentic AI, standards, research, education, or industry initiatives.",
    "featured": false,
    "url": "https://www.afternic.com/domain/responsibleagents.org"
  },
  {
    "name": "dataorig.in",
    "category": "Data & Provenance",
    "tag": "Selected",
    "description": "A clever split-domain concept for data origin, provenance, traceability, authenticity, and lineage tools.",
    "featured": false,
    "url": "https://www.afternic.com/domain/dataorig.in"
  },
  {
    "name": "choosethe.one",
    "category": "Brandable",
    "tag": "Selected",
    "description": "A memorable call-to-action domain for choice, matching, discovery, premium selection, or recommendation products.",
    "featured": false,
    "url": "https://www.afternic.com/domain/choosethe.one"
  }
];

document.getElementById("year").textContent = new Date().getFullYear();

const grid = document.getElementById("domainGrid");
const filters = document.getElementById("filters");

const categories = ["All", "Featured", ...new Set(PORTFOLIO.map(x => x.category))];

function renderFilters() {
  filters.innerHTML = "";
  categories.forEach((category, i) => {
    const button = document.createElement("button");
    button.className = "filter" + (i === 0 ? " active" : "");
    button.textContent = category;
    button.onclick = () => {
      document.querySelectorAll(".filter").forEach(b => b.classList.remove("active"));
      button.classList.add("active");
      renderDomains(category);
    };
    filters.appendChild(button);
  });
}

function renderDomains(filter = "All") {
  grid.innerHTML = "";
  const list = PORTFOLIO.filter(item =>
    filter === "All" ||
    (filter === "Featured" && item.featured) ||
    item.category === filter
  );

  list.forEach(item => {
    const article = document.createElement("article");
    article.className = "domain" + (item.featured ? " featured" : "");
    article.innerHTML = `
      <div class="domain-cat">${item.category}</div>
      <div class="domain-name">${item.name}</div>
      <div class="domain-desc">${item.description}</div>
      <div class="domain-foot">
        <span class="make-offer">Make Offer</span>
        <a class="btn buy" href="${item.url}" target="_blank" rel="noopener">Acquisition ↗</a>
      </div>
    `;
    grid.appendChild(article);
  });
}

renderFilters();
renderDomains();
