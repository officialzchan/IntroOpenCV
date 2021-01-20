import cv2
import numpy as np

#Greyscale
img = np.zeros((512, 512))

cv2.imshow("Image", img)

#RGB
img2 = np.zeros((512, 512, 3), np.uint8)
#Blue
#img2[:] = 255, 0, 0
#cv2.line(img2, (0,0), (300,300), (0, 255, 0), 3)
#cv2.line(image, (starting point), (ending point), (color), thickness)
cv2.line(img2, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
#cv2.line(image, (starting point), (diagonal point), (color), thickness)
cv2.rectangle(img2, (0, 0), (250,350), (0, 0, 255), 2)
#Fill Rectangle replace thickness with cv2.FILLED
#cv2.rectangle(img2, (0, 0), (250,350), (0, 0, 255), cv2.FILLED)
#cv2.circle(img, (starting point), radius, (color), thickness)
cv2.circle(img2, (400, 50), 30, (255, 255, 0), 5)
#cv2.putText(image, "text", (starting point), font, scale, (color), thickness)
cv2.putText(img2, " OPEN CV ", (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)

cv2.imshow("Image 2", img2)

cv2.waitKey(0)