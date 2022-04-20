# It is sometimes illuminating to plot things relative to a baseline, as
# seen in Figure 22-4. Modify plot_housing to produce such plots. The bars
# below the baseline should be in red. Hint: use the bottom keyword
# argument to plt.bar.

import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
import scipy.stats

# set line width
plt.rcParams['lines.linewidth'] = 4
# set font size for titles
plt.rcParams['axes.titlesize'] = 16
# set font size for labels on axes
plt.rcParams['axes.labelsize'] = 16
# set size of numbers on x-axis
plt.rcParams['xtick.labelsize'] = 16
# set size of numbers on y-axis
plt.rcParams['ytick.labelsize'] = 16
# set size of ticks on x-axis
plt.rcParams['xtick.major.size'] = 7
# set size of ticks on y-axis
plt.rcParams['ytick.major.size'] = 7
# set size of markers, e.g., circles representing points
plt.rcParams['lines.markersize'] = 10
# set number of times marker is shown when displaying legend
plt.rcParams['legend.numpoints'] = 1
# Set size of type in legend
plt.rcParams['legend.fontsize'] = 14


def plot_housing(impression):
    """Assumes impression a str. Must be one of 'flat',
          'volatile,' and 'fair'
        Produce bar chart of housing prices over time"""
    labels, prices = ([], [])
    with open('midWestHousingPrices.csv', 'r') as f:
        #Each line of file contains year quarter price
        #for Midwest region of U.S.
        for line in f:
            year, quarter, price = line.split(',')
            label = year[2:4] + '\n Q' + quarter[1]
            labels.append(label)
            prices.append(int(price)/1000)
    quarters = np.arange(len(labels)) #x coords of bars
    width = 0.8 #Width of bars
    baseline = 200
    bars = plt.bar(quarters, np.array(prices) - baseline, width,
                    bottom = baseline)
    for b in bars:
        if b.get_height() < 0:
            b.set_color('r')
    plt.axhline(200)
    plt.xticks(quarters+width/2, labels)
    plt.title('Housing Prices in U.S. Midwest')
    plt.xlabel('Quarter')
    plt.ylabel('Average Price ($1,000\'s)')
    if impression == 'flat':
        plt.ylim(1, 500)
    elif impression == 'volatile':
        plt.ylim(180, 220)
    elif impression == 'fair':
        plt.ylim(150, 250)
    else:
        raise ValueError
