from string import *


#read all attributes
fCent = open('files/centralites.tab')
headCent = fCent.readline()
fNeig = open('files/neighbor.tab')
headNeig = fNeig.readline()


llca=headCent.split()[1:]
#['degInt','degppi','degreg','degmet','betInt','betppi','betreg','betmet','regin','regout','metin','metout']
llna =headNeig.split()[2:]
#['cnInt','fswInt','jcInt','cnppi','fswppi','jcppi','cnreg','fswreg','jcreg','cnmet','fswmet','jcmet']		


#initialize dictionaires
exec("\n".join(['dic'+x+'={}' for x in llca]))
exec("\n".join(['dic'+x+'={}' for x in llna]))
dicShort={}

#fill dictionaries with data from files
dicCompletCent={}
for line in fCent:
	d = line.split()
	for i in range(len(llca)):
		dicCompletCent[d[0]]=d[1:]
		#exec('dic'+llca[i]+'[d[0]]=d['+str(i+1)+']')

#TEST
# print dicdegInt['b3356']	#5	
# print dicdegppi['b3352']	#1	
# print dicdegreg['b2517']	#0	
# print dicbetppi['b3131']	#1.42263677772e-05	

#function merge two lists in order min,max
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

#GROUP FILENEIGH TO CENTRALITIES TO GET A COMPLETE TRAINING SET
output = open('files/completeTrainingSet.csv','w')	

#['dicdegInt', 'dicdegppi', 'dicdegreg', 'dicdegmet', 'dicbetInt', 'dicbetppi', 'dicbetreg', 'dicbetmet', 'dicregin', 'dicregout', 'dicmetin', 'dicmetout']
headerCent = 'geneA,geneB,'+','.join([x+'_min'+','+x+'_max' for x in llca])+','+','.join([x for x in llna])+'\n'
output.write(headerCent)

for line in fNeig:
	n = line.split() #  n[0]=geneA, n[1]=geneB
	centA = dicCompletCent[n[0]]
	centB = dicCompletCent[n[1]]
	cAcB = mergeLists(centA,centB)
	strCent = ','.join([x for x in cAcB])+','
	strNeig = ','.join([x for x in n[2:]])+'\n'
	output.write(n[0]+','+n[1]+','+strCent+strNeig)

	


