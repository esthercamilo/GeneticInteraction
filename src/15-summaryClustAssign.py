t2=[200,400,600,800,1000]

f_out = open('weka/complete/cluster_algorithm/summary.txt','w')
			
def selectTree():
	for t in t2:
		for i in range(1,11):
			file = open('weka/complete/cluster_algorithm/' + str(t) + '/'+str(i)+'/cluster_assign.txt')
			print file
			group1 = []
			group2 = []
			group3 = []
			group4 = []
			for line in file:
				d = line.split()
				if len(d) < 2:
					continue
				if '0' in d[1]:
					group1.append(d[0])
				elif '1' in d[1]:
					group2.append(d[0])
				elif '2' in d[1]:
					group3.append(d[0])
				elif '3' in d[1]:
					group4.append(d[0])
				else:
					printf("only different zero\n");
			lengths = sorted([len(group1),len(group2),len(group3),len(group4)])
			f_out.write('%s,%s,%s,%s,%s\n' % (t,lengths[0],lengths[1],lengths[2],lengths[3]))

selectTree()			