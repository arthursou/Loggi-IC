class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices) ]


    def adiciona_aresta(self, u ,v, peso):
        #grafo direcionados simples
        self.grafo[u-1][v-1] = peso #trocar = por += se for grafo multiplas arestas

        self.grafo[v-1][u-1] = peso # caso não seja direcionado

    def mostrar_grafo(self):
        print(' A matriz de adjacencias:')
        for i in range( self.vertices):
            print( self.grafo[i])

#g = Grafo(4)

#g.adiciona_aresta(1,2,1)
#g.adiciona_aresta(2,3,2)
#g.adiciona_aresta(3,4,3)
#g.adiciona_aresta(4,1,4)

#g.mostrar_grafo()

v = int(input('Digite a quantidade de vertices'))

g = Grafo(v)

a = int(input('Digite a quantidade de arestas'))
for i  in range(a):
    u =  int(input('De qual vértice parte essa aresta?'))
    v =  int(input('Para qual vértice vai essa aresta?'))
    p =  int(input('Qual peso dessa aresta?'))

    g.adiciona_aresta(u,v,p)

g.mostrar_grafo()


