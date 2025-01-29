from Algoritmo import Algoritmo

class BFS (Algoritmo):
    
    def alg(self):
        cola = [(0,[self.origin],self.origin)] #La cola me va a almacenar el nodo actual, el camino que se ha seguido para llegar y el coste para llegar al nodo actual
        
        while cola:
            cost, path, whereWeAre = cola.pop(0) #Saco el primero nodo de la cola para explorarlo  
            if whereWeAre == self.destination:
                return cost , path
            if whereWeAre not in self.visitedNodes: #Si no está en visitados: 
                self.visitedNodes.append(whereWeAre) #lo añade a visitados y mete a la cola, todos los vecinos
                for neighbor, distance in self.graph[whereWeAre].items(): #Busca los vecinos y la distancia respecetiva del punto en el que estamos
                    cola.append((cost + distance, path + [neighbor], neighbor))#Añade a la cola el vecino, con el recorrido y sumandole el coste
                
        #Si el whereWeAre está en visitados, no hace cola de ese destino visitado y solo hace el pop, para no tener Arad dos veces
              
        return None, None  # Si no se encontró el destino

    
    def printPath(self,path):
        i=1
        for destinos in path:
          print (i,'-',destinos)
          i+=1

