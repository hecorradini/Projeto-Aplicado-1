from pathlib import Path
from urllib.request import Request, urlopen
from zipfile import ZipFile
from html.parser import HTMLParser
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'data'
SOURCES = ROOT / 'sources'
DATA.mkdir(parents=True, exist_ok=True)
SOURCES.mkdir(parents=True, exist_ok=True)

class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden = 0
        self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'): self.hidden += 1
    def handle_endtag(self, tag):
        if tag in ('script', 'style'): self.hidden = max(0, self.hidden - 1)
    def handle_data(self, data):
        if not self.hidden and data.strip(): self.parts.append(data.strip())

urls = {
    'dataset_download': 'https://www.kaggle.com/api/v1/datasets/download/olistbr/brazilian-ecommerce',
    'dataset_metadata': 'https://www.kaggle.com/api/v1/datasets/list/olistbr/brazilian-ecommerce',
    'olist_sobre': 'https://olist.com/sobre-nos/',
    'olist_agentes': 'https://olist.com/agentes/',
    'olist_colaboradores_historico': 'https://olist.com/blog/olist/olist-news/perfil-do-consumidor-no-e-commerce/',
    'navarro_descritiva': 'https://learningstatisticswithr.com/05-descriptives.html',
    'oliveira_visualizacao': 'https://github.com/Rogerio-mack/Visualizacao-de-Dados-em-Python',
    'data_to_viz': 'https://www.data-to-viz.com/',
    'licenca': 'https://creativecommons.org/licenses/by-nc-sa/4.0/',
}
manifest = []
for name, url in urls.items():
    entry = {'name': name, 'url': url, 'access_utc': datetime.now(timezone.utc).isoformat()}
    try:
        with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60) as response:
            payload = response.read()
            entry.update(status=response.status, content_type=response.headers.get('Content-Type'))
        suffix = '.zip' if name == 'dataset_download' else '.html'
        if 'json' in (entry['content_type'] or ''): suffix = '.json'
        path = (DATA if suffix == '.zip' else SOURCES) / (name + suffix)
        path.write_bytes(payload)
        entry.update(bytes=len(payload), sha256=hashlib.sha256(payload).hexdigest(), file=str(path.relative_to(ROOT)))
        if suffix == '.zip':
            with ZipFile(path) as archive:
                for item in archive.infolist():
                    target = (DATA / item.filename).resolve()
                    if not target.is_relative_to(DATA.resolve()): raise ValueError('Unsafe zip path')
                archive.extractall(DATA)
        elif suffix == '.html':
            parser = Text()
            parser.feed(payload.decode('utf-8', errors='replace'))
            (SOURCES / (name + '.txt')).write_text('\n'.join(parser.parts), encoding='utf-8')
        print(name, entry['status'], len(payload))
    except Exception as error:
        entry['error'] = str(error)
        print(name, 'ERROR', str(error))
    manifest.append(entry)
(SOURCES / 'manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding='utf-8')
