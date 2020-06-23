"""

author: @endormi

Automated real time vehicle detection

"""


import cv2

haar_cascade = 'cars.xml'
video = 'cars.mp4'

cascade_set = cv2.CascadeClassifier(haar_cascade)
video = cv2.VideoCapture(video)


while video.isOpened():
    ret, frames = video.read()
    if ret:
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

        cars = cascade_set.detectMultiScale(gray, 1.15, 4)
        for (x, y, w, h) in cars:
            cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 255), 2)

        cv2.imshow('Video', frames)

    elif cv2.waitKey(1) & 0xFF == ord('c'):
        break

    else:
        break

video.release()
cv2.destroyAllWindows()
