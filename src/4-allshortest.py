import networkx as nx
from string import *
from datetime import datetime
startTime = datetime.now()

fppi = open("files/ppi.tab")
freg = open("files/reg.tab")
fmet = open("files/met.tab")
fint = open("files/int.tab")
saida = open("files/shortest.tab","w")

GInt = nx.Graph()
Gppi=nx.Graph()
Greg=nx.DiGraph()
Gmet=nx.DiGraph()

def getInteraction(file):
	list = []
	for line in file:
		nodes=split(line)
		list.append((nodes[0],nodes[1]))
	return list

listppi=getInteraction(fppi)
listreg=getInteraction(freg)
listmet=getInteraction(fmet)
listint=getInteraction(fint)

def getGraph(graph,list):
	for elem in list:
		graph.add_edge(elem[0],elem[1])
	return graph
		
GInt=getGraph(GInt,listint)
Gppi=getGraph(Gppi,listppi)
Greg=getGraph(Greg,listreg)
Gmet=getGraph(Gmet,listmet)

def savePaths(G,file):
	size = len(G.nodes())
	genes = G.nodes()
	filepaths = open('files/'+file+'.tab','w')
	for i in range(size):
		for j in range(i+1,size):
			try:
				paths = nx.all_simple_paths(G,genes[i],genes[j])
				listpaths=[]
				t=0
				for p in paths:
					listpaths.append(p)
					t=len(p) #um tamanho qualquer
				#seleciona menor lista em listpaths
				for elem in listpaths:
					if len(elem)<t:
						t = len(elem)
				novaListPaths = []
				for elem in listpaths:
					if len(elem)==t:
						novaListPaths.append(elem)
				for elem in novaListPaths:
					filepaths.write(",".join(elem)+'\n')
			except Exception as e:
				print e

#shortest_path rede Integrada
savePaths(GInt,'spathsInt')
savePaths(Gppi,'spathsppi')
savePaths(Greg,'spathsreg')
savePaths(Gmet,'spathsmet')

			
