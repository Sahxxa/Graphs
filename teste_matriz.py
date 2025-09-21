from grafo_matriz import criaGrafo as CG
from grafo_matriz import adicionaAresta as AA
from grafo_matriz import removeAresta as RA
from grafo_matriz import exibeMatriz as EM
from grafo_matriz import temAresta as TA
from grafo_matriz import grauDoVertice as GDV


grafo = CG(5) #criar

AA(grafo, 0, 1) #adicionar as arestas
AA(grafo, 1, 2)
AA(grafo, 1, 3)
AA(grafo, 3, 4)
AA(grafo, 4, 2)

print("Matriz adj 1") #mostrar o grafo
EM(grafo)

v1=int(input("V1: ")) #inserir vértices p/ verificação
v2=int(input("V2: "))
print("Aresta entre os vértices {} e {}\n".format(v1, v2), TA(grafo, v1, v2)) #deve ter -> testa 1 e 2

v3=int(input("\nV3: ")) #inserir vértices p/ verificação
v4=int(input("V4: "))
print("Aresta entre os vértices {} e {}\n".format(v3, v4), TA(grafo, v3, v4)) #não ter -> testa 4 e 1
#vai ficar por conta do usuário e é sobre isso

print("Grau de v0", GDV(grafo, 0))
print("Grau de v1",GDV(grafo, 1))
print("Grau de v2",GDV(grafo, 2))
print("Grau de v3",GDV(grafo, 3))
print("Grau de v4",GDV(grafo, 4))





#Crie um grafo com 5 vértices.
#Adicione um conjunto de arestas para formar um grafo de sua escolha.
#Exiba a matriz resultante.
#Teste a função tem_aresta para um par de vértices que possui uma aresta e para um par que não possui.
#Calcule e imprima o grau de todos os vértices do grafo.
#Remova uma das arestas e exiba a matriz novamente para confirmar a remoção.