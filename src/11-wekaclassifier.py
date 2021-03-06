#################################
#AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################

import os
import sys

fcfg = open('config.txt')
folder = fcfg.readline().rstrip('\n')

wekalocation = fcfg.readline().rstrip('\n')

import os
from threading import Thread

threads = []
types = ['bet', 'bet_sp', 'complete', 'deg', 'neigh', 'spaths']
clust = [100,200, 400, 600, 800, 1000]
end = 101


# Convert csv to arff
def convert():
	print '***********CONVERTING FROM CSV TO ARFF - remove gene1 and gene2 attributes\n'
	for t in types:
		print t
		os.system(    "java -cp "+wekalocation+" weka.filters.unsupervised.attribute.Remove -R 1,2 -i "+folder+ "/weka/" + t + "/csv/umbalanced_nom.csv -o "+ folder+ "weka/" + t + "/arff/umbalanced_nom.arff")
		for i in range(1, end):
			os.system("java -cp "+wekalocation+" weka.filters.unsupervised.attribute.Remove -R 1,2 -i "+folder+ "/weka/" + t + "/csv/exp/" + str(i) + ".csv > "+ folder+ "weka/" + t + "/arff/" + str(i) + ".arff")
			os.system("java -cp "+wekalocation+" weka.filters.unsupervised.attribute.Remove -R 1,2 -i "+folder+ "/weka/" + t + "/csv/rnd/" + str(i) + ".csv > "+ folder+ "weka/" + t + "/arff_rnd/" + str(i) + ".arff")


def setClassOrder():
	for t in types:
		farff = open(folder+ "weka/" + t + "/arff/umbalanced_nom.arff")
		farff_out = open(folder+ "weka/" + t + "/arff/umbalanced2.arff","w")
		for line in farff:
			if line=="@attribute score numeric\n":
				farff_out.write("@attribute score {AGG,ALL}\n")
			else:
				farff_out.write(line)
		farff.close()
		farff_out.close()
		os.remove(folder+ "weka/" + t + "/arff/umbalanced_nom.arff")
		os.rename(folder+ "weka/" + t + "/arff/umbalanced2.arff",folder+ "weka/" + t + "/arff/umbalanced.arff")

# J48 output result, dot, model
def j48():
	print '***********J48 output result, dot, model\n '
	nLeaves = 50
	for t in types:
		for i in range(1, end):
			print 'J48 ', i
			str1 = "java -cp "+wekalocation+" -Xmx1000m weka.classifiers.trees.J48 -d "+ folder+ "weka/" + t + "/model/" + str(i) + ".model -M " + str(nLeaves) + " -t "+folder+"/weka/" + t + "/arff/" + str(i) + ".arff -i  > "+folder+"/weka/" + t + "/result/" + str(i) + "-result.txt"
			str2 = "java -cp "+wekalocation+" -Xmx1000m weka.classifiers.trees.J48 -M " + str(nLeaves) + " -t "+folder+"/weka/" + t + "/arff_rnd/" + str(i) + ".arff -i  > "+folder+"/weka/" + t + "/result_rnd/" + str(i) + "-result.txt"
			str3 = "java -cp "+wekalocation+" -Xmx1000m weka.classifiers.trees.J48 -M " + str(nLeaves) + " -g -t "+ folder+ "weka/" + t + "/arff/" + str(i) + ".arff -i  > "+ folder+ "weka/" + t + "/dot/" + str(i) + "-result.dot"
			os.system(str1)
			os.system(str2)
			os.system(str3)

# Draw trees
def drawTrees():
	print '***********DRAWING TREES\n '
	for t in types:
		for i in range(1, end):
			os.system(
				"dot -Tpng "+ folder+ "weka/" + t + "/dot/" + str(i) + "-result.dot -o "+ folder+ "weka/" + t + "/png/" + str(i) + "result.png")


