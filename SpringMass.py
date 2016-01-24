import numpy
import matplotlib.pyplot

#setting physical constants

c = 5   #k/m ratio
x0 = 3  #resting length of spring mass

#time constraints
dur = 30
dt = .05
tot_incr = int(dur/dt) + 1

#initialize arrays for position, velocity, acceleration

X = numpy.zeros(tot_incr)

V = numpy.zeros(tot_incr)

A = numpy.zeros(tot_incr)

#Setting initial velocity, position

X[0] = x0*1.5
V[0] = 0

#Computing Position

for t in range(0, tot_incr-1):
    A[t] = c*(x0 - X[t])
    V[t+1] = V[t] + A[t]*dt
    X[t+1] = X[t] + (V[t+1] + V[t])*dt/2

print(X)

matplotlib.pyplot.plot(X)
