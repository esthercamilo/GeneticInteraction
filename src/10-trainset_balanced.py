import random as rm

fcfg = open('config.txt')
folder = fcfg.readline().rstrip('\n')
classe = ['AGG','ALL']

types = ['bet', 'bet_sp', 'complete', 'deg', 'neigh', 'spaths']

def openfiles(t):
    listapos = []
    listaneg = []
    arq = open(folder+'weka/'+t+'/csv/umbalanced_num.csv')
    header = arq.readline()
    for line in arq:
        d = line.split(',')
        score = float(d[-1].rstrip('\n'))
        if score<0:
            listaneg.append(line.replace(str(score), 'AGG'))
        else:
            listapos.append(line.replace(str(score), 'ALL'))

    size = min(len(listaneg),len(listapos))

    #fill 100 csvs
    for i in range(1,101):
        f1 = open(folder+'weka/'+t+'/csv/exp/'+str(i)+'.csv','w')
        f2 = open(folder+'weka/'+t+'/csv/rnd/'+str(i)+'.csv','w')
        f1.write(header)
        f2.write(header)
        rm.shuffle(listaneg)
        rm.shuffle(listapos)
        for j in range(size):
            f1.write(listaneg[j])
            f1.write(listapos[j])
            f2.write(listaneg[j].replace('AGG',classe[rm.randint(0,1)]))
            f2.write(listapos[j].replace('ALL',classe[rm.randint(0,1)]))
    arq.close()

for t in types:
    openfiles(t)

listapos = []
listaneg = []
arq = open(folder+'weka/complete/csv/umbalanced_num.csv')
header = arq.readline()
for line in arq:
    d = line.split(',')
    score = float(d[-1].rstrip('\n'))
    if score<0:
        listaneg.append(line.replace(str(score), 'AGG'))
    else:
        listapos.append(line.replace(str(score), 'ALL'))
size = min(len(listaneg),len(listapos))
l = [100,200, 400, 600, 800, 1000]
for v in l:
    for n in range (1,11): #10 em cada arquivo
        for m in range(1, v+1):
            f = open(folder+'weka/complete/cluster_algorithm/'+str(v)+'/'+str(n)+'/csv/'+str(m)+'.csv','w')
            f.write(header)
            rm.shuffle(listaneg)
            rm.shuffle(listapos)
            for j in range(size):
                f.write(listaneg[j])
                f.write(listapos[j])
            f.close()
