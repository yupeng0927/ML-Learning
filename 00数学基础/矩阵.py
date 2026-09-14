import numpy as np

a=np.array([[1,2],[4,5]])
b=np.array([[1,2],[4,5]])

'''矩阵的向量化'''
print(a.flatten())
print(a.ravel())

# 3）矩阵内积
print('内积',np.sum(a * b))

print('内积',np.dot(a.flatten(), b.flatten()))#对位想乘，并相加

# 矩阵乘法 第一行乘以第一列
print('矩阵乘法\n',a.dot(b))
print('矩阵乘法\n',a @ b)

# 矩阵 Hadamard 积 对位相乘
print("Hadamard积：\n",np.multiply(a, b))
print("Hadamard积：\n", a * b)


# 矩阵 Kronecker 积（克罗内克积，张量积）

kronecker = np.kron(a, b)
print("Kronecker积：\n", kronecker)

# 一维数组
arr1 =np.array([[1, 2, 3]])# 形状为 (3,)
# 二维数组
arr2 = np.array([[4], [5], [6]])# 形状为 (3, 1)
# 对 arr1 应用规则 1，在其形状最左边补 1，变为 (1, 3)  [[1,2,3]]
# 此时 arr1 形状 (1, 3) 和 arr2 形状 (3, 1) 满足广播条件
result = arr1 + arr2
print("规则 1 示例结果：\n", result)


a=np.array([1,2,3])
b=np.array([1,2,3])
print(np.dot(a, b))

a=np.array([1,2,3])
b=np.array([1,2,3])
print(np.dot(a, b))#一维数组没有行或列的概念，因此对它进行转置（.T）不会改变它的形状，它依然是一维数组。

print(a - b)
