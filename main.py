import cv2
from os import getcwd
print ('package imported')
# test_image_path = getcwd() +"/resources/starfish-a.jpg"
# test_img = cv2.imread(test_image_path )
# cv2.imshow("output", test_img)
# cv2.waitKey(0)
cap = cv2.VideoCapture (0)
while True:
    success, image =cap.read()
    cv2.imshow("video", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.set (3,640)
cap.set (4,640)
cap.set (10,1000)

