from pathlib import Path
import hashlib, html, json, re
root = Path(__file__).resolve().parents[1]
data = json.loads((root/'catalog.json').read_text(encoding='utf-8'))
assert data['animation_count'] == 46 and data['xex_count'] == 92
assert len(data['animations']) == 46
assert len({p['id'] for p in data['animations']}) == 46
assert sum(p['kind']=='studio' for p in data['animations']) == 40
assert sum(p['kind']=='custom' for p in data['animations']) == 6
assert len(list((root/'downloads').glob('*.xex'))) == 92
for p in data['animations']:
    assert 'prototype' not in p['name'].lower()
    assert (root/p['image']).is_file()
    if p['kind']=='custom': assert (root/p['motion']).is_file()
    assert set(p['downloads']) == {'HDD','NAND'}
    for info in p['downloads'].values():
        raw = (root/info['url']).read_bytes()
        assert len(raw)==info['bytes'] and raw[:4]==b'XEX2'
        assert hashlib.sha256(raw).hexdigest()==info['sha256']
        import zlib
        assert f'{zlib.crc32(raw)&0xffffffff:08X}'==info['crc32']
page = (root/'index.html').read_text(encoding='utf-8')
assert page.startswith('<!doctype html>') and '<html lang="en">' in page
assert page.count('<article class="card"')==46
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
print('Verified: 46 animations, 92 unchanged XEX files, 46 stills, 6 motion previews; local links, hashes and privacy checks passed.')
