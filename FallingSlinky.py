#Initialize Variables

import numpy
     
h = 1000      # initial height
l = 30        # length of the spring
n = 10         # number of masses
d = l/n       # resting displacement between each mass
g = -9.8      # acceleration due to gravity in m/s/s
c = 7         # k/m constant for spring

#Initializing 
aFb = 0
aFt = 0

# duration of time (s)
dur = 5

# time increment (s)
dt = .1

#stretched length
d_stretched = 1.5*d

#total number of time increments (preparing array)
#the +1 below accounts for the full time,
#as the 0th second is naturally included in the caluclation
tot_incr = int(dur/dt) + 1



# Initializing Arrays

X = numpy.zeros((n, tot_incr))

V = numpy.zeros((n, tot_incr))

A = numpy.zeros((n, tot_incr))

#Integration function: computes for the mth mass provided

def compute(m):
    A[m][t] = a_Fb + a_Ft + g
    V[m][t+1] = V[m][t] + (A[m][t])*dt
    X[m][t+1] = X[m][t] + (V[m][t+1]+V[m][t])*dt/2
     

#Setting initial positions
for i in range(n):
    X[i][0] = h - d_stretched*i
    
#For time increment
for t in range(0, tot_incr-1):

    #This block does the following for each mass
    #1. Computes acceleration due to current position (known from previous iteration)
    #2. Computes future velocity with knowledge of current acceleration
    #3. Computes future position with knowledge of future and current velocity
    #4. Print current position, acceleration, velocities

    #Case 1: Top Mass

    xb0 = X[1][t] + d

    a_Ft = 0
    a_Fb = c*(xb0 - X[0][t])

    compute(0)

    #Case 2: Middle Masses        
    for i in range(1, n-1):

        #Constants

        xb0 = X[i+1][t] + d
        xt0 = X[i-1][t] - d

        a_Fb = c*(xb0 - X[i][t])
        a_Ft = c*(xt0 - X[i][t])

        compute(i)

    #Case 3: Bottom Mass

    xt0 = X[(n-1)-1][t] - d

    a_Ft = c*(xt0 - X[n-1][t])
    a_Fb = 0

    compute(n-1)
    
print(X)
