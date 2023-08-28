# Universidade Federal de Pernambuco
<img src="/assets/logo ufpe.png">

## Centro de Informática - UFPE

### Docente: Sérgio Ricardo de Melo Queiroz 
### Discente: Leonardo Bezerra de Oliveira

### Projeto Grafo - Algoritmo de Prim 
#### Base de dados utilizada: https://www.inf.pucrs.br/~danielc/peng1a/outros/distancias.xls

O Algoritmo de Prim que é um algoritmo guloso (greedy algorithm) empregado para encontrar uma árvore geradora mínima (minimal spanning tree) num grafo conectado, valorado e não direcionado.
Com base nisso o objetivo do projeto é criar um algoritmo para geração de um grafo utilizando uma base de dados pública.

## Resumo
Diante da minha escolha do Algoritmo de Prim para realização desse projeto, tentei buscar uma base de dados que fizesse sentido para mim tendo em vista a utilização desse algoritmo. Pensando bastante nesse assunto, acabei tendo a ideia de utilizar a distância entre países, estados, cidades, por ser algo mais palpável, utilizaria as distâncias como os pesos e os nomes das cidades como os vértices para criar o grafo baseado nesse algoritmo.
A base de dados utilizada conta com a distância rodoviária entre algumas das principais cidades brasileiras, como é o caso por exemplo da distância entre Anápolis, a cidade do estado de Goiás e a cidade de Campinas em São Paulo.

Ao início do projeto foi criado um planejamento, para ser usado de base para o desenvolvimento desse projeto.

Planejamento
21/08 criar estrutura inicial, buscar base de dados, organizar basicamente o github.

22/08 organizar o código do algoritmo de prim

23/08 definir a base de dados que será utilizada

24/08 - 

25/08 iniciar ligação base de dados, concluir alg prim

26/07 começar a organizar os dados do relatório

27/07 entrega

Bibliotecas utilizadas. 
Pandas, <https://pandas.pydata.org/>;
NetworkX <https://networkx.org/>
Matplotlib <https://matplotlib.org/>

Apps utilizados.
Gephi para gerar interface mais visualizável.
<https://gephi.org/>


## Implementação

A implementação se inicia com a chamada das bibliotecas utilizadas, pandas, networkx e matplotlib.
Implementação:
import, início, utilização do pandas para ligar o código com a base de dados.
<img src="/assets/img1.png">

Preenchimento do grafo, alterações

<img src="/assets/img2.png">

print número de vértices e arestar grafo geral
<img src="/assets/img3.png">

algoritmo de prim 
<img src="/assets/img4.png">

gerar árvore mínima:
<img src="/assets/img5.png">

Criar grafo no NetworkX, printar árvore mínima e distância, print da quantidade de vértices e arestas da árvore mínima:
<img src="/assets/img6.png">

Criação do grafo final do NetworkX, salvando o grafo como arquivo:
<img src="/assets/img7.png">


## Conclusão

Output grafo geral;
<img src="/assets/output1.png">

<img src= "/assets/output2.png">

Output grafo árvore mínima:

<img src="/assets/output3.png">

<img src="/assets/output4.png">


Imagem dos grafos

Grafo gerado no código: 
<img src="/assets/grafo1.png">

Grafo no software Gephi: 
<img src="/assets/grafo.png">


