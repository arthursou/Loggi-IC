#from Matriz_Distancias import Grafo

#g = Grafo(4)
#g.mostrar_grafo()

class Grafo:

    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adiciona_aresta(self,u,v,peso):
        self.grafo[u-1].append([v , peso])

      #  self.grafo[v-1].append([u , peso])# se o grafo  não for direcionado

    def mostrar_grafo(self):
        for i in range(self.vertices):#mostra as posiçoes 0 1 2 3...
            print(f'{i+1}:', end='  ')
            for j in self.grafo[i]:# mostra o que tem dentro e não as posiçoes
                print(f'{j} - >', end='  ')
            print('')

g = Grafo(4)

g.adiciona_aresta(1,3,5)
g.adiciona_aresta(1,2,7)
g.adiciona_aresta(1,4,6)
g.adiciona_aresta(2,3,9)

g.mostrar_grafo()
