import networkx as nx
import numpy as np

fcfg = open('config.txt')
folder = fcfg.readline().rstrip('\n')

# Construction of the networks

#read ppi,reg,met
fppi = open(folder+'files/ppi.tab')
freg = open(folder+'files/reg.tab')
fmet = open(folder+'files/met.tab')
fint = open(folder+'files/int.tab')


def readfile(file):
    listtuple = []
    for line in file:
        data = line.split()
        listtuple.append((data[0], data[1]))
    return listtuple


listppi = readfile(fppi)
listreg = readfile(freg)
listmet = readfile(fmet)
listInt = readfile(fint)

# Setting up graphs
GInt = nx.Graph()
Gppi = nx.Graph()
Greg = nx.DiGraph()  #directed graph
Gmet = nx.DiGraph()  #directed graph
#Fill graphs: Int is made up of all networks
for nodes in listInt:
    GInt.add_edge(nodes[0], nodes[1])
for nodes in listppi:
    Gppi.add_edge(nodes[0], nodes[1])
for nodes in listreg:
    Greg.add_edge(nodes[0], nodes[1])
for nodes in listmet:
    Gmet.add_edge(nodes[0], nodes[1])

#Nodes : list of nodes
nodesGInt = GInt.nodes()
nodesGppi = Gppi.nodes()
nodesGreg = Greg.nodes()
nodesGmet = Gmet.nodes()

#butland pairs
fbut = open(folder+'files/butscore.tab')
butheader = fbut.readline()
dicbut = {}
for line in fbut:
    d = line.split()
    dicbut[(d[0], d[1])] = d[2]

#read file genes.tab to get a list of all possible pairs
fgenes = open(folder+'files/genes.tab')
allpairs = [x.split()[0] for x in fgenes.readlines()]

#Average degree for each network (was having issues to sum - I mantained values on a list)
def avgDegree(dicValues):
    list = []
    for elem in dicValues.values():
        list.append(float(elem))
    avg = np.mean(list)
    return avg


#FSW(network) -> returns a dictionary with the gene and the fsw value key=g1,g2 value=fsw
def FSW(G, pairs):
    dic = {}
    nodes = G.nodes()
    avg = avgDegree(G.degree())
    for p in pairs:
        if p[0] in nodes and p[1] in nodes:
            n1 = G.neighbors(p[0])
            n2 = G.neighbors(p[1])
            i = len(set(n1) & set(n2))  #intersection
            m = abs(len(n1) - len(n2))
            l1 = max(0, avg - len(n1))
            l2 = max(0, avg - len(n2))
            #set formed by x ! in y
            xmy_init = n1
            for elem in n2:
                if elem in xmy_init:
                    xmy_init.remove(elem)
            xmy = len(xmy_init)
            #set formed by y ! in x
            ymx_init = n2
            for elem in n1:
                if elem in ymx_init:
                    ymx_init.remove(elem)
            ymx = len(ymx_init)
            try:
                fsw = (2 * i / (ymx + 2 * i + l1)) * (2 * i / (xmy + 2 * i + l2))
            except:
                fsw = 0
            dic[p] = fsw
        else:
            dic[p]=0
        return dic


def CN(G, pairs):  #common neighbors
    dic = {}
    nodes = G.nodes()
    for p in pairs:
        if p[0] in nodes and p[1] in nodes:
            n1 = G.neighbors(p[0])
            n2 = G.neighbors(p[1])
            inter = len(set(n1) & set(n2))
            dic[p] = inter
        else:
            dic[p]=0
    return dic


def JC(G, pairs):  #Jaccard
    dic = {}
    nodes = G.nodes()
    for p in pairs:
        if p[0] in nodes and p[1] in nodes:
            n1 = G.neighbors(p[0])
            n2 = G.neighbors(p[0])
            inter = len(set(n1) & set(n2))
            union = len(set(n1) | set(n2))
            jc = 0
            try:
                jc = inter / union
            except ZeroDivisionError:
                pass
            dic[p] = jc
        else:
            dic[p]=0
    return dic

#llna = Label List Neighbor Attributes
llna = ['cnInt', 'fswInt', 'jcInt', 'cnppi', 'fswppi', 'jcppi', 'cnreg', 'fswreg', 'jcreg', 'cnmet', 'fswmet', 'jcmet']

pairsbut = dicbut.keys()

#Butland
for s in llna:
    mycommand = 'dic' + s + ' = CN(G' + s[-3:] + ',pairsbut)'
    exec mycommand

#output butland
outbut = open(folder+'files/neigh_butland.tab','w')
header = 'gene1\tgene2\t'+'\t'.join(llna)+'\n'
outbut.write(header)
for p in pairsbut:
    var_dics = 'p[0],p[1],'+','.join(['dic'+x+'[p]' for x in llna])
    my_format = 13*"%s\t"+"%s\n"
    outbut.write( my_format % (eval(var_dics)))



#ALL PAIRS


























