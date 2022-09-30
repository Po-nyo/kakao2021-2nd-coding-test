import json
import requests
from config import app_properties


def get(url, **kwargs):
    headers, params = kwargs.get('headers', {}), kwargs.get('params', None)
    return requests.get(app_properties.BASE_URL + url, headers=headers, params=params).json()


def put(url, **kwargs):
    headers, data = kwargs.get('headers', {}), json.dumps(kwargs.get('data', None))
    return requests.put(app_properties.BASE_URL + url, headers=headers, data=data).json()


def post(url, **kwargs):
    headers, data = kwargs.get('headers', {}), json.dumps(kwargs.get('data', None))
    return requests.post(app_properties.BASE_URL + url, headers=headers, data=data).json()
