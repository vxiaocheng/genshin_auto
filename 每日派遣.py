import ctypes
import sys
from time import sleep

from util import keyctrl
# from util.is_admin import is_admin
from util.common import is_admin

skip_site = (500, 500)  # 过程点击
certain_site = () # 确认
receive_site = (1740, 1020) # 领取、选择角色
part_sites = [(450, 169), (450, 285)]
sleep(5)

def main():
    # 与凯瑟琳对话
    keyctrl.F()
    sleep(1.5)
    keyctrl.mouse_move_click(*skip_site)    # 过场
    sleep(1.5)
    keyctrl.mouse_move_click(1356, 666)    # 点击每日派遣
    sleep(1.5)

    # region 蒙德
    keyctrl.mouse_move_click(140, 157)
    sleep(1)
    # 蒙德 点击收取
    # site1 = [(1047, 333), (1172, 656)]
    # for i in range(2):
    #     keyctrl.mouse_move_click()
    #     sleep(1.5)
    #     keyctrl.mouse_move_click(*receive_site)   # 点击确认
    #     keyctrl.mouse_move_click(*skip_site)    # 领取
    #     sleep(1.5)
    # # 点击派遣
    # for i in range(2):
    #     keyctrl.mouse_move_click(*site1[i])
    #     sleep(1.5)
    #     keyctrl.mouse_move_click(*receive_site)   # 点击确认
    #     sleep(1.5)
    #     keyctrl.mouse_move_click(*part_sites[i])    # 领取
    #     sleep(1.5)
    # endregion

    # region 璃月
    keyctrl.mouse_move_click(140, 230)
    sleep(1.5)
    # # 璃月 点击收取
    site2 = [(727, 329), (964, 452)]
    for i in range(3):
        keyctrl.mouse_move_click(*site2[i])
        sleep(1.5)
        keyctrl.mouse_move_click(*receive_site)   # 点击确认
        sleep(1.5)
        keyctrl.mouse_move_click(*skip_site)    # 领取
        sleep(1.5)
    # 点击派遣
    for i in range(2):
        keyctrl.mouse_move_click(*site2[i])
        sleep(1.5)
        keyctrl.mouse_move_click(*receive_site)   # 点击确认
        sleep(1.5)
        keyctrl.mouse_move_click(*part_sites[i])    # 领取
        sleep(1.5)
    # endregion

    # region 稻妻
    keyctrl.mouse_move_click(140, 300)
    sleep(1.5)
    # 稻妻 点击收取
    site3 = [(829, 833)]
    for i in range(1):
        keyctrl.mouse_move_click(*site3[i])
        sleep(1.5)
        keyctrl.mouse_move_click(*receive_site)   # 点击确认
        sleep(1.5)
        keyctrl.mouse_move_click(*skip_site)    # 领取
        sleep(1.5)
    # 点击派遣
    for i in range(1):
        keyctrl.mouse_move_click(*site3[i])
        sleep(1.5)
        keyctrl.mouse_move_click(*receive_site)   # 点击确认
        sleep(1.5)
        keyctrl.mouse_move_click(*part_sites[i])    # 领取
        sleep(1.5)
    # endregion


if __name__ == '__main__':
    if is_admin():
        print(123)
        main()
        sleep(5)

    else:
        print(456)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)