#!/usr/bin/env python3
# coding=utf-8
import time
import ctypes
import sys
# import KeyMouse
# from Model.Action import Action
# from util.is_admin import is_admin
# from windKey import press_key, release_key
# from 疯物之诗琴2 import PlayThread


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except RuntimeError:
        return False


def main():
    print("疯物之诗琴 by luern0313")
    print("世界线变动率：1.1.0.61745723")
    for i in range(5):
        print(5-i)
        time.sleep(1)


    # press_key(0x11)
    # time.sleep(1)
    # release_key(0x11)
    # KeyMouse.keepKeyPress(Action.pick_up)
    # KeyMouse.keepKeyPress(Action.walk, 5)
    # while True:
    #     press_key(0x11)
    #     time.sleep(1)
    #     release_key(0x11)
    #     pass
#
# def main2():
#     print("鼠标移动测试")
#     print("世界线变动率：1.1.0.61745723")
#     for i in range(5):
#         print(5-i)
#         time.sleep(1)
    # KeyMouse.mouseScrollDown(10)
    # KeyMouse.mouseClick()
    # for i in range(100):
    #     KeyMouse.moveMouse(1, 0)
    #     time.sleep(0.01)
    # KeyMouse.moveMouse(50, 0)
    # time.sleep(1)
    # KeyMouse.moveMouse(-50,0)

if __name__ == "__main__":
    if is_admin():
        # print("success")
        # # main()
        # print("success1")
        # print()
        pass

    else:
        # print("------------------------")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        print("defeated")
    # main()
