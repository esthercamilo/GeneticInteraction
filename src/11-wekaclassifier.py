from string import *
import os
from threading import Thread



threads = []
end=101
types = ['deg','bet','neigh','complete']

#Convert csv to arff
def convert():
	print '***********CONVERTING FROM CSV TO ARFF\n'
	for t in types:
		os.system("java weka.core.converters.CSVLoader weka/"+t+"/csv/exp/umbalanced.csv > weka/"+t+"/arff/umbalanced.arff")
		# for i in range(1,end):
			# os.system("java weka.core.converters.CSVLoader weka/"+t+"/csv/exp/"+str(i)+".csv > weka/"+t+"/arff/"+str(i)+".arff")
		

def setUmbalanced():
	for t in types:
		lista = []
		file = open('weka/'+t+'/arff/umbalanced.arff')
		for line in file:
			if '@attribute class numeric' in line:
				lista.append(line.replace('@attribute class numeric','@attribute class {AGG,ALL}'))
			else:
				lista.append(line)
		file.close()
		saida = open('weka/'+t+'/arff/umbalanced.arff','w')
		for i in range(len(lista)):
			saida.write(lista[i])	
		
#J48 output result, dot, model 
def j48():
	print '***********J48 output result, dot, model\n '
	nLeaves = 50
	types = ['deg','bet','neigh','complete']
	for t in types:
		for i in range(1,end):
			#RESULT EXP
			print 'J48 ',i
			os.system("java -Xmx1000m weka.classifiers.trees.J48 -d weka/"+t+"/model/"+str(i)+".model -M "+str(nLeaves)+" -t weka/"+t+"/arff/"+str(i)+".arff -i  > weka/"+t+"/result/"+str(i)+"-result.txt")
			#RESULT TO DRAW TREE
			os.system("java -Xmx1000m weka.classifiers.trees.J48 -M "+str(nLeaves)+" -g -t weka/"+t+"/arff/"+str(i)+".arff -i  > weka/"+t+"/dot/"+str(i)+"-result.dot")
			#RESULT RANDOM
			os.system("java -Xmx1000m weka.classifiers.trees.J48 -M "+str(nLeaves)+" -t weka/"+t+"/csv/random/"+str(i)+".csv -i  > weka/"+t+"/result_random/"+str(i)+"-result.txt")
	
#Draw trees		
def drawTrees():
	print '***********DRAWING TREES\n '
	types = ['deg','bet','neigh','complete']
	for t in types:
		for i in range(1,end):	
			os.system("dot -Tpng weka/"+t+"/dot/"+str(i)+"-result.dot -o weka/"+t+"/png/"+str(i)+"result.png")
		


def setModel():
	print '***********APPLYING MODEL\n'
	types = ['deg','bet','neigh','complete']
	for t in types:
		for i in range(1,end):	
			os.system("java -Xmx1000m weka.classifiers.trees.J48 -p 0 -T weka/"+t+"/arff/umbalanced.arff -l weka/"+t+"/model/"+str(i)+".model > weka/"+t+"/out/"+str(i)+".out")


# threadConvert = Thread(target=convert,args=())
# threadConvert.start()
# threadConvert.join()
		
# thSetUmbalanced = Thread(target=setUmbalanced,args=())
# thSetUmbalanced.start()
# thSetUmbalanced.join()		
		
# threadj48 = Thread(target=j48,args=())
# threadj48.start()
# threadj48.join()

# threadDrawTree = Thread(target=drawTrees,args=())
# threadDrawTree.start()
# threadDrawTree.join()

threadModel = Thread(target=setModel,args=())
threadModel.start()
threadModel.join()



