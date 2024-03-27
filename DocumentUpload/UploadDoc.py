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

def Create_a_CaseOne():
    url = base_url
    #print("Post URL:" + url)
    data ={
  "name": "Facebook",
  "type": "New",
  "legalEntityName": "META",
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
  "customerInternalID": "CustIntID987",
  "entityID": "null"
  }
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    # print("POST Json Response body"+json_str)
    global Case_id
    Case_response = response.json()
    Case_id = Case_response['id']
    print(Case_id)
    return Case_id



case_id=Create_a_CaseOne()

Case_id=case_id
def Get_Details_For_Doc_Upload():
  upload_url = base_url + "/" + Case_id + "/documents"
  data={
    "username": "Abinash.txt",
    "fileName": "Presentation3.txt",
    "metadata":{
                "category": "abcd",
                "proofof": "vfvf",
                "expirationDate": "12-12-2026",
                "createdBy": "Abinash"
            }
      }

  response = requests.post(upload_url,json=data,headers=headers)
  post_response=response.json()
  #print(post_response)
  #global presigned_url
  presigned_url=post_response['presigned_url']
  #global fileId
  fileId=post_response['fileId']
  #global createdDateTime
  createdDateTime=post_response['createdDateTime']
  #print(presigned_url,createdDateTime,fileId)
  return presigned_url,fileId,createdDateTime


Get_Details_For_Doc_Upload()




def Upload_Put_Doc(presigned_url,fileId,createdDateTime):
  print(v,"*")
  print(fileId)
  print(createdDateTime)
  head = {'x-amz-meta-fileId':'{fileId}',
          'x-amz-meta-createdDateTime':'{createdDateTime}',
          'x-amz-meta-category':'{abcd}',
          'x-amz-meta-proofof':'{vfvf}',
          'x-amz-meta-expirationDate':'{12-12-2024}',
          'x-amz-meta-createdBy':'{Abinash}',
          }
  url = presigned_url
  response = requests.put(url,headers=head)
  print(response.status_code)

Upload_Put_Doc(presigned_url,fileId,createdDateTime)