import requests
import json
import os
import platform

URL = 'http://192.168.218.236:5000/api/'

def get_credentials(hostname):
    result = requests.post(URL + "devices", json={'name': hostname})
    if result.status_code == 200:
        data = result.json()
        os.mkdir("data")
        with open('data/device.json', 'w') as f:
            json.dump(data["device"], f)
        with open('data/admin.json', 'w') as f:
            json.dump(data["admin"], f)
    else:
        print ("An error has occured on the server")
        
        
def get_token(email, password):
    result = requests.post(URL + "users/login", json={"email": email, "password": password})
    if result.status_code == 200:
        data = result.json()
        with open('data/token.json', 'w') as f:
            json.dump(data["token"], f)
    
    
    
    
if not os.path.exists("data"):
    print("machine not registered")
    device_name = platform.node()
    try:
        get_credentials(device_name)
        print ("./data/device.json and ./data/admin.json created")
    except:
        print ("an error has occured")
        exit()
    

if not os.path.exists("data/token.json") :
    print("no token found")
    
    try:
        file = open("data/admin.json") 
        data = json.load(file)
        get_token(data['email'], data['password'])
        print("./data/token.json created")
    except:
        print ('an error has occured while creating token')
        exit()
    
