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
#base_url =
def Refresh():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Refresh",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    ######################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 200
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    Case_response = response.json()
    Case_Id = Case_response['id']
    print(Case_Id)
    if (Case_response['type']) == 'Refresh':
            assert (Case_response['type']) == 'Refresh'
            print("Case with Refresh Case type is created")
    if (Case_response['createReason']) == 'Change of Address':
            assert (Case_response['createReason']) == 'Change of Address'
            print("Case with 'Change of Address' Reason is created")

Refresh()

#Case created with case type = Material Trigger Event
def Material_Trigger_Event():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Material Trigger Event",
  "createReason": "Change of Name",
  "priority": "Yes",
  "uplifts":["N/A"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    #####################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 200
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    Case_response = response.json()
    if (Case_response['type']) == 'Material Trigger Event':
            assert (Case_response['type']) == 'Material Trigger Event'
            print("Case with Material Trigger Event Case type is created")
    if (Case_response['createReason']) == 'Change of Name':
            assert (Case_response['createReason']) == 'Change of Name'
            print("Case with 'Change of Name' Reason is created")

Material_Trigger_Event()

def New():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "New",
  "createReason": "Corporate Actions",
  "priority": "Yes",
  "uplifts":["N/A"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    #####################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 200
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    Case_response = response.json()
    if (Case_response['type']) == 'New':
            assert (Case_response['type']) == 'New'
            print("Case with New Case type is created")
    if (Case_response['createReason']) == 'Corporate Actions':
            assert (Case_response['createReason']) == 'Corporate Actions'
            print("Case with 'Corporate Actions' Reason is created")

New()

def Non_Material_Trigger_Event():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Non-Material Trigger Event",
  "createReason": "SMO Change",
  "priority": "Yes",
  "uplifts":["N/A"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    #####################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 200
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    Case_response = response.json()
    if (Case_response['type']) == 'Non-Material Trigger Event':
            assert (Case_response['type']) == 'Non-Material Trigger Event'
            print("Case with Material Trigger Event Case type is created")
    if (Case_response['createReason']) == 'SMO Change':
            assert (Case_response['createReason']) == 'SMO Change'
            print("Case with 'SMO Change' Reason is created")

Non_Material_Trigger_Event()

def Offboarding():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Offboarding",
  "createReason": "Change of Exchange Details or New Listing",
  "priority": "Yes",
  "uplifts":["N/A"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    #####################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 200
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    Case_response = response.json()
    if (Case_response['type']) == 'Offboarding':
            assert (Case_response['type']) == 'Offboarding'
            print("Case with Material Trigger Event Case type is created")
    if (Case_response['createReason']) == 'Change of Exchange Details or New Listing':
            assert (Case_response['createReason']) == 'Change of Exchange Details or New Listing'
            print("Case with 'Change of Exchange Details or New Listing' Reason is created")

Offboarding()

def Re_open():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Re-open",
  "createReason": "Significant Ownership Change",
  "priority": "Yes",
  "uplifts":["N/A"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    #####################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 200
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    Case_response = response.json()
    if (Case_response['type']) == 'Re-open':
            assert (Case_response['type']) == 'Re-open'
            print("Case with Material Trigger Event Case type is created")
    if (Case_response['createReason']) == 'Significant Ownership Change':
            assert (Case_response['createReason']) == 'Significant Ownership Change'
            print("Case with 'Significant Ownership Change' Reason is created")


Re_open()

def Back_Population_Initial_Load():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Back Population - Initial Load",
  "createReason": "Change of Exchange Details (No longer listed)",
  "priority": "Yes",
  "uplifts":["N/A"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    #####################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 200
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    Case_response = response.json()
    if (Case_response['type']) == 'Back Population - Initial Load':
            assert (Case_response['type']) == 'Back Population - Initial Load'
            print("Case with Material Trigger Event Case type is created")
    if (Case_response['createReason']) == 'Change of Exchange Details (No longer listed)':
            assert (Case_response['createReason']) == 'Change of Exchange Details (No longer listed)'
            print("Case with 'Change of Exchange Details (No longer listed)' Reason is created")

Back_Population_Initial_Load()

def Back_Population_Approved():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Back Population - Approved",
  "createReason": "Change of Regulator or New Regulator",
  "priority": "Yes",
  "uplifts":["N/A"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    #####################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 200
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    Case_response = response.json()
    if (Case_response['type']) == 'Back Population - Approved':
            assert (Case_response['type']) == 'Back Population - Approved'
            print("Case with Material Trigger Event Case type is created")
    if (Case_response['createReason']) == 'Change of Regulator or New Regulator':
            assert (Case_response['createReason']) == 'Change of Regulator or New Regulator'
            print("Case with 'Change of Regulator or New Regulator' Reason is created")

Back_Population_Approved()

def Back_Population_Closed():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Back Population - Closed",
  "createReason": "Change of Regulator Details (No longer regulated)",
  "priority": "Yes",
  "uplifts":["N/A"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    #####################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 200
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    Case_response = response.json()
    if (Case_response['type']) == 'Back Population - Closed':
            assert (Case_response['type']) == 'Back Population - Closed'
            print("Case with Material Trigger Event Case type is created")
    if (Case_response['createReason']) == 'Change of Regulator Details (No longer regulated)':
            assert (Case_response['createReason']) == 'Change of Regulator Details (No longer regulated)'
            print("Case with 'Change of Regulator Details (No longer regulated)' Reason is created")

Back_Population_Approved()

#Refresh_
def CaseType_and_jurisdiction_is_Invalid():
    url = base_url
    print("Post URL:" + url)
    data = {
  "name": "Amazon",
  "type": "Refresh_",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AQl"
}
    response = requests.post(url, json=data,headers=headers)
    assert response.status_code == 400
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("POST Json Response body" + json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Type is Invalid. Jurisdiction is Invalid."

CaseType_and_jurisdiction_is_Invalid()

def CaseType_is_Invalid():
    url = base_url
    print("Post URL:" + url)
    data = {
  "name": "Amazon",
  "type": "Refresh_",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AQ"
}
    response = requests.post(url, json=data,headers=headers)
    assert response.status_code == 400
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("POST Json Response body" + json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Type is Invalid."

CaseType_is_Invalid()

#def CaseType_is_Invalid()
#Refresh0
def RefreshNumber():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Refresh123",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    ######################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 400
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Type is Invalid."

RefreshNumber()

#Re-open#
def Re_open_Has():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Re-open#",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    ######################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 400
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Type is Invalid."

Re_open_Has()

#Refresh!
def RefreshNE():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Refresh!",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    ######################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 400
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Type is Invalid."

RefreshNE()
#Refresh()
def RefreshMBR():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Refresh()",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    ######################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 400
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Type is Invalid."

RefreshMBR()
#Offboarding+
def OffboardingPlus():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Offboarding+",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["N/A"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    #####################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 400
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Type is Invalid."

OffboardingPlus()
#Offb0arding=
def OffboardingEqual():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Offboarding=",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["N/A"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    #####################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 400
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Type is Invalid."

OffboardingEqual()

#Refresh?
def RefreshQ():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Refresh?",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    ######################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 400
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Type is Invalid."

RefreshQ()
#Refresh<>
def RefreshArrowBracket():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Refresh<>",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    ######################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 400
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Type is Invalid."

RefreshArrowBracket()
#Refresh[]
def RefreshSquareBracket():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Refresh[]",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    ######################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 400
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Type is Invalid."

RefreshSquareBracket()
#Refresh{}
def RefreshQbracket():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Refresh{}",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["US"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    ######################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 400
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Type is Invalid."

RefreshQbracket()
#Material Trigger Event@
def Material_Trigger_Event_At():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Material Trigger Event@",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["N/A"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    #####################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 400
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Type is Invalid."

Material_Trigger_Event_At()


#Non_Material_Trigger_Event$
def Non_Material_Trigger_Event_Dolar():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Non-Material Trigger Event$",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["N/A"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    #####################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 400
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Type is Invalid."

Non_Material_Trigger_Event_Dolar()

#New&
def New_And():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "New&",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["N/A"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    #####################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 400
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Type is Invalid."

New_And()

#Back Population - Closed*
def Back_Population_Closed_Star():
    url = base_url
    print("Post URL:"+url)
    data = {
  "name": "Amazon_Auto",
  "type": "Back Population - Closed*",
  "createReason": "Change of Address",
  "priority": "Yes",
  "uplifts":["N/A"],
  "products":["Equity"],
  "customerInternalID": "ADSRFF1235",
  "entityID": "123456",
  "legalEntityName": "Amazon Prime",
  "jurisdiction": "AU"
       }
    #####################
    response = requests.post(url, json=data ,headers=headers)
    assert response.status_code == 400
    json_data=response.json()
    json_str=json.dumps(json_data,indent=4)
    #print("POST Json Response body"+json_str)

    error_response = response.json()
    for response in error_response:
        print(error_response['error'])
        assert error_response['error'] == "Type is Invalid."

Back_Population_Closed_Star()
