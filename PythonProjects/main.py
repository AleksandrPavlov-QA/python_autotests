import requests

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
print(response.text)

data_petstore_change = {
  "id": 1,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "naughty_pie",
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
response = requests.post("https://petstore.swagger.io/v2/pet", json = data_petstore_change)
print(response.text)

response = requests.get("https://petstore.swagger.io/v2/pet/1")
print(response.text)
