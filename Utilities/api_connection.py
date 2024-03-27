import requests
# from requests_oauthlib import OAuth2Session
# OAuth2 Configuration
client_id = '6kjogklf4s4370ebpre78mfg79'
client_secret = '12biur7mk3f6q1jc70en2li20hkstc6emnkelvsi0gm4hhrrpf09'
token_url = 'https://auth.dev.karbon.deltacapita.net/oauth2/token'
# Requesting access token using client credentials grant type
token_data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
}
# Sending a POST request to get the access token
response = requests.post(token_url, data=token_data)
if response.status_code == 200:
    # Extracting the access token from the response
    access_token = response.json()['access_token']
    #print(access_token)
    # Example API endpoint
    api_endpoint = 'https://api.dev.karbon.deltacapita.net/cases/products'
    # Making a request to the API endpoint with the access token
    headers = {'Authorization': f'Bearer {access_token}'}
    api_response = requests.get(api_endpoint, headers=headers)
    print("API Response:")
    #print(api_response.json())
    # Processing the API response
    if api_response.status_code == 200:
        print("Successfully connected to the API endpoint.")
        data = api_response.json()
        # Process the response data as needed
    else:
        print("Failed to connect to the API endpoint. Error:", api_response.status_code)
        # Handle error
else:
    print("Failed to obtain access token. Error:", response.status_code)
    # Handle error
