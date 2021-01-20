import cv2 

"""
Open and display an image
"""
img = cv2.imread("C:/Users/Zac/Desktop/OpenCV/Images/lena.png")

cv2.imshow("Output", img)

cv2.waitKey(0)


"""
Open and display video
"""
'''
cap = cv2.VideoCapture("C:/Users/Zac/Desktop/OpenCV/Images/test_video.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''

"""
Using a webcam
"""
cap = cv2.VideoCapture(0)
#Define width
cap.set(3, 640)
#Define height
cap.set(4, 480)
#change brightness
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
