from Algoritmos.BFS import BFS
from Algoritmos.DFS import DFS
from Algoritmos.Astar import AStar


'''El algortimo, me almacena los datos como si el nodo de la izquierda fuese el vecino que 
está más a la derecha. Es decir, dependiendo de como estructure mi diccionario, voy a obtener un resultado distinto.'''

GrafoCiudades = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Timisoara': {'Lugoj': 111, 'Arad': 118},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova' : {'Drobeta': 120 , 'Rimnicu Vilcea': 146 , 'Pitesti': 138},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Oradea': {'Sibiu': 151, 'Zerind': 71},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Pitesti': {'Craiova' : 138 , 'Rimnicu Vilcea': 97, 'Bucharest': 101},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {"Bucharest": 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}      
        }
#Mensaje de bienvenida al programa
print('----------------------------------')
print('BIENVENIDO AL PROGRAMA DE BUSQUEDA')
print('----------------------------------')

#Bucle principal del programa
while True:
    print ('')
    print('Menu:')
    print('-------------------------------')
    print('1.Busqueda con Algoritmo de BFS')
    print('2.Busqueda con Algoritmo de DFS')
    print('3.Busqueda con Algoritmo de A*')
    print('-------------------------------')
    print('4.Salir ')
    print('-------------------------------')
    print('')


#Bucle para que el usuario me pase una opción correcta y no se me pare el programa si pone algo distinto
    opcionValida = False
    while opcionValida == False :
        opcion = int(input('Seleccione la operación que desea realizar: '))
        if opcion < 1 or opcion > 4:
            print ('Opción inválida, escriba una opción válida por favor')
            opcionValida = False
        else:
            opcionValida = True
 
    
    if (opcion >= 1 and opcion <= 3):
        print ('Esta es una lista de las ciudades de Rumania: ')
        ImprimirMapa = BFS.imprimirCiudades(GrafoCiudades) #Uso un algoritmo que hereda el imprimir ciudades para pasarselas al usuario y que pueda elegir
        print('----------------------------------------')
        print('POR FAVOR INTRODUZCA LOS SIGUIENTES DATOS')
        originEntrada = input ('Introduzca un punto de partida: ')
        destinationEntrada = input ('Introduzca el destino al que desea llegar: ')
        print('----------------------------------------')
    
    
    if opcion == 1:
        print ('')
        #Creo el objeto Algoritmo TIPO BFS y le meto los valores de entrada
        objetoBFS = BFS(originEntrada,destinationEntrada,GrafoCiudades)
        
        #Guardo los valores del return en los parámetros siguientes:
        costBFS, pathBFS = BFS.alg(objetoBFS) 
        
        print ('El origen es: ', originEntrada)
        print ('El destino es: ', destinationEntrada)
        print ('El coste para llegar al destino según BFS es: ', costBFS)
        
        #IMMPRIMIR CAMINO
        objetoBFS.printPath(pathBFS)
        print ('')
        
    elif opcion == 2:
        print ('')
        #Creo el objeto Algoritmo TIPO DFS y le meto los valores de entrada
        objetoDFS = DFS(originEntrada,destinationEntrada,GrafoCiudades)
        
        #Guardo los valores del return en los parámetros siguientes:
        costDFS, pathDFS = DFS.alg(objetoDFS) 
        
        #Imprimo los parametros de salida
        print ('El origen es: ', originEntrada)
        print ('El destino es: ', destinationEntrada)
        print ('El coste para llegar al destino según BFS es: ', costDFS)
        
        #IMMPRIMIR CAMINO
        objetoDFS.printPath(pathDFS)
        print ('')
        
    elif opcion == 3:
        print ('')
        #Creo el objeto Algoritmo TIPO Astar y le meto los valores de entrada
        objetoAStar = AStar(originEntrada,destinationEntrada,GrafoCiudades)
        
        #Guardo los valores del return en los parámetros siguientes:
        costAStar, pathAStar = AStar.alg(objetoAStar) 
        
        #Imprimo los parametros de salida
        print ('El origen es: ', originEntrada)
        print ('El destino es: ', destinationEntrada)
        print ('El coste para llegar al destino según A* es: ', costAStar)
        
        #IMMPRIMIR CAMINO
        objetoAStar.printPath(pathAStar)
        print ('')
        
    elif opcion == 4:
        print('Saliendo del programa...')
        break
    
    else:
        print('Opción no válida. Introduzca un número del 1 al 4.')


