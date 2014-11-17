#################################
#AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################

fcfg = open('config.txt')
folder = fcfg.readline().rstrip('\n')


fgenes=open(folder+'files/genes.tab')
genes = [x.split()[0] for x in fgenes.readlines()]

allpairs=[]
for i in range(len(genes)):
    for j in range(i+1,len(genes)):
        allpairs.append((genes[i],genes[j]))

fbut=open(folder+'files/butscore.tab')
butheader = fbut.readline()
dicbut={}
for line in fbut:
    d=line.split()
    dicbut[(d[0],d[1])]=d[2]
fbut.close()

fcent=open(folder+'files/centralites.tab')
centheader = fcent.readline()
llca=centheader.split()[1:]
diccent={}
for line in fcent:
    d=line.split()
    diccent[d[0]]=d[1:]
fcent.close()

def mergeLists(list1,list2):
	size = len(list1)
	newList=[]
	for i in range(size):
		x = float(list1[i])
		y = float(list2[i])
		min_c = min(x,y)
		max_c = max(x,y)
		newList.append(str(min_c))
		newList.append(str(max_c))
	return newList

def savePairs(nameFile,pares):
    out=open(folder+'files/'+nameFile+'.tab','w')
    h_str='geneA\tgeneB\t'+'\t'.join([x+'_min'+'\t'+x+'_max' for x in llca])+'\n'
    out.write(h_str)
    
    for p in pares:
        try:
            centA = diccent[p[0]]
            centB = diccent[p[1]]
            cAcB = mergeLists(centA,centB)
            strCent = '\t'.join([x for x in cAcB])+'\t'
            out.write(p[0]+'\t'+p[1]+'\t'+strCent+'\n')
        except:
            pass
        

savePairs('cent_but',dicbut.keys())
print 'Butland pairs saved'
savePairs('cent_all',allpairs)
print 'All pairs saved'

