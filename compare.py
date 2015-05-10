import time,csv,scipy
from scipy import cluster
from time import mktime, gmtime, strftime
import numpy as np

starttime=1322447279
endtime=1323674541
dic={}
deltat=60

#real time to unix time
#tstr="2011-11-28 02:27:59"
def tounix(tstr):
	return mktime(time.strptime(tstr,"%Y-%m-%d %H:%M:%S"))

#unix time to real time
#ustr=1322447279
def toreal(ustr):
	return strftime("%Y-%m-%d %H:%M:%S", gmtime(ustr))

#no. of slice to real time
#noslice=120
def storeal(noslice):
	return strftime("%Y-%m-%d %H:%M:%S", gmtime(noslice * deltat + starttime))


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

#sensor list
slist=[]

for sensor in dic:
	print sensor
	slist.append(sensor)
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


dataset={}
current=0
while current < int((endtime - starttime) / deltat):
	dataset[current]={}
	for sensor in dic:
		if current in result[sensor]:
			dataset[current][sensor]=round(result[sensor][current]/float(deltat),3)
	current+=1

x=np.zeros((len(dataset),len(dic)))
current=0
while current < int((endtime - starttime) / deltat):
	for item in dataset[current]:
		x[current][slist.index(item)]=dataset[current][item]
	current+=1

#orginal
output=cluster.vq.kmeans2(x,10,iter=1000,minit='points')

#rescaled
whitex=cluster.vq.whiten(x)
output_white=cluster.vq.kmeans2(whitex,10,iter=1000,minit='points')
