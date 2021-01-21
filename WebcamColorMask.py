import cv2
import numpy as np

def empty(a):
    pass

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

#path = "C:/Users/Zac/Desktop/OpenCV/Images/Lambo.png"
cap = cv2.VideoCapture(0)
#Define width
cap.set(3, 640)
#Define height
cap.set(4, 480)
#change brightness
cap.set(10, 200)


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
'''
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)
'''
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 64, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 17, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 121, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 137, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

#img = cv2.imread(path)

#imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while True:
    success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask = mask)

    img2 = cv2.imread("C:/Users/Zac/Desktop/OpenCV/Images/beach.jpg")
    img2HSV = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
    mask2 = cv2.inRange(img2HSV, lower, upper)
    img2Result = cv2.bitwise_and(img2, img2, mask = mask2)
    '''
    cv2.imshow("Original", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result Image", imgResult)
    '''
    imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgResult], [img2, img2HSV], [mask2, img2Result]))
    cv2.imshow("Stacked Images", imgStack)

    #img3 = cv2.add(imgResult, img2)

    #img1 = cv2.imread('messi5.jpg')
    #img2 = cv2.imread('opencv_logo.png')

    # I want to put logo on top-left corner, So I create a ROI
    rows,cols, = 480,640
    roi = img2[0:rows, 0:cols ]

    # Now create a mask of logo and create its inverse mask also
    img2gray = cv2.cvtColor(imgResult,cv2.COLOR_BGR2GRAY)
    ret, mask3 = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask3)

    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(imgResult,imgResult,mask = mask3)

    # Put logo in ROI and modify the main image
    dst = cv2.add(img1_bg,img2_fg)
    img2[0:rows, 0:cols ] = dst

    cv2.imshow("GreenSCreen?", img2)
    cv2.waitKey(1)