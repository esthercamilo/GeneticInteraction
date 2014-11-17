#################################
#AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################

from string import *
import xlrd
import collections
from collections import defaultdict

fcfg = open('config.txt')
folder = fcfg.readline().rstrip('\n')

saida=open(folder+'files/butscore.tab','w')
saida.write('geneA\tgeneB\ts-score\n')

dicbut={}
#Butland scores comes in xls file
workbook = xlrd.open_workbook(folder+'data/nmeth.1239-S4.xls')
worksheet = workbook.sheet_by_name('st3')
#calculate the average of repeated values
s=[]
d = defaultdict(list)
for i in range(3,1382): #need to check rows inside the xls file
	geneA = str(worksheet.cell_value(i, 1))
	geneB = str(worksheet.cell_value(i, 3))
	score = worksheet.cell_value(i, 7)
	s.append(((geneA,geneB),score))
for k,v in s:
	d[k].append(v)
result = {}
for na,va in d.iteritems():
	result[na] = sum(va) / float(len(va))
	dicbut[na]=result[na]

for k,v in dicbut.iteritems():
	saida.write('%s\t%s\t%s\n' % (k[0],k[1],v))

	
