from string import *
import numpy as np

f_single_del = open('fba/SingleDeletion.txt')
f_double_del = open('fba/DoubleDeletion.txt')

#function normlize list
def normalize(dic):
	min_v = min([float(x) for x in dic.values()])
	max_v = max([float(x) for x in dic.values()])
	d = max_v - min_v
	newDic = {}
	for key in dic.keys():
		new_v = (float(dic[key])-min_v)/d
		newDic[key]=new_v
	return newDic

dicSingle={}
for line in f_single_del:
	d = line.split()
	dicSingle[d[0]]=d[1]

dicDouble={}
for line in f_double_del:
	d = line.split()
	dicDouble[(d[0],d[1])]=d[2]
	dicDouble[(d[1],d[0])]=d[2]

dicSingle_norm = normalize(dicSingle)	
dicDouble_norm = normalize(dicDouble)

dicscorefba={}
for p in dicDouble.keys():
	score = dicDouble_norm[p]-(dicSingle_norm[p[0]]*dicSingle_norm[p[1]])
	dicscorefba[p]=score
	dicscorefba[(p[1],p[0])]=score #inverso

#butland file for training set
fbut=open('files/butscore.tab')
dicbut={}
for line in fbut:
	d = line.split()
	dicbut[(d[0],d[1])]=d[2]	
	
output = open('files/fba.tab','w')
output.write('gene1\tgene2\tfba\tscore\n')
for k,v in dicbut.iteritems():
	try:
		output.write('%s\t%s\t%s\t%s\n' % (k[0],k[1],dicscorefba[k],dicbut[k]))
	except:
		pass
	
# print '\n'.join([str(x) for x in dicSingle_norm.values()])
# print '\n'.join([str(x) for x in dicDouble_norm.values()])
print '\n'.join([str(x) for x in dicscorefba.values()])
