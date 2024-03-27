import requests
import random
import json
import string

import self

from Utilities.api_connection import access_token
from Utilities.resources import ApiResources


#print("Endpoint import",ApiResources.Base_endpoint)
#print(access_token)
base_url = ApiResources.Base_endpoint
headers = {'Authorization': f'Bearer {access_token}'}
#base_url =
def uplifts_NA_filter():
#####################For case uplift as N/A
    endpoint = 'https://api.dev.karbon.deltacapita.net/cases?'
    response = requests.get(endpoint + 'uplifts=N/A',headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    count=0
    i=0
    while i<=5:
        results_s = response_data['results'][i]
        Case_response1 = results_s
        userInput = 'uplifts'
        for j in Case_response1.keys():
            if j == userInput:
                value=Case_response1.get(j)
                expected_value='N/A'
                result=expected_value.find(value)
                try:
                 assert result==0
                except:
                    assert result!=0
                print("Case uplift is N/A")

        print(results_s)
        i=i+1


uplifts_NA_filter()

#####################For case uplift as US
def uplifts_US_filter():
    endpoint = 'https://api.dev.karbon.deltacapita.net/cases?'
    response = requests.get(endpoint + 'uplifts=US', headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    count = 0
    i = 0
    while i <= 20:
        results_s = response_data['results'][i]
        Case_response1 = results_s
        userInput = 'uplifts'
        for j in Case_response1.keys():
            if j == userInput:
                # print(Case_response1.get(i))
                assert Case_response1.get(j) == 'US'
                print("Case uplift is US")

        print(results_s)
        i = i + 1


uplifts_US_filter()