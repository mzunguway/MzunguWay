const PORTFOLIO = [
  {
    "name": "agentsecurity.help",
    "category": "AI Security",
    "tag": "Featured",
    "description": "A direct, high-intent name for agentic AI security, safe autonomous agents, governance, monitoring, or enterprise protection.",
    "featured": true,
    "url": "https://www.afternic.com/domain/agentsecurity.help"
  },
  {
    "name": "arabicvoiceagent.com",
    "category": "Voice & AI",
    "tag": "Featured",
    "description": "A clear .com built for Arabic voice agents, conversational AI, call automation, speech interfaces, or regional AI platforms.",
    "featured": true,
    "url": "https://www.afternic.com/domain/arabicvoiceagent.com"
  },
  {
    "name": "arabicvoice.xyz",
    "category": "Voice & AI",
    "tag": "Selected",
    "description": "A flexible, expressive name for Arabic voice AI, speech technology, creator tools, conversational products, or experimental platforms.",
    "featured": false,
    "url": "https://www.afternic.com/domain/arabicvoice.xyz"
  },
  {
    "name": "citationreadiness.com",
    "category": "AI Visibility",
    "tag": "Featured",
    "description": "A strong .com for AI-search readiness, citation optimization, answer-engine visibility, content authority, or digital reputation services.",
    "featured": true,
    "url": "https://www.afternic.com/domain/citationreadiness.com"
  },
  {
    "name": "deepfakes.help",
    "category": "Trust & Safety",
    "tag": "Featured",
    "description": "A memorable help-oriented domain for deepfake detection, victim support, awareness, verification, education, or incident response.",
    "featured": true,
    "url": "https://www.afternic.com/domain/deepfakes.help"
  },
  {
    "name": "hostelcheck.in",
    "category": "Travel & Trust",
    "tag": "Selected",
    "description": "A concise name for hostel reviews, verification, safety checks, booking confidence, traveler tools, or accommodation discovery.",
    "featured": false,
    "url": "https://www.afternic.com/domain/hostelcheck.in"
  },
  {
    "name": "promptinjection.help",
    "category": "AI Security",
    "tag": "Featured",
    "description": "A precise educational and support domain for prompt-injection defense, AI security guidance, incident response, and developer resources.",
    "featured": true,
    "url": "https://www.afternic.com/domain/promptinjection.help"
  },
  {
    "name": "responsibleagents.org",
    "category": "Responsible AI",
    "tag": "Selected",
    "description": "A mission-led domain for responsible agentic AI, standards, research, governance, education, or industry initiatives.",
    "featured": false,
    "url": "https://www.afternic.com/domain/responsibleagents.org"
  },
  {
    "name": "voicefraud.help",
    "category": "Voice & Fraud",
    "tag": "Featured",
    "description": "Built for voice-fraud prevention, impersonation defense, deepfake voice protection, authentication, awareness, or customer support.",
    "featured": true,
    "url": "https://www.afternic.com/domain/voicefraud.help"
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
