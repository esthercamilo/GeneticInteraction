Genetic Interaction
==================

To follow this workflow, first you need to satisfy all requirements described in the file "src/requirement.txt".

01-networks-ppi-reg-met.py
Build dictionaries from data from DIP, Regulon and BIGG to create ppi.tab files, reg.tab, met.tab.

02-integrated-interactions.py
Read files ppi.tab, reg.tab and met.tab. Build int.tab integrated network.
The file int.tab contains the intersection of the three networks.

03-deg-bet.py
Read files ppi.tab, reg.tab, met.tab and int.tab to generate centralities.tab file whose header contains:
gene, degInt, degppi, degreg, degmet, betInt, betppi, betreg, betmet, regin, regout, metin, metout. Also generates the file genes.tab containing all genes in the integrated network.

04-butscore.py
Create the file butscore.tab (Genea, geneB, s-score).

05-splenght.py
Generate spathsbut.tab file (Butland instances) and spathsall.tab (all possible instances), whose header is "geneA, geneB, sp_int, sp_ppi, sp_met". Each measurement refers to the length of the shortest paths for each network. It was the only shortest path measure that yielded  different results from random performance.

06-neighbor.py
Generate the files neig_all.tab and neigh_butland.tab whose header is:
geneA,geneB,'cnInt','fswInt','jcInt','cnppi','fswppi','jcppi','cnreg','fswreg','jcreg','cnmet','fswmet','jcmet'
When the pair of Butland was not found on the network, the measurement was set to zero.

07-folderstructure.py
Set up folders.

08-cent_pairs.py
create two files: cent_but.tab e centall.tab. They contains "gene1,gene2,centralidades_max, centralidades_min" for all networks (degree e betweeness)

09-trainsetcsv.py
create the training sets not balanced for each type of experiment

10-trainset_balanced.py
create 100 csv files (experiment and random) for each attribute type and for the clustering experiment.

11-wekaclassifier.py
Convert the csv files to arff by removing the two first rows (gene names). Correct umbalanced file to match with the undersampling training file.
Apply J48 for all training sets, including for the clustering experiment.

12- metaVote.py
compute the Meta Vote for each set of attributes. Fill the folders "vote_result", "vote_model" and "vote_threshold". The last one is used

13-stat_metrics.py
create the file "metrics.txt" with the average of all performance measures and generate an input matrix ("matrix.txt") for the clustering experiment.

14-clustering.py
Apply weka clustering k-means with the data obtained in the step 12. Output: "cluster_assign.txt".


15-summaryClustAssign.py
Exclusive for the clustering experiment. Create the output file named
