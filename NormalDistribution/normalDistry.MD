# 正太分布
正太分布图收到两个参数影响   
$ \\mu$     ==```loc # 均值```    
$ \\sigma$  ==```scale # 标准差```

## 绘制第一个正态分布图
> 引包

    import numpy as np
    import scipy.stats as stats
    import matplotlib
    import matplotlib.pyplot as plt
    import matplotlib.style as style
    from IPython.core.display import HTML
> 处理中文乱码问题

pyplot在绘制图像的时候，plt.text()函数在做文本填充可能会出现中文乱码【】【】
mac/Window 系统处理方式有一点点的区别，大家可以自行参考下面代码

    # Window
    # plt.rcParams["font.sans-serif"]=["SimHei"]
    # MAC
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    plt.rcParams["axes.unicode_minus"] = False

> 初始化风格

    print(plt.style.available)
    # plt.style.use('ggplot')
    style.use('fivethirtyeight')
    plt.rcParams["figure.figsize"] = (14,7)
> 绘制正态分布图

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
    #调用
    show1()
    
> 执行效果

[我的第一张正态分布图](static/1.png)
![我的第一张正态分布图](static/1.png)


## 均值
$ \\mu$     ==```loc # 均值```    
> 代码
```
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
`````
> 图形展示

[均值（$ \\mu$）不同的效果图](static/2.png)
![均值（$ \\mu$）不同的效果图](static/2.png)



