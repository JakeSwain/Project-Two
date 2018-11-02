# Input:
# 1. The XYZ vector directions of the hostile missle
# 2. The XYZ initial point of the hostile missle
# 3. The velocity of the hostile missle
# Output:
# The angle on the XY plane and the angle upward adjustments

# importing sympy and numpy
from sympy import *
import numpy as np

# first making a function that will be used later
# This function will be used once the collsion point is found
# It will output the missle direction in the form of angles
def direction(x_pos_col, y_pos_col, z_pos_col):
# finding the direction that my missle must fire using the collision point and the origin
    x_dir_good = x_pos_col - 0
    y_dir_good = y_pos_col - 0
    z_dir_good = z_pos_col - 0

# using direction of my missle finding angle that needed to be fired on xy
# using differnt trig cases and in each quadrent from 1 to 4
    if x_dir_good > 0 and y_dir_good > 0:
        angle_xy_plane = tan(y_dir_good / x_dir_good) + 0
        angle_dir = 'North East'

    if x_dir_good < 0 and y_dir_good > 0:
        angle_xy_plane = tan(x_dir_good / y_dir_good) + 90
        angle_dir = 'North West'

    if x_dir_good < 0 and y_dir_good < 0:
        angle_xy_plane = tan(y_dir_good / x_dir_good) + 180
        angle_dir = 'South West'

    if x_dir_good > 0 and y_dir_good < 0:
        angle_xy_plane = tan(x_dir_good / y_dir_good) + 270
        angle_dir = 'South East'

# finding angle in z direction
# fining hyponotouse by using x and y direction and distance formula then trig
# multiply by 10 * pi since the calculation will provide decimal in radians
    hypo = (x_dir_good**2 + y_dir_good**2)
    angle_up = tan(hypo / z_dir_good) * 10 * 3.14

# printing out results
    print ('adjust your missle', angle_xy_plane, 'degrees', angle_dir, 'and', angle_up, "degrees upward")

# defining new function for the first inpugts
def missle(x_dir_bad, y_dir_bad, z_dir_bad, x_pos_bad, y_pos_bad, z_pos_bad, vel_bad):

# finding the scale to multiply the direction based on magnitude and speed
    mag_bad = ((x_dir_bad **2) + (y_dir_bad **2) + (z_dir_bad  **2)) **.5
    k_bad = vel_bad / mag_bad

# using the dot product in order to find best perpentdicluar bisector (closest line)
# manipulate (x_pos_col * x_dir_bad) + (y_dir_bad * y_pos_col) + (z_dir_bad * z_pos_col) = 0
# split into numerator and domonitor to save space
    num = ((x_dir_bad * x_pos_bad) + (y_dir_bad * y_pos_bad) + (z_dir_bad * z_pos_bad))
    dom = k_bad * (x_dir_bad**2 + y_dir_bad**2 + z_dir_bad**2)

# finding the time where missle is closest to the origin
    time = num/dom

# using time in the parameter equations to find the cordnate of the collision
    x_pos_col = x_pos_bad + time * (k_bad * x_dir_bad)
    y_pos_col = y_pos_bad + time * (k_bad * y_dir_bad)
    z_pos_col = z_pos_bad + time * (k_bad * z_dir_bad)

# feeding values into the fuction previously made to find the angle
    direction(x_pos_col, y_pos_col, z_pos_col)


# in this example an hostile missle is incoming:
# at direction vector of 10 in x direction, 10 in the y direction, and 50 in the z direction
# from 100 kilometers west, 50 kilometers north, and from a silo 1 kilometer undergound
# 10 meters per second
missle(10, 10 ,50, -100 , 50 , -1 , 10 )
# outputs that the your missle would need to be rotated 29 degrees north and 91 degrees northwest to intersect
