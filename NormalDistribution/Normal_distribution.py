# -*- coding:utf-8 -*-
#@Time : 2022/6/17 上午8:52
#@Author: cym
#@File : Normal_distribution.py
#@Description : 正太分布


import numpy as np
import scipy.stats as stats
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.style as style
from IPython.core.display import HTML

# %matplotlib inline

print(plt.style.available)
# plt.style.use('ggplot')
style.use('fivethirtyeight')
plt.rcParams["figure.figsize"] = (14,7)
#### font.sans-serif 解决中文乱码问题
# WIN
# plt.rcParams["font.sans-serif"]=["SimHei"]
# MAC
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams["axes.unicode_minus"] = False

##正太分布
def show1():
    plt.figure(dpi=100)
    # PDF
    plt.plot(np.linspace(-4, 4, 100),
             stats.norm.pdf(np.linspace(-4, 4, 100)) / np.max(stats.norm.pdf(np.linspace(-3, 3, 100))), )
    plt.fill_between(np.linspace(-4, 4, 100),
                     stats.norm.pdf(np.linspace(-4, 4, 100)) / np.max(stats.norm.pdf(np.linspace(-3, 3, 100))),
                     alpha=0.15, )
    # CDF
    plt.plot(np.linspace(-4, 4, 100), stats.norm.cdf(np.linspace(-4, 4, 100)))

    # LEEND
    plt.text(x=-1.5, y=.7, s="pdf(narmed)", rotation=60, alpha=0.75, weight="bold", color="#008fd5")
    plt.text(x=-.4, y=.5, s="cdf", rotation=55, alpha=0.75, weight="bold", color="#fc4f30")

    # TICKS
    plt.tick_params(axis='both', which='major', labelsize=18)
    plt.axhline(y=0, color='black', linewidth=1.3, alpha=.7)

    # TITLE
    plt.text(x=-5, y=1.25, s="cym Nromal", fontsize=25, weight='bold', alpha=.7)
    plt.text(x=-5, y=1.15,
             s='cym,测试下正太分布曲线的快乐，$ y\\sim \\mathcal{N}(\\mu,\\sigma) $ , given $\\mu = 0$ and $\\sigma = 1$'
             , fontsize=19, alpha=.88)

    plt.savefig('static/1.png', bbox_inches='tight')
    plt.show()

#均值
def show2():
    plt.figure(dpi=100)
    # PDF MU = 0
    plt.plot(np.linspace(-4,4,100),stats.norm.pdf(np.linspace(-4,4,100)))
    plt.fill_between(np.linspace(-4,4,100),stats.norm.pdf(np.linspace(-4,4,100)),alpha=.75)
    # PDF MU = -2
    plt.plot(np.linspace(-4, 4, 100), stats.norm.pdf(np.linspace(-4, 4, 100) ,loc=-2))
    plt.fill_between(np.linspace(-4, 4, 100), stats.norm.pdf(np.linspace(-4, 4, 100),loc=-2), alpha=.75)

    # PDF MU = 2
    plt.plot(np.linspace(-4, 4, 100), stats.norm.pdf(np.linspace(-4, 4, 100),loc=2))
    plt.fill_between(np.linspace(-4, 4, 100), stats.norm.pdf(np.linspace(-4, 4, 100),loc=2), alpha=.75)

    # LEGEND
    plt.text(x=-1,y=0.35,s="$ \mu = 0 $",rotation=65,alpha=.7,weight="bold",color="#008fd5")
    plt.text(x=1,y=0.35,s="$ \mu = 2 $",rotation=65,alpha=.7,weight="bold",color="#fc4f30")
    plt.text(x=-3,y=0.35,s="$ \mu = -2 $",rotation=65,alpha=.7,weight="bold",color="#e5ae38")
    # TITLE
    plt.text(x=-4, y=.51, s="cym Nromal", fontsize=25, weight='bold', alpha=.7)
    plt.text(x=-4, y=.43,
             s='cym,测试下正太分布曲线的快乐，$ y\\sim \\mathcal{N}(\\mu,\\sigma) $ , given $\\mu = (0/2/-2)$ and $\\sigma = 1$'
             , fontsize=19, alpha=.88)

    plt.savefig('static/2.png', bbox_inches='tight')
    # plt.savefig('fig.png', bbox_inches ='tight')
    plt.show()



