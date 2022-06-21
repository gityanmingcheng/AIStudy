# -*- coding:utf-8 -*-
#@Time : 2022/6/21 下午10:54
#@Author: cym
#@File : uniform.py
#@Description :  uniform distribution 均匀分布


import numpy as np
import scipy.stats as stats
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.style as style
from IPython.core.display import HTML

style.use('fivethirtyeight')
plt.figure(dpi=100,figsize=(14,7))
#### font.sans-serif 解决中文乱码问题
# WIN
# plt.rcParams["font.sans-serif"]=["SimHei"]
# MAC
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams["axes.unicode_minus"] = False

