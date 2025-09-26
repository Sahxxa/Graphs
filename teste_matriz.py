from grafo_matriz import criaGrafo as CG
from grafo_matriz import adicionaAresta as AA
from grafo_matriz import removeAresta as RA
from grafo_matriz import exibeMatriz as EM
from grafo_matriz import temAresta as TA
from grafo_matriz import grauDoVertice as GDV

grafo = CG(5)

AA(grafo, 0, 1)
AA(grafo, 0, 4)
AA(grafo, 1, 2)
AA(grafo, 1, 3)
AA(grafo, 1, 4)
AA(grafo, 2, 3)
AA(grafo, 3, 4)

EM(grafo)


v1=int(input("V1: ")) #inserir vértices p/ verificação
v2=int(input("V2: "))
print("Aresta entre os vértices {} e {}: ".format(v1, v2), TA(grafo, v1, v2)) #TRUE -> testa 1 e 2

v3=int(input("\nV3: ")) #inserir vértices p/ verificação
v4=int(input("V4: "))
print("Aresta entre os vértices {} e {}: ".format(v3, v4), TA(grafo, v3, v4)) #FALSE -> testa 4 e 2
print(" ")

print("Grau dos vértices:")
for i in range(grafo["numVertices"]):
    grau = GDV(grafo, i)
    print(f"Grau do vértice {i}: {grau}")


RA(grafo, 1, 4)
print("\nMatriz após remoção:")
EM(grafo)
