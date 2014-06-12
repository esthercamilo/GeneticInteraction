from string import *
import networkx as nx
import sys, traceback
import numpy as np

#Construction of the networks

#read ppi,reg,met
fppi=open('files/ppi.tab')
freg=open('files/reg.tab')
fmet=open('files/met.tab')
fint=open('files/int.tab')

def readfile(file):
	listtuple=[]
	for line in file:
		data = line.split()
		listtuple.append((data[0],data[1]))
	return listtuple

listppi = readfile(fppi)	
listreg = readfile(freg)	
listmet = readfile(fmet)	
listInt = readfile(fint)	

# Setting up graphs
GInt = nx.Graph()
Gppi = nx.Graph()
Greg = nx.DiGraph() #directed graph
Gmet = nx.DiGraph() #directed graph
#Fill graphs: Int is made of all networks
for nodes in listInt:
	GInt.add_edge(nodes[0],nodes[1])
for nodes in listppi:
	Gppi.add_edge(nodes[0],nodes[1])
for nodes in listreg:
	Greg.add_edge(nodes[0],nodes[1])
for nodes in listmet:
	Gmet.add_edge(nodes[0],nodes[1])
		
#Nodes : list of nodes
nodesGInt = GInt.nodes()
nodesGppi = Gppi.nodes()
nodesGreg = Greg.nodes()
nodesGmet = Gmet.nodes()

#my variabl 'allpairs' are all possible genes pairs and the score is unknown "?"
def getPairs(G): #returns a list of tuples with pairs
	allpairs=[]
	nodes=G.nodes()
	size = len(nodes)
	for i in range(size):
		for j in range(i+1,size): #avoid redundant interactions
			n1 = nodes[i]
			n2 = nodes[j]
			allpairs.append((n1,n2))
	return allpairs
	
pairsInt = getPairs(GInt)
	
#Average degree for each network (was having issues to sum - I kept values on a list)
def avgDegree(dicValues):
	list = []
	for elem in dicValues.values():
		list.append(float(elem))
	avg = np.mean(list)
	return avg


#FSW(network) -> returns a dictionary with the gene and the fsw value key=g1,g2 value=fsw


def FSW(G):
	dic={}
	pairs = getPairs(G)
	avg=avgDegree(G.degree()) 
	for p in pairs:
		n1=G.neighbors(p[0])
		n2=G.neighbors(p[1])
		i = len(set(n1) & set(n2)) #intersection
		m = abs(len(n1)-len(n2))
		l2 = max(0,avg-len(n2))
		#set formed by x ! in y
		xmy_init =  n1
		for elem in n2:
			if elem in xmy_init:
				xmy_init.remove(elem)
		xmy = len(xmy_init)
		#set formed by y ! in x
		ymx_init =  n2
		for elem in n1:
			if elem in ymx_init:
				ymx_init.remove(elem)
		ymx = len(ymx_init)
		try:
			fsw = (2*i/(ymx+2*i+l1))*(2*i/(xmy+2*i+l2))
		except:
			fsw = 0
		dic[p]=fsw
	return dic

def CN(G): #common neighbors
	dic={}
	pairs = getPairs(G)
	for p in pairs:
		n1=G.neighbors(p[0])
		n2=G.neighbors(p[1])
		inter = len(set(n1) & set(n2))
		dic[p]=inter
	return dic
		
def JC(G): #Jaccard
	dic={}
	pairs = getPairs(G)
	for p in pairs:
		n1=G.neighbors(p[0])
		n2=G.neighbors(p[0])
		inter = len(set(n1) & set(n2))
		union = len(set(n1) | set(n2))
		jc=0
		try:
			jc = inter/union
		except ZeroDivisionError:
			pass
		dic[p]=jc	
	return dic

#llna = Label List Neighbor Attributes
llna = ['cnInt','fswInt','jcInt','cnppi','fswppi','jcppi','cnreg','fswreg','jcreg','cnmet','fswmet','jcmet']		

#inicialize all dictionaries with zero
exec("\n".join(['dic'+x+'={}' for x in llna]))

print pairsInt


for p in pairsInt:
	for s in llna:
		exec('dic'+s+'[("'+p[0]+'","'+p[1]+'")]=0')

for s in llna:
	exec('dic'+s+'=dict(dic'+s+'.items() + '+(s[:-3]).upper()+'((G'+s[-3:]+')).items())')
	
# Three NB were calculated: Common-Neighbors (CN), Jaccard (JC) and Functional Similarity Weight (FSW)
# for each gene pair from Butland file

#save attributes file
neighfile = open('files/neighbor.tab','w')
neighfile.write('geneA\tgeneB\t'+"\t".join(llna)+'\n')
ap=getPairs(GInt)
for gene in ap:
	vars = "gene[0],gene[1],"+",".join(['dic'+x+'[(gene[0],gene[1])]' for x in llna])
	format = ((('%s\t')*len(llna))+'%s\t%s\n')
	neighfile.write(format % eval(vars))


	

