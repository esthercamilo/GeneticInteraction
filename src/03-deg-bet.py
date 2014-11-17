#################################
#AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################

from string import *
import re
import os
from libsbml import *
import collections
from collections import defaultdict
import xlrd
import time
import datetime
import networkx as nx
import numpy as np
import random as rm
import traceback

fileLog = open('filelog.txt','w')
fcfg = open('config.txt')
folder = fcfg.readline().rstrip('\n')
#read ppi,reg,met
fppi=open(folder+'files/ppi.tab')
freg=open(folder+'files/reg.tab')
fmet=open(folder+'files/met.tab')
fint=open(folder+'files/int.tab')

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

#Each gene has associated two centralities (degree and betweeness)
#related to 4 networks: Int, ppi, reg and met resulting in 8 dictionaries
#plus regin,regout and metin,metout

llca=['degInt','degppi','degreg','degmet','betInt','betppi',\
'betreg','betmet','regin','regout','metin','metout'] #list with labels

#Initialize a dictionary for each centrality
exec("\n".join(["dic"+x+"={}" for x in llca]))

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
allpairs={}
size = len(nodesGInt)
for i in range(size):
	for j in range(i+1,size): #avoid redundant interactions
		n1 = nodesGInt[i]
		n2 = nodesGInt[j]
		allpairs[(n1,n2)]="?"
		
#Sizes: how many gene are there
lenGInt = len(nodesGInt)
lenGppi = len(nodesGppi)
lenGreg = len(nodesGreg)
lenGmet = len(nodesGmet)

#this part is done only if there was no file of centralities		

#Missing values will be zero (string)
for g in nodesGInt:
	exec("\n".join(['dic'+x+'[g]=0' for x in llca]))
#centralities calculation
dicdegInt = GInt.degree()
dicdegppi.update(Gppi.degree())
dicdegreg.update(Greg.degree())
dicdegmet.update(Gmet.degree())
dicregin.update(Greg.in_degree())
dicregout.update(Greg.out_degree())
dicmetin.update(Gmet.in_degree())
dicmetout.update(Gmet.out_degree())
print 'betweeness takes long, be patient...'

dicbetInt = nx.algorithms.centrality.betweenness_centrality(GInt)
dicbetppi.update(nx.algorithms.centrality.betweenness_centrality(Gppi))	
dicbetreg.update(nx.algorithms.centrality.betweenness_centrality(Greg))	
dicbetmet.update(nx.algorithms.centrality.betweenness_centrality(Gmet))	


#Save attributes file
fileCent = open(folder+'files/centralites.tab','w')
fileCent.write("gene\t"+("\t".join(llca))+'\n')
q1 = (("%s\t")*(len(llca)+1)).rstrip("\t")+"\n"
q2 = "n,"+(",".join(["dic"+x+"[n]" for x in llca]))+"\n"
for n in nodesGInt:
	fileCent.write( q1 % (eval(q2)))
fileCent.close()


#List of genes
fileNodes = open(folder+'files/genes.tab','w')
for g in nodesGInt:
	fileNodes.write(g+'\n')







