import ctypes
import sys
import time
import cv2
import numpy as np
import win32gui, win32ui, win32con, win32api
from Model import const


def is_admin():
    """
    获取管理员权限
    :return:
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except RuntimeError:
        return False


def compare_img(img1, img2, set=0.8):
    """
    计算两个图像的相识度
    :param img1:
    :param img2:
    :param set:阈值
    :return:
    """
    match1 = cv2.compareHist(img1, img2, cv2.HISTCMP_CORREL)
    return True if match1 > set else False


def match_img(img, target, type=cv2.TM_CCOEFF):
    """
    匹配图像在背景中位置
    :param img: 背景全图
    :param target: 检测图像
    :param type:
    :return:max_val,匹配度[0，1] 1最匹配
        max_loc[0], max_loc[1],左上点坐标
        max_loc[0] + w, max_loc[1] + h,右下点坐标
    """
    h, w = target.shape[:2]
    res = cv2.matchTemplate(img, target, type)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(min_val, max_val, min_loc, max_loc)
    return (
        max_val,
        max_loc[0],
        max_loc[1],
        max_loc[0] + w,
        max_loc[1] + h,
    )


def cap(region=None):
    """
    获取当前的截图
    :param region:截图尺寸，[left, top, w, h]
    :return:
    """
    if region is not None:
        left, top, w, h = region
    else:
        w = const.MONITOR_WIDTH  # set this
        h = const.MONITOR_HEIGHT  # set this
        left = 0
        top = 0

    # hwnd = win32gui.FindWindow(None, WINDOW_NAME)
    hwnd = win32gui.GetDesktopWindow()
    print(hwnd)
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()

    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)

    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (left, top), win32con.SRCCOPY)
    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype="uint8")
    img.shape = (h, w, 4)

    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    return cv2.cvtColor(np.asarray(img), cv2.COLOR_BGRA2GRAY)


if __name__ == "__main__":
    # if is_admin():
    #     for i in range(5):
    #         print(5 - i)
    #         time.sleep(1)
    # else:
    #     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    # time.sleep(5)
    # cv2.imshow("window", cap())
    tar = cv2.imread("img1.png", 0)
    start = time.clock()
    im = cap((0, 0, 1920, 1080))
    end = time.clock()
    print('CPU执行时间: ', end - start)
    start = time.clock()
    info = match_img(im, tar, cv2.TM_CCOEFF_NORMED)
    end = time.clock()
    print('CPU执行时间: ', end - start)
    print(info)

    cv2.rectangle(im, (info[1], info[2]), (info[3], info[4]), (0, 255, 0), 2)
    from matplotlib import pyplot as plt
    plt.imshow(im, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()
