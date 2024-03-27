import json
import csv
import requests
import requests
import random
import json
import string

from Functions.DateTime import DateAndTime
from Utilities.api_connection import access_token
from Utilities.resources import ApiResources


#print("Endpoint import",ApiResources.Base_endpoint)
#print(access_token)
headers = {'Authorization': f'Bearer {access_token}'}
base_url = ApiResources.Base_endpoint

def Create_a_Case():
    url = base_url
    print("Post URL:" + url)
    data ={
  "name": "Facebook",
  "type": "New",
  "legalEntityName": "META",
  "jurisdiction": "GB",
  "createReason": [
    "Change of Address","Change of Name"
  ],
  "priority": "Yes",
  "uplifts": [
    "US"
  ],
  "products": [
    "Equity"
  ],
  "targetDueDate": "21-03-2026",
  "customerInternalID": "CustIntID987",
  "entityID": "null"
  }
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    # print("POST Json Response body"+json_str)

    Case_response = response.json()
    Case_Id = Case_response['id']
    #print(Case_Id)
    if (Case_response['status']) == 'Created':
        assert (Case_response['status']) == 'Created'
        #print("Case with status Created")
    if (Case_response['name']) == 'Facebook':
        assert (Case_response['name']) == 'Facebook'
        #print("Case with Facebook name is created1")
    if (Case_response['type']) == 'New':
        assert (Case_response['type']) == 'New'
        #print("Case with New Case type is created2")
    if (Case_response['legalEntityName']) == 'Facebook Limites':
        assert (Case_response['legalEntityName']) == 'Facebook Limites'
        #print("Case with legalEntityName is created3")
    if (Case_response['jurisdiction']) == 'GB':
        assert (Case_response['jurisdiction']) == 'GB'
        #print("Case with New Case type is created4")
    if (Case_response['priority']) == 'Yes':
        assert (Case_response['priority']) == 'Yes'
        #print("Case with priority is created6")
    if (Case_response['targetDueDate']) == '21-03-2026':
        assert (Case_response['targetDueDate']) == '21-03-2026'
        #print("Case with targetDueDate is created7")
    if (Case_response['customerInternalID']) == 'CustIntID987':
        assert (Case_response['customerInternalID']) == 'CustIntID987'
        #print("Case with customerInternalID is created8")

    for j in Case_response.keys():
        if j == 'uplifts':
            assert ['US']==(Case_response.get(j))
            #print("Case uplift is US")
    for j in Case_response.keys():
        if j == 'createReason':
            assert ['Change of Address','Change of Name']==(Case_response.get(j))
            #print("Case createReason is Change of Address,Change of Name")
    for j in Case_response.keys():
        if j == 'products':
            assert ['Equity']==(Case_response.get(j))
            #print("Case products is Equity")
    if (Case_response['createDateTime']) == DateAndTime():
        assert (Case_response['createDateTime']) == DateAndTime
        print("Case with createDateTime is created")
        #print(DateAndTime())
    assert (Case_response['createdBy'])==None
    assert (Case_response['updatedBy'])==None
    assert (Case_response['updatedDateTime'])==None
    assert (Case_response['riskLevel'])==None
    assert (Case_response['riskOverride'])==None
    assert (Case_response['riskOverrideReason'])==None
    assert (Case_response['lastReviewDate'])==None
    assert (Case_response['nextReviewDate'])==None
    assert (Case_response['completeToPolicy'])==None
    assert (Case_response['nextReviewDateOverride'])==None
    assert (Case_response['nextReviewDateOverrideReason'])==None





Create_a_Case()