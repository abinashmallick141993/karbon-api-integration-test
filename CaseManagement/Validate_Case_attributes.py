import json
import configparser
#from Utilities.resources import *
from Utilities.configurations import *
import requests

config = getconfig()
print('##########################')
#response = requests.get('https://api.dev.karbon.deltacapita.net/cases/37fab691-abd3-4955-aa44-b6070630b13f')
response = requests.get('endpoint')
print(response.text)
assert response.status_code==200
attributes = json.loads(response.text)
json_response = response.json()
print(type(json_response))
print(response.headers)
print(type(response.headers))
if response.headers['Content-Type'] == 'application/json':
    print('Content type is working as expected')
else:
    print('Content type is wrong')
assert json_response['id']==  '37fab691-abd3-4955-aa44-b6070630b13f'

assert json_response['legalEntityName']== 'Tesco'

assert json_response['entityID']==None #Expected value is Null

assert json_response['jurisdiction']== 'UK'

assert json_response['legalEntityName']== 'Tesco'




