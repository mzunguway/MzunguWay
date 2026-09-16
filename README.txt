MZUNGUWAY V11 — CURATED DIGITAL ASSETS & BUNDLES

Static HTML, CSS and progressive-enhancement JavaScript. No runtime framework,
package installation, tracking script or external data request is required.

MAINTENANCE
The authoritative inventory, editorial positioning and package memberships are
in scripts/generate_domain_pages.py (DOMAINS, POSITIONING and BUNDLES). Update
these when adding or removing a verified holding. Delete a retired holding's
generated page too; the tests detect leftover pages. Do not edit generated
pages directly.

Homepage structure: templates/home.html
Shared design: styles.css (existing Manrope/Sora, navy/gold/cream palette)
Behavior: app.js (navigation and filters only)

Build: python3 scripts/generate_domain_pages.py
Check: python3 scripts/test_site.py
Check JS: node --check app.js
Preview: python3 -m http.server 8765

The generator writes index.html, all eleven domain pages and sitemap.xml.
Commit generated files with their source so GitHub Pages needs no build step.
Existing active domain URLs and marketplace links are preserved. The three new
holdings (perfum.world, agentpaymentid.com, agentpaymentrisk.com) use private
enquiries until a verified marketplace URL is supplied.

BUNDLES
Four curated pairs: Agent Payments, AI Agent Security, Arabic Voice, and
Synthetic Media & Voice Trust. Each member links to its individual page.
Request Bundle Offer opens a prefilled email naming every included domain.
No message is sent automatically. Confirm all names, combined pricing and
transaction/transfer arrangements before agreeing a package. The existing
individual marketplace links do not imply a marketplace bundle checkout.
No package price, discount or payment plan is invented. Individual enquiries
remain possible; unpaired domains are not forced into unrelated bundles.

ACQUISITION RULES
No prices or payment plans are asserted here. Afternic links point to the existing
listings; availability and current terms must be confirmed there. Private offers
open a prefilled email. No form data is sent automatically. No partnership,
certification, performance, revenue or product-functionality claims are made.
All concepts are illustrative. Only the domain name is offered.

LOGO
assets/mzunguway-original.jpg is the supplied 1448x1086 original, unchanged.
The hero preserves its full aspect ratio. The header uses a CSS layout window
around the wordmark without resampling or rewriting the image. This is not a
vector conversion: true unlimited-scale output needs the original vector asset.
Existing SVG/favicon/social assets remain available for backward compatibility.

SEARCH CONSOLE
All eleven detail pages are static, linked from the homepage and in sitemap.xml.
Titles, descriptions, canonicals, OG metadata and breadcrumbs are generated.
robots.txt permits crawling. No Search Console verification token is invented.
Owner action: verify the property and submit https://mzunguway.com/sitemap.xml.
Technical readiness does not guarantee indexing or search rankings.

V13 — MULTILINGUAL BUYING JOURNEY
Build: python3 scripts/build_multilingual.py
Validate: python3 scripts/test_site.py && python3 scripts/test_multilingual.py
The multilingual build calls the English generator, then generates all locales.
Do not run only generate_domain_pages.py for publication: that omits locale links.
Reviewed localized copy: scripts/locales.py. Layouts: scripts/build_multilingual.py.
English editorial detail remains in domain_editorial.py and generate_domain_pages.py.
Production locales: English, French, Kiswahili and Japanese, with reciprocal hreflang on the 84 canonical SEO routes.
Three highlighted names in one eleven-name catalogue; existing holdings unchanged.
Contact forms compose an email locally; the visitor must send it from their mail
application. No backend, delivery claim, analytics or third-party form service is
introduced. The copy fallback remains available when no email app is configured.
