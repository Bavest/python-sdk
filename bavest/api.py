import requests


def post(url, headers, body):
    response = requests.post(url, headers=headers, json=body)
    return response


def get(url, headers):
    response = requests.get(url, headers=headers)
    return response
