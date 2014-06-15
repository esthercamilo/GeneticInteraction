from string import *
from scipy.stats import wilcoxon
import numpy as np


types = ['deg','bet','neigh','complete']

#Read result and return the averages:  TP, FP, Precision, Recall, F, AUC for the cross-validation
def readWeka(att):
	listExpRan=[]
	for er in ['','_random']:
		listFiles=[]
		for i in range(1,101):
			file = open("weka/"+att+"/result"+er+"/"+str(i)+"-result.txt")
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
		listExpRan.append(listFiles)
	return listExpRan	
		

def avgListArrays(listArrays):
	summation = 0
	for elem in listArrays:
		summation = summation+elem
	return summation/len(listArrays)


def pvalue(lista1,lista2):
	pvalues=[]
	for k in range(len(lista1[0])):
		exp = []
		rnd = []
		for i in range(len(lista1)):
			exp.append(lista1[i][k])
		for j in range(len(lista2)):
			rnd.append(lista2[i][k])
		this_pvalue = wilcoxon(exp,rnd)
		pvalues.append(this_pvalue[1])
	return pvalues
	
def metricas(tipo):
	arrayDeg=readWeka(tipo)
	arrayDegExp = arrayDeg[0]
	arrayDegRnd = arrayDeg[1]

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
	
	arrayAGGrnd=[]
	arrayALLrnd=[]
	arrayAVGrnd=[]
	for elem in arrayDegRnd:
		arrayAGGrnd.append(np.array(elem['AGG']))
		arrayALLrnd.append(np.array(elem['ALL']))
		arrayAVGrnd.append(np.array(elem['AVG']))
	#Average random
	avgAGGrnd=avgListArrays(arrayAGGrnd)
	avgALLrnd=avgListArrays(arrayALLrnd)
	avgAVGrnd=avgListArrays(arrayAVGrnd)

	#p-value AGG
	pvaluesAgg = pvalue(arrayAGGexp,arrayAGGrnd)
	#p-value ALL
	pvaluesAll = pvalue(arrayALLexp,arrayALLrnd)	
	#p-value AVG
	pvaluesAvg = pvalue(arrayAVGexp,arrayAVGrnd)	
	
	output=open('weka/'+tipo+'/metrics.txt','w')

	output.write('EXPERIMENT\n')
	output.write('TP\t&\tFP\t&\tPrecision\t&\tRecall\t&\tF\t&\tAUC\n')
	output.write('\nAGG\n')
	output.write('\t&\t'.join([str(x) for x in avgAGGexp]))
	output.write('\nALL\n')
	output.write('\t&\t'.join([str(x) for x in avgALLexp]))
	output.write('\nAVG\n')
	output.write('\t&\t'.join([str(x) for x in avgAVGexp]))

	output.write('\n\n\nRANDOM\n')
	output.write('\nAGG\n')
	output.write('\t&\t'.join([str(x) for x in avgAGGrnd]))
	output.write('\nALL\n')
	output.write('\t&\t'.join([str(x) for x in avgALLrnd]))
	output.write('\nAVG\n')
	output.write('\t&\t'.join([str(x) for x in avgAVGrnd]))

	output.write('\n\n\np-values\n\n')
	output.write('\nAGG\n')
	output.write('\t&\t'.join([str(x) for x in pvaluesAgg]))
	output.write('\nALL\n')
	output.write('\t&\t'.join([str(x) for x in pvaluesAll]))
	output.write('\nAVG\n')
	output.write('\t&\t'.join([str(x) for x in pvaluesAvg]))

	output.close()
	

#MATRIX INPUT FOR REPRESENTATIVE TREE

def readOutFile(tipo):
	#firstLine
	saida = open('weka/'+tipo+'/matrix.csv','w')
	primer="tree1"
	for j in range(2,101):
		primer = primer+",tree"+str(j)
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
	#invert 
	for j in range(len(inst[0])):
		linha = str(inst[0][j])
		for k in range(1,len(inst)):
			linha = linha+","+str(inst[k][j])
		saida.write(linha.rstrip()+"\n")

	
for t in types:
	metricas(t)
	readOutFile(t)
