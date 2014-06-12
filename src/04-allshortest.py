#!/usr/bin/env python
from string import *
import networkx as nx
import itertools
import collections
from collections import defaultdict


fint = open('int.tab')

def readfile(file):
	listtuple=[]
	for line in file:
		data = line.split()
		listtuple.append((data[0],data[1]))
	return listtuple

listint = readfile(fint)
GInt = nx.Graph()
for nodes in listint:
	GInt.add_edge(nodes[0],nodes[1])		
	
paths = nx.shortest_path(GInt)

listPaths=[]
listNodes = paths.keys()
for source in listNodes:
	valdic = paths[source]
	#valdic eh um dic key=target values=lista
	for v in valdic.values():
		listPaths.append(v)

temPath=listPaths
for elem in temPath:
	if len(elem)<2:
		listPaths.remove(elem)
		
		
#Concatenate paths
nList=listPaths		
size=len(listPaths)		
for i in range (size):
	for j in range(i+1,size):
		a = listPaths[i][-1]
		b = listPaths[j][0]
		z = listPaths[i]+listPaths[j][1:]
		if (a == b) and (z not in nList):
			nList.append(listPaths[i]+listPaths[j][1:])
			
#remove all paths where source==target
temPath=listPaths
for elem in temPath:
	if elem[0]==elem[-1]:
		listPaths.remove(elem)

nList = sorted(listPaths)

#reverter cada elemento e verificar se esta na lista
listPaths=[]
for elem in nList:
	listPaths.append(elem)


for i in range(len(listPaths)):
	elem = listPaths[i]
	listToBeVerified = listPaths[i+1:]
	a = [m for m in (reversed(elem))]
	if (a in listToBeVerified):
		nList.remove(a)

listPaths=[]
for elem in nList:
	listPaths.append(elem)

for elem in listPaths:
	k = sorted(elem)
	dedup = [k[i] for i in range(len(k)) if i == 0 or k[i] != k[i-1]]
	if len(dedup)<len(k):
		nList.remove(elem)
s=[]	
d=defaultdict(list)		
for elem in nList:
	a=elem[0]
	b=elem[-1]
	s.append(((a,b),elem))
for k,v in s:
	d[k].append(v)
result={}

shortestList=[]

for na,va in d.iteritems():
	size = len(va[0])
	for elem in va:
		if len(elem)<size:
			size=len(elem)
	for elem in va:
		if len(elem)==size:
			shortestList.append(elem)

	
#Save file with all paths
f_allpaths=open('allshortespaths.tab','w')
for elem in shortestList:
	f_allpaths.write(','.join(elem)+'\n')

