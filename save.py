import cv2
import os
import numpy as np
import string

def skinFilter(frame):
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    filter = cv2.inRange(frame_HSV, np.array([0, 58, 30]), np.array([33, 255, 255]))
    return filter

def create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

commandName = "name" #name of the command to save

vid = cv2.VideoCapture(0)

while(True):
    ret, frame = vid.read()
    cFrame = frame
    filter = skinFilter(cFrame)[0:300, 0:255]
    cv2.imshow("frame", cFrame)
    cv2.imshow("filtered frame", filter)
    if cv2.waitKey(1) & 0xFF == ord('\r'): #ENTER key to take screenshot
        create_dir("Commands")
        cv2.imwrite("Commands/" + commandName + ".jpg", filter)
        break
    if cv2.waitKey(33) == 27: #ESC key to stop
        break
vid.release()
cv2.destroyAllWindows()