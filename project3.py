import requests

url = "https://webexapis.com/v1/people/me"

headers = {
    "Authorization": "Bearer your_access_token_here"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(" User Info:")
    print(data)
else:
    print(f" Error: {response.status_code}")
    print("Details:", response.text)

