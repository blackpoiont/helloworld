"""
    程序名:
        概率论可视化界面
    作者:
        彭学典 20193231037
    使用指南:
        1.运行程序后，在所求分布右侧输入相对应参数
        2.点击分布所属按钮得到相对应函数图像或者答案

"""


import math
import random
import time

import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

from scipy import stats
from matplotlib.figure import Figure



#---------------------------------------------------------------

#                    按钮对应功能



# 蒙特卡洛方法（求圆周率）
def fun1():
    print("open蒙特卡洛方法（求圆周率）")
    n = eval(m_1.get())
    i = 0
    count = 0
    while i <= n:
        x = random.random()
        y = random.random()
        if pow(x, 2) + pow(y, 2) < 1:
            count += 1
        i += 1
    pi = 4 * count / n

    m_ans.delete(0,"end")
    m_ans.insert(0,pi)



# 泊松定理
def fun2():
    print("open泊松定理")
    # 为了具有可比性, 利用lamda = n * p, 计算p
    lamda = eval(b_2.get())

    n1 = eval(b_1.get())
    p1 = lamda/n1  # 二项分布中的参数，单次实验成功的概率

    n2 = 50
    p2 = lamda/n2

    poisson_dist = stats.poisson(lamda)  # 初始化泊松分布
    binom_dist1 = stats.binom(n1, p1)  # 初始化第一个二项分布
    binom_dist2 = stats.binom(n2, p2)  # 初始化第二个二项分布

    # 计算pmf
    X = np.arange(poisson_dist.ppf(0.0001), poisson_dist.ppf(0.9999))
    y_po = poisson_dist.pmf(X)
    print(X)
    print(y_po)
    y_bi1 = binom_dist1.pmf(X)
    y_bi2 = binom_dist2.pmf(X)

    # 作图
    # First group
    # 当n比较小，p比较大时，两者差别比较大
    plt.figure(1)
    plt.subplot(211)
    plt.plot(X, y_bi1, 'b-', label='binom1 (n={}, p={})'.format(n1, p1))
    plt.plot(X, y_po, 'r--', label='poisson (%c=%d)'%(chr(955),lamda))
    plt.ylabel('Probability')
    plt.title('Comparing PMF of Poisson Dist. and Binomial Dist.')
    plt.legend(loc='best', frameon=False)
    plt.grid()

    # second group
    # 当n比较大，p比较小时，两者非常相似
    plt.subplot(212)
    plt.plot(X, y_bi2, 'b-', label='binom1 (n={}, p={})'.format(n2, p2))
    plt.plot(X, y_po, 'r--', label='poisson (%c=%d)'%(chr(955),lamda))
    plt.ylabel('Probability')
    plt.legend(loc='best', frameon=False)
    plt.grid()
    plt.show()



# 指数分布
def fun3():
    print("hello")
    lambd = eval(z_1.get())#参数

    x = np.arange(0,15,0.1)
    y1 = lambd*np.exp(-lambd*x)
    y2 = 1 - np.exp(-lambd*x)    

    #创建图形
    plt.figure(1)

    ax1 = plt.subplot(1, 3, 1)
    ax2 = plt.subplot(1, 3, 3)
    
    #选择ax1
    plt.sca(ax1)
    plt.plot(x,y1,'r-.')
    plt.ylim(0,1)  #限定y axis
    plt.title('Exponential:$\lambda$=%.2f' % lambd)
    plt.xlabel('x')
    plt.ylabel('Probability density')
    
    #选择ax2
    plt.sca(ax2)
    plt.plot(x,y2,'g--')
    plt.ylim(0,1)
    plt.title('Exponential:$\lambda$=%.2f' % lambd)
    plt.xlabel('x')
    plt.ylabel('cumulative distribution')

    plt.show()



# 正态分布（一维）
def fun4():
    print("open正态分布（一维）")
    u = eval(z1_1.get())   # 均值μ
    sig = eval(z1_2.get())  # 标准差δ
    x = np.linspace(u - 3*sig, u + 3*sig, 50)
    y = np.exp(-(x - u) ** 2 /(2* sig **2))/(math.sqrt(2*math.pi)*sig)
    plt.title("One dimensional normal distribution:μ=%d δ=%d"%(u,sig))
    plt.plot(x, y, "r-", linewidth=2)
    plt.grid(True)
    plt.show()


