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
	indexStart = indexStart-2
	indexEnd = indexEnd-1
	for i in range(1,101):
		file_exp = open('weka/'+groupName+'/csv/exp/'+str(i)+'.csv','w')
		file_ran = open('weka/'+groupName+'/csv/random/'+str(i)+'.csv','w')
		file_exp.write(','.join(header[indexStart+2:indexEnd+2])+',class\n')
		file_ran.write(','.join(header[indexStart+2:indexEnd+2])+',class\n')
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
			
#DEGREE
i_start = header.index('degInt_min')
i_end = header.index('degmet_max')
setGroups(i_start,i_end,'deg')

#BETWEENESS
i_start = header.index('betInt_min')
i_end = header.index('betmet_max')
setGroups(i_start,i_end,'bet')

#NEIGHBORHOOD
i_start = header.index('cnInt')
i_end = header.index('jcmet')
setGroups(i_start,i_end,'neigh')

#COMPLETE
i_start = header.index('degInt_min')
i_end = header.index('jcmet')
setGroups(i_start,i_end,'complete')


		
