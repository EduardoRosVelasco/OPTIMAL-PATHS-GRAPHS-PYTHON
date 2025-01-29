from Algoritmo import Algoritmo

class DFS (Algoritmo): 
    
    def alg(self):
        pila = [(0,[self.origin],self.origin)] #Uso el termino pila para diferenciarlo de la cola pila es LIFO (Last in last out)
    
        while pila:
            cost, path, whereWeAre = pila.pop() #Saco el ultimo nodo de la pila para explorarlo
            if whereWeAre == self.destination:
                return cost, path
            if whereWeAre not in self.visitedNodes:
                self.visitedNodes.append(whereWeAre)
                for neighbor, distance in self.graph[whereWeAre].items():
                    if neighbor not in self.visitedNodes:
                        pila.append((cost + distance, path + [neighbor], neighbor))


    def printPath(self,path):
        i=1
        for destinos in path:
            print (i,'-',destinos)
            i+=1


        
        