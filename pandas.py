import time,csv,scipy
from scipy import sign,integrate
from time import mktime
import pandas as pd
import numpy as np
from pandas import to_datetime


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

s = to_datetime(starttime, unit='s')
e = to_datetime(endtime, unit='s')
ts1 = pd.Series(content, s)
print ts1
ts2 = pd.Series(content, e)
print ts2
daterange = pd.date_range(s[0], e[0], freq="s")
ts3=pd.Series(content[0],daterange)
print daterange
print ts3
print starttime[0]
#print ts3[to_datetime(starttime[0]):to_datetime(starttime[0]+20)]


#print starttime
#print endtime
#print content
#variable={}
#variable['starttime']=starttime[0]
#variable['endtime']=endtime[-1]

#now=starttime[0]
#while now < starttime[0]+100000:
#	ii=0
#	while ii<= 60:
#		if now in starttime:
#			print content[starttime.index(now)]
#		if now in endtime:
#			print content[endtime.index(now)]
#		now+=1
#		ii+=1


#index=0
#id=0
#event={}
#print endtime[index]

#print integrate.quad(lambda x: (sign(x-1)+1)/2-(sign(x-3)+1)/2, 0, 4.5)

#while (now<endtime[-1]+60):
#	while (now>endtime[index]) & (index<len(content)-1):
#		print now
#		print endtime[index]
#		print index
#		index+=1
#	event[id]=[now,content[index]]
#	id+=1
#	now+=60
#print event

# didn't consider the case that time divided the events
