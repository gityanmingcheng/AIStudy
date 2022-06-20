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


# PLOTTING CONFIG 绘图配置
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



#在保险业务中，我们经常需要根据实际情况适当调整保费问题，以保证保险公司的利润达到一定要求，同时保险公司的业务量也达到要求，对于这一类问题，
# 可以对已知实际情况做一定的概率分析。例如某保险公司有10000客户购买人身意外保险，该公司规定每人每年付公司120元 ，若遇意外死亡，
# 公司将赔偿10000元。若每人每年死亡率为0.006，从而不难利用二项分布算出公司获利、亏本的各种情形了。实际上对于随机现象，了解其分布非常有意义，
# 利用概率论讨论得到的结果对保险公司有一定的指导意义。

def sample2():
    # 定义随机种子
    np.random.seed(42)
    # 采样一个
    print(stats.binom.rvs(p=0.006,n=10))
    # 采样 10 个
    print(stats.binom.rvs(p=0.006,n=10,size=10))
    # Probability mass function 概率质量函数
    x_s = np.arange(11)
    y_s = stats.binom.pmf(x_s,p=.006,n=10)
    plt.scatter(x_s,y_s,s=100)
    plt.savefig('static/5.png', bbox_inches='tight')
    plt.show()
    # Cumulative distribution function
    print( "P(x<= 3) = {}".format(stats.binom.cdf(k=1,p=0.006,n=10)))
    print( "P(2< x <= 8) = {}".format(stats.binom.cdf(k=8,p=0.006,n=10) - stats.binom.cdf(k=2,p=0.006,n=10)))

sample()
# binomial2()
# binomial3()