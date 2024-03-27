import requests
import random
import json
import string

from Functions.DateTime import DateAndTime
from Utilities.api_connection import access_token
from Utilities.resources import ApiResources


#print(access_token)
base_url = ApiResources.Base_endpoint
headers = {'Authorization': f'Bearer {access_token}'}

def CreateCaseForComment():
    url = base_url
    #print("Post URL:"+url)
    data = {
  "name": "A!rbus",
  "type": "Refresh",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "AirBu$",
  "jurisdiction": "AU"
       }
    ######################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 200
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    Case_response = response.json()
    global case_Id
    case_Id = Case_response['id']
    #print(Case_Id)
    return case_Id

Case_id = CreateCaseForComment()

def GetCaseDetailsEndpoint():
    New1 = Case_id
    #print(New1)
    response = requests.get(base_url + "/" + New1, headers=headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    # print("Get Json Response body"+json_str)
    global case_url
    case_url = base_url + "/" + New1
    print(response)
    return case_url
case_url = GetCaseDetailsEndpoint()

def AddComment():
    url=case_url+'/comments'
    print(url)
    comment={
    "comment": "你好'cvvv89",
    "scope": "Comment added By BatManxcvv"
    }
    response=requests.post(url,json=comment,headers=headers)
    res=response.status_code
    print(res)
    print(response)
AddComment()


