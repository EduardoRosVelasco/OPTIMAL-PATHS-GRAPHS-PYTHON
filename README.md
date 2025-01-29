# OPTIMAL-PATHS-GRAPHS-PYTHON
# Graph Search Algorithms

Este proyecto implementa algoritmos de búsqueda en grafos: **BFS (Breadth-First Search), DFS (Depth-First Search)** y **A* (A-Star)**, usando un conjunto de ciudades en Rumania como ejemplo de prueba.

## Estructura del Proyecto

```
GRAPHS/
│── main.py               # Archivo principal del programa
│── algoritmo.py          # Definición de la clase base Algoritmo
│── __init__.py           # Archivo para convertir la carpeta en un módulo
│
├── Algoritmos/           # Carpeta que contiene los algoritmos específicos
│   ├── BFS.py            # Implementación del algoritmo BFS
│   ├── DFS.py            # Implementación del algoritmo DFS
│   ├── Astar.py          # Implementación del algoritmo A*
│   ├── __init__.py       # Archivo para convertir la carpeta en un módulo
```

## Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd GRAPHS
```

### 2. Ejecutar el Programa
Asegúrate de tener Python 3 instalado y ejecuta:
```bash
python main.py
```

## Uso del Programa
1. Al iniciar el programa, verás un **menú** con las siguientes opciones:
   - BFS (Búsqueda en anchura)
   - DFS (Búsqueda en profundidad)
   - A* (Búsqueda informada con heurística)
   - Salir

2. Debes elegir un algoritmo y luego ingresar la ciudad de **origen** y **destino**.
3. El programa mostrará el **camino óptimo** y el **costo** del trayecto.

## Ejemplo de Entrada y Salida
### Entrada:
```
Seleccione la operación que desea realizar: 1
Introduzca un punto de partida: Arad
Introduzca el destino al que desea llegar: Bucharest
```

### Salida esperada:
```
El origen es: Arad
El destino es: Bucharest
El coste para llegar al destino según BFS es: 450
Ruta: Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest
```

## Contacto
Si tienes dudas o sugerencias, puedes abrir un **issue** en el repositorio o contactarme.
