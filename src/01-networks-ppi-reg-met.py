#################################
#AUTHOR: ESTHER CAMILO          #
#e-mail: esthercamilo@gmail.com #
#################################

from string import *
import re
from libsbml import *
import collections
import sys

#from collections import defaultdict
#import numpy as np
#import random as rm


#Local of input files
finput = open("config.txt")
fstringinput = finput.readline().rstrip("\n")

if not os.path.exists(fstringinput+'/files'):
		os.makedirs(fstringinput+'/files')


#return a dictionary key=GeneName,value=BlatnerName
def geneBlatner(fileName):
	file = open(fileName)
	labelfileGNB = file.readline()
	dicGNB={}
	for line in file:
		line = line.replace('"','').replace(" ","") #remove spaces and commas
		data = line.rstrip().split(",")
		names = data[3].split("//")
		dicGNB[data[0].lower()]=data[1]
		for elem in names:
			dicGNB[elem.lower()]=data[1]
	file.close()
	return dicGNB

def uniprotBlatner(fileName):
	file=open(fileName)
	labelfileUP = file.readline()
	dicUPB={}
	#fileLog.write("The following uniprotkb id has no Blatner Number\n")
	p = re.compile('b\d\d\d\d')
	for line in file:
		data = line.split("\t")
		#Dic Uniprot - Blatner
		try:
			bname = (p.search(data[4])).group()
			dicUPB[data[0]]=bname
		except:
			try:
				names = data[4].split()
				for elem in names:
					dicUPB[data[0]]=dicGNB[elem] #Try to find in the dictionary dicUPGN
					break
			except:
				pass
	return dicUPB

def processList(list):
	listItera = set(list)
	newList = set(list)
	for elem in listItera:
		oito = elem[0]+elem[1]
		if (len(oito) < 8):
			newList.remove(elem)
	return newList

def saveTemp(list,namefile): #without extension
	saida = open(fstringinput+"files/"+namefile+".tab","w")
	for elem in list:
		if len(elem)==2:
			saida.write(elem[0]+"\t"+elem[1]+"\n")
	saida.close()	


#Dictionary (key=GeneName,value=BlatnerName)
dicGNB=geneBlatner(fstringinput+'data/GeneNames.csv') #(GNB=GeneNameBlatner)
#Dictionary (key=UniProtkb,value=BlatnerName)
dicUPB=uniprotBlatner(fstringinput+'data/uniprot-organismEscherichiaColi.tab')#(UPB=UniProtBlatner)


	
def getPpi():
	listppi=[]
	fileDIP=open(fstringinput+'data/Ecoli20140117.txt')
	labelFileDIP = fileDIP.readline()
	p = re.compile('uniprotkb:.*')
	for line in fileDIP:
		data=line.split("\t")
		#count number of times "uniprotkb" appears on the line
		soma=0
		for index in data:
			if "uniprotkb" in index:
				soma=soma+1
		if soma==2: #if uniprot appear twice, then we have reference for both interacting genes
			try:
				queryA = ((p.search(data[0])).group()).replace("uniprotkb:","")
				queryB = ((p.search(data[1])).group()).replace("uniprotkb:","")
				upNameA= dicUPB[queryA]
				upNameB= dicUPB[queryB]
				listppi.append((dicGNB[upNameA],dicGNB[upNameB]))
			except:
				pass
				#print traceback.format_exc()
	print len(listppi)			
	return listppi		
	
def readRegulon(file,listreg):
	provListTF=[]
	for line in file:
		if line[0]=="#":
			next(file)
		else:
			data = line.split()
			try:
				if "-" in data[0] and len(data[0])>4:
					twofs = data[0].split("-")
					for g in twofs:
						provListTF.append((g,data[1]))
				elif "-" in data[0] and len(data[0])<=4:
					newGene = data[0].replace("-","")
					provListTF.append((newGene,data[1]))
				else:
					provListTF.append((data[0],data[1]))	
			except Exception as e:
				print e
	file.close()
	#take care capital letters
	#important cases: HU (hupA and hupB) and IHF (ihfA and ihfB)
	for t in provListTF:
		if (t[0]=="HU"):
			try:
				listreg.append((dicGNB["hupa"],dicGNB[t[1].lower()]))
				listreg.append((dicGNB["hupb"],dicGNB[t[1].lower()]))
			except:
				pass
		elif (t[0]=="IHF"):
			try:
				listreg.append((dicGNB["ihfa"],dicGNB[t[1].lower()]))
				listreg.append((dicGNB["ihfb"],dicGNB[t[1].lower()]))
			except:
				pass
		elif (len(t[0])>4):
			g1 = t[0][0:4].lower()
			g2 = (t[0][0:3]+t[0][4]).lower()
			try:
				listreg.append((dicGNB[g1],dicGNB[t[1].lower()]))
				listreg.append((dicGNB[g2],dicGNB[t[1].lower()]))
			except:
				pass
		else:
			try:
				listreg.append((dicGNB[t[0].lower()],dicGNB[t[1].lower()]))
			except:
				pass
	file.close()
	return listreg
	
