class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices) ]


    def adiciona_aresta(self, u ,v):
        #grafo direcionados simples
        self.grafo[u-1][v-1] += 1 #trocar = por += se for grafo multiplas arestas
        if u != v:
           self.grafo[v-1][u-1] += 1 # caso não seja direcionado

    def mostrar_grafo(self):
        print('A matriz de adjacencias:')
        for i in range( self.vertices):
            print(self.grafo[i])

    def tem_aresta(self,u,v):
        if self.grafo[u-1][v-1] ==0:
            print(f'Não tem aresta entre os vertices {u} e {v}')
        else:
            print(f'Tem aresta {self.grafo[u-1][v-1]} quantidade de aresta entre {u} e {v}')

    def eh_euleriano(self):
        contador = 0
        for i in range(self.vertices):
            grau = 0
            for j in range(self.vertices):
                if i == j:
                    grau += 2 * self.grafo[i][j]
                else:
                    grau += self.grafo[i][j]
            if grau % 2 != 0:
                contador += 1

        if contador ==0:
            print('Grafo é euleriano')

        elif contador ==2:
            print('Grafo é semieuleriano')
        else:
            print('O grafo não é nada')


g = Grafo(4)

g.adiciona_aresta(1,2)

g.adiciona_aresta(1,2)
g.adiciona_aresta(2,3)
g.adiciona_aresta(3,4)
g.adiciona_aresta(4,1)

g.tem_aresta(1,2)
g.eh_euleriano()

g.mostrar_grafo()