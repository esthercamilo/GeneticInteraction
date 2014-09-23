#####################################################################################
# Temos 100 arvores. Cada uma contem a probabilidade de classificacao               
# de cada instancia. Essas instancias por sua vez, sao os pares de genes.
# Foi construida uma matrix.csv cujas linhas representam cada arvore e as colunas 
# sao as instancias. Assim, cada coluna mostra como cada conjunto de treinamento 
# gera diferentes probabilidades de classificacao de uma mesma instancia. Seria
# desejavel que os valores em uma mesma coluna fossem os mesmos, mas nao sao, pois, mesmo
# que as amostras tenham sido derivadas de um mesmo conjunto, elas sao diferentes.
# Assim, encontramos a media para cada coluna dentro de cada cluster. Por minimizacao
# de distancias, encontramos a arvore que mais se aproxima desse centro.
######################################################################################

from string import *
import numpy as np

f1=open('cluster_assign.txt')

#um dicionario Key:tree e Value:cluster
dicclust={}
for line in f1:
	try:
		d = line.rstrip().split(" ")
		tree = int(d[0])
		clust = int(d[1])
		dicclust[tree]=clust
	except:
		print "1 erro sempre ocorre na ultima linha"
		

def dist(x,y):   
    return np.sqrt(np.sum((x-y)**2))
		
f2 = open('matrix.csv')

m0=[]
m1=[]
m2=[]
m3=[]

f2.readline()
i=0
for line in f2:
	d = line.rstrip().split(',')
	linha = []
	for l in d:
		linha.append(float(l))
	n = dicclust[i]
	if n==0:	
		m0.append((i,linha))
	elif n==1:	
		m1.append((i,linha))
	elif n==2:
		m2.append((i,linha))
	elif n==3:
		m3.append((i,linha))
	else:
		print 'tem alguma coisa errada'
	i=i+1

	
def getTree(m): #(m vem com o numero da tree e linha)
	
	#gerar lista de arvores no cluster
	treesnocluster=[]
	for am in m:
		treesnocluster.append(am[0])
	#gerar matrix somente com linha
	mat = []
	for a in m:
		mat.append(a[1])	
	npmat = np.array(mat)
	tmat = np.transpose(npmat)
	
	matavg = []
	for line in tmat:
		av = np.mean(line)
		matavg.append(av)
	matavg = np.array(matavg)	
		
	dist	
	#Arvore mais proxima
	distancia = dist(npmat[0],matavg) #faz a primeira pra ter comparativo
	menorTree = m[0][0]
	for j in range(len(npmat)):
		tdist = dist(npmat[j],matavg)
		if tdist<distancia:
			distancia = tdist
			menorTree = m[j][0]
	#importante somar +1 pois a numeracao das arvores nao comeca em zero.	
	return (treesnocluster,menorTree)


	
#OUTPUT
output = open('repTree.csv','w')

def outputf(b,i):
	mp = getTree(b)
	treesnocluster = mp[0]
	menorTree = mp[1]
	s1 = ""
	for k in treesnocluster:
		s1 = s1 + str(k) + ', '
	
	
	output.write("Cluster%s : %s\n" % (i,menorTree))
	output.write(s1.rstrip()+"\n\n\n")

# Cluster 1
outputf(m0,0)
outputf(m1,1)
outputf(m2,2)
outputf(m3,3)
	
	
	
	
	
	
	
	