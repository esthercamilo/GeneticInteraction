import random as rm

types = ['bet', 'bet_spaths', 'complete', 'deg', 'neigh', 'spaths']

def openfiles(t):
    listapos = []
    listaneg = []
    arq = open('weka/'+t+'/csv/umbalanced_num.csv')
    header = arq.readline()
    for line in arq:
        d = line.split(',')
        score = float(d[-1].rstrip('\n'))
        if score<0:
            listaneg.append(line.replace(str(score), 'AGG'))
        else:
            listapos.append(line.replace(str(score), 'ALL'))
    f_umb = open('weka/'+t+'/csv/umbalanced.csv','w')
    #convert from numeric to nominal
    for elem in listapos:
        f_umb.write(elem)
    for elem in listaneg:
        f_umb.write(elem)
    size = min(len(listaneg),len(listapos))

    #fill 100 csvs
    for i in range(1,101):
        f = open('weka/'+t+'/csv/'+str(i)+'.csv','w')
        f.write(header)
        rm.shuffle(listaneg)
        rm.shuffle(listapos)
        for j in range(size):
            f.write(listaneg[j])
            f.write(listapos[j])
    arq.close()

for t in types:
    openfiles(t)


listapos = []
listaneg = []
arq = open('weka/complete/csv/umbalanced_num.csv')
header = arq.readline()
for line in arq:
    d = line.split(',')
    score = float(d[-1].rstrip('\n'))
    if score<0:
        listaneg.append(line.replace(str(score), 'AGG'))
    else:
        listapos.append(line.replace(str(score), 'ALL'))
size = min(len(listaneg),len(listapos))
l = [200, 400, 600, 800, 1000]
for v in l:
    for n in range (1,11): #10 em cada arquivo
        for m in range(1, v+1):
            f = open('weka/complete/cluster_algorithm/'+str(v)+'/'+str(n)+'/csv/'+str(m)+'.csv','w')
            f.write(header)
            rm.shuffle(listaneg)
            rm.shuffle(listapos)
            for j in range(size):
                f.write(listaneg[j])
                f.write(listapos[j])
            f.close()
