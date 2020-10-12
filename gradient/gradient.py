# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import matplotlib.pyplot as plt

#数据集点的数量
m = 20

#点的x坐标和虚拟值
X0 = np.ones((m,1))
X1 = np.arange(1,m+1).reshape(m,1)
X = np.hstack((X0,X1))                 #hstack函数水平方向平铺

#y坐标
y = np.array([3,4,5,5,2,4,7,8,11,8,12,11,13,13,16,17,18,17,19,21]).reshape(m,1)

#学习率
alpha = 0.02

def error_function(theta,X,y):
    '''error function J definition'''
    diff = np.dot(X,theta) - y       #diff是目标值与预测值之间的差值
    return (1./(2*m)) * np.dot(np.transpose(diff),diff)

def gradient_function(theta,X,y):
    '''Gradient of the function J definition.'''
    diff = np.dot(X,theta) - y
    return (1./m) * np.dot(np.transpose(X),diff)

def gradient_descent(X,y,alpha):
    '''Perform gradient descent.'''
    theta = np.array([1,2]).reshape(2,1)
    gradient = gradient_function(theta,X,y)
    while not np.all(np.absolute(gradient) <= 1e-5):
        theta = theta - alpha * gradient
        gradient = gradient_function(theta,X,y)
    return theta


optimal = gradient_descent(X, y, alpha)
print('optimal:',optimal)
print('error function:',error_function(optimal,X,y)[0,0])


x = np.linspace(0,20,500)
test_y = optimal[0] + x*optimal[1]

plt.figure()
plt.plot(x, test_y)
plt.scatter(X1, y, color='red')
plt.show()





















    