# 正态分布（二维）
def fun5():
    print("open正态分布（二维）")
    x, y = np.mgrid[-2:2:200j, -2:2:200j]
    u = eval(z2_3.get())   # 均值μ
    sig = eval(z2_4.get())  # 标准差δ
    z=(1/2*math.pi*u*sig)*np.exp(-(x**2+y**2)/2*u*sig)
    ax = plt.subplot(111, projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='rainbow', alpha=0.9)#绘面

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.title("Two dimensional normal distribution:μ=%d δ=%d"%(u,sig))
    plt.show()


# 卡方分布
def fun6():
    print("open卡方分布")
    fx = stats.chi2(df = eval(k_1.get()))

    x = np.linspace(fx.ppf(0.65),fx.ppf(0.999999),100)

    fig, ax = plt.subplots(1, 1)
    ax.plot(x, fx.pdf(x), "b-", lw=2, label=r"df = %d"%eval(k_1.get()))

    plt.ylabel('Probability')
    plt.title(r'PDF of $\chi^2$ Distribution')
    ax.legend(loc='best', frameon=False)
    plt.grid()
    plt.show()

def fun7():
    print("open三大抽样分布")
    #绘制 正态分布 卡方分布 t分布 F分布
    nor_dis = stats.norm()
    chi2_dis = stats.chi2(df=eval(k_1.get()))
    t_dis = stats.t(df=eval(t_1.get()))
    f_dis = stats.f(dfn=eval(f_1.get()), dfd=eval(f_2.get()))

    x1 = np.linspace(nor_dis.ppf(0.001), nor_dis.ppf(0.999), 1000)
    x2 = np.linspace(chi2_dis.ppf(0.001), chi2_dis.ppf(0.999), 1000)
    x3 = np.linspace(t_dis.ppf(0.001), t_dis.ppf(0.999), 1000)
    x4 = np.linspace(f_dis.ppf(0.001), f_dis.ppf(0.999), 1000)
    fig, ax = plt.subplots(1, 1, figsize=(16, 8))
    ax.plot(x1, nor_dis.pdf(x1), 'r-', lw=2, label=r'N(0, 1)')
    ax.plot(x2, chi2_dis.pdf(x2), 'g-', lw=2, label=r'$\chi^2$(%d)'%eval(k_1.get()))
    ax.plot(x3, t_dis.pdf(x3), 'b-', lw=2, label='t(%d)'%eval(t_1.get()))
    ax.plot(x4, f_dis.pdf(x4), 'm-', lw=2, label='F(%d, %d)'%(eval(f_1.get()),eval(f_2.get())))

    plt.xlabel("x")
    plt.ylabel('Probability')
    plt.title(r'PDF of Three Sampling Distribution')
    ax.legend(loc='best', frameon=False)
    plt.grid()
    plt.show()




#--------------------------------------------------------------------------------------------------------

#                              主界面

# 初始化主窗口
main_window = tk.Tk()
main_window.title("概率论可视化界面")
main_window.maxsize(700, 500)
main_window.minsize(700, 500)
main_window.resizable(0, 0)  # 窗口固定



#------------------------------------------------------------------------------------------------------------

#                                            按钮设置

# 选择函数图像按钮
tk.Button(main_window, text="蒙特卡洛方法（求圆周率）", width=20, command=fun1) \
    .grid(row=1, column=0, padx=10, pady=5)
tk.Button(main_window, text="泊松定理", width=20, command=fun2) \
    .grid(row=2, column=0, padx=10, pady=5)
tk.Button(main_window, text="指数分布", width=20, command=fun3) \
    .grid(row=3, column=0, padx=10, pady=5)
tk.Button(main_window, text="正态分布（一维）", width=20, command=fun4) \
    .grid(row=4, column=0, padx=10, pady=5)
tk.Button(main_window, text="正态分布（二维）", width=20, command=fun5) \
    .grid(row=5, column=0, padx=10, pady=5)
tk.Button(main_window, text="卡方分布", width=20, command=fun6) \
    .grid(row=9, column=0, padx=10, pady=5)
tk.Button(main_window, text="三大抽样分布", width=20, command=fun7) \
    .grid(row=11, column=0, padx=10, pady=5)
# tk.Button(main_window, text="f分布", width=20, command=showF_Distribution(main_window)) \
#     .grid(row=11, column=0, padx=10, pady=5)

