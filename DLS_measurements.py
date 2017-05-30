"""
Program to plot measurements obtained from DLS experiments
"""


import csv
import sys
from matplotlib import pyplot as plt
import numpy as np
import os


def plot_DLS_measurements(directory):
	f=open(directory)
	reader = list(csv.reader(f,delimiter=','))
	if len(reader) > 61:
		reader = reader[:-1]
	columns = len(reader[0])
	x = [row[0] for row in reader if not str(row[0][0]).isalpha()]
	y=[[row[i] for row in reader if not str(row[i][0]).isalpha()] for i in range(1,columns)]
	for i in range(len(y)):
		plt.semilogx(x,y[i],'r',label="med%s" % i,)
	plt.legend(loc="upper right")	
	plt.savefig("./figures/%s" % (filename[:-4]))
	plt.close()

directories = next(os.walk("."))[1]
for directory in directories:
	cur_dir = directory
	files= next(os.walk("./%s" % (cur_dir)))[2]
	for filename in files:
		if "all" in filename and ".csv" in filename:
			plot_DLS_measurements("./"+cur_dir+"/"+filename)
