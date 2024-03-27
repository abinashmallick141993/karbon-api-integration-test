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
#print(access_token)
base_url = ApiResources.Base_endpoint
headers = {'Authorization': f'Bearer {access_token}'}

#Get list of products
#Create two products
#Update product two
#Create a case and add one product
#Update the case and add second product
#delete product one
#validate that the product one got auto deleted from the case
#Get product one should fail
#Get product should pass
#delete product two
def Get_Product():
    endpoint = 'https://api.dev.karbon.deltacapita.net/cases'
    response = requests.get(endpoint + '/products', headers=headers)
    try:
        assert response.status_code == 200
        response_data = response.json()
        data = json.dumps(response_data, indent=4)
        print(data)
    except Exception as e:
        print(e)


Get_Product()