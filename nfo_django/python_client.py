import requests

#endpoint = "https://httpbin.org/get"
endpoint = "http://127.0.0.1:8000/api/"
getresponse = requests.get(endpoint, json={"query":"Hello, World!"})

#print(getresponse.text)
print(getresponse.status_code)
#print(getresponse.json()['message'])
print(getresponse.json())