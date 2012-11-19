#Program to read and display an image

#jayneil.dalal@gmail.com

#!/usr/bin/python
import cv
src = cv.LoadImage("/home/jayneil/12.png")
cv.NamedWindow("RGB",cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("RGB", src)
cv.WaitKey(500)
cv.DestroyWindow("RGB")

