# 全局鼠标控制器
import time

from pynput import mouse

NumberOfMouseClicks = 0

def on_click(x, y, button, pressed):
    print(x, y)
    print()

mouse.Listener.stop

while NumberOfMouseClicks < 20 :
    NumberOfMouseClicks = NumberOfMouseClicks + 1
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    # print()

