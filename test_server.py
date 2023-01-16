import requests

URL = 'http://192.168.218.236:8000/api/'

result = requests.post(URL + "nfc/login", json={'email': "samiaouad7@gmail.com", "password": "1234"})

print (result.json())