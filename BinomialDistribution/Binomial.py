# -*- coding:utf-8 -*-
#@Time : 2022/6/19 上午9:05
#@Author: cym
#@File : Binomial.py
#@Description :


import numpy as np
import scipy.stats as stats
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.style as style


# print(style.available)
style.use('fivethirtyeight')
plt.figure(dpi=100,figsize=(14,7))
#### font.sans-serif 解决中文乱码问题
# WIN
# plt.rcParams["font.sans-serif"]=["SimHei"]
# MAC
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams["axes.unicode_minus"] = False



plt.show()