def setModel():
	print '***********APPLYING MODEL\n'
	for t in types:
		for i in range(1, end):
			os.system(
				"java -cp "+wekalocation+" -Xmx1000m weka.classifiers.trees.J48 -p 0 -T "+ folder+ "weka/" + t + "/arff/umbalanced.arff -l "+ folder+ "weka/" + t + "/model/" + str(
					i) + ".model >  "+ folder+ "weka/" + t + "/out/" + str(i) + ".out")


def arffcluster():
    print '***********CLUSTER EXPERIMENT: Converting to arff\n '
    for c in clust:
        for n in range(1, 11):
            os.system("java -cp "+wekalocation+" weka.filters.unsupervised.attribute.Remove -R 1,2 -i "+folder+"/weka/complete/cluster_algorithm/"+str(c)+"/"+str(n)+"/csv/umbalanced_nom.csv -o "+ folder+ "weka/complete/cluster_algorithm/"+str(c)+"/"+str(n)+"/arff/umbalanced_nom.arff")
            for i in range(1, c + 1):
                print "c:",c," n:",n," i:",i
                f1 = folder+ "weka/complete/cluster_algorithm/" + str(c)+"/" + str(n) + "/csv/" + str(i) + ".csv"
                f2 = folder+"weka/complete/cluster_algorithm/" + str(c)+"/" + str(n) + "/arff/" + str(i) + ".arff"
                mystr = "java -cp "+wekalocation+" weka.filters.unsupervised.attribute.Remove -R 1,2 -i "+f1+" -o "+f2
                os.system(mystr)


def j48_cluster():
    print '***********J48 output result, model\n '
    nLeaves = 50
    for c in clust:
        for n in range(1,11):
            for i in range(1, c+1):
                print "c:",c," n:",n," i:",i
                f2 = folder+"weka/complete/cluster_algorithm/" + str(c)+"/" + str(n) + "/arff/" + str(i) + ".arff"
                f3 = folder+"weka/complete/cluster_algorithm/" + str(c)+"/" + str(n) + "/model/" + str(i) + ".model"
                f4 = folder+"weka/complete/cluster_algorithm/" + str(c)+"/" + str(n) + "/result/" + str(i) + ".result"
                os.system("java -cp "+wekalocation+" -Xmx1000m weka.classifiers.trees.J48 -d "+f3+" -M " + str(nLeaves) + " -t "+f2+" -i  > "+f4)


def setModelCluster():
    print '***********APPLYING MODEL IN THE CLUSTERS\n'
    for c in clust:
        for g in range(1,11):
            for i in range(1, c+1):
                t = "complete/cluster_algorithm/"+str(c)+"/"+str(g)
                f1 = folder+ "weka/"+t+"/arff/umbalanced_nom.arff"
                f2 = folder+ "weka/"+t+"/model/"+ str(i)+".model"
                f3 = folder+ "weka/"+t+"/out/"+ str(i)+".out"
                os.system("java -cp "+wekalocation+" -Xmx1000m weka.classifiers.trees.J48 -p 0 -T "+ f1+" -l "+ f2 + " >  "+ f3)



threadConvert = Thread(target=convert, args=())
threadConvert.start()
threadConvert.join()

threadSetOrder = Thread(target=setClassOrder(), args=())
threadSetOrder.start()
threadSetOrder.join()

threadj48 = Thread(target=j48, args=())
threadj48.start()
threadj48.join()

threadDrawTree = Thread(target=drawTrees, args=())
threadDrawTree.start()
threadDrawTree.join()

threadModel = Thread(target=setModel, args=())
threadModel.start()
threadModel.join()

threadAffClust = Thread(target=arffcluster, args=())
threadAffClust.start()
threadAffClust.join()

th_j48_cluster = Thread(target=j48_cluster(), args = ())
th_j48_cluster.start()
th_j48_cluster.join()

th_Model_cluster = Thread(target=setModelCluster(), args = ())
th_Model_cluster.start()
th_Model_cluster.join()