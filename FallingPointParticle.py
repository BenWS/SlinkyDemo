#Initialize Variables

x_i = 100     # initial position
v_i = 0       # initial velocity
g = -9.8      # acceleration due to gravity
t = 0         # initial time
dt = .1       # time increment

#Computing Position using the Runge-Kutta method of numerical integration

while (x_i > 0):
    t = t + dt
    v_f = v_i + g*dt
    x_f = x_i + (v_i+v_f)*dt/2
    
    #Setting initial values to final
    v_i = v_f
    x_i = x_f
    print (x_f, v_f, t)
