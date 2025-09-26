def criaGrafo(numVertices):

    if numVertices <= 0:
        print("O número de vértices deve ser > 0")
        return None

    grafo = {
        "numVertices": numVertices,
        "matriz": [[0] * numVertices for _ in range(numVertices)]
    }
    return grafo

def adicionaAresta(grafo, v1, v2):

    numVertices = grafo["numVertices"]
    if 0 <= v1 < numVertices and 0 <= v2 < numVertices:
        grafo["matriz"][v1][v2] = 1
        grafo["matriz"][v2][v1] = 1 
    else:
        print("Vértice(s) inválido(s).")

def removeAresta(grafo, v1, v2):

    numVertices = grafo["numVertices"]
    if 0 <= v1 < numVertices and 0 <= v2 < numVertices:
        grafo["matriz"][v1][v2] = 0
        grafo["matriz"][v2][v1] = 0  
    else:
        print("Vértice(s) inválido(s).")

def exibeMatriz(grafo):

    print("\n*** Matriz de Adjacência ***")
    for linha in grafo["matriz"]:
        print(" ".join(map(str, linha)))
    print("--------------------------\n")

def temAresta(grafo, v1, v2):

    numVertices = grafo["numVertices"]
    if 0 <= v1 < numVertices and 0 <= v2 < numVertices:
        return grafo["matriz"][v1][v2] == 1
    return False

def grauDoVertice(grafo, vertice):

    numVertices = grafo["numVertices"]
    if 0 <= vertice < numVertices:
        return sum(grafo["matriz"][vertice])
    else:
        print("Vértice {} é inválido.".format(vertice))
        return -1
