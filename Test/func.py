import face_recognition
import cv2
import os
import numpy as np

path = '/home/aditya/Desktop/face-recog/Test/Image/Adp'
images = []
classNames = []
myList = os.listdir(path)
print(type(myList))
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

a = np.array()
for i in range(len(images)):
    images[i] = cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB)
    encodingElon = face_recognition.face_encodings(images[i])[0]
    enc = encodingElon.tolist()
    a.append(enc)
    # a.append(str(enc))
    


try:
    with open('/home/aditya/Desktop/face-recog/Test/data/adp.txt', 'x') as f:
            f.write(str(a))
except FileNotFoundError:
    print("The 'docs' directory does not exist")
