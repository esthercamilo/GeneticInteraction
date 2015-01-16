#################################
#AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################

fcfg = open('config.txt')
folder = fcfg.readline().rstrip('\n')

# open files
fcent = open(folder+'files/cent_all.tab')
hcent = fcent.readline().split()
fneig = open(folder+'files/neigh_all.tab')
hneig = fneig.readline().split()
fshor = open(folder+'files/spathsall.tab')
hshor = fshor.readline().split()
fbabu = open(folder+'data/s-score-babu.tab')
hbabu = fbabu.readline()

#read Babu file
dicbabu={}    #numeric class
dicnombabu={} #nominal class
for line in fbabu:
    d = line.split()
    float_d = float(d[2].replace(',', '.'))
    classe = "AGG"
    if float_d>0:
        classe = "ALL"
    dicbabu[(d[0],d[1])]=d[2]
    dicnombabu[(d[0],d[1])]=classe
    dicbabu[(d[1],d[0])]=d[2]
    dicnombabu[(d[1],d[0])]=classe


diccent={}
for l in fcent:
    d = l.split()
    diccent[(d[0],d[1])]=d[2:]

dicneigh={}
for l in fneig:
    d = l.split()
    dicneigh[(d[0],d[1])]=d[2:]

dicsp={}
for l in fshor:
    d = l.split()
    dicsp[(d[0],d[1])]=d[2:]


dic_complete={}
for k in diccent.keys():
    dic_complete[k] = diccent[k] + dicneigh[k] + dicsp[k]






