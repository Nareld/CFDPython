import numpy                 #numpy is a library for array operations akin to MATLAB
import matplotlib.pyplot as plt   #matplotlib is 2D plotting library

def linearconv(nx):
    dx = 2 / (nx - 1)
    nt = 20    #nt is the number of timesteps we want to calculate
    dt = .025  #dt is the amount of time each timestep covers (delta t)
    c = 1
    sigma = .5  # CFL condition

    dt = sigma * dx

    u = numpy.ones(nx)      #defining a numpy array which is nx elements long with every value equal to 1.
    u[int(.5/dx):int(1 / dx + 1)] = 2  #setting u = 2 between 0.5 and 1 as per our I.C.s

    un = numpy.ones(nx) #initializing our placeholder array, un, to hold the values we calculate for the n+1 timestep

    for n in range(nt):  #iterate through time
        un = u.copy() ##copy the existing values of u into un
        for i in range(1, nx):
            u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
        
    plt.plot(numpy.linspace(0, 2, nx), u)

linearconv(41)  # call the function with 41 grid points.
linearconv(61)  # call the function again with 61 grid points.
linearconv(81)  # call the function again with 81 grid points.

plt.show()