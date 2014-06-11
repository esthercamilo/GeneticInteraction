from string import *
import random as rm
import os
#from os import listdir

#Gerar 10 conjuntos aleatorios de interacoes
#com nodos e arestas crescentes

def getInt(filename,numberNodes,numberEdges):
	nodes=['node'+str(x) for x in range(numberNodes)]
	edges=[]
	nE = 0
	m=0
	while nE < numberEdges:
		for i in range(numberNodes-1):
			subList=nodes[i+1:numberNodes]
			rm.shuffle(subList)
			numbNeigh = rm.randint(1,int(0.1*len(subList)+1))
			n=0
			for j in range(numbNeigh):
				tupla = (nodes[i],subList[j])
				if tupla[0]!=tupla[1]:
					edges.append(tupla)
		nE = len(set(edges))
		edges=list(set(edges))
	file = open('int/'+filename,'w')
	for elem in edges:
		file.write(elem[0]+'\t'+elem[1]+'\n')
	file.close()

def maxNumberOfEdges(numberOfNodes):
	max = numberOfNodes*(numberOfNodes-1)/2
	return max

# for numbNodes in range(10,200,10):
	##for numbEdges in range(10,5*numbNodes,20):
	# numbEdges = 10*numbNodes
	# if numbEdges < maxNumberOfEdges(numbNodes):
		# name = 'int_%03d_%03d.tab' % (numbNodes,numbEdges)
		# getInt(name,numbNodes,numbEdges)

listDir = (os.listdir('int'))
for f in listDir:
	os.system('python 4-allshortest.py int/'+f)
	
	
