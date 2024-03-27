import requests
import random
import json
import string


base_url = "https://api.dev.karbon.deltacapita.net/cases"

def IdentifayJurisdiction():
    url  = base_url+"/28129178-bd30-4c7d-b9e9-10ff83dc115d"
    response = requests.get(url)
    assert response.status_code==200

    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    #print("GET response body01 : ", json_str)

    error_response = response.json()
    for response in error_response:
        if (error_response['jurisdiction'])=='AU':
         assert (error_response['jurisdiction'])=='AU'

    data = {
  "jurisdiction": "AQ"
 }
    response = requests.patch(url ,json=data)

IdentifayJurisdiction()

def UpdateJurisdiction():
        url = base_url+"/28129178-bd30-4c7d-b9e9-10ff83dc115d"
        print("Post URL:" + url)
        data = {
               "jurisdiction": "AQ"
               }
        response = requests.patch(url, json=data)
        assert response.status_code == 200

UpdateJurisdiction()