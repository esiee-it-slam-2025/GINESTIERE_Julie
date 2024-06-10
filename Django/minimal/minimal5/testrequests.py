import requests

basepath = "http://localhost:8000/"

req = requests.get(basepath + "api")
print(req.text)

donnees = {
    "message": "Hello world"
}
req = requests.post(basepath + "api", data=donnees)
print(req.text)
