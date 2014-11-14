from string import *
import os

fcfg = open('config.txt')
folder = fcfg.readline().rstrip('\n')

def makedir(namedir):
	if not os.path.exists(namedir):
		os.makedirs(namedir)

#Folders structure

def folders(ce):
	makedir(folder+'weka/'+ce+'/arff')
	makedir(folder+'weka/'+ce+'/csv/exp')
	makedir(folder+'weka/'+ce+'/csv/rnd')
	makedir(folder+'weka/'+ce+'/dot')
	makedir(folder+'weka/'+ce+'/model')
	makedir(folder+'weka/'+ce+'/out')
	makedir(folder+'weka/'+ce+'/png')
	makedir(folder+'weka/'+ce+'/result')
	makedir(folder+'weka/'+ce+'/vote_result')
	makedir(folder+'weka/'+ce+'/vote_threshold')
	makedir(folder+'weka/'+ce+'/vote_model')
	
folders('deg')
folders('bet')
folders('neigh')
folders('complete')
folders('spaths')
folders('bet_sp')

def foldersCluster(ce):
    for i in range(1,11):
        makedir(folder+'weka/complete/cluster_algorithm/'+ce+'/'+str(i)+'/arff')
        makedir(folder+'weka/complete/cluster_algorithm/'+ce+'/'+str(i)+'/csv')
        makedir(folder+'weka/complete/cluster_algorithm/'+ce+'/'+str(i)+'/model')
        makedir(folder+'weka/complete/cluster_algorithm/'+ce+'/'+str(i)+'/out')

foldersCluster('100')
foldersCluster('200')
foldersCluster('400')
foldersCluster('600')
foldersCluster('800')
foldersCluster('1000')


    