# 标准差 scale
def show3():
    plt.figure(dpi=100)
    # PDF SIGMA = 1
    plt.plot(np.linspace(-4,4,100),stats.norm.pdf(np.linspace(-4,4,100),scale=1))
    plt.fill_between(np.linspace(-4,4,100),stats.norm.pdf(np.linspace(-4,4,100),scale=1),alpha=.75)
    # PDF SIGMA = 2
    plt.plot(np.linspace(-4, 4, 100), stats.norm.pdf(np.linspace(-4, 4, 100) ,scale=2))
    plt.fill_between(np.linspace(-4, 4, 100), stats.norm.pdf(np.linspace(-4, 4, 100),scale=2), alpha=.75)

    # PDF SIGMA = 0.5
    plt.plot(np.linspace(-4, 4, 100), stats.norm.pdf(np.linspace(-4, 4, 100),scale=.5))
    plt.fill_between(np.linspace(-4, 4, 100), stats.norm.pdf(np.linspace(-4, 4, 100),scale=.5), alpha=.75)

    # LEGEND
    plt.text(x=-1.25,y=0.3,s="$ \sigma = 1 $",rotation=65,alpha=.7,weight="bold",color="#008fd5")
    plt.text(x=-2.5,y=0.12,s="$ \sigma = 2 $",rotation=65,alpha=.7,weight="bold",color="#fc4f30")
    plt.text(x=-0.75,y=0.55,s="$ \sigma = 0.5 $",rotation=65,alpha=.7,weight="bold",color="#e5ae38")
    # TITLE
    plt.text(x=-4, y=1, s="cym Nromal", fontsize=25, weight='bold', alpha=.7)
    plt.text(x=-4, y=.9,
             s='cym,测试下正太分布曲线的快乐，$ y\\sim \\mathcal{N}(\\mu,\\sigma) $ , given $\\mu = 0$ and $\\sigma = (1/2/0.5)$'
             , fontsize=19, alpha=.88)
    plt.savefig('static/3.png', bbox_inches='tight')
    # plt.savefig('fig.png', bbox_inches ='tight')
    plt.show()


def nrom():
    ## loc ：均值
    ## scale ：标准差
    ## Random variable sample
    print(stats.norm.rvs())
    print(stats.norm.rvs(size=10))
    print(stats.norm.rvs(loc=10,scale=0.1))

def show4():
    x = -1
    y = 2
    stats.norm.pdf(x) # 概率密度 probability density Function
    print("pdf(x) = {} \npdf(x) = {}".format(stats.norm.pdf(x),stats.norm.pdf(y)))

    x_s = np.linspace(-3,4,50)
    y_s = stats.norm.pdf(x_s)
    plt.scatter(x_s,y_s)
    plt.savefig('static/4.png', bbox_inches='tight')
    plt.show()

    print("P(X < 0.3) = {}".format(stats.norm.cdf(0.3)))
    print("P(-0,2 < X < 0.2) = {}".format(stats.norm.cdf(0.2) - stats.norm.cdf(-.2)))


# Cumulative distribution function


def show5():
    mu_real = 10
    sigma_real = 2
    np.random.seed(42)
    sample = stats.norm.rvs(loc=mu_real,scale=sigma_real,size=1000)
    mu_est = np.mean(sample)
    sigma_est = np.std(sample)
    print("Estimated MU:{}\nEstimated SIGMA:{}".format(mu_est,sigma_est))

    ##### PLOTTING #####
    plt.hist(sample,bins=50,density =True ,alpha=.25)
    plt.plot(np.linspace(2,18,1000),stats.norm.pdf(np.linspace(2,18,1000),loc=mu_real,scale=sigma_real))
    plt.plot(np.linspace(2,18,1000),stats.norm.pdf(np.linspace(2,18,1000),loc=np.mean(sample),scale= np.std(sample)))

    # LEGEND
    plt.text(x=9,y=0.1,s="sample",alpha=.7,weight="bold",color="#008fd5")
    plt.text(x=7,y=0.1,s="mu_real",rotation=65,alpha=.7,weight="bold",color="#fc4f30")
    plt.text(x=13,y=0.1,s="mu_est",rotation=-65,alpha=.7,weight="bold",color="#e5ae38")

    # TICKS
    plt.tick_params(axis='both', which='major', labelsize=18)
    plt.axhline(y=0, color='black',linestyle='--' ,lw=16, alpha=.7)
    # plt.axhline(x=2, color='black', linewidth=.25, alpha=.7,lw=)
    # TITLE
    plt.text(x=2, y=.3, s="cym Nromal", fontsize=25, weight='bold', alpha=.7)
    plt.text(x=2, y=.27,
             s='cym,测试下正太分布曲线的快乐，$ y\\sim \\mathcal{N}(\\mu,\\sigma) $ , given $\\mu = 0$ and $\\sigma = (1/2/0.5)$'
             , fontsize=19, alpha=.88)

    plt.savefig('static/5.png', bbox_inches='tight')
    plt.show()


show1()
# show2()
# show3()
# show4()
# show5()