# 退出按钮
tk.Button(main_window, text="退出", bg="black", fg="white", width=20, command=main_window.quit) \
    .grid(row=20, column=0, padx=10, pady=5)



#------------------------------------------------------------------------------------------------

#                                        文本框输入提示



# 蒙特卡洛方法（求圆周率）
tk.Label(main_window, text="n:").grid(row=1, column=1)
tk.Label(main_window,text = "答案:").grid(row = 1,column = 3)
# 泊松定理
tk.Label(main_window, text="n:").grid(row=2, column=1)
tk.Label(main_window, text="%c:" % chr(955)).grid(row=2, column=3)
# 指数分布
tk.Label(main_window, text="%c:" % chr(955)).grid(row=3, column=1)
# 正态分布（一维）
tk.Label(main_window, text="%c:" % chr(956)).grid(row=4, column=1)
tk.Label(main_window, text="%c:" % chr(948)).grid(row=4, column=3)
# 正态分布（二维）
tk.Label(main_window, text="%c:" % chr(956)).grid(row=5, column=1)
tk.Label(main_window, text="注意：这里根据函数只需要输入%c的值即可" % chr(948)).grid(row=6, column=0)
tk.Label(main_window, text="%c:" % chr(948)).grid(row=6, column=1)
tk.Label(main_window, text="%c:" % chr(961)).grid(row=7, column=1)
# 卡方分布
tk.Label(main_window, text="n:").grid(row=9, column=1)

#三大抽样分布
tk.Label(main_window, text="t分布参数1:").grid(row=11, column=1)
tk.Label(main_window, text="f分布参数1:").grid(row=12, column=1)
tk.Label(main_window, text="f分布参数2:").grid(row=12, column=3)


#指引
tk.Label(main_window, text = "使用指南：").grid(row = 12, column =0)
tk.Label(main_window, text = "1.在所求分布右侧输入相对应参数").grid(row = 13, column =0)
tk.Label(main_window, text = "2.点击分布所属按钮得到相对应函数图像或者答案").grid(row = 14, column =0)

#----------------------------------------------------------------------------------

#                                            文本框



# 蒙特卡洛方法（求圆周率）
m_1 = tk.Entry(main_window)
m_1.grid(row=1, column=2)
m_1.insert(0, "10")
m_ans = tk.Entry(main_window)
m_ans.grid(row=1, column=4)

# 泊松定理
b_1 = tk.Entry(main_window)
b_1.grid(row=2, column=2)
b_1.insert(0, "8")
b_2 = tk.Entry(main_window)
b_2.grid(row=2, column=4)
b_2.insert(0, "4")


# 指数分布
z_1 = tk.Entry(main_window)
z_1.grid(row=3, column=2)
z_1.insert(0, "0.5")

# 正态分布（一维）
z1_1 = tk.Entry(main_window)
z1_1.grid(row=4, column=2)
z1_1.insert(0, "0")
z1_2 = tk.Entry(main_window)
z1_2.grid(row=4, column=4)
z1_2.insert(0, "1")

# 正态分布（二维）
z2_1 = tk.Entry(main_window)
z2_1.grid(row=5, column=2)
z2_1.insert(0, "10")
z2_2 = tk.Entry(main_window)
z2_2.grid(row=5, column=4)
z2_2.insert(0, "10")
z2_3 = tk.Entry(main_window)
z2_3.grid(row=6, column=2)
z2_3.insert(0, "10")
z2_4 = tk.Entry(main_window)
z2_4.grid(row=6, column=4)
z2_4.insert(0, "10")
z2_5 = tk.Entry(main_window)
z2_5.grid(row=7, column=2)
z2_5.insert(0, "10")

# 卡方分布
k_1 = tk.Entry(main_window)
k_1.grid(row=9, column=2)
k_1.insert(0, "10")

#三大抽样分布
t_1 = tk.Entry(main_window)
t_1.grid(row=11, column=2)
t_1.insert(0, "5")
f_1 = tk.Entry(main_window)
f_1.grid(row=12, column=2)
f_1.insert(0, "30")
f_2 = tk.Entry(main_window)
f_2.grid(row=12, column=4)
f_2.insert(0, "5")




#---------------------------------------------------------------



#保持程序运行
main_window.mainloop()