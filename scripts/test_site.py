"""Dependency-free checks for the generated static portfolio."""
import json
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote, parse_qs
from generate_domain_pages import ASSET_VERSION, BUNDLES, DOMAINS, ROOT, bundle_offer_url, render


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.tags = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


class SiteTests(unittest.TestCase):
    def test_inventory_and_routes(self):
        expected = {'agentsecurity.help', 'arabicvoiceagent.com', 'arabicvoice.xyz',
                    'citationreadiness.com', 'deepfakes.help', 'promptinjection.help',
                    'responsibleagents.org', 'voicefraud.help', 'perfum.world',
                    'agentpaymentid.com', 'agentpaymentrisk.com'}
        self.assertEqual({d['name'] for d in DOMAINS}, expected)
        self.assertEqual(len(DOMAINS), 11)
        private_enquiries = {'perfum.world', 'agentpaymentid.com', 'agentpaymentrisk.com'}
        for d in DOMAINS:
            self.assertEqual(d['afternic'], None if d['name'] in private_enquiries else f"https://www.afternic.com/domain/{d['name']}")
        self.assertEqual({p.parent.name for p in ROOT.glob('domains/*/index.html')}, {d['slug'] for d in DOMAINS})

    def test_pages_metadata_links_and_concepts(self):
        descriptions = set()
        for d in DOMAINS:
            path = ROOT / 'domains' / d['slug'] / 'index.html'
            source = path.read_text()
            self.assertEqual(source, render(d).replace('?v=7', f'?v={ASSET_VERSION}'))
            page = Page(source)
            self.assertEqual(sum(tag == 'h1' for tag, attrs in page.tags), 1)
            meta = {a.get('name', a.get('property')): a.get('content') for t, a in page.tags if t == 'meta'}
            descriptions.add(meta['description'])
            self.assertNotIn('noindex', meta['robots'])
            self.assertTrue(meta['og:title'])
            self.assertTrue(meta['og:description'])
            self.assertIn(f'https://mzunguway.com/domains/{d["slug"]}/', source)
            for label in ['Why this domain', 'Built for', 'Imagine', 'Ideal for', 'Why it matters', 'Illustrative concept only']:
                self.assertIn(label, source)
            self.assertEqual(source.count('>Make an Offer</a>'), 4)
        self.assertEqual(len(descriptions), 11)
        for path in [ROOT / 'index.html', *ROOT.glob('domains/*/index.html')]:
            source = path.read_text()
            self.assertNotIn('@@', source)
            for tag, attrs in Page(source).tags:
                for field in ('href', 'src'):
                    href = attrs.get(field, '')
                    if href.startswith('/') and not href.startswith('//'):
                        target = ROOT / unquote(urlsplit(href).path).lstrip('/')
                        self.assertTrue(target.exists(), f'{path}: {href}')
                if tag == 'a' and attrs.get('target') == '_blank':
                    self.assertIn('noopener', attrs.get('rel', ''))
            # Validate every JSON-LD block, not merely its presence.
            for fragment in source.split('<script type="application/ld+json">')[1:]:
                json.loads(fragment.split('</script>')[0])

    def test_home_and_sitemap(self):
        source = (ROOT / 'index.html').read_text()
        cards = [a for t, a in Page(source).tags if t == 'article' and 'data-category' in a]
        self.assertEqual(len(cards), 15)  # eleven holdings plus four featured cards
        sitemap_urls = {e.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text for e in ET.parse(ROOT / 'sitemap.xml').getroot()}
        self.assertEqual(len(sitemap_urls), 17)
        for path in ROOT.glob('collections/**/index.html'):
            self.assertIn('https://mzunguway.com/' + str(path.parent.relative_to(ROOT)) + '/', sitemap_urls)
        self.assertIn('qCcFSDu1fIHom87n-l1ZQqGqbgTom5Xb3y1dMI6KCQU', source)
        self.assertIn('Sitemap: https://mzunguway.com/sitemap.xml', (ROOT / 'robots.txt').read_text())

    def test_bundle_enquiries_and_membership(self):
        inventory = {d['name']: d for d in DOMAINS}
        home = (ROOT / 'index.html').read_text()
        self.assertEqual(len(BUNDLES), 4)
        for bundle in BUNDLES:
            names = [name for name, _ in bundle['members']]
            self.assertEqual(len(set(names)), 2)
            self.assertTrue(set(names).issubset(inventory))
            url = urlsplit(bundle_offer_url(bundle))
            self.assertEqual((url.scheme, url.path), ('mailto', 'hello@mzunguway.com'))
            query = parse_qs(url.query)
            self.assertIn(bundle['title'], query['subject'][0])
            self.assertIn('Offer for the complete bundle:', query['body'][0])
            self.assertIn(f'id="bundle-{bundle["slug"]}"', home)
            for name in names:
                self.assertIn(name, query['body'][0])
                page = (ROOT / 'domains' / inventory[name]['slug'] / 'index.html').read_text()
                self.assertIn(f'href="/#bundle-{bundle["slug"]}"', page)
                self.assertIn('Request Bundle Offer', page)
        for name in ['perfum.world', 'citationreadiness.com', 'responsibleagents.org']:
            page = (ROOT / 'domains' / inventory[name]['slug'] / 'index.html').read_text()
            self.assertNotIn('Also available as a bundle', page)

    def test_removed_names_are_not_published(self):
        paths = [ROOT / 'index.html', ROOT / 'sitemap.xml', *ROOT.glob('domains/*/index.html')]
        for path in paths:
            for retired in ['dataorig.in', 'choosethe.one', 'dataorig-in', 'choosethe-one']:
                self.assertNotIn(retired, path.read_text())


if __name__ == '__main__':
    unittest.main()
