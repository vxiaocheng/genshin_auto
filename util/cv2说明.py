"""
cv2.imread(filename, flags)
参数：
filepath：读入imge的完整路径
flags：标志位，{cv2.IMREAD_COLOR，cv2.IMREAD_GRAYSCALE，cv2.IMREAD_UNCHANGED}
cv2.IMREAD_COLOR：默认参数，读入一副彩色图片，忽略alpha通道，可用1作为实参替代
cv2.IMREAD_GRAYSCALE：读入灰度图片，可用0作为实参替代
cv2.IMREAD_UNCHANGED：顾名思义，读入完整图片，包括alpha通道，可用-1作为实参替代
"""