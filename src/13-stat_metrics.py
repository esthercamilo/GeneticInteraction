# ################################
#AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################

from string import *
import numpy as np

fcfg = open('config.txt')
folder = fcfg.readline().rstrip('\n')

types = ['deg', 'bet', 'neigh', 'complete', 'spaths', 'bet_sp']
clust = [100, 200, 400, 600, 800, 1000]

#Read result and return the averages:  TP, FP, Precision, Recall, F, AUC for the cross-validation
def readWeka(att, folder_result):
    listFiles = []
    for i in range(1, 101):
        file = open(folder + "weka/" + att + "/" + folder_result + "/" + str(i) + "-result.txt")
        thisLine = ''
        while 'Stratified cross-validation' not in thisLine:
            thisLine = file.readline()
        while 'Detailed Accuracy By Class' not in thisLine:
            thisLine = file.readline()
        for j in range(2):
            thisLine = file.readline()
        dic = {}
        for l in range(3):
            avg = file.readline()
            TP = float(avg[16:24].strip())
            FP = float(avg[25:35].strip())
            Precision = float(avg[35:45].strip())
            Recall = float(avg[45:55].strip())
            F = float(avg[55:65].strip())
            ROC = float(avg[65:75].strip())
            classe = avg[75:85].strip()
            if classe == '':
                classe = 'AVG'
            dic[classe] = [TP, FP, Precision, Recall, F, ROC]
        listFiles.append(dic)
    return listFiles


def avgListArrays(listArrays):
    summation = 0
    for elem in listArrays:
        summation = summation + elem
    return summation / len(listArrays)


def metricas(tipo,name_output):

    output = open(folder + 'weka/' + tipo + '/'+name_output, 'w')

    output.write(tipo+"\n\n")

    output.write("Respectively, the J48 experiment, J48 random, Meta Vote experiment and Meta Vote random\n")
    output.write("-----------------------------------------------------------------------------------------\n")
    output.write("-----------------------------------------------------------------------------------------\n")
    #Average Experiment

    for resulttype in ["result","result_rnd","vote_result","vote_result_rnd"]:
        arrayDeg = readWeka(tipo, resulttype)
        arrayAGGexp = []
        arrayALLexp = []
        arrayAVGexp = []
        for elem in arrayDeg:
            arrayAGGexp.append(np.array(elem['AGG']))
            arrayALLexp.append(np.array(elem['ALL']))
            arrayAVGexp.append(np.array(elem['AVG']))

        avgAGGexp = avgListArrays(arrayAGGexp)
        avgALLexp = avgListArrays(arrayALLexp)
        avgAVGexp = avgListArrays(arrayAVGexp)

        output.write(resulttype+'\n')
        output.write('TP\t&\tFP\t&\tPrecision\t&\tRecall\t&\tF\t&\tAUC\n')
        output.write('\nAGG\n')
        output.write('\t&\t'.join([str(x) for x in avgAGGexp]))
        output.write('\nALL\n')
        output.write('\t&\t'.join([str(x) for x in avgALLexp]))
        output.write('\nAVG\n')
        output.write('\t&\t'.join([str(x) for x in avgAVGexp]))
        output.write('\n\n\n\n')
    output.close()


#MATRIX INPUT FOR REPRESENTATIVE TREE


def readOutFile(tipo):
    #firstLine
    saida = open(folder + 'weka/' + tipo + '/matrix.csv', 'w')

    #check the lenght of any tree
    tempfile = open(folder+'weka/' + tipo + '/out/1.out')
    templines = tempfile.readlines()
    last = int(templines[-2][0:10].strip())
    tempfile.close()

    primer = "inst1"
    for j in range(2, last+1):
        primer = primer + ",inst" + str(j)
    saida.write(primer + "\n")
    inst = []
    for tree in range(100):
        thisTree = []
        file = open(folder+'weka/' + tipo + '/out/' + str(tree + 1) + '.out')
        lines = file.readlines()[5:-1]
        for i in range(len(lines)):
            if "AGG" in lines[i]:
                (thisTree.append(float((lines[i][33:]).strip())))
            else:
                (thisTree.append(1 - float((lines[i][33:]).strip())))
        inst.append(thisTree)

    for elem in inst:
        line = ','.join([str(x) for x in elem])
        saida.write(line + "\n")



for t in types:
    metricas(t,"metrics.txt")
    readOutFile(t)



#MATRIX INPUT FOR CLUSTERING EXPERIMENT
for c in clust:
    for g in range(1,11):
        tipo = "complete/cluster_algorithm/"+str(c)+"/"+str(g)
        readOutFile(tipo)

