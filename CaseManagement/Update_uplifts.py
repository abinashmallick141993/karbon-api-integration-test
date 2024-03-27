import requests
import random
import json
import string
from Utilities.api_connection import access_token
from Utilities.resources import ApiResources


print(access_token)
base_url = ApiResources.Base_endpoint
headers = {'Authorization': f'Bearer {access_token}'}

def New():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Google",
  "type": "New",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Alfabet.co",
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
    if (Case_response['type']) == 'New':
            assert (Case_response['type']) == 'Refresh'
            print("Case with Refresh Case type is created")
    return case_Id

Case_id = New()


New1 = Case_id
print(New1)
response = requests.get(base_url +"/"+ New1, headers=headers)
json_data=response.json()
json_str=json.dumps(json_data,indent=4)
print("Get Json Response body"+json_str)
case_url = print("Get Case end point: ",base_url +"/"+ New1)
print(response)
New_url=base_url+"/"+New1
# for item in response:
#     print(item['resultCount'])
#first_case = response['results'][1]
#print(first_case)
def Update_upliftsOne():
    url = New_url
    print("Patch_url: "+url)
    data1= {
          "legalEntityName": "Google.Browser",
          "jurisdiction": "US",
          "name": "CORS Security",
          "type": "New",
          "createReason": ["Change of Name"],
          "priority": "No",
          "uplifts": ["N/A","US"],
          "products": ["FX","Bond"],
          "status": "In Progress",
          "entityID":"US1234567890",
          "customerInternalID": "ID123",
          "riskLevel": "Standard",
          "riskOverride":"Low",
          "riskOverrideReason":"reason for override",
          "nextReviewDate": "04-03-2028",
          "nextReviewDateOverride": "02-2-2026",
          "nextReviewDateOverrideReason": "NRD override reason",
          "targetDueDate": "",
          "completeToPolicy":"",
          "assignee":"Abinash"
          }

    product_update_response=requests.patch(url, json=data1 ,headers=headers)
    assert product_update_response.status_code==200
    print(product_update_response.status_code)
    Product_update_json_data=product_update_response.json()
    json_str1 = json.dumps(Product_update_json_data, indent=4)
    print(json_str1)

    Case_response = response.json()
    if (Case_response['uplifts']) == '"FX","Bond"':
        assert (Case_response['uplifts']) == '"FX","Bond","CTF","Equity"'

Update_upliftsOne()

def Update_upliftsTwo():
    url2 = New_url
    print("Patch_url: "+url2)
    data2= {
          "legalEntityName": "Google.Map",
          "jurisdiction": "US",
          "name": "CORS Security",
          "type": "Rework",
          "createReason": ["Change of Name"],
          "priority": "No",
          "uplifts": ["N/A"],
          "products": ["FX","Bond"],
          "status": "In Progress",
          "entityID":"US1234567890",
          "customerInternalID": "ID123",
          "riskLevel": "Heightened",
          "riskOverride":"Heightened",
          "riskOverrideReason":"reason for override",
          "nextReviewDate": "04-03-2028",
          "nextReviewDateOverride": "02-2-2026",
          "nextReviewDateOverrideReason": "NRD override reason",
          "targetDueDate": "",
          "completeToPolicy":"",
          "assignee":"Abinash_M"
          }

    product_update_response2=requests.patch(url2, json=data2 ,headers=headers)
    assert product_update_response2.status_code==200
    print(product_update_response2.status_code)
    Product_update_json_data2=product_update_response2.json()
    json_str2 = json.dumps(Product_update_json_data2, indent=4)
    print(json_str2)

Update_upliftsTwo()

