import os


def file_n (f_name)
        a =r'os.path.join(os.path.dirname(__file__), f'{'f_name}'

class Gold_test:
    def __init__(self, test):
        self.test = test

    def are_you_gold(self):
        test_image_path = r'C:\Users\noaml\PycharmProjects\SET\test_1.jpg'
        test_img = cv2.imread(test_image_path)
        gray_p = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
        face = faceCascade.detectMultiScale(
            gray_p,
            scaleFactor=1.5,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, w, h) in face:
            cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray_p = gray_p[y:y + h, x:x + w]
            roi_color_p = test_img[y:y + h, x:x + w]
            n_img = cv2.line(roi_color_p, (x, n_y), (x + w, n_y), (0, 255, 0), 2)
            ratio = (h - y) / (x - w)
            #r_ratio = float(ratio) * float(g_fact)

            eyes = eye_cascade.detectMultiScale(roi_gray_p)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(n_img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)