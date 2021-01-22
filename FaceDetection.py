import cv2

#Viola and Jones real-time face detection
#Use positive faces and negatives (non faces) to train a cascade (xml) file
#Use a pretrained model from opencv
#Opencv provides cascades 
'''
haarcascade_eye.xml
haarcascade_eye_tree_eyeglasses.xml
haarcascade_frontalcatface.xml
haarcascade_frontalcatface_extend...
haarcascade_frontalface_alt.xml
haarcascade_frontalface_alt2.xml
haarcascade_frontalface_alt_tree.xml
haarcascade_frontalface_default.xml
haarcascade_fullbody.xml
haarcascade_lefteye_2splits.xml
haarcascade_licence_plate_rus_16st..
haarcascade_lowerbody.xml
haarcascade_profileface.xml
haarcascade_righteye_2splits.xml
haarcascade_russian_plate_number...
haarcascade_smile.xml
haarcascade_upperbody.xml
'''
'''
faceCascade = cv2.CascadeClassifier("C:/Users/Zac/Desktop/OpenCV/haarcascades/haarcascade_frontalface_default.xml")

img = cv2.imread("C:/Users/Zac/Desktop/OpenCV/Images/lena.png")
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#imgGray, scale, minimum neighbors
faces = faceCascade.detectMultiScale(imgGrey, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Result", img)
'''
cap = cv2.VideoCapture(0)
#Define width
cap.set(3, 640)
#Define height
cap.set(4, 480)
#change brightness
cap.set(10, 100)

faceCascade = cv2.CascadeClassifier("C:/Users/Zac/Desktop/OpenCV/haarcascades/haarcascade_frontalface_default.xml")

while True:
    success, img2 = cap.read()
    img2Grey = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    #imgGray, scale, minimum neighbors
    faces = faceCascade.detectMultiScale(img2Grey, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img2, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Video", img2)
    cv2.waitKey(1)

