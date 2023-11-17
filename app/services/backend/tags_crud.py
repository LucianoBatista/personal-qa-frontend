import requests


def get_all_tags():
    response = requests.get("http://web:8000/tags/get_all")
    return response
