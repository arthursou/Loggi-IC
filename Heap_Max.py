import math


class Heap_Max:

      def __init__(self):
          self.nos = 0
          self.heap = []

      def adiciona_nos(self, u):
          self.heap.append(u)
          self.nos += 1
          filho = self.nos
          while True :# enquanto verdade
              if filho == 1:
                  break
              pai = filho//2 #com duas barras é parte inteira e posição do pai
              if self.heap[pai-1] >= self.heap[filho-1]: #Heap minimo <=
                  break
              else:
                  self.heap[pai-1], self.heap[filho -1] = self.heap[filho -1], self.heap[pai-1] # trocar de posição otimizado!!
                  filho = pai

      def mostrar_heap(self):
          print(self.heap) #forma simples
          print('A estrutura heap é a seguinte:')
          nivel = int(math.log(self.nos,2))# armazenar apenas inteiro
          a = 0
          for i in range(nivel):
              for j in range(2 ** i): # potencia em python
                  print(f'{self.heap[a]}', end = '  ')
                  a += 1
              print('')

          for i in range(self.nos -a ):
              print(f'{self.heap[a]}', end='  ')
              a += 1


      def remove_no(self):
          x = self.heap[0]
          self.heap[0] = self.heap[self.nos -1]
          self.heap.pop()#elimina o ultimo elemento
          self.nos -= 1
          p = 1#posição
          while True:
              f = 2 * p#posição no heap e não nós e filho a esquerda
              if f >self.nos:# ele não existe se for maior
                  break
              if f+1 <= self.nos:#filho direita
                  if self.heap[f] > self.heap[f-1]:#<se for heap min
                      f +=1

              if self.heap[p-1] >= self.heap[f-1]:# se o pai for maior que o filho
                  break
              else:
                  self.heap[f-1],self.heap[p-1] = self.heap[p-1], self.heap[f-1]
                  p = f
          return x

      def tamanho(self):
          return self.nos

      def maior_elemento(self):
          return self.heap[0]

      def filho_esquerda(self, i):
          if self.nos >= 2*i:
              return self.heap[2*i -1]
          return 'Esse nó não tem filho!'

      def filho_direita(self, i):
          if self.nos >= 2*i+1:
              return self.heap[2*i]
          return 'Esse nó não tem filho á direita!'

      def pai(self,i):
          return self.heap[i//2]



h = Heap_Max()

h.adiciona_nos(17)
h.adiciona_nos(36)
h.adiciona_nos(25)
h.adiciona_nos(7)
h.adiciona_nos(3)
h.adiciona_nos(100)
h.adiciona_nos(1)
h.adiciona_nos(2)
h.adiciona_nos(19)

elementomax = h.remove_no()

print(f'Elemento max:{elementomax}')

print(f'Tamanho: {h.tamanho()}')

print(f'Filho à esquerda de 17: {h.filho_esquerda(4)}')
print(f'Filho à direita de 17: {h.filho_direita(4)}')

h.mostrar_heap()

