Genetic Interaction
==================
01-networks-ppi-reg-met.py
Build dictionaries from data from DIP, Regulon and BIGG to create ppi.tab files, reg.tab, met.tab.

02-integrated-interactions.py
Read files ppi.tab, reg.tab and met.tab. Build int.tab integrated network.
The file int.tab contains the intersection of the three networks.

03-deg-bet.py
Read files ppi.tab, reg.tab, met.tab and int.tab to generate centralities.tab file whose header contains:
gene, degInt, degppi, degreg, degmet, betInt, betppi, betreg, betmet, regin, regout, metin, metout. Also generates the file genes.tab containing all genes in the integrated network.

04-splenght.py
Generate spathsbut.tab file (Butland instances) and spathsall.tab (all possible instances), whose header is "geneA, geneB, sp_int, sp_ppi, sp_met". Each measurement refers to the length of the shortest paths for each network. It was the only shortest path measure that yielded  different results from random performance.

05-butscore.py
Create the file butscore.tab (Genea, geneB, s-score).

06-neighbor.py
Generate the files neighbor.tab and neigh_butland.tab whose header is:
geneA,geneB,'cnInt','fswInt','jcInt','cnppi','fswppi','jcppi','cnreg','fswreg','jcreg','cnmet','fswmet','jcmet'
When the pair of Butland was not found on the network, the measurement was set to zero.

07-folderstructure.py
Set up folders.

08-cent_pairs.py
cria dois arquivos: cent_but.tab e centall.tab. Eles contêm gene1,gene2,centralidades_max, centralidades_min para todas as redes. (degree e betweeness)
O arquivo cent_but.tab tem 1013 instâncias que são todos os pares do butland que estão na rede integrada.

09-trainsetcsv.py
cria os csv não balanceados, os 100 balanceados para cada tipo de experimento e preenche os csv para o experimento de clusterização.

10-trainset_balanced.py
gera 100 csv para cada tipo de atributo e para o experimento de clustering.

11-wekaclassifier.py
Várias threads para cálculo J48, geração de modelos, pngs, out.

12-stat_metrics.py
cria arquivo metrics.txt com a média das medidas de desempenho e a matriz input para experimento de clusterização.

13-clustering.py
Efetual weka clustering k-means com os dados gerados na etapa anterior.

14- metaVote.py
calcula meta vote para cada conjunto de atributos

15-summaryClustAssign.py
exclusivo para o experimento de clusterização. Cria um arquivo com o número de árvores em cada cluster para o cálculo da entropia no R.
