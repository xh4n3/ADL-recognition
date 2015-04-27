import time
import csv
from time import mktime

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

#print starttime
#print endtime
#print content

print starttime[0]
print endtime[-1]

now=starttime[0]
index=0
id=0
event={}
print endtime[index]

while (now<endtime[-1]+60):
	while (now>endtime[index]) & (index<len(content)-1):
		print now
		print endtime[index]
		print index
		index+=1
	event[id]=[now,content[index]]
	id+=1
	now+=60
print event

# didn't consider the case that time divided the events
