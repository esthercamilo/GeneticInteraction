from string import *
import numpy as np


types = ['deg', 'bet', 'neigh', 'complete', 'spaths', 'bet_spaths']

#Read result and return the averages:  TP, FP, Precision, Recall, F, AUC for the cross-validation
def readWeka(att):
	listFiles=[]
	for i in range(1,101):
		file = open("weka/"+att+"/result/"+str(i)+"-result.txt")
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
	arrayDeg=readWeka(tipo)

	arrayAGGexp=[]
	arrayALLexp=[]
	arrayAVGexp=[]
	for elem in arrayDeg:
		arrayAGGexp.append(np.array(elem['AGG']))
		arrayALLexp.append(np.array(elem['ALL']))
		arrayAVGexp.append(np.array(elem['AVG']))
	#Average experiment
	avgAGGexp=avgListArrays(arrayAGGexp)
	avgALLexp=avgListArrays(arrayALLexp)
	avgAVGexp=avgListArrays(arrayAVGexp)
	output=open('weka/'+tipo+'/metrics.txt','w')

	output.write('EXPERIMENT\n')
	output.write('TP\t&\tFP\t&\tPrecision\t&\tRecall\t&\tF\t&\tAUC\n')
	output.write('\nAGG\n')
	output.write('\t&\t'.join([str(x) for x in avgAGGexp]))
	output.write('\nALL\n')
	output.write('\t&\t'.join([str(x) for x in avgALLexp]))
	output.write('\nAVG\n')
	output.write('\t&\t'.join([str(x) for x in avgAVGexp]))
	output.close()
	

#MATRIX INPUT FOR REPRESENTATIVE TREE

def readOutFile(tipo):
	#firstLine
	saida = open('weka/'+tipo+'/matrix.csv', 'w')
	primer="inst1"
	for j in range(2, 1014):
		primer = primer+",inst"+str(j)
	saida.write(primer+"\n")
	inst=[]
	for tree in range(100):
		thisTree=[]
		file = open('weka/'+tipo+'/out/'+str(tree+1)+'.out')
		lines = file.readlines()[5:1000]
		for i in range(len(lines)):
			if "AGG" in lines[i]:
				(thisTree.append(float((lines[i][33:]).strip())))
			else:
				(thisTree.append(1-float((lines[i][33:]).strip())))
		inst.append(thisTree)
	
	for elem in inst:
		line = ','.join([str(x) for x in elem])
		saida.write(line+"\n")

# for t in types:
	# metricas(t)
	# readOutFile(t)


#For clustering
def setClustMatrix(tipo):
	for f in range(1,11):
		#firstLine
		strFile = 'weka/complete/cluster_algorithm/'+str(tipo)+'/'+str(f)+'/matrix.csv'
		saida = open(strFile, 'w')
		primer="inst1"
		for j in range(2, 1014):
			primer = primer+",inst"+str(j)
		saida.write(primer+"\n")
		inst=[]
		for tree in range(tipo):
			thisTree=[]
			strFile2 = 'weka/complete/cluster_algorithm/'+str(tipo)+'/'+str(f)+'/out/'+str(tree+1)+'.out'
			file = open(strFile2)
			lines = file.readlines()[5:1018]
			for i in range(len(lines)):
				if "AGG" in lines[i]:
					(thisTree.append(float((lines[i][33:]).strip())))
				else:
					(thisTree.append(1-float((lines[i][33:]).strip())))
			inst.append(thisTree)
		
		for elem in inst:
			line = ','.join([str(x) for x in elem])
			saida.write(line+"\n")	

t_clust=[200,400,600,800,1000]			
for t in t_clust:
	setClustMatrix(t)