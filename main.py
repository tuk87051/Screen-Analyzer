import cv2 as cv
import numpy as np
import pyautogui
from time import time
import mss

w, h = pyautogui.size()
print("Screen resolution size: " + str(w) + str(h))

loop_time = time()

with mss.mss() as sct:

    monitor = {'left': 0, 'top': 0, 'width': w, 'height': h}

    while True:

        screenshot = sct.grab(monitor)
        screenshot = np.array(screenshot)

        # Display the resulting frame
        cv.imshow('frame', screenshot)

        print('FPS {}'.format(1 / (time() - loop_time)))
        loop_time = time()

        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

