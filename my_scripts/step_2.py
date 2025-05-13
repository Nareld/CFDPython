import numpy as np
import matplotlib.pyplot as plt

# define the number of points and step size in space
nx = 41
dx = 2 / (nx - 1)

# define the number of time steps and step size in time
nt = 25
dt = .025

# wavespeed assumption
# c = 1.0 # no linear convection

# define the initial conditions as a function of space
u = np.ones(nx)
u[int(.5 / dx):int(1 / dx + 1)] = 2.0 # here we are setting u = 2 between 0.5 and 1 as per our I.C.s

# plot the initial conditions
# 创建子图画布
fig = plt.figure(figsize=(12, 5))  # 设置画布尺寸

# 初始条件子图
ax1 = fig.add_subplot(1, 2, 1)  # 1行2列的第1个子图
ax1.plot(np.linspace(0, 2, nx), u)
ax1.set_title('Initial Conditions')  # 设置子图标题

# define the solution as a function of space and time
un = np.ones(nx) #initialize a temporary array

for n in range(nt):  #loop for values of n from 0 to nt, so it will run nt times
    un = u.copy() ##copy the existing values of u into un
    for i in range(1, nx): ## then we'll iterate through the array, but we can't go all the way to the end (the last point is nx-1)
        u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i-1]) ## this is the discretized equation for the 1D convection equation

# plot the solution
# 结果子图
ax2 = fig.add_subplot(1, 2, 2)  # 1行2列的第2个子图
ax2.plot(np.linspace(0, 2, nx), u)
ax2.set_title('After 25 Time Steps') 

plt.tight_layout()  # 自动调整子图间距
plt.show()  # 只需调用一次show