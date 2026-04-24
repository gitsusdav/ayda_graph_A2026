# Documentación de Algoritmos Implementados - graph_algorithms.py

## Resumen
Documentación de los bloques de código **RESUELTOS** en `python/graph_algorithms.py`. Solo se documentan las funciones completamente implementadas.

---

## 1. GraphTraversals.traverse_bfs()
**Ubicación:** líneas 43-73

### Descripción
Implementa un recorrido en amplitud (BFS) comenzando desde un nodo inicial. Aplica una operación (función visitor) a cada nodo visitado.

### Algoritmo
1. Inicializa un conjunto `visited` para rastrear nodos ya visitados
2. Crea una cola con el nodo inicial
3. Mientras la cola no esté vacía:
   - Extrae el nodo al frente de la cola
   - Si ya fue visitado, continúa al siguiente
   - Lo marca como visitado
   - Aplica la operación `op()` al nodo
   - Añade todos los vecinos no visitados a la cola

### Complejidad
- **Temporal:** O(V + E) donde V = vértices, E = aristas
- **Espacial:** O(V) para la cola y el conjunto de visitados

### Uso
```python
def print_node(node):
    print(node.value)

GraphTraversals.traverse_bfs(graph, start_node, print_node)
```

---

## 2. GraphTraversals.find_shortest_path_bfs()
**Ubicación:** líneas 76-108

### Descripción
Encuentra el camino más corto (en términos de número de aristas) entre dos nodos en un grafo NO PONDERADO usando BFS.

### Algoritmo
1. Inicializa un diccionario `predecessors` para reconstruir el camino
2. Ejecuta BFS desde el nodo inicial
3. Durante el recorrido, registra el predecesor de cada nodo descubierto
4. Cuando se encuentra el nodo destino, reconstruye el camino hacia atrás
5. Retorna el camino en orden correcto

### Complejidad
- **Temporal:** O(V + E)
- **Espacial:** O(V)

### Caso especial
Retorna lista vacía `[]` si no existe camino entre los nodos.

---

## 3. GraphTraversals.traverse_dfs()
**Ubicación:** líneas 111-137

### Descripción
Implementa un recorrido en profundidad (DFS) usando una pila explícita. Aplica una operación a cada nodo visitado.

### Algoritmo
1. Inicializa un conjunto `visited` y una pila con el nodo inicial
2. Mientras la pila no esté vacía:
   - Extrae un nodo de la pila
   - Si ya fue visitado, continúa
   - Lo marca como visitado
   - Aplica la operación `op()` al nodo
   - Añade todos los vecinos no visitados a la pila

### Complejidad
- **Temporal:** O(V + E)
- **Espacial:** O(V)

### Nota
Se implementó con enfoque iterativo (pila explícita), no recursivo.

---

## 4. GraphTraversals.build_spanning_tree_dfs()
**Ubicación:** líneas 140-174

### Descripción
Construye un árbol de cobertura (spanning tree) del grafo utilizando DFS. El árbol contiene todos los nodos pero solo las aristas que forma el recorrido DFS.

### Algoritmo
1. Crea un nuevo grafo vacío para el árbol
2. Mantiene un mapeo de nodos originales a nodos en el árbol
3. Ejecuta DFS con una pila
4. Cuando se descubre un vecino no visitado:
   - Lo añade al árbol si no existe
   - Añade la arista correspondiente al árbol
5. Retorna el árbol de cobertura

### Complejidad
- **Temporal:** O(V + E)
- **Espacial:** O(V)

### Propiedades
- Contiene exactamente V-1 aristas (es un árbol)
- Conecta todos los V nodos
- Preserva los pesos de las aristas originales

---

## 5. GraphTraversals.build_spanning_tree_bfs()
**Ubicación:** líneas 178-212

### Descripción
Construye un árbol de cobertura utilizando BFS. Similar a `build_spanning_tree_dfs()` pero explora por niveles.

### Algoritmo
1. Crea un nuevo grafo vacío y un mapeo de nodos
2. Inicializa una cola con el nodo inicial
3. Ejecuta BFS:
   - Para cada vecino no visitado:
     - Lo marca como visitado
     - Lo añade a la cola
     - Lo añade al árbol si no existe
     - Añade la arista al árbol
4. Retorna el árbol de cobertura

### Complejidad
- **Temporal:** O(V + E)
- **Espacial:** O(V)

### Diferencia con DFS
El árbol resultante tiene la misma estructura base (V nodos, V-1 aristas) pero con diferentes niveles de profundidad según el orden de exploración.

---

## 6. GraphTopological.get_sort()
**Ubicación:** líneas 254-287

### Descripción
Obtiene una ordenación topológica de un grafo dirigido acíclico (DAG) usando el **Algoritmo de Kahn**.

### Algoritmo
1. Calcula el in-degree (grado de entrada) de cada nodo
2. Inicializa una cola con todos los nodos de in-degree 0
3. Mientras la cola no esté vacía:
   - Extrae un nodo y lo añade al resultado
   - Para cada arista saliente: decrementa in-degree del destino
   - Si in-degree llega a 0, añade el nodo a la cola
4. Si no se visitaron todos los nodos, el grafo tiene ciclos

### Complejidad
- **Temporal:** O(V + E)
- **Espacial:** O(V)

### Casos de error
- Lanza `RuntimeError` si el grafo contiene un ciclo

### Orden correcto
Retorna una lista de nodos en orden topológico válido para dependencias.

---

## 7. GraphTopological.get_ranks()
**Ubicación:** líneas 290-330

### Descripción
Calcula el "rango" o nivel de cada nodo en un DAG. El rango representa la distancia máxima desde los nodos raíz (in-degree 0) hasta ese nodo.

### Algoritmo
1. Calcula in-degrees y inicializa rangos de nodos raíz en 0
2. Usa cola como en Kahn's para procesar nodos
3. Para cada vecino no visitado:
   - Actualiza su rango como máximo de (rango actual, rango del nodo actual + 1)
   - Cuando in-degree llega a 0, añade a cola
4. Lanza excepción si hay ciclos

### Complejidad
- **Temporal:** O(V + E)
- **Espacial:** O(V)

### Propiedades
- Nodos con in-degree 0 tienen rango 0
- Si múltiples caminos llegan a un nodo, su rango es el del camino más largo
- Útil para detectar el nivel de un nodo en una estructura de dependencias

### Ejemplo práctico
En un grafo de tareas (A → B → D, A → C → D):
- A: rango 0
- B, C: rango 1
- D: rango 2

---

## Resumen de Complejidades

| Función | Temporal | Espacial | Uso |
|---------|----------|----------|-----|
| traverse_bfs | O(V+E) | O(V) | Recorrer grafo por niveles |
| find_shortest_path_bfs | O(V+E) | O(V) | Camino más corto sin pesos |
| traverse_dfs | O(V+E) | O(V) | Recorrer grafo en profundidad |
| build_spanning_tree_dfs | O(V+E) | O(V) | Árbol de cobertura DFS |
| build_spanning_tree_bfs | O(V+E) | O(V) | Árbol de cobertura BFS |
| get_sort | O(V+E) | O(V) | Orden topológico |
| get_ranks | O(V+E) | O(V) | Niveles en DAG |

---

**Fecha de documentación:** 2026-04-07  
**Archivo referenciado:** `python/graph_algorithms.py`
