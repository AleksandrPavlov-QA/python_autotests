import pytest
import requests

def test_status_code():
    data_petstore = {
  "id": 1,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "sweetie_pie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
    response = requests.put("https://petstore.swagger.io/v2/pet", json = data_petstore)
    assert response.status_code == 200

    response = requests.get("https://petstore.swagger.io/v2/pet/1")  
    assert response.status_code == 200
    
def test_chaeck_responce():
    response = requests.get("https://petstore.swagger.io/v2/pet/1")  
    response = response.json()  
    assert response["name"] == "sweetie_pie"

    