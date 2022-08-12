import cv2
import os
import numpy as np
import string

def skinFilter(frame):
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    filter = cv2.inRange(frame_HSV, np.array([0, 58, 30]), np.array([33, 255, 255]))
    return filter

def getCommandData():
    command_names = []
    command_pics = []
    command_files = os.listdir("Commands/")
    for data in command_files:
        command_names.append(data.replace(".jpg", ""))
        command_pics.append(cv2.imread("Commands/" + data, 0))
    return command_names, command_pics

def find_difference(pic1, pic2):
    pic2 = cv2.resize(pic2, (pic1.shape[1], pic1.shape[0]))
    diff = 0
    for y in range(pic1.shape[0]):
        for x in range(pic1.shape[1]):
            if(pic1[y][x] != pic2[y][x]):
                diff += 1
    return diff
    
def result(frame, command_names, commands):
    index = 0
    difference = 0
    min_diff = find_difference(frame, commands[0])
    for i in range(len(command_names)):
        difference = find_difference(frame, commands[i])
        if(min_diff > difference):
            min_diff = difference
            index = i
    return command_names[index]

vid = cv2.VideoCapture(0)
command_names, commands = getCommandData()

while(True):
    ret, frame = vid.read()
    cFrame = frame[0:300, 0:255]
    filter = skinFilter(cFrame)
    cv2.imshow("frame", cFrame)
    cv2.imshow("filtered frame", filter)
    if(len(command_names) > 0):
        print(result(filter, command_names, commands))
    if cv2.waitKey(33) == 27: #ESC key to stop
        break
vid.release()
cv2.destroyAllWindows()