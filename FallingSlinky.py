#Initialize Variables

import numpy
     
h = 1000      # initial height
l = 12        # length of the spring
n = 3         # number of masses
d = l/n       # resting displacement between each mass
g = -9.8      # acceleration due to gravity in m/s/s
c = 1         # k/m constant for spring

# duration of time (s)
dur = 1

# time increment (s)
dt = .1       

#total number of time increments (preparing array)
#the +1 below accounts for the full time,
#as the 0th second is naturally included in the caluclation

tot_incr = int(dur/dt) + 1



# Initializing Arrays

X = numpy.zeros((n, tot_incr))

V = numpy.zeros((n, tot_incr))

A = numpy.zeros((n, tot_incr))

#Setting initial positions
for i in range(n):
    X[i][0] = h - d*i
    
#For time increment
for t in range(0, tot_incr-1):

    #This block does the following for each mass
    #1. Computes acceleration due to current position (known from previous iteration)
    #2. Computes future velocity with knowledge of current acceleration
    #3. Computes future position with knowledge of future and current velocity
    #4. Print current position, acceleration, velocities

    #Case 1: Top Mass

        
    #Compute positional change due to accleration gravity, spring forces
    xb0 = X[1][t] - d
    #Spring force acceleration due to this moment's position
    a_Fb = c*(xb0 - X[0][t])

    #Compute current acceleration
    A[0][t] = a_Fb + g

    #Compute new velocity
    V[0][t+1] = V[0][t] + (A[0][t])*dt

    #Change in Position
    X[0][t+1] = X[0][t] + (V[0][t+1]+V[0][t])*dt/2

    #Case 2: Middle Masses        
    for i in range(1, n-1):

        #Constants

        #Compute positional change due to accleration gravity, spring forces
        xb0 = X[i+1][t] - d
        xt0 = X[i-1][t] + d

        #Spring force acceleration due to this moment's position
        a_Fb = c*(xb0 - X[i][t])
        a_Ft = c*(xt0 - X[i][t])

        #Compute current acceleration
        A[i][t] = a_Fb + a_Ft + g

        #Compute new velocity
        V[i][t+1] = V[i][t] + (A[i][t])*dt

        #Change in Position
        X[i][t+1] = X[i][t] + (V[i][t+1]+V[i][t])*dt/2

    #Case 3: Bottom Mass

    #Compute positional change due to accleration gravity, spring forces
    xt0 = X[n-2][t] + d

    #Spring force acceleration due to this moment's position
    a_Ft = c*(xt0 - X[n-1][t])

    #Compute current acceleration
    A[n-1][t] = a_Ft + g

    #Compute new velocity
    V[n-1][t+1] = V[n-1][t] + (A[n-1][t])*dt

    #Change in Position
    X[n-1][t+1] = X[n-1][t] + (V[n-1][t+1]+V[n-1][t])*dt/2
    
print(X)
