#################################
#AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################

from string import *
import os

fcfg = open('config.txt')
folder = fcfg.readline().rstrip('\n')

def makedir(namedir):
	if not os.path.exists(namedir):
		os.makedirs(namedir)

#Folders structure

def folders(ce):
	makedir(folder+'weka/standart/'+ce+'/arff')
	makedir(folder+'weka/standart/'+ce+'/arff_rnd')
	makedir(folder+'weka/standart/'+ce+'/csv/exp')
	makedir(folder+'weka/standart/'+ce+'/csv/rnd')
	makedir(folder+'weka/standart/'+ce+'/dot')
	makedir(folder+'weka/standart/'+ce+'/model')
	makedir(folder+'weka/standart/'+ce+'/out')
	makedir(folder+'weka/standart/'+ce+'/png')
	makedir(folder+'weka/standart/'+ce+'/result')
	makedir(folder+'weka/standart/'+ce+'/result_rnd')
	makedir(folder+'weka/standart/'+ce+'/vote_result')
	makedir(folder+'weka/standart/'+ce+'/vote_result_rnd')
	makedir(folder+'weka/standart/'+ce+'/vote_threshold')
	
folders('deg')
folders('bet')
folders('neigh')
folders('complete')
folders('spaths')
folders('bet_sp')

def foldersCluster(ce):
    for i in range(1,11):
        makedir(folder+'weka/cluster_algorithm/'+ce+'/'+str(i)+'/arff')
        makedir(folder+'weka/cluster_algorithm/'+ce+'/'+str(i)+'/csv')
        makedir(folder+'weka/cluster_algorithm/'+ce+'/'+str(i)+'/model')
        makedir(folder+'weka/cluster_algorithm/'+ce+'/'+str(i)+'/out')
        makedir(folder+'weka/cluster_algorithm/'+ce+'/'+str(i)+'/result')

foldersCluster('100')
foldersCluster('200')
foldersCluster('400')
foldersCluster('600')
foldersCluster('800')
foldersCluster('1000')

#Experiment varying networks only for complete experiment
def foldersNet(ce):
    makedir(folder+'weka/networks/'+ce+'/arff')
    makedir(folder+'weka/networks/'+ce+'/csv')
    makedir(folder+'weka/networks/'+ce+'/model')
    makedir(folder+'weka/networks/'+ce+'/out')
    makedir(folder+'weka/networks/'+ce+'/result')


foldersNet('ppi') #excluding only ppi - evaluates the impact of ppi
foldersNet('reg') #excluding only reg - evaluates the impact of reg
foldersNet('met') #excluding only met - evaluates the impact of met

#Experiment testing BABU data
def foldersBabu():
    makedir(folder+'weka/Babu/arff')
    makedir(folder+'weka/Babu/csv')
    makedir(folder+'weka/Babu/model')
    makedir(folder+'weka/Babu/out')
    makedir(folder+'weka/Babu/result')

foldersBabu()

#Experiment varying percentage of nodes in network
def foldersPerc(t):
    makedir(folder+'weka/Percent/'+t+'/arff')
    makedir(folder+'weka/Percent/'+t+'/csv')
    makedir(folder+'weka/Percent/'+t+'/model')
    makedir(folder+'weka/Percent/'+t+'/out')
    makedir(folder+'weka/Percent/'+t+'/result')

t=[5,10,15,20,25,30]
for x in t:
    foldersPerc(str(x))

