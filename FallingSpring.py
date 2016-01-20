#This program does the following for a spring mass
#1. Compute acceleration due to current position (known from previous iteration)
#2. Compute future velocity with knowledge of current acceleration
#3. Compute future position with knowledge of future and current velocity
#4. Print current position, acceleration, velocities

#Constants

c = 1
x0 = 

#Compute positional change due to accleration gravity, spring forces
xb0 = x[i-1][t] + x0
xt0 = x[i+1][t] - x0

#Spring force acceleration due to this moment's position
a_Fb = c(xb0 - x[i][t])
a_Ft = c(xt0 - x[i][t])

#Compute current acceleration
A[i][t] = a_Fb + a_Ft + g

#Compute new velocity
V[i][t+1] = V[i][t] + (A[i][t])*dt

#Change in Position
X[i][t+1] = X[i][t] + (V[i][t+1]+V[i][t])*dt/2
