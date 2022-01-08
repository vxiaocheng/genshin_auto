#!/usr/bin/env python3
# coding=utf-8
import ctypes
import sys
from time import sleep

from util import keyctrl
from util.common import is_admin

a = 1
sleep(5)
# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except RuntimeError:
#         return False


def main():
    # global note_map
    print("疯物之诗琴 by luern0313")
    print("世界线变动率：1.1.0.61745723")
    # read_configure()
    for i in range(2):
        sleep(3)
        # keyController.W()
        # keyController.W()
        # keyController.A()
        # keyController.W()
        # keyController.mouse_slip()
        # keyController.mouse_slip("right")
        keyctrl.mouse_move_click(1000, 1000)



if __name__ == "__main__":
    if is_admin():
        print(123)
        main()

    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    # main()
