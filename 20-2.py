# Finger exercise: In a vacuum, the speed of a falling object is defined
# by the equation v = v0 + gt, where v0 is the initial velocity of the
# object, t is the number of seconds the object has been falling, and g is
# the gravitational constant, roughly 9.8 m/sec2 on the surface of the
# Earth and 3.711 m/ sec2 on Mars. A scientist measures the velocity of a
# falling object on an unknown planet. She does this by measuring the
# downward velocity of an object at different points in time. At time 0,
# the object has an unknown velocity of v0.
#
# Implement a function that fits a model to the time and velocity data
# and estimates g for that planet and v0 for the experiment. It should
# return its estimates for g and v0, and also r-squared for the model.

import math
import random
import numpy


def create_fall_data(g=random.randint(5, 15), v0=random.randint(5, 15)):
    """Creates a sorted list of tuples for a given g and v0"""
    fall_data = []
    start_time = random.randint(2, 5)
    duration = start_time + random.randint(10, 15)
    print(f'g={g},v0={v0}')
    for i in range(start_time, start_time + duration):
        v = v0 + g * i
        fall_data.append((i, v))
    return fall_data

def r_squared(measured, predicted):
    """Assumes measured a one-dimensional array of measured values
               predicted a one-dimensional array of predicted values
       Returns coefficient of determination"""
    estimated_error = ((predicted - measured)**2).sum()
    mean_of_measured = measured.sum()/len(measured)
    variability = ((measured - mean_of_measured)**2).sum()
    return 1 - estimated_error/variability

def estimate_fall_variables(fall_data=[]):
    """Creates a model of the acceration of a physical object dropped
        in a place with positive gravity and initial velocity
        Assumes fall_data is a sorted list of tuples containing fall data (format: time,velocity) as input
        Returns a list containing estimated g, v0 and r**2 for the model"""
    times, velocities, predicted_velocities=[],[],[]
    for i in range(len(fall_data)):
        times.append(fall_data[i][0])
        velocities.append(fall_data[i][1])
    fit = numpy.polyfit(times,velocities,1)
    for i in times:
        predicted_velocities.append(fit[0]*i+fit[1])
    return([fit[0], fit[1], r_squared(numpy.array(velocities),numpy.array(predicted_velocities))])
