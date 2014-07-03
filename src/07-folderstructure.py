from string import *
import os

def makedir(namedir):
	if not os.path.exists(namedir):
		os.makedirs(namedir)

#Folders structure

def folders(ce):
	makedir('weka/'+ce+'/arff')
	makedir('weka/'+ce+'/csv')
	makedir('weka/'+ce+'/dot')
	makedir('weka/'+ce+'/model')
	makedir('weka/'+ce+'/out')
	makedir('weka/'+ce+'/png')
	makedir('weka/'+ce+'/result')
	makedir('weka/'+ce+'/vote_result')
	makedir('weka/'+ce+'/vote_threshold')
	makedir('weka/'+ce+'/vote_model')
	
folders('deg')
folders('bet')
folders('neigh')
folders('complete')
folders('spaths')


def foldersCluster(ce):
    for i in range(1,11):
        makedir('weka/complete/cluster_algorithm/'+ce+'/'+str(i)+'/arff')
        makedir('weka/complete/cluster_algorithm/'+ce+'/'+str(i)+'/csv')
        makedir('weka/complete/cluster_algorithm/'+ce+'/'+str(i)+'/model')
        makedir('weka/complete/cluster_algorithm/'+ce+'/'+str(i)+'/out')

foldersCluster('200')    
foldersCluster('400')
foldersCluster('600')
foldersCluster('800')
foldersCluster('1000')


    