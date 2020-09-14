# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 12:26:30 2020

@author: micha
"""


#import mudules needed
import matplotlib.pyplot as plt
import numpy
'''
Set Constants in the equations 

Set the initial data v_x, v_y, x, y
    v_x = v_(x,i)
    v_y = v_(y,i)
    x = x_i
    y = y_i
    # the i denote the initial data provided in the lab

Set time step 
    dt = t  (some t given )
        
Create time array with given time step
    time = numpy.arange(0,1, dt)
    
    
Create arrays to record each v_x, v_y, x, y value   
    velocity_x = numpy.ones(len(time))
    velocity_y = numpy.ones(len(time))
    position_x = numpy.ones(len(time))
    position_y = numpy.ones(len(time))
    
Set initial data:
    velocity_x[0] = v_x
    velocity_y[0] = v_y
    position_x[0] = x
    position_y[0] = y
    

    
#updating velocities first since we use updated velocity in Eular-Cromer method
numerically integrate for v_(x,i+1) and v_(y,i+1) by a for loop and update
it in the array
    with result:
    v_（x,i+1） = -G*(M_s)*(x_i)*dt /r**3 + v_(x,i)
    v_（y,i+1） = -G*(M_s)*(y_i)*dt /r**3 + v_(y,i)
    x_(i+1) = dt*v_(x,i+1)+ x_i
    y_(i+1) = dt*v_(y,i+1)+ y_i
    
    for i in range of len(time):
        velocity_x [i+1]= -G*(M_s)*(x[i])*dt /r**3 + velocity_x[]
        velocity_y [i+1] += -G*(M_s)*(y[i])*dt /r**3 + v_y
        x[i+1]= dt*velocity_x[i+1]+ x
        y[i+1]= dt*velocity_y[i+1]+ y

Create plots using matplotlib.pyplot
    set labels, legend, and axis
    Create plot for velocity components vs. time and x vs. y using array above'''
    
    
    
#Part C codes

#Set constants
M_s = 1 #unit is solar mass 
G = 39.5 #AU^3/(M_S)/(year^2)

#set time step
dt = 0.0001 #year

#Create time array with time step 0.0001 and up to 1 year.
time = numpy.arange(0,1.0001, dt)

#Create arrays to record each v_x, v_y, x, y value   
velocity_x = numpy.ones(len(time))
velocity_y = numpy.ones(len(time))
x = numpy.ones(len(time))
y = numpy.ones(len(time))

#Set initial data
velocity_x[0] = 0 #AU/year
velocity_y[0] = 8.17 #AU/year
x[0] = 0.47 #AU
y[0] = 0 #AU                  
    

for i in range(0,len(time)-1):
    r = numpy.sqrt(x[i]**2+y[i]**2)
    velocity_x [i+1]= (-G*(M_s)*(x[i])*dt /(r**3)) \
               + velocity_x[i]
    velocity_y [i+1] = (-G*(M_s)*(y[i])*dt /(r**3)) + \
                        velocity_y[i]
    x[i+1]= dt*velocity_x[i+1]+ x[i]
    y[i+1]= dt*velocity_y[i+1]+ y[i]

#plot velocity_y vs. time
plt.figure()
plt.title("y-direction Velocity vs. Time Plot")
plt.ylabel("Velocity in y Direction (AU/year)")
plt.xlabel("Time (year)")
plt.plot(time, velocity_y)

#plot velocity_x vs. time 
plt.figure()
plt.title("x-direction Velocity vs. Time Plot") #title
plt.ylabel("Velocity in x Direction (AU/year)") #y-axis
plt.xlabel("Time (year)")   #x_axis
plt.plot(time, velocity_x)

#plot orbit x vs. y
plt.figure()
plt.title("Mercury Orbit (x vs. y Position) Plot")
plt.xlabel("Position in x Direction (AU)")
plt.ylabel("Position in y Direction (AU)")
plt.plot(x,y)



#Part D code:
#Set constants
M_s = 1 #unit is solar mass 
G = 39.5 #AU^3/(M_S)/(year^2)
alpha = 0.01 #AU^2

#set time step
dt = 0.0001 #year

#Create time array with time step 0.0001 and total of 1 year
time_rel = numpy.arange(0,1.0001, dt)

#Create arrays to record each v_x, v_y, x, y value   
velocity_x_rel = numpy.ones(len(time_rel))
velocity_y_rel = numpy.ones(len(time_rel))
x_rel = numpy.ones(len(time_rel))
y_rel = numpy.ones(len(time_rel))

#Set initial data
velocity_x_rel[0] = 0 #AU/year
velocity_y_rel[0] = 8.17 #AU/year
x_rel[0] = 0.47 #AU
y_rel[0] = 0 #AU                  
    

for i in range(0,len(time)-1):
    r = numpy.sqrt(x_rel[i]**2+y_rel[i]**2)
    velocity_x_rel [i+1]= (-G*(M_s)*(x_rel[i])*(1+alpha/(r**2))*dt/(r**3)) \
               + velocity_x_rel[i]
    velocity_y_rel [i+1] = (-G*(M_s)*(y_rel[i])*(1+alpha/(r**2))*dt/(r**3)) \
                + velocity_y_rel[i]
    x_rel[i+1]= dt*velocity_x_rel[i+1]+ x_rel[i]
    y_rel[i+1]= dt*velocity_y_rel[i+1]+ y_rel[i]
    
#plot velocity_y vs. time
plt.figure()
plt.title("y-direction Velocity vs. Time Plot")
plt.ylabel("Velocity in y Direction (AU/year)")
plt.xlabel("Time (year)")
plt.plot(time_rel, velocity_y_rel)

#plot velocity_x vs. time 
plt.figure()
plt.title("x-direction Velocity vs. Time Plot") #title
plt.ylabel("Velocity in x Direction (AU/year)") #y-axis
plt.xlabel("Time (year)")   #x_axis
plt.plot(time_rel, velocity_x_rel)

#plot orbit x vs. y
plt.figure()
plt.title("Mercury Orbit (x vs. y Position) Plot")
plt.xlabel("Position in x Direction (AU)")
plt.ylabel("Position in y Direction (AU)")
plt.plot(x_rel,y_rel)




