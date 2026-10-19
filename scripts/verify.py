from pathlib import Path
import hashlib, html, json, re
from html.parser import HTMLParser
root = Path(__file__).resolve().parents[1]
data = json.loads((root/'catalog.json').read_text(encoding='utf-8'))
total = data['animation_count']
custom = data['custom_animation_count']
original = data['color_theme_count']
assert total == custom + original and data['xex_count'] == total * 2
assert len(data['animations']) == total
assert len({p['id'] for p in data['animations']}) == total
assert sum(p['kind']=='original' for p in data['animations']) == data['color_theme_count'] == 40
assert sum(p['kind']=='custom' for p in data['animations']) == custom
assert len(list((root/'downloads').glob('*.xex'))) == total * 2
for p in data['animations']:
    assert 'prototype' not in p['name'].lower()
    assert (root/p['image']).is_file()
    if p['kind']=='custom':
        assert (root/p['motion']).is_file()
        assert isinstance(p['sound'],str) and p['sound'].strip()
    assert set(p['downloads']) == {'HDD','NAND'}
    for info in p['downloads'].values():
        raw = (root/info['url']).read_bytes()
        assert len(raw)==info['bytes'] and raw[:4]==b'XEX2'
        assert hashlib.sha256(raw).hexdigest()==info['sha256']
        import zlib
        assert f'{zlib.crc32(raw)&0xffffffff:08X}'==info['crc32']
page = (root/'index.html').read_text(encoding='utf-8')
assert page.startswith('<!doctype html>') and '<html lang="en">' in page
assert page.count('<article class="card"')==total
class Sections(HTMLParser):
    def __init__(self):
        super().__init__();self.stack=[];self.cards={};self.ids=set();self.motion=[]
    def handle_starttag(self, tag, attributes):
        attrs=dict(attributes)
        if attrs.get('id'):
            assert attrs['id'] not in self.ids,attrs['id']
            self.ids.add(attrs['id'])
        if tag=='section':self.stack.append(attrs.get('data-section-kind'))
        if tag=='article' and attrs.get('class')=='card':
            kind=attrs['data-kind'];assert self.stack[-1]==kind
            self.cards[kind]=self.cards.get(kind,0)+1
        if 'data-preview' in attrs:
            assert attrs.get('data-sound');self.motion.append(attrs['data-preview'])
    def handle_endtag(self, tag):
        if tag=='section':self.stack.pop()
sections=Sections();sections.feed(page)
assert sections.cards=={'custom':custom,'original':original}
assert {'custom-animations','original-recolored'}<=sections.ids
assert len(set(sections.motion))==custom
for link in re.findall(r'(?:href|src|data-image|data-preview)="([^"#]+)"',page):
    if link.startswith(('https://','http://','data:')): continue
    assert (root/html.unescape(link)).is_file(), link
for line in (root/'SHA256SUMS.txt').read_text().splitlines():
    expected, name = line.split('  ',1)
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==expected, name
for file in root.rglob('*'):
    if not file.is_file() or '.git' in file.relative_to(root).parts: continue
    assert file.suffix.lower() not in ('.exe','.dll','.pyc','.bin','.log'), file
    raw = file.read_bytes().lower()
    personal = bytes([106,97,110,55,50])
    prefix = bytes([99,58,92,117,115,101,114,115,92])
    for needle in (prefix, personal, prefix.decode().encode('utf-16le'), personal.decode().encode('utf-16le')):
        assert needle not in raw, file
print(f'Verified: {custom} custom + {original} original color editions, {total*2} XEX files, {total} stills, {custom} sound previews; section membership, local links, hashes and privacy checks passed.')
