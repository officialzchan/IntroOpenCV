import cv2
import numpy as np

img = cv2.imread("C:/Users/Zac/Desktop/OpenCV/Images/cards.jpg")

#Normal playing card is 2.5" wide x 3.5" tall
width, height = 250, 350
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)

cv2.imshow("Image Output", imgOutput)
cv2.waitKey(0)