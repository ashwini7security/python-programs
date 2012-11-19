#Program to draw a circle on a given image

#jayneil.dalal@gmail.com

#!/usr/bin/python
import cv
src = cv.LoadImage("/home/ashwini/Documents/driving_python/image_processing/d.jpg")
print(src)
cv.NamedWindow("RGB", cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("RGB", src)
cv.WaitKey(1000)
cv.DestroyWindow("RGB")
thickness = 3
lineType=8
Point = (292,300)
cv.Circle(src, Point,100, cv.Scalar(0,0,255), thickness, lineType)
cv.NamedWindow("Circle_on_image", cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("Circle_on_image", src)
cv.WaitKey(3000)
cv.DestroyWindow("RGB")

