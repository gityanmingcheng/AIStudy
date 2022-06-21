# -*- coding:utf-8 -*-
#@Time : 2022/6/21 下午11:02
#@Author: cym
#@File : Poisson.py
#@Description : 泊松分布 Poisson distribution

import numpy as np
import scipy.stats as stats
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.style as style
from IPython.core.display import HTML


style.use('fivethirtyeight')
plt.figure(dpi=100,figsize=(14,7))
#### font.sans-serif 解决中文乱码问题
# WIN  ，If your machine is windows ，you need this configs
# plt.rcParams["font.sans-serif"]=["SimHei"]
# MAC ,If your machine is MAC ，you need this configs
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams["axes.unicode_minus"] = False

def poisson():
    # PDF
    plt.bar(np.arange(20),height=(stats.poisson.pmf(np.arange(20), mu=5)) ,width=.75,alpha=.75)
    # CDF
    plt.plot(np.arange(20),stats.poisson.cdf(np.arange(20), mu=5),color='#fc4f30' ,alpha=.75)


    # LEEND
    plt.text(x=5, y=.2, s="pdf(narmed)", alpha=0.75, weight="bold", color="#008fd5")
    plt.text(x=5, y=.56, s="cdf", alpha=0.75, weight="bold", color="#fc4f30")

    # TICKS
    plt.xticks(range(20)[::2])
    plt.tick_params(axis='both', which='major', labelsize=18)
    plt.axhline(y=0.005, color='black', linewidth=1.3, alpha=.7)

    # TITLE
    plt.text(x=-2,y=1.3,s='Poisson distribution -Overview',fontsize=26,weight='bold',alpha=.7)

    plt.text(x=-2,y=1.12,s="The following describes that the norm probability mass function (PMF) and cumulative density \n"
                           " function (CDF) are random variables of Poisson distribution $y \\sim Poi(\\lambda)$, given $\\lambda = 5$."
             ,fontsize=19,weight='bold',alpha=.75)



    plt.show()
    pass

poisson()