def getReg(listreg):		 
	fileTFsigma=open(fstringinput+"data/network_sigma_gene.txt")
	fileTFgene=open(fstringinput+"data/network_tf_gene.txt")
	fileNetTF=open(fstringinput+"data/network_tf_tf.txt")

	dicsigma={}
	dicsigma["Sigma19"]="feci"
	dicsigma["Sigma24"]="rpoe"
	dicsigma["Sigma28"]="flia"
	dicsigma["Sigma32"]="rpoh"
	dicsigma["Sigma38"]="rpos"
	dicsigma["Sigma54"]="rpon"
	dicsigma["Sigma70"]="rpod"
			
	provListSigmas=[] #create tuple with sigma - gene, because there is line with two sigmas
	for line in fileTFsigma:
		if line[0]=="#":
			next(fileTFsigma)
		else:
			data = line.split()
			try:
				if "," in data[0]:
					twoSigmas = data[0].split(",")
					for g in twoSigmas:
						provListSigmas.append((g,data[1]))				
			except Exception as e:
				print e
	#fill the listreg
	for i in provListSigmas:
		gA=gB=None
		try:
			gA = dicGNB[dicsigma[i[0]]]
		except:
			pass
		try:
			gB = dicGNB[i[1].lower()]
		except:
			pass
		if (gA != None) and (gB !=None):
			listreg.append((gA,gB))

	provListTF=[] #create tuple with tf - gene, because there is line with two tf
	#Obs: there is h-ns. Change to hns
	#do all the same for the file 		
	readRegulon(fileTFgene,listreg)		
	readRegulon(fileNetTF,listreg)		
	return listreg	
	
def getMet():
	listmet=[]
	sbmldoc = readSBML(fstringinput+"data/msb201165-s3.xml")
	model = sbmldoc.getModel();
	reactions = model.getListOfReactions()
	dicReactionGenes={} # key = reaction; value = gene list
	p = re.compile('b\d\d\d\d')
	#I did a dictionary which a string reactions as key
	for r in reactions:
		notes = r.getNotesString()
		try:
			bname = re.findall(p,notes)
			dicReactionGenes[str(r)]=(bname)
		except:
			print "erro"
	listmet=[]
	#exclude promiscuous species as H20
	# First step is to generate a list with these repetitive species
	speciesFromReactions=[]
	for r in reactions:
		lop = r.getListOfProducts()
		lor = r.getListOfReactants()
		for p in lop:
			speciesFromReactions.append(p.getSpecies())
		for r in lor:
			speciesFromReactions.append(r.getSpecies())
	counter=collections.Counter(speciesFromReactions)
	#The 8 more promiscuous
	tuplesOfPromiscuous = counter.most_common(8) #tuple (species,repetitions)
	listOfPromiscuous=[]
	for t in tuplesOfPromiscuous:
		listOfPromiscuous.append(model.getSpecies(t[0]).getId())
	for reactionA in reactions:
		listOfProducts = reactionA.getListOfProducts()
		for product in listOfProducts:
			specieProduct = product.getSpecies()
			#If in promiscuous, skip it		
			if specieProduct in listOfPromiscuous:
				continue
			for reactionB in reactions:
				listOfReactants = reactionB.getListOfReactants()
				for reactant in listOfReactants:
					specieReactant = reactant.getSpecies()
					
					#print "esther",specieProduct,specieReactant
					
					#If in promiscuous, skip it
					if specieReactant in listOfPromiscuous:
						continue
					if specieProduct==specieReactant:
						listG_A = dicReactionGenes[str(reactionA)] # get list of genes from reaction A
						listG_B = dicReactionGenes[str(reactionB)] # get list of genes from reaction B
						for x in listG_A: # combine genes from A and B
							for y in listG_B:
								listmet.append((x,y))
	return listmet
	
	

listppi=getPpi()
#ppi is not directed (remove a=b b=a)
listppi=processList(listppi)
saveTemp(set(listppi),"ppi")	

listreg=[]
listreg=getReg(listreg)
listreg = processList(listreg)
saveTemp(listreg,"reg")	

listmet=getMet()
listmet = processList(listmet)		
saveTemp(listmet,"met")	
	

	
