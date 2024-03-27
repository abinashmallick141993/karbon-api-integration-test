import requests
import random
import json
import string
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

#base_url = "https://api.dev.karbon.deltacapita.net/cases"
def Optional_fields_():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Facebook",
  "type": "Back Population - Initial Load",
  "createReason": "",
  "priority": "",
  "uplifts":[],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "WEN",
  "legalEntityName": "家",
  "jurisdiction": "UG"
  }
    response = requests.post(url, headers=headers, json=data )
    assert response.status_code == 200
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)


Optional_fields_()

def Name_Is_Mandatory():
    url = base_url
    print("Post URL:" + url)
    data = {
  "name": "",
  "type": "Back Population - Initial Load",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "WEN",
  "legalEntityName": "家@",
  "jurisdiction": "UG"
}
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 400
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("POST Json Response body" + json_str)


Name_Is_Mandatory()

def Type_Is_Mandatory():
    url = base_url
    print("Post URL:" + url)
    data = {
  "name": "Tesla",
  "type": "",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "Automated_ADSRFF1235",
  "entityID": "WEN",
  "legalEntityName": "家#",
  "jurisdiction": "UG"
}
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 400
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("POST Json Response body" + json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Value for Type is Mandatory."

Type_Is_Mandatory()

def LegalEntityName_Is_Mandatory():
    url = base_url
    print("Post URL:" + url)
    data = {
  "name": "Tesla",
  "type": "Back Population - Initial Load",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Bond"],
  "customerInternalID": "Automated_ADSRFF1200",
  "entityID": "WEN",
  "legalEntityName": "",
  "jurisdiction": "UG"
}
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 400
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("POST Json Response body" + json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Value for LegalEntityName is Mandatory"

LegalEntityName_Is_Mandatory()


def Jurisdiction_Is_Mandatory():
    url = base_url
    print("Post URL:" + url)
    data = {
  "name": "Tesla",
  "type": "Back Population - Initial Load",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["CTF"],
  "customerInternalID": "Automated_ADSRFF1235",
  "entityID": "WEN",
  "legalEntityName": "Tesla & Motors, Inc.",
  "jurisdiction": ""
}
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 400
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("POST Json Response body" + json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Value for Jurisdiction is Mandatory."

Jurisdiction_Is_Mandatory()


def LegalEntityName_is_MandatoryJurisdiction_is_Mandatory():
    url = base_url
    print("Post URL:" + url)
    data = {
  "name": "Netflix",
  "type": "Back Population - Initial Load",
  "createReason": "Change of Address",
  "priority": "No",
  "uplifts":["N/A"],
  "products":["Equity"],
  "customerInternalID": "Automated_ADSRFF1243",
  "entityID": "WEN",
  "legalEntityName": "",
  "jurisdiction": ""
}
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 400
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    #print("POST Json Response body" + json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Value for LegalEntityName is MandatoryValue for Jurisdiction is Mandatory."

LegalEntityName_is_MandatoryJurisdiction_is_Mandatory()


def Jurisdiction_is_Invalid():
    url = base_url
    print("Post URL:" + url)
    data = {
  "name": "Amazon",
  "type": "Refresh",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AQl"
}
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 400
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    #print("POST Json Response body" + json_str)

    error_response = response.json()
    #print(type(error_response))
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Jurisdiction is Invalid."

Jurisdiction_is_Invalid()

def Jurisdiction_is_LowerCase():
    url = base_url
    print("Post URL:" + url)
    data = {
  "name": "Amazon",
  "type": "Refresh",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "Cn"
}
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 400
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    #print("POST Json Response body" + json_str)

    error_response = response.json()
    #print(type(error_response))
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Jurisdiction is Invalid."

Jurisdiction_is_LowerCase()

def Jurisdiction_is_LowerCase():
    url = base_url
    print("Post URL:" + url)
    data = {
  "name": "Amazon",
  "type": "Refresh",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "Cn"
}
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 400
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    #print("POST Json Response body" + json_str)

    error_response = response.json()
    #print(type(error_response))
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Jurisdiction is Invalid."

Jurisdiction_is_LowerCase()

def Name_With_Numerics_Char():
    url = base_url
    print("Post URL:" + url)
    data = {
  "name": "[{(1+2-3*0/5=6_7)}]",
  "type": "Back Population - Initial Load",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "WEN",
  "legalEntityName": "家@",
  "jurisdiction": "UG"
}
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    #print("POST Json Response body" + json_str)
    print("Case name with numeric values and brackets got created")


Name_With_Numerics_Char()

def Name_With_Special_Char():
    url = base_url
    print("Post URL:" + url)
    data = {
  "name": "abc!@#$%^&<?>,.;:'",
  "type": "Back Population - Initial Load",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "WEN",
  "legalEntityName": "家@",
  "jurisdiction": "UG"
}
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    #print("POST Json Response body" + json_str)
    print("Case name with minimum three characters got created")


Name_With_Special_Char()

def Name_at_least_3_alphanumeric():
    url = base_url
    print("Post URL:" + url)
    data = {
  "name": "!@#$%^&<?>,.;:'",
  "type": "Back Population - Initial Load",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "WEN",
  "legalEntityName": "家@",
  "jurisdiction": "UG"
}
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 400
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    #print("POST Json Response body" + json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Value for Name is Mandatory and must have at least 3 alphanumeric characters."


Name_With_Special_Char()

