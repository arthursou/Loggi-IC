class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices) ]


    def adiciona_aresta(self, u ,v):
        #grafo direcionados simples
        self.grafo[u-1][v-1] = 1 #trocar = por += se for grafo multiplas arestas

        #self.grafo[v-1][u-1] = 1 # caso não seja direcionado

    def mostrar_grafo(self):
        print(' A matriz de adjacencias:')
        for i in range( self.vertices):
            print('Olá', self.grafo[i])

g = Grafo(4)

g.adiciona_aresta(1,2)
g.adiciona_aresta(2,3)
g.adiciona_aresta(3,4)
g.adiciona_aresta(4,1)

g.mostrar_grafo()