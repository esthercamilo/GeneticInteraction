from string import *
import networkx as nx
import random as rm
import uuid
import pickle

def readint():
	listint=[]
	dicnodes={}
	file = open('int.tab')
	for line in file:
		data = line.split()
		listint.append((data[0],data[1]))
		dicnodes[data[0]]=0
		dicnodes[data[1]]=0
	return (dicnodes.keys(),listint)

	
readintegrated = readint()
listPaths=[]
listint = readintegrated[1]
for index in range(100):
	randNameFile = str(uuid.uuid1())
	file = open('files/spaths/'+randNameFile+'.dic','w')
	ord=range(len(listint))
	rm.shuffle(ord)
	dic={}
	antidic={}
	nodes=readintegrated[0]
	for i in range(len(nodes)):
		dic[nodes[i]]=str(ord[i])
		antidic[str(ord[i])]=nodes[i]
	G = nx.Graph()
	for i in range(len(listint)):
		G.add_edge(dic[listint[i][0]],dic[listint[i][1]])        
	paths = nx.shortest_path(G)
	pickle.dump(paths,file)


