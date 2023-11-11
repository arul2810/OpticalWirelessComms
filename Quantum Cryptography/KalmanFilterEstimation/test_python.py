import numpy as np
import matplotlib.pyplot as matplot
import math

from numpy.lib.shape_base import expand_dims

d_time = 1.5625e-12

print ("Entered D_time value is : ", d_time)

# Code verified to work until here

#calculation loop

current_time = 0 #start_time
current_phase = 1.5708
current_amplitude = 1

Signal_Freq = 500000000 #signal frequency

StopTime = 1.4e-8 #end_time

sine_array = []
time_array = []

while ( current_time < StopTime ) :

    temp = math.sin ( 2* math.pi * current_time * Signal_Freq + current_phase )
    current_time = current_time + d_time


    sine_array.append (temp)
    time_array.append (current_time)


matplot.plot(time_array,sine_array)   

print("I am updated")