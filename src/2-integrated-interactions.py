from string import *

fppi = "ppi.tab"
freg = "reg.tab"
fmet = "met.tab"
fint = open("files/int.tab","w")

def getInteraction(namefile):
	file = open('files/'+namefile)
	list = []
	for line in file:
		nodes=split(line)
		nodes = sorted(nodes)
		list.append((nodes[0],nodes[1]))
	return list

listppi=getInteraction(fppi)
listreg=getInteraction(freg)
listmet=getInteraction(fmet)

#Rede integrada
listInt = list(set(listppi) | set(listreg) | set(listmet))

for elem in listInt:
	fint.write(elem[0]+"\t"+elem[1]+"\n")
