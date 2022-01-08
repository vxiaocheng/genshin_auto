from time import sleep

from Model import const
from util.keys import Keys

keys = Keys()


def mouse_left(sec=0.5):
    """
    点击鼠标左键
    :param sec: 按下时长
    :return:
    """
    keys.directMouse(buttons=keys.mouse_lb_press)
    sleep(sec)
    keys.directMouse(buttons=keys.mouse_lb_release)


def mouse_right():
    """
    点击鼠标右键
    :param sec: 按下时长
    :return:
    """
    keys.directMouse(buttons=keys.mouse_rb_press|keys.mouse_rb_release)
    # sleep(sec)
    # keys.directMouse(buttons=keys.mouse_rb_release)


def mouse_move_click(x=0, y=0):
    """
    移动鼠标并点击
    :param x:
    :param y:
    """
    keys.directMouse(int(x*65536/const.width), int(y*65536/const.height),
                     buttons=keys.mouse_absolute|keys.mouse_lb_press|keys.mouse_lb_release)
    print("点击位置：" + str((x, y)))
    # sleep(0.5)
    # keys.directMouse(x, y, buttons=keys.mouse_absolute, is_absolute=True)


def mouse_slip(toward="left", delt=50):
    """
    滑动鼠标，旋转镜头
    :param toward: 方向，left为向左转，right为向右转
    :param delt: 偏移量，越大旋转越多
    :return:
    """
    dic = {"left": -1, "right": 1}
    for i in range(delt):
        keys.directMouse(dic[toward] * i, 0)
        sleep(0.008)


def keyon(key_v, sec=1):
    """
    点击键盘
    :param key_v: 按键
    :param sec: 时长
    :return:
    """
    keys.directKey(key_v)
    sleep(sec)
    keys.directKey(key_v, keys.key_release)


# =================================================================
# 常用操作---------------------------------------------------------
# =================================================================
def attack():
    """
    攻击
    """
    for i in range(2):
        keys.directMouse(buttons=keys.mouse_lb_press|keys.mouse_lb_release)
        sleep(0.3)
        # keys.directMouse(buttons=keys.mouse_lb_release)


def W():
    """
    向前
    """
    keyon("w")


def A():
    """
    向左
    """
    keyon("a")


def S():
    """
    向后
    """
    keyon("w")


def D():
    """
    向右
    """
    keyon("a")


def X():
    """
    下
    """
    keyon("x")


def Blank():
    """
    跳跃
    """
    keyon("SPACE")


def F():
    """
    拾取
    """
    keyon("f")

# def D():
#     keyon("a")
