import cv2 

img = cv2.imread("C:/Users/Zac/Desktop/OpenCV/Images/lambo.png")
cv2.imshow("Image", img)

#(height, width, numChannels)
print(img.shape)

#Resize(img, (width, height))
imgResize = cv2.resize(img, (1920, 1080))
cv2.imshow("Resized Image", imgResize)
print(imgResize.shape)

#Crop. Height then width. 
imgCropped = img[0:200, 200:500]
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)