"""Dependency-free checks for the generated static portfolio."""
import json
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from generate_domain_pages import DOMAINS, ROOT, render


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
                    'responsibleagents.org', 'voicefraud.help', 'dataorig.in', 'choosethe.one'}
        self.assertEqual({d['name'] for d in DOMAINS}, expected)
        self.assertEqual(len(DOMAINS), 10)
        for d in DOMAINS:
            self.assertEqual(d['afternic'], None if d['name'] == 'dataorig.in' else f"https://www.afternic.com/domain/{d['name']}")

    def test_pages_metadata_links_and_concepts(self):
        descriptions = set()
        for d in DOMAINS:
            path = ROOT / 'domains' / d['slug'] / 'index.html'
            source = path.read_text()
            self.assertEqual(source, render(d).replace('?v=7', '?v=10'))
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
        self.assertEqual(len(descriptions), 10)
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
        self.assertEqual(len(cards), 14)  # ten holdings plus four featured cards
        self.assertEqual(len(ET.parse(ROOT / 'sitemap.xml').getroot()), 11)
        self.assertIn('Sitemap: https://mzunguway.com/sitemap.xml', (ROOT / 'robots.txt').read_text())


if __name__ == '__main__':
    unittest.main()
