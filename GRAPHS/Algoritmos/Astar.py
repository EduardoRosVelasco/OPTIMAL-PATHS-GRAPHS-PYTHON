from Algoritmo import Algoritmo

class AStar (Algoritmo):

      
    def calculoCaminoyHeuristica (self,totalCost):
        '''Voy a asumir que la heuristica es 1 , porque no tengo ni las coordenadas de las ciudades
        ni cual seria el coste al destino en linea recta ni nada. La unica manera que hay de hacer eso
        desde mi punto de vista, es implementar el algoritmo coste y que me genere automáticamente costes 
        desde cada nodo al destino que yo he propuesto y me los añada al diccionario nada mas empezar para 
        poder usar esos costes desde cada nodo al destino dicho como heuristica'''
        #El heuristic cost deberia ser distinto para cada nodo... asumo que es 1 ...
        heuristica = 1
        prioridad = heuristica + totalCost
    
        return prioridad
    
    '''Con esta funcion lo que pretendo hacer es recibir de vuelta si el coste registrado para ir x ciudad es mayor 
    que el coste que me propone este nuevo camino, que me devuelva FALSE y la posicion de esa ciudad en la lista. 
    De esta manera, yo se que posicion borrar de la lista para añadir la ciudad con su menor coste'''

    def verifyCity(self,visitedNodesASTAR, whereaAreWe, newCostAstar):
        cityPosition = 0
        for cost, city in visitedNodesASTAR:
            if city == whereaAreWe:
                if cost < newCostAstar:
                    return True, cityPosition
                else:
                    return False, cityPosition
            cityPosition += 1  
        return False, -1  # Si no se encuentra la ciudad, devuelve False y -1
      

    def alg(self):
        visitedNodesASTAR = []
        cola1 = [(0,[self.origin],self.origin)] #Almaceno el coste de los caminos para luego sumarle la heuristica final
        cola2 = [(0,[self.origin],self.origin)] #Almaceno el coste de los caminos con eurísticas en cada iteración. Con esta hago el algoritmo
        
        
        while cola1:
            #Esto me ordena de menor a mayor la cola de heuristicas intermedias segun el primer numero que encuentra en la tupla[0]
            cola2.sort()
            
            #VER EJECUCIONES QUE HACE
            '''for cost, path, whereWeAre in cola2:
                print (cost,path,whereWeAre)'''
            cost, path, whereWeAre= cola2.pop(0)
            '''print ('NUEVA ITERACION')'''
            
            #Si el destino me coincide
            if whereWeAre == self.destination:
                #Saco el coste REAL del camino sin heuristicas intermedias
                for costEND, pathEND, _ in cola1:
                    if pathEND == path:
                        #Cuando encentro el camino, almaceno el coste en una variable y hago break para salir del bucle
                        costeReal = costEND
                        break
                #Devuelvo el coste real + la heuristica del nodo final  
                return self.calculoCaminoyHeuristica(costeReal) , pathEND          
            
            trueORfalse,cityPosition = self.verifyCity(visitedNodesASTAR,whereWeAre,self.calculoCaminoyHeuristica(cost))
            #Si está y además tiene un coste menor el self.priority que el coste registrado, devuelvo False 
            #También devuelvo el numero de posición que tengo que eliminar para meter el nuevo coste
            if trueORfalse == False: 
                #Si la ciudad esta en la lista la elimino y la sobreescribo porque el coste será menor 
                if (cityPosition != -1):
                    visitedNodesASTAR.pop(cityPosition)
                #Ordeno la lista de menor a mayor
                visitedNodesASTAR.sort()
                visitedNodesASTAR.append((self.calculoCaminoyHeuristica(cost),whereWeAre))
                
                
                for neighbor, distance in self.graph[whereWeAre].items(): #Busca los vecinos y la distancia respecetiva del punto en el que estamos
                    cola1.append((cost + distance, path + [neighbor], neighbor)) #Almaceno el coste real sin heurísticas intermedias
                    cola2.append((self.calculoCaminoyHeuristica(cost)+distance, path+[neighbor], neighbor))
            
            
    def printPath(self,path):
        i=1
        for destinos in path:
          print (i,'-',destinos)
          i+=1



