from string import *

#Read butland pairs
butfile = open('files/butscore.tab')
header = butfile.readline()
tuplasBut=[]
for line in butfile:
	data = line.split()
	tuplasBut.append((data[0],data[1]))

dicshortInt={}	
dicshortppi={}	
dicshortreg={}	
dicshortmet={}	
	
saida = open('spaths.tab','w')
saida.write('geneA\tgeneB\tspathsInt,spathsppi,spathsreg,spathsmet\n')
	
def getShort(nameFile,dic):
	shortfile = open('files/'+nameFile+'.tab')
	shortList = []
	for line in shortList:
		shortList.append(line.rstrip())

	for t in tuplasBut:
		s=0
		for l in shortList:
			if (t[0] in shortList) and (t[1] in shortList):
				s=s+1
		dic[t]=str(s)

getShort('spathsInt',dicshortInt)
getShort('spathsppi',dicshortppi)
getShort('spathsreg',dicshortreg)
getShort('spathsmet',dicshortmet)

#write files
for key in tuplasBut.keys():
	try:
		saida.write((('%s\t')*5)+'%s\n' % (key[0],key[1],dicshortInt[key],dicshortppi[key],dicshortreg[key],dicshortmet[key]))
	except Exception as e:
		print e
		
