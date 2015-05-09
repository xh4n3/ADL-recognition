import time,csv,scipy
from scipy import sign,integrate
from time import mktime, gmtime, strftime
import numpy as np

#real time to unix time
#str1="2011-11-28 02:27:59"
#a=time.strptime(str1,"%Y-%m-%d %H:%M:%S")
#mktime(a)

#unix time to real time
#unixtime=1322447279
#strftime("%Y-%m-%d %H:%M:%S", gmtime(unixtime))

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

def ishigh(current,sensor):
	global nth
	while current > dic[sensor][nth][1]:
		nth+=1
		#print nth
		#print len(dic[sensor])
		if nth >= len(dic[sensor]):
			return False
	if current < dic[sensor][nth][0]:
		return False
	else:
		return True

for sensor in dic:
	print sensor
	current=starttime
	nth=0
	while current <= endtime:
		if nth >= len(dic[sensor]):
			break
		if ishigh(current,sensor):
			if sensor not in result:
				result[sensor]={}
			if int((current - starttime) / deltat) not in result[sensor]:
				result[sensor][int((current - starttime) / deltat)]=0
			result[sensor][int((current - starttime) / deltat)]+=1
		current+=1