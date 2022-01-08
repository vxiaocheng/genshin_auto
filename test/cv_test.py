import cv2
import numpy as np
import win32gui, win32ui, win32con, win32api
from PIL import ImageGrab

import KeyMouse
from Model.action import Action


def grab_screen(region=None):
    screen = np.array(ImageGrab.grab(bbox=region))
    return cv2.cvtColor(screen, cv2.COLOR_BGRA2RGB)


if __name__ == '__main__':
    while (True):
        screen = np.array(ImageGrab.grab(bbox=(0, 0, 720, 640)))
        img = cv2.cvtColor(screen, cv2.COLOR_BGRA2RGB)

        cv2.imshow('window', img)
        KeyMouse.keepKeyPress(Action.pick_up)
        KeyMouse.keepKeyPress(Action.jump, 1)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break