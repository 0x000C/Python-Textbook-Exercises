#%%
import numpy as np
import matplotlib.pyplot as plt
import math
#set line width
plt.rcParams['lines.linewidth'] = 4
#set font size for titles 
plt.rcParams['axes.titlesize'] = 18
#set font size for labels on axes
plt.rcParams['axes.labelsize'] = 16
#set size of num_bers on x-axis
plt.rcParams['xtick.labelsize'] = 16
#set size of num_bers on y-axis
plt.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
plt.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
plt.rcParams['ytick.major.size'] = 7
#set size of markers, e.g., circles representing points
plt.rcParams['lines.markersize'] = 10
#set num_ber of times marker is shown when displaying legend
plt.rcParams['legend.numpoints'] = 1
#Set size of type in legend
plt.rcParams['legend.fontsize'] = 14

def get_data(input_file):
    with open(input_file, 'r') as data_file:
        distances = []
        masses = []
        data_file.readline() #ignore header
        for line in data_file:
            d, m = line.split(',')
            distances.append(float(d))
            masses.append(float(m))
    return (masses, distances)

def fit_data(input_file):
    masses, distances = get_data(input_file)
    distances = np.array(distances)
    forces = np.array(masses)*9.81
    plt.plot(forces, distances, 'ko',
               label = 'Measured displacements')
    plt.title('Measured Displacement of Spring')
    plt.xlabel('|Force| (Newtons)')
    plt.ylabel('Distance (meters)')
    #find linear fit
    a,b = np.polyfit(forces, distances, 1)
    predicted_forces = np.concatenate((forces,[15]))
    predicted_distances = a*np.array(predicted_forces) + b    
    k = 1.0/a #see explanation in text
    plt.plot(predicted_forces, predicted_distances,
             label = 'Linear fit, k = ' + str(round(k, 5)))
    #find cubic fit
    fit = np.polyfit(forces, distances, 3)
    predicted_distances = np.polyval(fit, predicted_forces)
    plt.plot(predicted_forces, predicted_distances, 'k:', label = 'cubic fit')
    plt.legend(loc = 'best')

fit_data("springData.csv")