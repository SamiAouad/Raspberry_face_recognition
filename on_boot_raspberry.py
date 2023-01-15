import requests
import json
import os
import platform

URL = 'http://192.168.218.236:5000/api/'

def get_credentials(hostname):
    result = requests.post(URL + "devices", json={'name': hostname})
    print(result.status_code)
    data = result.json()
    os.mkdir("data")
    with open('data/device.json', 'w') as f:
        json.dump(data["device"], f)
    with open('data/admin.json', 'w') as f:
        json.dump(data["admin"], f)
        
        
def get_token(email, password):
    data = requests.post(URL + "users/login", json={"email": email, "password": password}).json()
    with open('data/token.json', 'w') as f:
        json.dump(data["token"], f)
    
    
    
    
if not os.path.exists("data"):
    print("machine not registered")
    device_name = platform.node()
    try:
        get_credentials(device_name)
    except:
        print ("an error has occured")
    print ("./data/device.json and ./data/admin.json created")

if not os.path.exists("data/token.json") :
    print("no token found")
    file = open("data/admin.json") 
    data = json.load(file)
    try:
        get_token(data['email'], data['password'])
    except:
        print ('an error has occured while creating token')
    print("./data/token.json created")
