import cv
src = cv.LoadImage("/home/ashwini/Documents/driving_python/image_processing/d.jpg")
print (src)
cv.NamedWindow("rgb 2 grey", cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("rgb 2 grey",src)
cv.WaitKey(500)
cv.DestroyWindow("rgb 2 grey")

# below code will convert rgb image to grey image

dst = cv.CreateImage(cv.GetSize(src),cv.IPL_DEPTH_8U, 1 )
cv.CvtColor(src, dst , cv.CV_RGB2GRAY)
cv.NamedWindow("GRAY", cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("GRAY",dst)
cv.WaitKey(1000)
cv.DestroyWindow("GRAY")

#this will make a circle on image
src=cv.LoadImage("/home/ashwini/Documents/driving_python/image_processing/d.jpg")
thickness = 3
linetype = 8
Point = (250,200)
cv.Circle(src,Point,100,cv.Scalar(0,0,255),thickness,linetype)
cv.NamedWindow("circle on image",cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("circle on image", src)
cv.WaitKey(3000)
cv.DestroyWindow("circle on image")

# laplace of image
src = cv.LoadImage("/home/ashwini/Documents/driving_python/image_processing/d.jpg")
print (src)
cv.NamedWindow("rgb", cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("rgb",src)
cv.WaitKey(500)
cv.DestroyWindow("rgb")
dst = cv.CreateImage(cv.GetSize(src),cv.IPL_DEPTH_16S, 3 )
laplace = cv.Laplace(src,dst)
cv.Canny(dst,src, 1.0 , 4.0 , aperture_size=3)
#cv.SaveImage("/home/ashwini/Documents/driving_python/image_processing/laplace.png",dst)
#temp = cv.LoadImage(("/home/ashwini/Documents/driving_python/image_processing/laplace.png")
cv.NamedWindow("laplace of image",cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage("laplace of image", src)
cv.WaitKey(500)
cv.DestroyWindow("laplace of image")

# for Canny filter
#cv.canny(dst, dst1 , 1.0 , 4.0 , aperture_size=3)
 
