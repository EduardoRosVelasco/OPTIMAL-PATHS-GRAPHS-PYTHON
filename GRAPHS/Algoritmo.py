'''Creo la clase algoritmo con los atributos que voy a usar en los distintos tipos de algoritmos,
hago el constructor del algoritmo que va necesitar 3 datos de entrada, origen, destino y grafo 
y por ultimo creo el visitedNodes que va a ser una lista donde voy a almacenar los nodos que he 
ido visitando mientras implemento los distintos algoritmos'''

class Algoritmo:  
    def __init__(self,origin,destination,graph):
        self.origin = origin
        self.destination = destination
        self.graph = graph
        self.visitedNodes = []
        
    def imprimirCiudades(graph):
        i = 1
        Ciudades = list(graph.keys()) #Le digo que me cree una lista de las keys de mi grafo 
        for ciudad in Ciudades : 
            print (i, " - " ,ciudad) #Le pido que me imprima las ciudades para dcirle al usuario cuales son
            i+=1