
from WindowCapture import WindowCapture
import cv2 as cv
import time


# create a new window capture object

capture = WindowCapture('RuneLite - assemblys')

i = 0
while(True):
    test = capture.get_screenshot()
    cv.imwrite(f'data\\test{i}.png',test)
    i+=1
    time.sleep(1)


