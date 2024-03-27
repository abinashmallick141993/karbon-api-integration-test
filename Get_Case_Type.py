import json

import requests

response = requests.get('https://api.dev.karbon.deltacapita.net/mockcases/caseTypes')
print(response.text)
print(type(response.text))
disc_response = json.loads(response.text)
print(disc_response[0])
assert disc_response[0] == 'New'
print(disc_response[1])
assert disc_response[1] == 'Refresh'
print(disc_response[2])
assert disc_response[2] == 'Rework'
print(disc_response[3])
assert disc_response[3] == 'Material Trigger Event'
print(disc_response[4])
assert disc_response[4] == 'Screening Escalation'
print(disc_response[5])
assert disc_response[5] == 'Back Population - Initial Load'
print(disc_response[6])
assert disc_response[6] == 'Back Population - Approved'
print(disc_response[7])
assert disc_response[7] == 'Back Population - Closed'
print(disc_response[8])
assert disc_response[8] == 'Non Material Trigger Event'
assert response.status_code==200
print("Get CaseType Status code =",response.status_code)