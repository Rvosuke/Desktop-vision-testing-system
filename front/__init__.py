# import random
# from Dva.backPy.hands import judge_direction
#
# a = judge_direction(2)
# print(a)
# exit()
# import win32api
# import win32con
#
# winX = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
# winY = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
#
# print(winX, winY)
# exit(0)
# import ctypes
#
# user32 = ctypes.windll.user32
# gdi32 = ctypes.windll.gdi32
# LOGPIXELSX = 88
# LOGPIXELSY = 90
#
# user32.SetProcessDPIAware()
# hDC = user32.GetDC(0)
# hdpi = gdi32.GetDeviceCaps(hDC, LOGPIXELSX)
# ydpi = gdi32.GetDeviceCaps(hDC, LOGPIXELSY)
# print(hdpi, ydpi)
# import csv
# import numpy as np
# import time
# head = np.array(['name', 'age', 'time'])
# with open('test.csv', 'w', newline='', encoding='utf-8-sig') as f:
#     writer = csv.writer(f)
#     writer.writerow(head)
#     f.close()
# t = time.strftime('%y-%m-%d %H:%M', time.localtime())
# data = np.array(['鸡蛋', '20', t])
# with open('test.csv', 'a', newline='', encoding='utf-8-sig') as f:
#     writer = csv.writer(f)
#     writer.writerow(data)
#     f.close()
# exit(0)
# import math
# import random
# for i in range(2):
#     v = random.uniform(0.3, 0.8)
#
#     log = 5 + math.log10(v)
#     print(f'{v:.2f}', f'{log:.2f}')
# exit(0)

# import numpy as np
#
# A = np.array([4.68, 4.74, 4.84, 4.80, 4.71, 4.90, 4.88, 4.81, 4.84, 4.76])
# B = np.array([4.77, 4.91, 4.94, 4.81, 4.91, 4.84, 4.91, 4.79, 4.85, 4.92])
# C = np.array([4.38, 4.53, 4.41, 4.40, 4.49, 4.44, 4.50, 4.44, 4.36, 4.39])
# D = np.array([3.95, 4.08, 4.10, 4.17, 4.09, 4.09, 3.98, 4.09, 4.22, 4.04])
#
# ABCD = np.array([4.80, 4.90, 4.45, 4.10])
#
# # 平均值
# mean_A = np.mean(A)
# mean_B = np.mean(B)
# mean_C = np.mean(C)
# mean_D = np.mean(D)
# mean_ABCD = np.mean(ABCD)
#
# # 中位数
# median_A = np.median(A)
# median_B = np.median(B)
# median_C = np.median(C)
# median_D = np.median(D)
# median_ABCD = np.median(ABCD)
#
# # 众数
# mode_A = np.mode(A)
# mode_B = np.mode(B)
# mode_C = np.mode(C)
# mode_D = np.mode(D)
# mode_ABCD = np.mode(ABCD)
#
# # 标准差
# std_A = np.std(A, ddof=1)
# std_B = np.std(B, ddof=1)
# std_C = np.std(C, ddof=1)
# std_D = np.std(D, ddof=1)
# std_ABCD = np.std(ABCD, ddof=1)
#
# # 最大值
# max_A = np.max(A)
# max_B = np.max(B)
# max_C = np.max(C)
# max_D = np.max(D)
# max_ABCD = np.max(ABCD)
#
# # 最小值
# min_A = np.min(A)
# min_B = np.min(B)
# min_C = np.min(C)
# min_D = np.min(D)
# min_ABCD = np.min(ABCD)
# for i in range(5):
#     print(i)