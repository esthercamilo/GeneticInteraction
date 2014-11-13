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

#read butland
dicbut={}
for line in fbut:
    d = line.split()
    dicbut[(d[0],d[1])]=d[2]

#generate a dictionary for each type
start_dics = ['dic_' + x for x in types]
#initialize
exec ('\n'.join([x + '={}' for x in start_dics]))

#dics deg e bet
dicdegbet={}
dic_deg={}
dic_bet={}
dic_neigh={}
dic_spaths={}
dic_bet_spaths={}
dic_complete={}

for line in fcent:
    d = line.rstrip('\n').split(",")
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
    dic_bet_spaths[k] = dic_bet[k] + dic_spaths[k]

#dic complete
for k in dic_bet.keys():
    dic_complete[k] = dicdegbet[k] + dic_neigh[k] + dic_spaths[k]

#Output umbalanced:
def writedic(t,dic,header):
    file = open(folder+'weka/'+t+'/csv/umbalanced_num.csv','w')
    file.write(header)
    for k,v in dic.iteritems():
        file.write(k[0]+','+k[1]+','+','.join([x for x in v])+','+dicbut[k]+'\n')

headDeg = 'gene1,gene2,'+','.join(hcent[2:10]+hcent[18:])+',score\n'
writedic('deg', dic_deg,headDeg)

headBet = 'gene1,gene2,'+','.join(hcent[10:18])+',score\n'
writedic('bet', dic_bet,headBet)

headNei = 'gene1,gene2,'+','.join(hneig[2:])+',score\n'
writedic('neigh',dic_neigh,headNei)

headSho = 'gene1,gene2,'+','.join(hshor[2:])+',score\n'
writedic('spaths', dic_spaths, headSho)

headBetSho = 'gene1,gene2,'+','.join(hcent[10:18])+','+','.join(hshor[2:])+',score\n'
writedic('bet_sp', dic_bet_spaths, headBetSho)

headComp = 'gene1,gene2,'+','.join(hcent[2:])+','+','.join(hneig)+','+','.join(hshor)+',score\n'
writedic('complete', dic_complete, headComp)



