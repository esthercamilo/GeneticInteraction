GeneticInteraction
==================
1-networks-ppi-reg-met.py
Obtém dicionários a partir dos dados do DIP, Regulon e BIGG para criar os arquivos ppi.tab, reg.tab, met.tab.

2-integrated-interactions.py
Lê os arquivos de interação ppi.tab, reg.tab e met.tab. Constrói a rede integrada int.tab.
O arquivo int.tab contém a intersecção não direcionada sem repetições de todas as interações das outras redes.

3-deg-bet.py
Lê os arquivos de interação ppi.tab, reg.tab, met.tab e int.tab e gera o arquivo centralities.tab, cujo header contém: 
gene,degInt,degppi,degreg,degmet,betInt,betppi,betreg,betmet,regin,regout,metin,metout. Também gera o arquivo genes.tab contendo todos os genes na rede integrada.

4-allshortest.py
Gera um arquivo contendo todos os caminhos geodésicos para cada rede: spathsInt.tab, spathsppi.tab, spathsreg.tab, spathsmet.tab.

5-butscore.py
Cria o arquivo butscore.tab (geneA,geneB,s-score)

6-spaths.py
Gera arquivo spaths.tab que contém "geneA,geneB,spathsInt,spathsppi,spathsreg,spathsmet"
onde spaths é o número de caminhos geodésicos que contém simultaneamente os genes A e B.

7-neighbor.py
Gera o arquivo neighbor.tab cujo header é: 
geneA,geneB,'cnInt','fswInt','jcInt','cnppi','fswppi','jcppi','cnreg','fswreg','jcreg','cnmet','fswmet','jcmet'

8-completset.py
Gera o arquivo 'files/completeTrainingSet.csv' que contém todos os atributos (centralidades e neighborhood) e score butland numérco (996).

9-trainingset.py
gera o conjunto desbalanceado com todos os atributos e scores de butland numerico. OUTPUT: 'files/trainingSetButland.csv'

10-traingroups.py
Configura conjunto de pastas para experimentos com a seguinte estrutura: 
weka/{deg,bet,neigh,complete}. Dentro de cada uma há {arff,csv{exp,random},dot,model,out,png,result,result_random}. A partir do 'files/trainingSetButland.csv' ger preenche a pasta csv/{exp,random} com 100 grupos de treinamento

12-stat_metrics.py
calcula o p-value para o experimento e aleatório. Gera a matriz input para a clusterização. 
