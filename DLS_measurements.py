"""
Program to plot measurements obtained from DLS experiments
"""


import csv
import sys
from matplotlib import pyplot as plt
import numpy as np

filename = sys.argv[1]
f=open(filename)
reader = list(csv.reader(f,delimiter=','))
columns = len(reader[0])
x = np.log([float(row[0]) for row in reader if not str(row[0][0]).isalpha()])
y=[[row[i] for row in reader if not str(row[1][0]).isalpha()] for i in range(1,columns)]
for i in range(len(y)):
	plt.scatter(x,y[i],label="med%s" % i )

plt.legend(loc="upper right")	
plt.show()
