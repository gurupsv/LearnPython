import requests
import json
import jsonpath

url = "https://reqres.in/api/users"

def test_create_new_user():
    print("Starting GET Request!")
    response = requests.get(url)
    assert response.status_code == 200
    print(response)

def test_some_new_case():
    print("New GET request!")
    response = requests.get(url)
    assert response.status_code == 300
    print(response)