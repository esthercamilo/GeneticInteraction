GeneticInteraction
==================
01-networks-ppi-reg-met.py
Obtém dicionários a partir dos dados do DIP, Regulon e BIGG para criar os arquivos ppi.tab, reg.tab, met.tab.

02-integrated-interactions.py
Lê os arquivos de interação ppi.tab, reg.tab e met.tab. Constrói a rede integrada int.tab.
O arquivo int.tab contém a intersecção não direcionada sem repetições de todas as interações das outras redes.

03-deg-bet.py
Lê os arquivos de interação ppi.tab, reg.tab, met.tab e int.tab e gera o arquivo centralities.tab, cujo header contém: 
gene,degInt,degppi,degreg,degmet,betInt,betppi,betreg,betmet,regin,regout,metin,metout. Também gera o arquivo genes.tab contendo todos os genes na rede integrada.

04-splenght.py
Gera o arquivo spathsbut.tab (instâncias de Butland) e spathsall.tab (todas as possíveis instâncias), cujo header é "geneA, geneB, sp_int, sp_ppi, sp_met". Cada medida é referente ao comprimento dos caminhos mais curtos para cada rede. Foi a única medida de shortest path que rendeu desempenho diferente do aleatório. Há baixa intersecção entre os genes da rede regulatória e os genes do experimento do Butland, por isso, a rede reg não foi utilizada.

05-butscore.py
Cria o arquivo butscore.tab (geneA,geneB,s-score). Tem 1288 instancias.

06-neighbor.py
Gera os arquivos neighbor.tab e neigh_butland.tab, cujo header é: 
geneA,geneB,'cnInt','fswInt','jcInt','cnppi','fswppi','jcppi','cnreg','fswreg','jcreg','cnmet','fswmet','jcmet'
Tem todas as 1288 instancias do butland, pois quando o par de butland não era encontrado na rede, a medida de neighborhood foi definida como zero.

07-folderstructure.py
cria pastas.

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
