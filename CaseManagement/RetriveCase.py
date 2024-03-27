import json
import csv
import requests
import requests
import random
import json
import string
from Utilities.api_connection import access_token
from Utilities.resources import ApiResources


#print("Endpoint import",ApiResources.Base_endpoint)
print(access_token)
base_url = ApiResources.Base_endpoint
headers = {'Authorization': f'Bearer {access_token}'}


def From():
    endpoint = 'https://api.dev.karbon.deltacapita.net/cases?'
    response = requests.get(endpoint + 'jurisdiction=AQ', headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    data = json.dumps(response_data, indent=4)
    # print(data)
    resultCount = response.json()
    for response in resultCount:
        print("Number of Cases having AQ as jurisdiction are", resultCount['resultCount'])
        break

    endpoint = 'https://api.dev.karbon.deltacapita.net/cases?'
    response = requests.get(endpoint + 'uplifts=US', headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    data = json.dumps(response_data, indent=4)
    # print(data)
    resultCount_US = response.json()
    for response in resultCount:
        print("Number of Cases having US as uplifts are", resultCount_US['resultCount'])
        break
    ############
    endpoint = 'https://api.dev.karbon.deltacapita.net/cases?'
    response = requests.get(endpoint + 'uplifts=N/A', headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    data = json.dumps(response_data, indent=4)
    # print(data)
    resultCount_NA = response.json()
    for response in resultCount:
        print("Number of Cases having N/A as uplifts are", resultCount_NA['resultCount'])
        break
    ###########
    endpoint = 'https://api.dev.karbon.deltacapita.net/cases?'
    response = requests.get(endpoint + 'activecase=1', headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    data = json.dumps(response_data, indent=4)
    # print(data)
    resultCount_TotalCases = response.json()
    for response in resultCount:
        print("Number of Active cases are", resultCount_TotalCases['resultCount'])
        break

    # assert resultCount_TotalCases['resultCount']>(resultCount_US['resultCount']+resultCount_NA['resultCount'])
    # print("fine")

    endpoint = 'https://api.dev.karbon.deltacapita.net/cases?'
    response = requests.get(endpoint + 'activecase=0', headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    data = json.dumps(response_data, indent=4)
    #print(data)
    for items in response_data:
        print("Number of Inactive cases are", resultCount_TotalCases['resultCount'])
        break



From()