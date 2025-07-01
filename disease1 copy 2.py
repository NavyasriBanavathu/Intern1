import requests

url = "https://disease.sh/v3/covid-19/countries"

response = requests.get(url)

data = response.json()

if isinstance(data, list) and len(data) > 0:
    first_country = data[0]
    print("Country:", first_country["country"])
    print("COVID cases:", first_country["cases"])
else:
    print("No data available or unexpected response format.")
