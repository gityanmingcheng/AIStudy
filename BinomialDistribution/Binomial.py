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



def binomial1():
    # PMF ~ PDF
    plt.bar(x=np.arange(20),height=(stats.binom.pmf(np.arange(20),p=0.5,n=20)),width=.75,alpha=.75)

    # CDF
    plt.plot(np.arange(20),stats.binom.cdf(np.arange(20),p=.5,n=20) ,color='#fc4f30')
    # LEEND
    plt.text(x=4.5, y=.7,s="pmf(narmed)",alpha=.75,weight="bold",color="#008fd5")
    plt.text(x=14.5,y=.9,s="cdf",alpha=.75,weight="bold",color="#fc4f30")
    # plt.text(x=-.4, y=.5, s="cdf", rotation=55, alpha=0.75, weight="bold", color="#fc4f30")

    # TICKS which : {'major',  'minor',  'both'}
    plt.xticks(range(21)[::2])
    plt.tick_params(axis="both",which="major",labelsize=18)
    plt.axhline(y=0.005,color="black",linewidth=1.3, alpha=.7)

    # TITLE
    plt.text(x=-2.5,y=1.25,s="Binomial distribution - Overview" ,fontsize=26 ,weight='bold',alpha=.75)
    plt.text(x=-2.5,y=1.1,s="Depicted below are the norm probabitity mass funtion(pmf) and the cumlative density \n"+
                " function(cdf) a Binomial distributed random varible $y \\sim Binom(N, p)$,given $N = 20$ and $p = 0.5$."
             ,fontsize=19 ,weight='bold',alpha=.75)
    plt.savefig('static/1.png', bbox_inches='tight')
    plt.show()



def binomial2():
    # 概率 P 对结果的影响
    # PMF  P= .2
    plt.scatter(np.arange(21),stats.binom.pmf(np.arange(21),p=.2,n=20),alpha=.75)
    # PMF
    plt.plot(np.arange(21),stats.binom.pmf(np.arange(21),p=.2,n=20) ,alpha=.75)

    # PMF  P= .5
    plt.scatter(np.arange(21),stats.binom.pmf(np.arange(21),p=.5,n=20),alpha=.75)
    plt.plot(np.arange(21),stats.binom.pmf(np.arange(21),p=.5,n=20) ,alpha=.75)
    # PMF  P= .9
    plt.scatter(np.arange(21),stats.binom.pmf(np.arange(21),p=.9,n=20),alpha=.75)
    plt.plot(np.arange(21),stats.binom.pmf(np.arange(21),p=.9,n=20) ,alpha=.75)

    # LEEND
    plt.text(x=3.5, y=.075,s="$p = 0.2$",alpha=.75,weight="bold",color="#008fd5")
    plt.text(x=9.5,y=.075,s="$p = 0.5$",alpha=.75,weight="bold",color="#fc4f30")
    plt.text(x=17.4, y=.075, s="$p = 0.9$", alpha=0.75, weight="bold", color="#e5ae38")

    # TICKS which : {'major',  'minor',  'both'}
    plt.xticks(range(21)[::2])
    plt.tick_params(axis="both",which="major",labelsize=18)
    plt.axhline(y=0.005,color="black",linewidth=1.3, alpha=.7)

    # TITLE
    plt.text(x=-2.5,y=.35,s="Binomial distribution - Overview" ,fontsize=26 ,weight='bold',alpha=.75)
    plt.text(x=-2.5,y=.3,s="Depicted below are the norm probabitity mass funtion(pmf) and the cumlative density \n"+
                " function(cdf) a Binomial distributed random varible $y \\sim Binom(N, p)$,given $N = 20$ and $p = (0.2,0.5,0.9)$."
             ,fontsize=19 ,weight='bold',alpha=.75)


    plt.savefig('static/2.png', bbox_inches='tight')
    plt.show()


def binomial3():
    # 次数 N 对结果的影响
    # PMF  N= 10
    plt.scatter(np.arange(11),stats.binom.pmf(np.arange(11),p=.5,n=10),alpha=.75)
    plt.plot(np.arange(11),stats.binom.pmf(np.arange(11),p=.5,n=10) ,alpha=.75)
    # PMF  N= 15
    plt.scatter(np.arange(16),stats.binom.pmf(np.arange(16),p=.5,n=15),alpha=.75)
    plt.plot(np.arange(16),stats.binom.pmf(np.arange(16),p=.5,n=15) ,alpha=.75)
    # PMF  N= 20
    plt.scatter(np.arange(21),stats.binom.pmf(np.arange(21),p=.5,n=20),alpha=.75)
    plt.plot(np.arange(21),stats.binom.pmf(np.arange(21),p=.5,n=20) ,alpha=.75)

    # LEEND
    plt.text(x=6, y=.225,s="$N = 10$",alpha=.75,weight="bold",color="#008fd5")
    plt.text(x=8.5,y=.215,s="$N = 15$",alpha=.75,weight="bold",color="#fc4f30")
    plt.text(x=11, y=.175, s="$N = 20$", alpha=0.75, weight="bold", color="#e5ae38")

    # TICKS which : {'major',  'minor',  'both'}
    plt.xticks(range(21)[::2])
    plt.tick_params(axis="both",which="major",labelsize=18)
    plt.axhline(y=0.005,color="black",linewidth=1.3, alpha=.7)

    # TITLE
    plt.text(x=-2.5,y=.35,s="Binomial distribution - Overview" ,fontsize=26 ,weight='bold',alpha=.75)
    plt.text(x=-2.5,y=.28,s="Depicted below are the norm probabitity mass funtion(pmf) and the cumlative density \n"+
                " function(cdf) a Binomial distributed random varible $y \\sim Binom(N, p)$,given $N = (10,15,20)$ \n and $p = 0.5$."
             ,fontsize=19 ,weight='bold',alpha=.75)

    plt.savefig('static/3.png', bbox_inches='tight')
    plt.show()

def sample():
    # 定义随机种子
    np.random.seed(42)
    # 采样一个
    print(stats.binom.rvs(p=0.3,n=10))
    # 采样 10 个
    print(stats.binom.rvs(p=0.3,n=10,size=10))
    # Probability mass function 概率质量函数
    x_s = np.arange(11)
    y_s = stats.binom.pmf(x_s,p=.3,n=10)
    plt.scatter(x_s,y_s,s=100)
    plt.savefig('static/4.png', bbox_inches='tight')
    plt.show()

    # Cumulative distribution function
    print( "P(x<= 3) = {}".format(stats.binom.cdf(k=3,p=0.3,n=10)))
    print( "P(2< x <= 8) = {}".format(stats.binom.cdf(k=8,p=0.3,n=10) - stats.binom.cdf(k=2,p=0.3,n=10)))

# sample()
# binomial2()
binomial3()