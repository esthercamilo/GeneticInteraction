import os
import random as rm

def makedir(namedir):
	if not os.path.exists(namedir):
		os.makedirs(namedir)

#Cria estrutura de arquivos

def folders(ce):
	makedir('weka/'+ce+'/arff')
	makedir('weka/'+ce+'/csv/exp')
	makedir('weka/'+ce+'/csv/random')
	makedir('weka/'+ce+'/dot')
	makedir('weka/'+ce+'/model')
	makedir('weka/'+ce+'/out')
	makedir('weka/'+ce+'/png')
	makedir('weka/'+ce+'/result')
	makedir('weka/'+ce+'/result_random')
	
folders('deg')
folders('bet')
folders('neigh')
folders('complete')

#Read butland training
ftrain=open('files/trainingSetButland.csv') 
header = ftrain.readline().rstrip().split(',')

listTrainPos=[]
listTrainNeg=[]
for elem in ftrain:
	data = elem.rstrip().split(',')
	if float(data[len(data)-1])<0:
		listTrainNeg.append(data[2:len(data)])
	else:
		listTrainPos.append(data[2:len(data)])

size = min(len(listTrainNeg),len(listTrainPos))
		
def setGroups(indexStart,indexEnd,groupName):
	thisHeader = ','.join(header[indexStart+2:indexEnd+2])+',class\n'
	fumbalanced=open('weka/'+groupName+'/csv/exp/umbalanced.csv','w')
	#fill umbalanced
	fumbalanced.write(thisHeader)
	for a in range(len(listTrainNeg)):
		subUmb = ','.join([x for x in listTrainNeg[a][indexStart:indexEnd]])
		fumbalanced.write(subUmb+',AGG\n')
	for a in range(len(listTrainPos)):
		subUmb = ','.join([x for x in listTrainPos[a][indexStart:indexEnd]])
		fumbalanced.write(subUmb+',ALL\n')
	fumbalanced.close()
	
	
	#fill balanced
	for i in range(1,101):
		file_exp = open('weka/'+groupName+'/csv/exp/'+str(i)+'.csv','w')
		file_ran = open('weka/'+groupName+'/csv/random/'+str(i)+'.csv','w')
		file_exp.write(thisHeader)
		file_ran.write(thisHeader)
		rm.shuffle(listTrainNeg)
		rm.shuffle(listTrainPos)
		for j in range(size):
			classes=['AGG','ALL']
			subNeg = [x for x in listTrainNeg[j][indexStart:indexEnd]]
			file_exp.write(','.join(subNeg)+',AGG\n')
			rm.shuffle(classes)
			file_ran.write(','.join(subNeg)+','+classes[0]+'\n')
			subPos = [x for x in listTrainPos[j][indexStart:indexEnd]]
			file_exp.write(','.join(subPos)+',ALL\n')
			rm.shuffle(classes)
			file_ran.write(','.join(subPos)+','+classes[0]+'\n')
		file_exp.close()
		file_ran.close()
		
		
#DEGREE
i_start = header.index('degInt_min')-2
i_end = header.index('degmet_max')-1
setGroups(i_start,i_end,'deg')

#BETWEENESS
i_start = header.index('betInt_min')-2
i_end = header.index('betmet_max')-1
setGroups(i_start,i_end,'bet')

#NEIGHBORHOOD
i_start = header.index('cnInt')-2
i_end = header.index('jcmet')-1
setGroups(i_start,i_end,'neigh')

#COMPLETE
i_start = header.index('degInt_min')-2
i_end = header.index('jcmet')-1
setGroups(i_start,i_end,'complete')


		
