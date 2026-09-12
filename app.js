const PORTFOLIO = [
  {
    "name": "agentsecurity.help",
    "category": "AI Security",
    "tag": "Featured",
    "description": "A direct, high-intent name for agentic AI security, safe autonomous agents, governance, monitoring, or enterprise protection.",
    "useCase": "Imagine an AI company giving every customer a dedicated security hub for autonomous agents: permission reviews, deployment checklists, risk assessments, incident guidance, policy templates and a clear place to report suspicious agent behaviour. agentsecurity.help could become the trust-and-support layer behind secure agent adoption.",
    "idealFor": "AI security vendors · Agent platforms · Enterprise security teams",
    "featured": true,
    "url": "https://www.afternic.com/domain/agentsecurity.help"
  },
  {
    "name": "arabicvoiceagent.com",
    "category": "Voice & AI",
    "tag": "Featured",
    "description": "A clear .com built for Arabic voice agents, conversational AI, call automation, speech interfaces, or regional AI platforms.",
    "useCase": "Imagine a platform where a business can create an Arabic-speaking voice agent in minutes, choose the dialect and tone, connect a phone number, and deploy it for reservations, customer service, appointment booking or lead qualification. The domain explains the product before the visitor even opens the page.",
    "idealFor": "Voice AI companies · Contact-center platforms · MENA SaaS",
    "featured": true,
    "url": "https://www.afternic.com/domain/arabicvoiceagent.com"
  },
  {
    "name": "arabicvoice.xyz",
    "category": "Voice & AI",
    "tag": "Selected",
    "description": "A flexible, expressive name for Arabic voice AI, speech technology, creator tools, conversational products, or experimental platforms.",
    "useCase": "Imagine a modern Arabic voice laboratory where creators and developers can test voices, compare dialects, generate speech, discover voice models and access APIs. arabicvoice.xyz feels naturally suited to an experimental, developer-friendly or next-generation voice brand.",
    "idealFor": "Speech-tech labs · Voice marketplaces · Creator platforms",
    "featured": false,
    "url": "https://www.afternic.com/domain/arabicvoice.xyz"
  },
  {
    "name": "citationreadiness.com",
    "category": "AI Visibility",
    "tag": "Featured",
    "description": "A strong .com for AI-search readiness, citation optimization, answer-engine visibility, content authority, or digital reputation services.",
    "useCase": "Imagine a SaaS product that scans a company's website and produces a Citation Readiness Score: which pages contain clear facts, quotable evidence, trustworthy sourcing, structured information and authority signals that make the content easier for AI search and answer engines to understand and cite. The product could then generate a prioritized improvement plan.",
    "idealFor": "AEO/GEO platforms · SEO agencies · Brand intelligence tools",
    "featured": true,
    "url": "https://www.afternic.com/domain/citationreadiness.com"
  },
  {
    "name": "deepfakes.help",
    "category": "Trust & Safety",
    "tag": "Featured",
    "description": "A memorable help-oriented domain for deepfake detection, victim support, awareness, verification, education, or incident response.",
    "useCase": "Imagine a trusted first-stop portal for someone who suspects a deepfake: preserve the evidence, understand the warning signs, submit media for professional review, learn how to report impersonation, request platform takedowns and find the right legal or cybersecurity support. For companies, it could also become a deepfake incident-response and employee-awareness center.",
    "idealFor": "Trust & safety firms · Cybersecurity vendors · Public-interest services",
    "featured": true,
    "url": "https://www.afternic.com/domain/deepfakes.help"
  },
  {
    "name": "hostelcheck.in",
    "category": "Travel & Trust",
    "tag": "Featured",
    "description": "A concise domain for secure digital guest check-in, identity verification and smoother hostel arrivals.",
    "useCase": "Imagine a hostel chain sending every guest one simple link before arrival. On HostelCheck.in, the traveler securely completes pre-check-in, provides the required identity details, confirms the booking, signs the guest registration and receives arrival instructions before reaching reception. Staff spend less time on paperwork and guests move from booking to bed with almost no friction. It is especially relevant in markets where digital guest-registration workflows are already part of accommodation operations.",
    "idealFor": "Hostel chains · PMS providers · Travel-tech platforms",
    "featured": true,
    "url": "https://www.afternic.com/domain/hostelcheck.in"
  },
  {
    "name": "promptinjection.help",
    "category": "AI Security",
    "tag": "Featured",
    "description": "A precise educational and support domain for prompt-injection defense, AI security guidance, incident response, and developer resources.",
    "useCase": "Imagine a practical security center for teams shipping LLM products: explain prompt-injection attacks, provide defensive checklists, safe testing examples, architecture guidance and an incident-response playbook when an AI assistant is manipulated by hostile instructions. The name is immediately understandable to developers and security teams.",
    "idealFor": "AI security companies · Developer platforms · Security education",
    "featured": true,
    "url": "https://www.afternic.com/domain/promptinjection.help"
  },
  {
    "name": "responsibleagents.org",
    "category": "Responsible AI",
    "tag": "Selected",
    "description": "A mission-led domain for responsible agentic AI, standards, research, governance, education, or industry initiatives.",
    "useCase": "Imagine an independent initiative that publishes principles for responsible AI agents, practical governance templates, safety benchmarks, research, case studies and an open directory of organizations committing to responsible deployment. The .org extension gives it the natural tone of a standards, research or public-interest initiative.",
    "idealFor": "Research groups · Standards initiatives · Nonprofits · Consortia",
    "featured": false,
    "url": "https://www.afternic.com/domain/responsibleagents.org"
  },
  {
    "name": "voicefraud.help",
    "category": "Voice & Fraud",
    "tag": "Featured",
    "description": "Built for voice-fraud prevention, impersonation defense, deepfake voice protection, authentication, awareness, or customer support.",
    "useCase": "Imagine a bank, telecom operator or fraud-prevention company offering one memorable place for customers who receive a suspicious call or voice message. VoiceFraud.help could guide them through verification steps, explain voice-cloning scams, help preserve evidence, route urgent cases to the right team and host training for employees who handle high-risk voice requests.",
    "idealFor": "Banks · Telecoms · Fraud-prevention firms · Identity vendors",
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

  list.forEach((item, index) => {
    const article = document.createElement("article");
    article.className = "domain" + (item.featured ? " featured" : "");
    const panelId = `usecase-${index}-${item.name.replace(/[^a-z0-9]/gi, "-")}`;
    article.innerHTML = `
      <div class="domain-cat">${item.category}</div>
      <div class="domain-name">${item.name}</div>
      <div class="domain-desc">${item.description}</div>
      <button class="usecase-toggle" type="button" aria-expanded="false" aria-controls="${panelId}">
        <span>See functional use case</span><span class="usecase-plus">+</span>
      </button>
      <div class="usecase-panel" id="${panelId}" hidden>
        <div class="usecase-label">Imagine this</div>
        <p>${item.useCase}</p>
        <div class="ideal-for"><strong>Ideal for</strong><span>${item.idealFor}</span></div>
      </div>
      <div class="domain-foot">
        <span class="make-offer">Make Offer</span>
        <a class="btn buy" href="${item.url}" target="_blank" rel="noopener">Acquisition ↗</a>
      </div>
    `;

    const toggle = article.querySelector(".usecase-toggle");
    const panel = article.querySelector(".usecase-panel");
    toggle.addEventListener("click", () => {
      const isOpen = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!isOpen));
      panel.hidden = isOpen;
      toggle.querySelector(".usecase-plus").textContent = isOpen ? "+" : "−";
    });

    grid.appendChild(article);
  });
}

renderFilters();
renderDomains();
