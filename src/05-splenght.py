#################################
#AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################

from string import *
import networkx as nx

fcfg = open('config.txt')
folder = fcfg.readline().rstrip('\n')

fbut=open(folder+'files/butscore.tab')
fbut.readline()
fppi=open(folder+'files/ppi.tab')
freg=open(folder+'files/reg.tab')
fmet=open(folder+'files/met.tab')
fint=open(folder+'files/int.tab')

dicBut={}
for line in fbut:
	d = line.split()
	dicBut[(d[0],d[1])]=d[2]

	
#SET GRAPHS
Gint = nx.Graph()
Gppi = nx.Graph()
Gmet = nx.DiGraph()

def readFiles(G,file):
	for l in file:
		nodes = l.split()
		G.add_edge(nodes[0],nodes[1])
readFiles(Gint,fint)		
readFiles(Gppi,fppi)		
readFiles(Gmet,fmet)		

allgenes=Gint.nodes()

dicAllPairs={}
size=len(allgenes)
for i in range(size):
	for j in range(i+1,size):
		dicAllPairs[(allgenes[i],allgenes[j])]='?'

dicspint={}
dicspppi={}
dicspmet={}

butkeys=dicBut.keys()
allpairs=dicAllPairs.keys()

def spaths(G,dic,source):
	for p in source:
		try:		
			dic[p] = nx.shortest_path_length(G, p[0],p[1])
		except:
		#IMPORTANTE -> PARES DE BUTLAND FALTANTES NA REDE FORAM CONSIDERADOS ZERO
			dic[p]=0
			

spaths(Gint,dicspint,butkeys)
spaths(Gppi,dicspppi,butkeys)
spaths(Gmet,dicspmet,butkeys)

outputbut=open(folder+'files/spathsbut.tab','w')
outputbut.write('geneA\tgeneB\tsp_int\tsp_ppi\tsp_met\n')
for k in dicBut.keys():
        try:
	   outputbut.write('%s\t%s\t%s\t%s\t%s\n' %(k[0],k[1],dicspint[k],dicspppi[k],dicspmet[k]))
        except:
            pass
            
spaths(Gint,dicspint,allpairs)
spaths(Gppi,dicspppi,allpairs)
spaths(Gmet,dicspmet,allpairs)

outputall=open(folder+'files/spathsall.tab','w')
outputall.write('geneA\tgeneB\tsp_int\tsp_ppi\tsp_met\n')
for k in dicAllPairs.keys():
	outputall.write('%s\t%s\t%s\t%s\t%s\n' %(k[0],k[1],dicspint[k],dicspppi[k],dicspmet[k]))






