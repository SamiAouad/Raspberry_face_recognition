import cv2
import requests
import numpy as np

def surface(face_location):
    top, right, bottom, left = face_location
    return abs(bottom - top) + abs(left - right)


def one_face_detection(img):
    # cropped_faces = []
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(img, 1.1, 4)
    if len (faces) > 0:
        closest_face_location = max(faces, key=surface)
        x, y, w, h = closest_face_location
        return img[y:y+h, x:x+w]
    return None


def record():
    capture = cv2.VideoCapture(0)
    open_door = False

    while not open_door:
        _, img = capture.read()
        cropped_face = one_face_detection(img)
        url = 'http://localhost:8000/recognize'
        # myobj = {'key': cropped_face}
        if cropped_face is not None:
            _, img_encoded = cv2.imencode('.jpg', cropped_face)
            file = {'file': ('image.jpg', img_encoded.tobytes())}
            open_door = requests.post(url, files = file).json()
        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    capture.release()
    cv2.destroyAllWindows()
    

record() 