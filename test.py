import face_recognition
import cv2
import numpy as np


imgElon = face_recognition.load_image_file("Image/2.jpg")
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file("Image/adp/1.jpg")
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

# print(imgTest)

faceLoc = face_recognition.face_locations(imgElon)[0]
encodingElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]),
              (faceLoc[1], faceLoc[2]), (255, 0, 0), 2)


faceLocc = face_recognition.face_locations(imgTest)[0]
encodingTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocc[3], faceLocc[0]),
              (faceLocc[1], faceLocc[2]), (255, 0, 0), 2)

results = face_recognition.compare_faces([encodingElon], encodingTest)
print(results)


cv2.imshow("Elon", imgElon)
cv2.imshow("Elonmusl", imgTest)
cv2.waitKey(0)
