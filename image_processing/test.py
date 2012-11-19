import cv
src = cv.LoadImage("/home/ashwini/Documents/driving_python/image_processing/d.jpg")
cv.NamedWindow("test image",cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("test image",src)
cv.WaitKey(500)
cv.DestroyWindow("test image")
