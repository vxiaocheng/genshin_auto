import time

from KeyMouse import my_mouse


def main():
    while True:
        time.sleep(1)
        nowP = my_mouse.position
        print(nowP)

if __name__ == '__main__':
    main()