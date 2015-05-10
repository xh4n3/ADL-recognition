import time,csv,scipy
from scipy import cluster
from time import mktime, gmtime, strftime
import numpy as np

starttime=1322447279
endtime=1323674541
deltat=60
dic=[]

def check(t):
	return labels[int((t-starttime)/deltat)]

labels=scipy.load('labels.npy')

with open('OrdoneA_Label.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		i=0
		for item in row:
			if i == 0:
				start=mktime(time.strptime(item,"%Y-%m-%d %H:%M:%S"))
			if i == 1:
				stop=mktime(time.strptime(item,"%Y-%m-%d %H:%M:%S"))
			if i == 2:
				dic.append((start,stop))
			i+=1

result={}

for tslice in dic:
	result[tslice]={}
	current=tslice[0]
	while current <= tslice[1]:
		if check(current) not in result[tslice]:
			result[tslice][check(current)]=0
		result[tslice][check(current)]+=1
		current+=1