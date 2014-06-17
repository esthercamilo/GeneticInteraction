import numpy as np
types=['complete']#,'bet','neigh','complete']
for t in types:
	output = open('weka/'+t+'/vote_threshold_summary.csv','w')
	output.write('TP,FP\n')
	lista = []
	for i in range(1,101):
		file = open('weka/'+t+'/vote_threshold/'+str(i)+'.csv')
		header = file.readline()
		for line in file:
			data = line.split(',')
			TP = data[5] 
			FP = data[4]
			output.write(TP+','+FP+'\n')

			
#CALCULATION OF THE AVERAGE PERFORMANCE
#Read result and return the averages:  TP, FP, Precision, Recall, F, AUC for the cross-validation
def readWeka(att):
	listFiles=[]
	for i in range(1,101):
		file = open("weka/"+att+"/vote_result/"+str(i)+"-result.dat")
		thisLine = ''
		while 'Stratified cross-validation' not in thisLine:
			thisLine = file.readline()
		while 'Detailed Accuracy By Class' not in thisLine:
			thisLine = file.readline()
		for j in range(2):
			thisLine = file.readline()
		dic={}
		for l in range(3):
			avg = file.readline()
			TP=float(avg[16:24].strip())
			FP=float(avg[25:35].strip())
			Precision=float(avg[35:45].strip())
			Recall=float(avg[45:55].strip())
			F=float(avg[55:65].strip())
			ROC=float(avg[65:75].strip())
			classe=avg[75:85].strip()
			if classe == '':
				classe = 'AVG'
			dic[classe]=[TP,FP,Precision,Recall,F,ROC]
		listFiles.append(dic)
	return listFiles	
		

def avgListArrays(listArrays):
	summation = 0
	for elem in listArrays:
		summation = summation+elem
	return summation/len(listArrays)

def metricas(tipo):

	arrayDegExp = readWeka(tipo)

	arrayAGGexp=[]
	arrayALLexp=[]
	arrayAVGexp=[]
	for elem in arrayDegExp:
		arrayAGGexp.append(np.array(elem['AGG']))
		arrayALLexp.append(np.array(elem['ALL']))
		arrayAVGexp.append(np.array(elem['AVG']))
	#Average experiment
	avgAGGexp=avgListArrays(arrayAGGexp)
	avgALLexp=avgListArrays(arrayALLexp)
	avgAVGexp=avgListArrays(arrayAVGexp)
	
	
	output=open('weka/'+tipo+'/vote_metrics.txt','w')

	output.write('TP\t&\tFP\t&\tPrecision\t&\tRecall\t&\tF\t&\tAUC\n')
	output.write('\nAGG\n')
	output.write('\t&\t'.join([str(x) for x in avgAGGexp]))
	output.write('\nALL\n')
	output.write('\t&\t'.join([str(x) for x in avgALLexp]))
	output.write('\nAVG\n')
	output.write('\t&\t'.join([str(x) for x in avgAVGexp]))

for t in types:
	metricas(t)