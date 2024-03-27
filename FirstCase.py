import requests
import random
import json
import string
from Utilities.api_connection import access_token
from Utilities.resources import ApiResources


#print("Endpoint import",ApiResources.Base_endpoint)
#print(access_token)
base_url = ApiResources.Base_endpoint
headers = {'Authorization': f'Bearer {access_token}'}
#base_url =
def uplifts_filter():
    endpoint = 'https://api.dev.karbon.deltacapita.net/cases?'
    response = requests.get(endpoint + 'uplifts=N/A',headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    count=0
    i=0
    results_s = response_data['results'][i]
    Case_response1 = results_s
    userInput = 'uplifts'
    for i in Case_response1.keys():
        if i==userInput:
            #print(Case_response1.get(i))
            assert Case_response1.get(i)=='N/A'
            print("Case uplift is N/A")










uplifts_filter()