import requests
API_URL = "http://localhost:5000"


def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()["payload"]
    return data


def post_data(url, payload):
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.ok
