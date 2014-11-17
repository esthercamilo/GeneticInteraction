#################################
#AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################

import os

fcfg = open('config.txt')
folder = fcfg.readline().rstrip('\n')
wekalocation = fcfg.readline().rstrip('\n')

types = ['deg', 'bet', 'neigh', 'complete', 'spaths', 'bet_sp']

def clustering():
	for t in types:
		try:
			os.remove(folder+'weka/' + t + '/cluster_assign.txt')
		except:
			pass
		os.system(
			'java weka.clusterers.SimpleKMeans -p 0 -N 4 -t '+folder+'weka/' + t + '/matrix.csv > '+folder+'weka/' + t + '/cluster_assign.txt')




t2=[100,200,400,600,800,1000]

def clust2():
	for t in t2:
		for i in range(1,11):
			f_in  = folder+'weka/complete/cluster_algorithm/' + str(t) + '/'+str(i)+'/matrix.csv'
			f_out = folder+'weka/complete/cluster_algorithm/' + str(t) + '/'+str(i)+'/cluster_assign.txt'
			os.system('java -cp '+wekalocation+' weka.clusterers.SimpleKMeans -p 0 -N 4 -t '+f_in+' > '+f_out)

clust2()	
	
	


