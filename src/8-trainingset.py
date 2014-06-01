from string import *

#butland file for training set
fbut=open('files/butscore.tab')
dicbut={}
for line in fbut:
	d = line.split()
	dicbut[(d[0],d[1])]=d[2]

butpairs = dicbut.keys()	
	
fCompSet=open('files/completeSet.csv')
header=fCompSet.readline()

fTrainingSet = open('files/TrainingSet.csv')
fTrainingSet.write(header)
for line in fCompSet:
	d=line.split(',')
	try:
		t1=(d[0],d[1])
		score = dicbut[t1]
		fTrainingSet.write(line.replace('?',str(score)))
		continue
	except:
		pass
	try:
		t2=(d[1],d[0])
		score = dicbut[t2]
		fTrainingSet.write(line.replace('?',str(score)))
	except:
		pass
		
		
		