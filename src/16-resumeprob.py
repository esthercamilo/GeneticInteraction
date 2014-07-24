#given a probability file, this program extracts the probability value and 
#write a file with the instance name with the purpose of creating a prioritization list.

#to sort it in ascending order I used linux bash (sort)

import numpy as np
output = open('resumeprob.txt','w')


#read list of instances names
finst=open('completeSetAll.csv')
finst.readline()
listInst=[]
for line in finst:
	d=line.split(',')
	listInst.append((d[0],d[1]))
finst.close()


listas = []
for i in range(1,5):
	f = open('probabilities/'+str(i)+'_pred.out')
	l=[]
	for i in range(5):
		f.readline()
	allLines =  f.readlines()[0:-1]
	for elem in allLines:
		classe = elem[21:31]
		p = float(elem[33:].strip())
		if 'ALL' in classe:
			p = 1-p
		l.append(p)
	listas.append(l)

l_array = np.array(listas)
t_array = l_array.T
avgs = np.mean(t_array,axis=1)

for v in range(len(avgs)):
	output.write('%s\t%s\t%s\n' % (listInst[v][0],listInst[v][1],avgs[v]))


	