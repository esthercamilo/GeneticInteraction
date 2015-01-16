#################################
#AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################

fcfg = open('config.txt')
folder = fcfg.readline().rstrip('\n')

types = ['bet', 'bet_sp', 'complete', 'deg', 'neigh', 'spaths']

# open files
fcent = open(folder+'files/cent_but.tab')
hcent = fcent.readline().split()
fneig = open(folder+'files/neigh_butland.tab')
hneig = fneig.readline().split()
fshor = open(folder+'files/spathsbut.tab')
hshor = fshor.readline().split()
fbut = open(folder+'files/butscore.tab')
hbut = fbut.readline()
fbabu = open(folder+'data/s-score-babu.tab')
hbabu = fbabu.readline()

#read butland
dicbut={}    #numeric class
dicnombut={} #nominal class
for line in fbut:
    d = line.split()
    float_d = float(d[2])
    classe = "AGG"
    if float_d>0:
        classe = "ALL"
    dicbut[(d[0],d[1])]=d[2]
    dicnombut[(d[0],d[1])]=classe

#read Babu file
dicbabu={}    #numeric class
dicnombabu={} #nominal class
for line in fbabu:
    d = line.split()
    float_d = float(d[2].replace(',', '.'))
    classe = "AGG"
    if float_d>0:
        classe = "ALL"
    dicbut[(d[0],d[1])]=d[2]
    dicnombut[(d[0],d[1])]=classe


#generate a dictionary for each type
start_dics = ['dic_' + x for x in types]
#initialize
exec ('\n'.join([x + '={}' for x in start_dics]))
dicdegbet={}

for line in fcent:
    d = line.split()
    p = (d[0], d[1])
    dic_deg[p] = d[2:10] + d[18:]
    dic_bet[p] = d[10:18]
    dicdegbet[p]=d[2:] #criei esse dic para preencher o completo

#dic neigh
for line in fneig:
    d = line.split()
    p = (d[0], d[1])
    dic_neigh[p] = d[2:]


#dic spaths
for line in fshor:
    d = line.split()
    p = (d[0], d[1])
    dic_spaths[p] = d[2:]

#dic bet_spaths
for k in dic_bet.keys():
    dic_bet_sp[k] = dic_bet[k] + dic_spaths[k]

#dic complete
for k in dic_complete.keys():
    dic_complete[k] = dicdegbet[k] + dic_neigh[k] + dic_spaths[k]

#Output umbalanced:
def writedic(t,dic,header):
    file1 = open(folder+'weka/'+t+'/csv/umbalanced_num.csv','w')
    file2 = open(folder+'weka/'+t+'/csv/umbalanced_nom.csv','w')
    file1.write(header)
    file2.write(header)
    for k,v in dic.iteritems():
        file1.write(k[0]+','+k[1]+','+','.join([x for x in v])+','+dicbut[k]+'\n')
        file2.write(k[0]+','+k[1]+','+','.join([x for x in v])+','+dicnombut[k]+'\n')

headDeg = 'gene1,gene2,'+','.join(hcent[2:10]+hcent[18:])+',score\n'
writedic('standart/deg', dic_deg,headDeg)

headBet = 'gene1,gene2,'+','.join(hcent[10:18])+',score\n'
writedic('standart/bet', dic_bet,headBet)

headNei = 'gene1,gene2,'+','.join(hneig[2:])+',score\n'
writedic('standart/neigh',dic_neigh,headNei)

headSho = 'gene1,gene2,'+','.join(hshor[2:])+',score\n'
writedic('standart/spaths', dic_spaths, headSho)

headBetSho = 'gene1,gene2,'+','.join(hcent[10:18])+','+','.join(hshor[2:])+',score\n'
writedic('standart/bet_sp', dic_bet_sp, headBetSho)

headComp = 'gene1,gene2,'+','.join(hcent[2:])+','+','.join(hneig[2:])+','+','.join(hshor[2:])+',score\n'
writedic('standart/complete', dic_complete, headComp)


#Create umbalanced for clustering experiment

clust = [100, 200, 400, 600, 800, 1000]
for c in clust:
    for g in range(1,11):
        for i in range(1, c+1):
            t = "cluster_algorithm/"+str(c)+"/"+str(g)
            headComp = 'gene1,gene2,'+','.join(hcent[2:])+','+','.join(hneig[2:])+','+','.join(hshor[2:])+',score\n'
            writedic(t, dic_complete, headComp)




