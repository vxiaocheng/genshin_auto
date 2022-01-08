import time

import cv2

from util import common


def cut_dialog(wait = 1):
    """等待对话"""
    site = (180, 800, 900, 200)
    start = time.clock()
    end = time.clock()
    screen1 = common.cap(site)
    while end - start < wait:
        time.sleep(0.2)
        screen2 = common.cap(site)
        if common.compare_img(screen1, screen2): return
        end = time.clock()
    raise Exception("对话没有完成")


def img_arise(img_path, wait=1):
    """等待屏幕中出现目标图像"""
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    start = time.clock()
    end = time.clock()
    while end - start < wait:
        time.sleep(0.2)
        screen = common.cap()
        if common.match_img(img, screen): return
        end = time.clock()
    raise Exception("未检测到目标图像")

