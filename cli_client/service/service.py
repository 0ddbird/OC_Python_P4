import requests

API_URL = "http://localhost:5000"


def get_data(url):
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()["payload"]
    return data


def post_data(url, payload=None):
    headers = {"Content-Type": "application/json"}
    if payload:
        response = requests.post(url, json=payload, headers=headers)
    else:
        response = requests.post(url)
    response.raise_for_status()
    return response.ok


def patch_data(url, payload=None):
    headers = {"Content-Type": "application/json"}
    print(f"Request URL: {url}")
    print(f"Request payload: {payload}")

    if payload:
        response = requests.patch(url, json=payload, headers=headers)
    else:
        response = requests.patch(url, headers=headers)

    response.raise_for_status()
    return response.ok
