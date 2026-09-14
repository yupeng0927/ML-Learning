import numpy as np
import matplotlib.pyplot as plt
#返回在给定范围内用均匀间隔的值填充的一维数组。
plt.figure(figsize=(10, 6))
x = np.arange(0, 10,0.01)
y1=np.sin(x)
# 绘制曲线
plt.title('y=sinx')
plt.plot(x,y1,label='y=cosx')

y2 = np.cos(x)
# plt.subplot(2,1,2)
plt.plot(x,y2,label=' y=sinx',linestyle='--')
plt.legend()
plt.show()




