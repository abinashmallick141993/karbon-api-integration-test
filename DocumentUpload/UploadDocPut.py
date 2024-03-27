import requests
import random
import json
import string
import os
from Functions.DateTime import DateAndTime
from Utilities.api_connection import access_token
from Utilities.resources import ApiResources

headers = {'Authorization': f'Bearer {access_token}'}
base_url = ApiResources.Base_endpoint

# def Create_a_CaseOne():
#     url = base_url
#     data ={
#   "name": "Facebook",
#   "type": "New",
#   "legalEntityName": "META",
#   "jurisdiction": "GB",
#   "createReason": [
#     "Change of Address"
#   ],
#   "priority": "Yes",
#   "uplifts": [
#     "US"
#   ],
#   "products": [
#     "Equity"
#   ],
#   "targetDueDate": "21-03-2026",
#   "customerInternalID": "CustIntID987",
#   "entityID": "null"
#   }
#     response = requests.post(url, json=data, headers=headers)
#     assert response.status_code == 200
#     json_data = response.json()
#     json_str = json.dumps(json_data, indent=4)
#     global Case_id
#     Case_response = response.json()
#     Case_id = Case_response['id']
#     print(Case_id)
#     return Case_id

##########
def Create_a_CaseOne():
    global Case_id
    Case_id='5407b567-19f0-4c23-85df-7ce4f7e93b49'
    return Case_id


def Get_Details_For_Doc_Upload(Case_id):
  upload_url = base_url + "/" + Case_id + "/documents"
  data={
    "username": "Abinash",
    "fileName": "Santa.txt",
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
  files = open('C:/Users/AbinashMallick/Downloads/Santa.txt')
  head = {'x-amz-meta-fileId':'{fileId}',
          'x-amz-meta-createdDateTime':'{createdDateTime}',
          'x-amz-meta-category':'{abcd}',
          'x-amz-meta-proofof':'{vfvf}',
          'x-amz-meta-expirationDate':'{12-12-2024}',
          'x-amz-meta-createdBy':'{Abinash}',
          }
  url = presigned_url
  #print(url)
  print(fileId)
  print(createdDateTime)
  response = requests.put(url,files,headers=head)
  print(response.status_code)
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


