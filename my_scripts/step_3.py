import numpy as np
from matplotlib import pyplot as plt

# 定义网格和时间步长
nx = 41
dx = 2 / (nx - 1)
nt = 20
nu = .3 #the value of viscosity
sigma = .2 #cfl number
dt = sigma * dx**2 / nu #dt is defined using sigma ... more later!

# 定义初始条件
u = np.ones(nx) #numpy function ones()
u[int(.5 / dx):int(1 / dx + 1)] = 2 #setting u = 2 between 0.5 and 1 as per our I.C.s

# 绘制初始条件
fig = plt.figure(figsize=(12, 5))  # 设置画布尺寸

# 初始条件子图
ax1 = fig.add_subplot(1, 2, 1)  # 1行2列的第1个子图
ax1.plot(np.linspace(0, 2, nx), u)  

# 定义解
un = np.ones(nx) #initialize a temporary array

for n in range(nt):  #loop for values of n from 0 to nt, so it will run nt times
    un = u.copy() ##copy the existing values of u into un
    for i in range(1, nx - 1):
        u[i] = un[i] + nu * dt / dx**2 * (un[i+1] - 2 * un[i] + un[i-1])

# 绘制结果
# 结果子图
ax2 = fig.add_subplot(1, 2, 2)  # 1行2列的第2个子图
ax2.plot(np.linspace(0, 2, nx), u)  
plt.tight_layout()  # 自动调整子图间距
plt.show()  # 只需调用一次show