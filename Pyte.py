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
def test_uplifts_filter():
    endpoint = 'https://api.dev.karbon.deltacapita.net/cases?'
    response = requests.get(endpoint + 'uplifts=N/A',headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    count=0
    i=0
    while i<=5:
        results_s = response_data['results'][i]
        print(results_s)
        i=i+1










test_uplifts_filter()