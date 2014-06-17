import os
from threading import Thread
import random as rm

types = ['deg','bet','neigh','complete']

fSelected = open('weka/SelectedTrees.txt','w')
listSelected=[]

def clustering():
	for t in types:
		try:
			os.remove('weka/'+t+'/cluster_assign.txt')
		except:
			pass
		os.system('java weka.clusterers.SimpleKMeans -p 0 -N 4 -t weka/'+t+'/matrix.csv > weka/'+t+'/cluster_assign.txt')

threadCluster = Thread(target=clustering,args=())
threadCluster.start()
threadCluster.join()

def selectTree():
	for t in types:
		file = open('weka/'+t+'/cluster_assign.txt')
		group1=[]
		group2=[]
		group3=[]
		group4=[]
		for line in file:
			d = line.split()
			if len(d)<2:
				continue
			if '0' in d[1]:
				group1.append(d[0])
			elif '1' in d[1]:
				group2.append(d[0])
			elif '2' in d[1]:
				group3.append(d[0])
			elif '3' in d[1]:
				group4.append(d[0])
			else:
				printf("only different zero\n");
		#largest group:
		largest = max(max(max(len(group1),len(group2)),len(group3)),len(group4))
		dicSize={}
		dicSize[len(group1)]='group1'	
		dicSize[len(group2)]='group2'	
		dicSize[len(group3)]='group3'	
		dicSize[len(group4)]='group4'		
			 
		largestGroup = dicSize.get(largest)	 

		randomTree = rm.randint(0, len(eval(largestGroup)))
		fSelected.write('TREE SELECTED: '+t+'\t'+str(randomTree+1)+'\n')


thSelectTree = Thread(target=selectTree,args=())
thSelectTree.start()
thSelectTree.join()	