import cv2
import matplotlib.pyplot as plt
import dlib
from imutils import face_utils
font = cv2.FONT_HERSHEY_SIMPLEX

pythonpath="/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages"
cascPath = pythonpath+"/cv2/data/haarcascade_frontalcatface_extended.xml"
eyePath = pythonpath+"/cv2/data/haarcascade_eye.xml"
smilePath = pythonpath+"/cv2/data/haarcascade_smile.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
eyeCascade = cv2.CascadeClassifier(eyePath)
smileCascade = cv2.CascadeClassifier(smilePath)

img=cv2.imread("/Users/guruprasadsv/PycharmProjects/LearnPython/Advanced/_DSC4951.jpg",3)

print(img.shape)


faces = faceCascade.detectMultiScale(
img,
scaleFactor=1.2,
minNeighbors=1,
flags=cv2.CASCADE_SCALE_IMAGE
)
# For each face
for (x, y, w, h) in faces:
    # Draw rectangle around the face
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 3)

cv2.imshow("MyImage", img)

#plt.figure(figsize=(12,8))
#plt.imshow(img,cmap="gnuplot")
#plt.show()