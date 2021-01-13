import numpy as np
from numpy import *
import sys
import time 
import matplotlib.pyplot as plt

# Code for plotting graph of Number of Hospitals and Execution time
# For each value of hospital, code was run three times and the average time was taken
hospitals = [1,3,40,80,160,320]
time = [0.995,1.998, 5.983, 18.949, 74.399, 295.661]
fig,plots = plt.subplots()
plots.plot(hospitals, time)
plots.set(xlabel = 'Number of Hospitals', ylabel='Execution Time (in ms)', title = 'Trend of Number of Hospitals with Execution Time')
plots.grid()
fig.savefig("time.png")
