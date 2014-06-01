from string import *


#read all attributes
fCent = open('files/centralites.tab')
headCent = fCent.readline()
fNeig = open('files/neighbor.tab')
headNeig = fNeig.readline()
fShor = open('files/shortest.tab')
headShor = fShor.readline()

llca=['degInt','degppi','degreg','degmet','betInt','betppi','betreg','betmet','regin','regout','metin','metout'] #list with labels
llna = ['cnInt','fswInt','jcInt','cnppi','fswppi','jcppi','cnreg','fswreg','jcreg','cnmet','fswmet','jcmet']		

#initialize dictionaires
exec("\n".join(['dic'+x+'={}' for x in llca]))
exec("\n".join(['dic'+x+'={}' for x in llna]))
dicShort={}

#fill dictionaries with data from files

for line in fCent:
	for i in range(1,len(llca)-1):
		d = line.split()
		for i in range(1,len(d)):
			exec('dic'+llca[i-1]+'[d[0]]=d['+str(i)+']')

for line in fNeig:
	for i in range(2,len(llna)):
		d = line.rstrip('\n').split(",")
		exec('dic'+llna[i-2]+'[(d[0],d[1])]=d['+str(i)+']')

			
for line in fShor:
	try:
		d=line.split()
		dicShort[(d[0],d[1])]=d[2]
	except Exception as e:
		pass
		
#all pairs can be taken from any dictionary
allpairs = diccnInt.keys()	
#save file with all attributes
fCompSet=open('files/completeSet.csv','w')
completeHeader = "geneA,geneB,"+    ",".join([x+"_max,"+x+"_min" for x in llca])    +","+    ",".join([x for x in llna])+",shortest,score\n"
fCompSet.write(completeHeader)

for genes in allpairs:
	try:
		gA = genes[0]
		gB = genes[1]
		strVars = ",".join(["max(dic"+x+"[gA],dic"+x+"[gB]),min(dic"+x+"[gA],dic"+x+"[gB])" for x in llca])+","+ ",".join(['dic'+x+'[(gA,gB)]' for x in llna])+",dicShort[(gA,gB)]"
		vars = eval(strVars)
		format = '%s,'*(2*len(llca)+len(llna)+1)+'?\n'
		fCompSet.write(format % vars)
	except Exception as e:
		pass
		


















		