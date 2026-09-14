import numpy as np

#均匀分布

a=np.random.rand(5) #5个 0-1的浮点数
b=np.random.rand(2,3) #2维 0-1的浮点数
print(a)

#randint（下限，上限），不包含上限
a=np.random.randint(0,3,5) #0-3 5个数
print(a)
b=np.random.r andint(0,3,size=(3,2)) #0-3 5个数
print(b)

#正态分布
randn = np.random.randn(10) #标准正态分布，均值为0，方差为1,生成10个
randn1 = np.random.randn(2,5) #两行 5列
print(f'{randn=}')

#normal(均值，标准差，维度）
normal = np.random.normal(1, 0, size=(2, 3))
print(normal)
