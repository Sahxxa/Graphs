#matriz quadrada
numVertices = int 
grafo = {}

#function to create a graph
def criaGrafo(numVertices: int):
    if numVertices <= 0: #validar se o numero de vertices é positivo
        raise ValueError("O número deve ser positivo > 0")
    else:
        grafo = {
        "numVertices": numVertices,
        "matriz": [[0 for _ in range(numVertices)] for _ in range(numVertices)] 
        } #cria a matriz com base nos vertices }
    return grafo


#funcao para adicionar uma aresta entre dois vertices v1 e v2 -> atualizar (v1, v2) e (v2, v1) -> ver se estão dentro do intervalo
#function to add an edge between two vertices v1 and v2 -> update (v1, v2) and (v2, v1) -> see if they are within the range
def adicionaAresta(grafo, v1, v2):
    if v1 < 0 or v2<0 or v1 >= grafo["numVertices"] or v2 >= grafo ["numVertices"] : #verificação se existe 
        raise IndexError("Fora do intervalo")
    #torna o valor 1
    grafo["matriz"][v1][v2]=1
    grafo["matriz"][v2][v1]=1

#function to remove an edge between two vertices
def removeAresta(grafo, v1, v2):
    if v1 < 0 or v2<0 or v1 >= grafo[numVertices] or v2 >= grafo [numVertices] : #verificação
        raise IndexError("Fora do intervalo")
    #torna o valor 0
    grafo["matriz"][v1][v2]=0 
    grafo["matriz"][v2][v1]=0

#print the graph
def exibeMatriz(grafo):
    for linha in grafo["matriz"]:
        print(linha) 

#verify if there is an edge between two vertices
def temAresta(grafo, v1, v2): #verificar se há uma aresta entre os vértices
    if v1 < 0 or v2 < 0 or v1 >= grafo["numVertices"] or v2 >= grafo["numVertices"]:
        raise IndexError("Vértice fora do intervalo")
    return grafo["matriz"][v1][v2] == 1

# Calcula o grau de um vértice
#calculates the degree of a vertex
def grauDoVertice(grafo, vertice):
    if vertice < 0 or vertice >= grafo["numVertices"]:
        raise IndexError("Vértice fora do intervalo")
    return sum(grafo["matriz"][vertice])
