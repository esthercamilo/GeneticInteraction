#################################
#AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################

from string import *
import numpy as np

fcfg = open('config.txt')
folder = fcfg.readline().rstrip('\n')

types = ['bet', 'bet_sp', 'complete', 'deg', 'neigh', 'spaths']


def dist(x,y):
    return np.sqrt(np.sum((x-y)**2))

def getTree(m):

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

def outputf(b,i,output):
    mp = getTree(b)
    treesnocluster = mp[0]
    menorTree = mp[1]
    s1 = ""
    for k in treesnocluster:
        s1 = s1 + str(k) + ', '


    output.write("Cluster%s : %s\n" % (i,menorTree))
    output.write(s1.rstrip()+"\n\n\n")


for t in types:
    dicclust={}
    f1 = open(folder+'weka/'+t+'/cluster_assign.txt')
    for line in f1:
        if line == '\n':
                    continue
        try:
            d = line.rstrip().split(" ")
            tree = int(d[0])
            clust = int(d[1])
            dicclust[tree]=clust
        except:
            print "Last line is empty - that is ok"

    f2 = open(folder+'weka/'+t+'/matrix.csv')
    f2.readline()
    i=0
    m0=[]
    m1=[]
    m2=[]
    m3=[]
    for line in f2:
        d = line.rstrip().split(',')
        linha = []
        for l in d:
            linha.append(float(l))
        n = dicclust[i]
        if n == 0:
            m0.append((i,linha))
        elif n == 1:
            m1.append((i,linha))
        elif n == 2:
            m2.append((i,linha))
        elif n == 3:
            m3.append((i,linha))
        else:
            "check your input file!"
        i = i + 1

    output = open(folder+'weka/'+t+'/repTree.csv','w')
    # Cluster 1
    outputf(m0,0,output)
    outputf(m1,1,output)
    outputf(m2,2,output)
    outputf(m3,3,output)


###################################################################################################################
#THE OUTPUT FOR THE CLUSTERING EXPERIMENT MUST BE DIFFERENT: We need only one file with the following format:
#
#   exp       group      size_clust1     size_clust2       size_clust3          size_clust4
#
#There are 6 experiments (100, 200, 400, 600, 800 and 1000) and 10 groups for each of them.
#
# The file output is weka/complete/cluster_algorithm/input4Shannon.csv
#
###################################################################################################################

output_sh = open(folder+'weka/complete/cluster_algorithm/input4Shannon.csv','w')
output_sh.write('exp,group,c1,c2,c3,c4\n')
clust=[100,200,400,600,800,1000]
for c in clust:
        for n in range(1,11):
            t="/complete/cluster_algorithm/" + str(c)+"/" + str(n)
            sizes = []
            m_0=0
            m_1=0
            m_2=0
            m_3=0
            f1 = open(folder+'weka/'+t+'/cluster_assign.txt')
            for line in f1:
                if line == '\n':
                    continue
                d = line.rstrip().split(" ")
                cluster = int(d[1])
                if cluster == 0:
                    m_0 += 1
                elif cluster ==1:
                    m_1 += 1
                elif cluster == 2:
                    m_2 += 1
                elif cluster == 3:
                    m_3 += 1
                else:
                    print "The clustering experiment got exception."
            ol = [m_0,m_1,m_2,m_3] #create a Ordered List
            ol.sort()
            output_sh.write('%s,%s,%s,%s,%s,%s\n' % (c,n,ol[0],ol[1],ol[2],ol[3]))




