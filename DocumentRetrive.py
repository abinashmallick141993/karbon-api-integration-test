import json

import requests

req = requests.get('https://api.dev.karbon.deltacapita.net/cases/e4246728-2b75-49c6-86f5-0bded4e6ffa4/documents')
data = req.json()
print(data)

for doc_data in data:
    print(doc_data['fileName'])
    assert doc_data['fileName']=='testfile30.pdf'





