#!/usr/bin/env python
# coding: utf-8

# In[9]:


from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
# Physics 216
# Plotting code to use the whole year!
# Jaylene Naylor
# September 2015, modified Sept 2017, August 2018
# -------------------------------------------#

# Import packages and libraries needed and give them shortcut names

# -------------------------------------------#
# Data Section - Create Arrays for data. Perform necessary calculations
# CHANGE THE VARIABLE NAMES and numbers to match your data
xvariable_changeme = np.array([-2.69,-2.77,-2.85,-2.94,-3.05,-3.15,-3.28,-3.42,-3.59,-3.79,-4.38,-4.89])  # what are units?
yvariable_changeme = np.array([1.89,1.72,1.02,1.51,2.10,1.81,2.29,3.04,2.70,3.33,4.76,4.25])  # what are units?
#y = r mid
#x = ln
# --------------------------------------------#
# Create arrays for uncertainties
# CHANGE THE VARIABLE NAME and numbers to match your data
err_yvariable_changeme = np.array([.01,.011,.012,.013,.014,.016,.018,.021,.025,.031,.039,.055])

# --------------------------------------------#
# Re-assign variables as x, y, dy so that the following code may remain generic

x = xvariable_changeme  # this should be the array you want to plot on the x axis
y = yvariable_changeme
dy = err_yvariable_changeme 
# this should be your error in y array= 

# ----------------------------------------------#
# Don't need to change anything in this section!

# Find the intercept and slope, b and m, from Python's polynomial fitting function
b, m = np.polynomial.polynomial.polyfit(x, y, 1, w=dy)
# Write the equation for the best fit line based on the slope and intercept
fit = b + m * x


# Calculate the error in slope and intercept
# def Delta(x, dy) is a function, and we will learn how to write our own at a later date. They are very useful!
def Delta(x, dy):
    D = (sum(1 / dy ** 2)) * (sum(x ** 2 / dy ** 2)) - (sum(x / dy ** 2)) ** 2
    return D


D = Delta(x, dy)

dm = np.sqrt(1 / D * sum(1 / dy ** 2))  # error in slope
db = np.sqrt(1 / D * sum(x ** 2 / dy ** 2))  # error in intercept


# Calculate the "goodness of fit" from the linear least squares fitting document
def LLSFD2(x, y, dy):
    N = sum(((y - b - m * x) / dy) ** 2)
    return N


N = LLSFD2(x, y, dy)

# -----------------------------------------------------------------------#
# Plot data on graph. Plot error bars and place values for slope, error in slope and goodness of fit on the plot using "annotate"
plt.figure(figsize=(15, 10))

plt.plot(x, fit, color='green', linestyle='--')
plt.scatter(x, y, color='blue', marker='o')

# create labels  YOU NEED TO CHANGE THESE!!!
plt.xlabel('ln(rmid/1m)')
plt.ylabel('ln(E/1V)')
plt.title('Electric Fields Variance')

plt.errorbar(x, y, yerr=dy, xerr=None, fmt="none")  # don't need to plot x error bars

plt.annotate('Slope () = {value:.{digits}E}'.format(value=m, digits=2),
             (0.05, 0.9), xycoords='axes fraction')

plt.annotate('Error in Slope () = {value:.{digits}E}'.format(value=dm, digits=1),
             (0.05, 0.85), xycoords='axes fraction')

plt.annotate('Goodness of fit = {value:.{digits}E}'.format(value=N, digits=2),
             (0.05, 0.80), xycoords='axes fraction')

plt.show()


# In[ ]:





# In[ ]:




