from pathlib import Path
import json,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];O="https://mzunguway.com";L=["en","fr","sw","ja"];P={"en":"","fr":"/fr","sw":"/sw","ja":"/ja"}
def u(l,r):return O+P[l]+(r if r!="/" else "/")
def main():
 d=sorted(p.parent.name for p in (ROOT/"domains").glob("*/index.html"));b=sorted(p.parent.name for p in (ROOT/"bundles").glob("*/index.html") if p.parent.name!="bundles");routes=["/"]+[f"/domains/{x}/" for x in d]+[f"/bundles/{x}/" for x in b]+["/contact/"];assert len(routes)==21
 for r in routes:
  for l in L:
   rel=(P[l].lstrip("/")+r).lstrip("/");p=ROOT/(rel+("index.html" if rel.endswith("/") else "/index.html"));p=ROOT/"index.html" if r=="/" and l=="en" else ROOT/l/"index.html" if r=="/" else p;s=p.read_text();assert re.search(fr'<html\s+lang="{l}"',s);assert re.findall(r'<link rel="canonical" href="([^"]+)">',s)==[u(l,r)];a=re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)">',s);assert [x for x,_ in a]==["en","fr","sw","ja","x-default"];assert a[-1][1]==u("en",r);[json.loads(x) for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S)]
 ns={"s":"http://www.sitemaps.org/schemas/sitemap/0.9"};assert len(ET.parse(ROOT/"sitemap.xml").getroot().findall("s:url",ns))==84;print("SEO locale validation passed: 84 canonical URLs.")
if __name__=="__main__":main()
