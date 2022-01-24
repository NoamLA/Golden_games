from dataclasses import dataclass, field
import cv2
from os import getcwd


# defining integers and objects cascades
cascPath = r"C:\Users\noaml\PycharmProjects\SET\alt_frontalface_casc"
faceCascade = cv2.CascadeClassifier(cascPath)
eyePath = r"C:\Users\noaml\PycharmProjects\SET\alt_eye_eyeglasses"
eye_cascade = cv2.CascadeClassifier(eyePath)
fistpath = r"C:\Users\noaml\PycharmProjects\SET\fist"
fist_cascade = cv2.CascadeClassifier(fistpath)
font = cv2.FONT_HERSHEY_SIMPLEX  # font
org = (20, 30)  # org
fontScale = 0.8  # fontScale
color = (255, 0, 0)  # Blue color in BGR
thickness = 1  # Line thickness of 1 px
gest = True
g_fact = 0.77


video_capture = cv2.VideoCapture(0)

while True:
    ret, img = video_capture.read() # Capture frame-by-frame and num
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # the detection works better on grayscale

    #Face detection and recengular output
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    # While loop for gesture detection

    if gest:
        img = cv2.putText(img, f'Are you golden? To find out, raise your fist!', org, font, fontScale, color,
                      thickness, cv2.LINE_AA)
    else:
        break

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            cv2.line(roi_color, (ex, ew), (ey, eh), (0, 255, 0), 2)


    fist = fist_cascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for (fx, fy, fw, fh) in fist:
        cv2.rectangle(img, (fx, fy), (fx + fw, fy + fh), (0, 0, 255), 2)
        test_images =('test_1',)
        for i in range (3):
            test_img = cv2.imwrite(f'test_{i}.jpg', img)
            i +=1
            #test_images += (f'test_{i}.jpg',)
            test_images += (f'{getcwd()}\\test_{i}.jpg',)
            print (test_images)
        gest = False

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
# test_images = Gold_test(test = 'test_1')
# Gold_test.are_you_gold

