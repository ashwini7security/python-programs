#Program to apply a Canny Filter on a given image

#jayneil.dalal@gmail.com

#!/usr/bin/python
import cv
src = cv.LoadImage("/home/ashwini/Documents/driving_python/image_processing/d.jpg")
cv.NamedWindow("RGB", cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("RGB", src)
cv.WaitKey(1000)
cv.DestroyWindow("RGB")
dst = cv.CreateImage(cv.GetSize(src), cv.IPL_DEPTH_8U, 1)
cv.CvtColor(src, dst, cv.CV_RGB2GRAY)
cv.NamedWindow("GRAY", cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("GRAY", dst)
cv.WaitKey(1000)
cv.DestroyWindow("GRAY")
dst1 = cv.CreateImage(cv.GetSize(src), cv.IPL_DEPTH_8U, 1)
cv.Canny(dst, dst1, 1.0, 4.0, aperture_size=3)
cv.NamedWindow("Canny_Filter", cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("Canny_Filter", dst1)
cv.WaitKey(4500)
cv.DestroyWindow("Canny_Filter")

