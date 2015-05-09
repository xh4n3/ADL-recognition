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

result={}
nth=0
current=starttime

def ishigh(current):
	global nth
	while current > dic['Toilet'][nth][1]:
		print current
		print nth
		print dic['Toilet'][nth][1]
		nth+=1
		print nth
		print len(dic['Toilet'])
		if nth >= len(dic['Toilet']):
			nth-=1
			return False
	if current < dic['Toilet'][nth][0]:
		return False
	else:
		return True

while current <= endtime:
	if ishigh(current):
		if int(current - starttime / deltat) not in result:
			result[int(current - starttime / deltat)]=0
		result[int(current - starttime / deltat)]+=1
	current+=1