import requests
import webbrowser

result = requests.get('https://en.wikipedia.org/wiki/Baseball')
source = result.text
tokens = source.split('"')

for i, tok in enumerate(tokens):
    if tok.endswith('href=') and i + 1 < len(tokens):
        if tokens[i+1].endswith('html'):
            base = 'https://en.wikipedia.org/wiki/'
            site = 'https://en.wikipedia.org/'
            prot = 'https:'
            url = tokens[i+1]
            if tokens[i+1].startswith('//'):
                # same protocol
                url = prot + tokens[i+1]
            elif tokens[i+1].startswith('/'):
                # same site
                url = site + tokens[i+1]
            elif '://' not in tokens[i+1]:
                url = base + tokens[i+1]
            webbrowser.open(url)
