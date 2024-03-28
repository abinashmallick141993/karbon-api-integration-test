import requests
import random
import json
import string
import os
from Functions.DateTime import DateAndTime
from Utilities.api_connection import access_token
from Utilities.resources import ApiResources
#from Sample_Documents import

headers = {'Authorization': f'Bearer {access_token}'}
base_url = ApiResources.Base_endpoint

def Create_a_CaseOne():
    url = base_url
    data ={
  "name": "Youtube",
  "type": "New",
  "legalEntityName": "Alf@bet",
  "jurisdiction": "GB",
  "createReason": [
    "Change of Address"
  ],
  "priority": "Yes",
  "uplifts": [
    "US"
  ],
  "products": [
    "Equity"
  ],
  "targetDueDate": "21-03-2026",
  "customerInternalID": "CustIntID988",
  "entityID": "null"
  }
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    global Case_id
    Case_response = response.json()
    Case_id = Case_response['id']
    print(Case_id)
    return Case_id


def Get_Details_For_Doc_Upload(Case_id):
  upload_url = base_url + "/" + Case_id + "/documents"
  data={
    "username": "Abinash",
    "fileName": "Santaasdfg.txt",
    "metadata":{
                "category": "abcd",
                "proofof": "vfvf",
                "expirationDate": "12-12-2026",
                "createdBy": "Abinash"
            }
      }

  response = requests.post(upload_url,json=data,headers=headers)
  post_response=response.json()
  presigned_url = post_response.get('presigned_url')
  fileId = post_response.get('fileId')
  createdDateTime = post_response.get('createdDateTime')


  return presigned_url, fileId, createdDateTime

def Upload_Put_Doc(presigned_url,fileId,createdDateTime):
  files = 'C:/Users/AbinashMallick/PycharmProjects/pythonProjectAPI/Sample_Documents/Santaasdfg.txt'
  bin = open(files, 'rb')
  content = bin.read()
  bin.close()
  head = {
      'x-amz-meta-fileId': fileId,
      'x-amz-meta-createdDateTime': createdDateTime,
      'x-amz-meta-category': 'abcd',
      'x-amz-meta-proofof': 'vfvf',
      'x-amz-meta-expirationDate': '12-12-2026',
      'x-amz-meta-createdBy': 'Abinash',
  }
  url = presigned_url
  response = requests.put(url, headers=head, data=content)

  try:
      json_data = response.json()
      json_str = json.dumps(json_data, indent=4)
      print("POST Json Response body" + json_str)
  except Exception as e:
      print(e)


Case_id = Create_a_CaseOne()
presigned_url, fileId, createdDateTime = Get_Details_For_Doc_Upload(Case_id)
response = Upload_Put_Doc(presigned_url, fileId, createdDateTime)
print("Response:", response)


