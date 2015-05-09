import time,csv,scipy
from scipy import sign,integrate
from time import mktime
import numpy as np

#str1="2011-11-28 02:27:59"
#a=time.strptime(str1,"%Y-%m-%d %H:%M:%S")
#mktime(a)

starttime=1322447279
endtime=1323674541
dic={}
deltat=600

with open('OrdoneA.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		i=0
		for item in row:
			if i == 0:
				start=mktime(time.strptime(item,"%Y-%m-%d %H:%M:%S"))
			if i == 1:
				stop=mktime(time.strptime(item,"%Y-%m-%d %H:%M:%S"))
			if i == 2:
				if item not in dic:
					dic[item]=[]
				dic[item].append((start,stop))
			i+=1

formula="0"
for tslice in dic['Toilet']:
	formula=formula+"+(sign(x-"+str(int(tslice[0]))+")+1)/2-(sign(x-"+str(int(tslice[1]))+")+1)/2"

#print formula
lam=lambda x: eval(formula)

offset=starttime

record={}
record['Toilet']={}

while offset < endtime:
	record['Toilet'][offset]=int(integrate.quad(lam,offset,offset+deltat)[0])
	offset+=deltat

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
