#Program to detect faces in a given image

#jayneil.dalal@gmail.com

#!/usr/bin/python
import cv  #import the openCV lib to python
a=cv.LoadImage("/home/ashwini/Documents/driving_python/image_processing/d.jpg")
print(a)
cv.NamedWindow("Original Image", cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("Original Image", a)
cv.WaitKey(6000)
cv.DestroyWindow("Original Image")
hc = cv.Load("/home/jayneil/haarcascade_frontalface_default.xml")
img = cv.LoadImage("/home/ashwini/Documents/driving_python/image_processing/d.jpg", 0)
faces = cv.HaarDetectObjects(img,hc, cv.CreateMemStorage())
for (x, y, w, h), n in faces:
    cv.Rectangle(img, (x, y), (x+w, y+h), 255)
cv.SaveImage("faces_detected.jpg", img)
print(faces)
dst=cv.LoadImage("faces_detected.jpg")
cv.NamedWindow("Face Detected", cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("Face Detected", dst)
cv.WaitKey(5000)
cv.DestroyWindow("Face Detected")

