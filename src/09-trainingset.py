from string import *

#butland file for training set
fbut=open('files/butscore.tab')
dicbut={}
for line in fbut:
	d = line.split()
	dicbut[(d[0],d[1])]=d[2]

butpairs = dicbut.keys()	
	
fCompSet=open('files/completeTrainingSet.csv')
header=fCompSet.readline()

fTrainingSet = open('files/trainingSetButland.csv','w')
fTrainingSet.write(header.rstrip()+',class\n')
listTraining=[]
for line in fCompSet:
	d=line.split(',') # geneA = d[0]   geneB = d[1]
	if (d[0],d[1]) in butpairs:
		listTraining.append(line.replace('\n',','+dicbut[(d[0],d[1])]+'\n'))
		continue
	elif (d[1],d[0]) in butpairs or (d[1],d[0]) in butpairs:
		listTraining.append(line.replace('\n',','+dicbut[(d[1],d[0])]+'\n'))
		continue

listTraining = set(listTraining)
for elem in listTraining:
	fTrainingSet.write(elem)
		
		
		
