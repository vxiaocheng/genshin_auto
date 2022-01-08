import time

import KeyMouse

f = open('我的脚本1.rec', 'w', encoding='utf-8')
x = KeyMouse.newKeyboardListener(f)
y = KeyMouse.newMouseListener(f)
print('开始录制 F12结束')
x.start()
y.start()
while (x.is_alive()):
    i = 1
y.stop()
f.close()
print(y.is_alive())
print('录制完成')
f = open('我的脚本1.rec', 'r', encoding='utf-8')
time.sleep(3)
print('开始回放')
KeyMouse.executeRecord(f)