from string import *
import networkx as nx

fbut=open('files/butscore.tab')
fbut.readline()
fppi=open('files/ppi.tab')
freg=open('files/reg.tab')
fmet=open('files/met.tab')
fint=open('files/int.tab')

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

outputbut=open('files/spathsbut.tab','w')
outputbut.write('geneA\tgeneB\tsp_int\tsp_ppi\tsp_met\n')
for k in dicBut.keys():
        try:
	   outputbut.write('%s\t%s\t%s\t%s\t%s\n' %(k[0],k[1],dicspint[k],dicspppi[k],dicspmet[k]))
        except:
            pass
            
spaths(Gint,dicspint,allpairs)
spaths(Gppi,dicspppi,allpairs)
spaths(Gmet,dicspmet,allpairs)

outputall=open('files/spathsall.tab','w')
outputall.write('geneA\tgeneB\tsp_int\tsp_ppi\tsp_met\n')
for k in dicAllPairs.keys():
	outputall.write('%s\t%s\t%s\t%s\t%s\n' %(k[0],k[1],dicspint[k],dicspppi[k],dicspmet[k]))
