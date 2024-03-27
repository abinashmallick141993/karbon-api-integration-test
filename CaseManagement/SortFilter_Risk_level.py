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
def riskLevel_Low_filter():
#####################For case uplift as N/A
    endpoint = 'https://api.dev.karbon.deltacapita.net/cases?'
    response = requests.get(endpoint + 'riskLevel=Low',headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    count=0
    i=0
    while i<=20:
        results_s = response_data['results'][i]
        Case_response1 = results_s
        userInput = 'riskLevel'
        for j in Case_response1.keys():
            if j == userInput:
                # print(Case_response1.get(i))
                assert Case_response1.get(j) == 'Low'
                print("Case riskLevel is Low")

        print(results_s)
        i=i+1


riskLevel_Low_filter()

#####################For case uplift as US
def riskLevel_Standard_filter():
    endpoint = 'https://api.dev.karbon.deltacapita.net/cases?'
    response = requests.get(endpoint + 'riskLevel=Standard', headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    count = 0
    i = 0
    while i <= 20:
        results_s = response_data['results'][i]
        Case_response1 = results_s
        userInput = 'riskLevel'
        for j in Case_response1.keys():
            if j == userInput:
                # print(Case_response1.get(i))
                assert Case_response1.get(j) == 'Standard'
                print("Case riskLevel is Standard")

        print(results_s)
        i = i + 1


riskLevel_Standard_filter()

def riskLevel_Heightened_filter():
    endpoint = 'https://api.dev.karbon.deltacapita.net/cases?'
    response = requests.get(endpoint + 'riskLevel=Heightened', headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    count = 0
    i = 0
    while i <= 20:
        results_s = response_data['results'][i]
        Case_response1 = results_s
        userInput = 'riskLevel'
        for j in Case_response1.keys():
            if j == userInput:
                # print(Case_response1.get(i))
                assert Case_response1.get(j) == 'Heightened'
                print("Case riskLevel is Heightened")

        print(results_s)
        i = i + 1


riskLevel_Heightened_filter()