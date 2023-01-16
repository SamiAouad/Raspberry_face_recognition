import nfc
import requests
import signal

URL = 'http://192.168.218.236:8000/api/'



def signal_handler(signal, frame):
    global interupted
    interrupted = True


def on_startup(targets):
    print("Listening for NFC tags...")
    return targets

def on_connect(tag):
    print("Tag detected:")
    print("ID: " + str(tag.identifier.hex()))
    print("Type: " + tag.type)
    requests.post(URL + "nfc/login", json={'id': str(tag.identifier.hex())})
    return str(tag.identifier.hex())


signal.signal(signal.SIGINT, signal_handler)

clf = nfc.ContactlessFrontend('usb')
while True:
    try:
        test = clf.connect(rdwr={'on-connect': on_connect}, device='/dev/bus/usb/001/007')

    except Exception as e:
        print(e)
    if interupted:
        print('exiting')
        break