import numpy as np
from scipy.optimize import curve_fit


# x = np.arange(0, 20)
# y=2*x**2 + np.random.randint(0, 100, (1,20))[0]
x = [160,170,180,190,200,210,220]
x = np.array(x)
y = [120,115,110,105,100,70,60]

#最小二乘法 平方和最小 2是多项式阶数 适合一元多项式
p = np.polyfit(x, y, 2)
print(np.poly1d(p))
y1 = p[0] * x**2 + p[1]*x + p[2]
y2 = y1.astype(np.int)

# #最小二乘法 适用范围更广 可以拟合任意函数，取决于fun怎么定义
# def fun(x, a):
#     return a * x**2
# p,cov = curve_fit(fun,x,y,1)
# y2 = fun(x,p[0])
# print(np.poly1d(p))

import matplotlib.pyplot as plt

plt.scatter(x, y,marker= 'x',lw = 1)
plt.plot(x, y1,c='r')
plt.plot(x, y2,c='green')
plt.show()