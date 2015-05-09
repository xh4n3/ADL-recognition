import time,csv,scipy
from time import mktime
import numpy as np


str="2011-11-28 02:27:59"
a=time.strptime(str,"%Y-%m-%d %H:%M:%S")
mktime(a)

starttime=[]
endtime=[]
content=[]

with open('OrdoneA.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		i=0
		for item in row:
			if i == 0:
				starttime.append(mktime(time.strptime(item,"%Y-%m-%d %H:%M:%S")))
			if i == 1:
				endtime.append(mktime(time.strptime(item,"%Y-%m-%d %H:%M:%S")))
			if i == 2:
				content.append(item)
			i+=1

print starttime
print endtime
print content

print content.index('Cooktop')

while slicestart+60 < endtime[-1]:
	count=0
	for i in range(0,60):
		if (t2-slicestart-i) and (origin+i-t1):
			count+=1
	y.append(count)

#variable={}
#variable['starttime']=starttime[0]
#variable['endtime']=endtime[-1]

#now=starttime[0]
