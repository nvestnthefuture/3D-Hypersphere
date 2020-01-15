import matplotlib.pyplot as plt
import numpy
import random
import math
from mpl_toolkits import mplot3d

"""
Name: Hypersphere 3D
Purpose: Produce a 3D image of a sampling
         of a circle segment & Test Values
Author: Jessica Byrd
Date: 12/05/2019
Version: 1.0
"""

"""Figure Plot ranges
Initialization & Declaration
"""
def figurePlot(ranges):
    numpy.random.seed(28394837)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    for index in range(1,1000):
        r = random.random()
        r = r * (ranges[1] - ranges[0])
        theta = random.random()
        theta = theta * (ranges[3] - ranges[2])
        phi = random.random()
        phi = phi * (ranges[5] - ranges[4])
        x = math.pow(r, (1.0/3.0)) * math.cos(theta) * math.sin(phi)
        y = math.pow(r, (1.0/3.0)) * math.sin(theta) * math.sin(phi)
        z = math.pow(r, (1.0/3.0)) * math.cos(phi)
        ax.scatter(x,y,z,color = "green")

    plt.show()

"""
--Ask user to enter the Lower and Upper Bounds of r, Theta and Phi
--ValueError message if incorrectly entered
"""
def getRBounds():
    ranges = []
    while(True):
        range = input('Enter the Lower Bound of r: ')
        try:
            range = float(range)
            ranges.append(range)
            break
        except ValueError:
            print('Error, Try again! You must enter a number for the Lower Bound of r!')

    while(True):

        range = input('Enter the Upper Bound of r: ')
        try:
            range = float(range)
            ranges.append(range)
            break
        except ValueError:
            print('Error, Try again! You must enter a number for the Upper Bound of r!')
    
    while(True):
        range = input('Enter the Lower Bound of Theta: ')
        try:
            range = float(range)
            ranges.append(range)
            break
        except ValueError:
            print('Error, Try again! You must enter a number for the Lower Bound of Theta!')

    while(True):

        range = input('Enter the Upper Bound of Theta: ')
        try:
            range = float(range)
            ranges.append(range)
            break
        except ValueError:
            print('Error, Try again! You must enter a number for the Upper Bound of Theta!')
    
    while(True):

        range = input('Enter the Lower Bound of Phi: ')
        try:
            range = float(range)
            ranges.append(range)
            break
        except ValueError:
            print('Error, Try again! You must enter a number for the Lower Bound of Phi!')

    while(True):

        range = input('Enter the Upper Bound of Phi: ')
        try:
            range = float(range)
            ranges.append(range)
            break
        except ValueError:
            print('Error, Try Again! You must enter a number for the Upper Bound of Phi!')

    print('\nThe range of r is from ' + str(ranges[0]) + ' to ' + str(ranges[1]))
    print('\nThe range of Theta is from ' + str(ranges[2]) + ' to ' + str(ranges[3]))
    return ranges
def main():
    ranges = getRBounds()
    figurePlot(ranges)
if __name__ == "__main__":
    main()


