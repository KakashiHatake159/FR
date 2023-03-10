from os import listdir
from PIL import Image as img

import face_recognition

from cv2 import VideoCapture, imshow ,imwrite

import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(str):
    engine.say(str)
    engine.runAndWait()
    pass

path ='\\face_images'
path1 ='\\cam_images'


def loadimg(path):
    imgset=listdir(path)
    imglist=[]
    for i in imgset:
        imglist.append(path+'\\'+i)
    
    return imglist

imgs=loadimg(path)

cport=0
cam=VideoCapture(cport)

result,camImage=cam.read()
if result:
    imwrite(path1+'\\'+"hi.jpg",camImage)
else:
    print("again you bot")
    
camimg=face_recognition.load_image_file(path1+"\\"+"hi.jpg")
    
for i in imgs:
        
    dataimg=face_recognition.load_image_file(i)
    l=i
    k=l.split("\\")
    f=k[len(k)-1]
    name=f
    try:
        camimg_encode= face_recognition.face_encodings(camimg)[0]   
        dataimg_encode= face_recognition.face_encodings(dataimg)[0]
        results = face_recognition.compare_faces([camimg_encode], dataimg_encode)
        c=0
        if results:
            
            speak(f"hi, {name} ,sir")
            c+=1
            break

        elif c==0:
            speak("sorry your data is not found in dataset")
            
    except IndexError as e:
        print(e)
        speak("please. take again")
        break
