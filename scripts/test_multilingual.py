"""Check complete buying routes, localization and SEO links before publication."""
import unittest, json, re
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from build_multilingual import ROOT, LANGUAGES, ORIGIN, path, base
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__(); self.tags=[];self.feed(text)
    def handle_starttag(self,t,a): self.tags.append((t,dict(a)))
class LocalizedRoutes(unittest.TestCase):
    def test_all_pages(self):
        pages=[ROOT/'index.html',*ROOT.glob('domains/*/index.html'),*ROOT.glob('collections/**/index.html'),ROOT/'contact/index.html']
        for l in ['fr','de','es']: pages.extend((ROOT/l).rglob('index.html'))
        self.assertEqual(len(pages),72)
        for file in pages:
            with self.subTest(page=file.relative_to(ROOT)):
                text=file.read_text();tags=Page(text).tags
                ids=[a['id'] for t,a in tags if 'id' in a];self.assertEqual(len(ids),len(set(ids)))
                self.assertEqual(sum(t=='h1' for t,a in tags),1)
                self.assertNotIn('@@',text)
                lang=next(a['lang'] for t,a in tags if t=='html')
                expected_lang=file.relative_to(ROOT).parts[0]
                self.assertEqual(lang,expected_lang if expected_lang in LANGUAGES else 'en')
                links=[a for t,a in tags if t=='link' and a.get('rel')=='alternate']
                self.assertEqual({a['hreflang'] for a in links},{'en','fr','de','es','x-default'})
                self.assertEqual(len(links),5)
                self.assertEqual(sum(t=='script' and a.get('src')=='/app.js?v=14' for t,a in tags),1)
                self.assertEqual(sum(t=='script' and a.get('src')=='/assets/ui.js?v=14' for t,a in tags),1)
                canon=next(a['href'] for t,a in tags if t=='link' and a.get('rel')=='canonical')
                rel=str(file.parent.relative_to(ROOT));expected=ORIGIN+'/' + (rel+'/' if rel!='.' else '')
                self.assertEqual(canon,expected)
                for t,a in tags:
                    for attr in ['href','src']:
                        value=a.get(attr,'');url=urlsplit(value)
                        if value.startswith('/') or value.startswith(ORIGIN):
                            target=ROOT/unquote(url.path).lstrip('/')
                            self.assertTrue(target.exists(),value)
                            if url.fragment and t=='a':
                                dest=target/'index.html' if target.is_dir() else target
                                self.assertIn(url.fragment,[x.get('id') for _,x in Page(dest.read_text()).tags],value)
                    if t=='a' and a.get('target')=='_blank':self.assertIn('noopener',a.get('rel',''))
                for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S):json.loads(block)
    def test_catalog(self):
        for l in LANGUAGES:
            source=(ROOT/path(l).lstrip('/')/'index.html').read_text(); tags=Page(source).tags
            cards=[a for t,a in tags if t=='article' and 'data-category' in a]
            self.assertEqual(len(cards),11)
            self.assertEqual(sum(a.get('data-featured')=='true' for a in cards),3)
            self.assertLess(source.index('id="domains"'),source.index('id="bundles"'))
            self.assertLess(source.index('id="studio"'),source.index('id="domains"'))
    def test_forms(self):
        for l in LANGUAGES:
            tags=Page((ROOT/path(l,'contact/').lstrip('/')/'index.html').read_text()).tags
            self.assertFalse(any(t=='form' and a.get('action') for t,a in tags))
            required={a.get('name') for t,a in tags if 'required' in a}
            self.assertEqual(required,{'domain','email','message'})
    def test_translated_detail_content(self):
        for l in ['fr','de','es']:
            for d in base.DOMAINS:
                source=(ROOT/l/'domains'/d['slug']/'index.html').read_text()
                self.assertIn(d['name'],source)
                for english in ['Make an Offer','View Opportunity','Why this domain','Private enquiry only']:
                    self.assertNotIn(english,source)
if __name__=='__main__':unittest.main()
