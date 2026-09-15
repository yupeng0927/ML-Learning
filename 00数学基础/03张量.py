import numpy as np

'''
 张量可以视为多维数组
qwer
 例如：
 3维度张量的每个元素 都是一个矩阵
 '''

#张量的定义
tensor=np.array([[1,2,3],[4,5,6],[7,8,9]]) #2维
print(tensor.shape)

#离散梯度  每个索引位置的变化率
# 列：索引1位置，（5-1）/2（∆x）=2
# 索引0，（3-1）/1（∆x)=2

a=np.array([1,3,5,9,19,6,7])
print(np.gradient(a))#[ 2.   2.   3.   7.  -1.5 -6.   1. ]

print(np.gradient(tensor))#二维矩阵 ，在横纵 两个方向上的 梯度
