# Guia de Ejercicios Resueltos — Grafos (AYDA)

Ejercicios resueltos paso a paso usando las funciones de `graph_algorithms.py`.
Todos usan `DirectedGraph` o `UndirectedGraph` de la libreria y las clases
`GraphTraversals` y `GraphTopological`.

---

## Ejercicio 1: Camino mas corto en un grafo no ponderado (BFS)

**Problema:**
Dado un grafo no ponderado y dos nodos `A` y `D`, encuentra el camino mas corto
entre ellos (el que usa menos aristas).

**Codigo:**

```python
from graph import UndirectedGraph
from graph_algorithms import GraphTraversals

graph = UndirectedGraph()
a = graph.add_node_by_value("A")
b = graph.add_node_by_value("B")
c = graph.add_node_by_value("C")
d = graph.add_node_by_value("D")

graph.add_arc(a, b, 0.0)
graph.add_arc(a, c, 0.0)
graph.add_arc(b, d, 0.0)
graph.add_arc(c, d, 0.0)

path = GraphTraversals.find_shortest_path_bfs(graph, a, d)
print("Camino mas corto:", [node.value for node in path])
```

**Salida esperada:**

```
Camino mas corto: ['A', 'B', 'D']
```

**Explicacion:**
`find_shortest_path_bfs` ejecuta un BFS desde `a`. Internamente mantiene un
diccionario `predecessors` que registra desde que nodo se descubrio cada vecino.
Cuando llega a `d`, reconstruye el camino hacia atras usando ese diccionario y
lo invierte. BFS garantiza que el primer camino encontrado tiene el **minimo
numero de aristas**, porque explora todos los nodos a distancia 1 antes de
pasar a distancia 2, y asi sucesivamente. Si no existe camino, retorna `[]`.

---

## Ejercicio 2: Detectar si un nodo es alcanzable (DFS)

**Problema:**
Dado un grafo dirigido y un nodo `start`, recorre todos los nodos alcanzables
y recoge sus valores.

**Codigo:**

```python
from graph import DirectedGraph
from graph_algorithms import GraphTraversals

graph = DirectedGraph()
a = graph.add_node_by_value("A")
b = graph.add_node_by_value("B")
c = graph.add_node_by_value("C")
d = graph.add_node_by_value("D")

graph.add_arc(a, b, 0.0)
graph.add_arc(b, c, 0.0)
graph.add_arc(c, d, 0.0)

visited_nodes = []
GraphTraversals.traverse_dfs(graph, a, lambda node: visited_nodes.append(node.value))
print("Nodos alcanzables desde A:", visited_nodes)
```

**Salida esperada:**

```
Nodos alcanzables desde A: ['A', 'B', 'C', 'D']
```

**Explicacion:**
`traverse_dfs` usa una pila explicita. Saca un nodo de la pila, lo marca como
visitado y ejecuta `op(nodo)` (en este caso el lambda que agrega el valor a la
lista). Luego empuja los vecinos no visitados a la pila. Como la pila es LIFO,
DFS avanza lo mas profundo posible por una rama antes de retroceder. Esto lo
diferencia de BFS, que explora por niveles. Ambos tienen complejidad O(V + E),
pero el **orden de visita** es distinto. DFS es util para detectar alcanzabilidad,
encontrar caminos en laberintos y construir arboles de expansion.

---

## Ejercicio 3: Arbol de expansion con DFS

**Problema:**
Construye un arbol que conecte todos los nodos del grafo usando DFS.
El arbol resultante tiene exactamente V-1 aristas y no contiene ciclos.

**Codigo:**

```python
from graph import UndirectedGraph
from graph_algorithms import GraphTraversals

graph = UndirectedGraph()
a = graph.add_node_by_value("A")
b = graph.add_node_by_value("B")
c = graph.add_node_by_value("C")
d = graph.add_node_by_value("D")

graph.add_arc(a, b, 0.0)
graph.add_arc(b, c, 0.0)
graph.add_arc(c, d, 0.0)
graph.add_arc(a, d, 0.0)  # arista extra que forma ciclo

tree = GraphTraversals.build_spanning_tree_dfs(graph, a)

print("Arcos del arbol de expansion:")
for node in tree:
    for arc in tree.get_outgoing_arcs(node):
        print(f"  {node.value} -> {arc.target.value}")
```

**Salida esperada (puede variar segun el orden DFS):**

```
Arcos del arbol de expansion:
  A -> B
  B -> C
  C -> D
```

**Explicacion:**
`build_spanning_tree_dfs` crea un grafo nuevo vacio y ejecuta DFS sobre el
grafo original. Cada vez que descubre un vecino no visitado, agrega ese nodo y
la arista al arbol nuevo. Usa un `node_mapping` (diccionario) para traducir
nodos del grafo original a nodos del arbol. El resultado es un arbol: tiene
todos los V nodos pero solo V-1 aristas, sin ciclos. Observa que la arista
A-D del grafo original no aparece en el arbol porque D ya fue descubierto
por otro camino (C -> D).

---

## Ejercicio 4: Orden topologico de tareas (Kahn)

**Problema:**
Dado un DAG (grafo dirigido aciclico) que representa dependencias entre tareas,
devuelve un orden valido de ejecucion donde cada tarea aparece despues de todas
sus dependencias.

**Codigo:**

```python
from graph import DirectedGraph
from graph_algorithms import GraphTopological

graph = DirectedGraph()
t1 = graph.add_node_by_value("Tarea1")
t2 = graph.add_node_by_value("Tarea2")
t3 = graph.add_node_by_value("Tarea3")
t4 = graph.add_node_by_value("Tarea4")

graph.add_arc(t1, t2, 0.0)
graph.add_arc(t1, t3, 0.0)
graph.add_arc(t2, t4, 0.0)
graph.add_arc(t3, t4, 0.0)

order = GraphTopological.get_sort(graph)
print("Orden topologico:", [node.value for node in order])
```

**Salida esperada:**

```
Orden topologico: ['Tarea1', 'Tarea2', 'Tarea3', 'Tarea4']
```

**Explicacion:**
`get_sort` implementa el algoritmo de Kahn:

1. Calcula el in-degree (numero de aristas entrantes) de cada nodo.
2. Mete en una cola todos los nodos con in-degree == 0 (no tienen dependencias).
3. Saca un nodo de la cola, lo agrega al resultado, y "elimina" sus aristas
   decrementando el in-degree de sus vecinos.
4. Cuando un vecino llega a in-degree 0, entra a la cola.
5. Si al final el resultado no contiene todos los nodos, hay ciclo y lanza
   `RuntimeError`.

El orden resultante garantiza que si existe una arista A -> B, entonces A
aparece antes que B en la lista. Puede haber multiples ordenes validos.

---

## Ejercicio 5: Rango (nivel) de cada nodo en un DAG

**Problema:**
Para el mismo DAG de tareas, calcula el rango de cada nodo. El rango indica
el "nivel" o semestre mas temprano en que puedes ejecutar esa tarea, contando
desde 0.

**Codigo:**

```python
from graph import DirectedGraph
from graph_algorithms import GraphTopological

graph = DirectedGraph()
t1 = graph.add_node_by_value("Tarea1")
t2 = graph.add_node_by_value("Tarea2")
t3 = graph.add_node_by_value("Tarea3")
t4 = graph.add_node_by_value("Tarea4")

graph.add_arc(t1, t2, 0.0)
graph.add_arc(t1, t3, 0.0)
graph.add_arc(t2, t4, 0.0)
graph.add_arc(t3, t4, 0.0)

ranks = GraphTopological.get_ranks(graph)
for node, level in ranks.items():
    print(f"{node.value}: nivel {level}")
```

**Salida esperada:**

```
Tarea1: nivel 0
Tarea2: nivel 1
Tarea3: nivel 1
Tarea4: nivel 2
```

**Explicacion:**
`get_ranks` funciona similar a Kahn pero en lugar de solo ordenar, asigna un
numero (rango) a cada nodo:

- Nodos sin predecesores (in-degree 0) reciben rango 0.
- Para cada vecino, el rango se calcula como `rango del nodo actual + 1`,
  tomando el maximo si el vecino ya tiene un rango asignado.
- El rango representa la **longitud del camino mas largo** desde cualquier raiz
  hasta ese nodo.

Esto es util para planificacion: si las tareas son materias universitarias,
el rango te dice en que semestre mas temprano puedes cursarla. Tarea2 y Tarea3
tienen rango 1 porque ambas dependen solo de Tarea1. Tarea4 tiene rango 2
porque necesita que terminen Tarea2 y Tarea3 primero.

---

## Ejercicio 6: Detectar ciclo en grafo dirigido

**Problema:**
Dado un grafo dirigido, determina si contiene un ciclo.

**Codigo:**

```python
from graph import DirectedGraph
from graph_algorithms import GraphTopological

graph = DirectedGraph()
a = graph.add_node_by_value("A")
b = graph.add_node_by_value("B")
c = graph.add_node_by_value("C")

graph.add_arc(a, b, 0.0)
graph.add_arc(b, c, 0.0)
graph.add_arc(c, a, 0.0)  # ciclo: C -> A

try:
    GraphTopological.get_sort(graph)
    print("No hay ciclo")
except RuntimeError:
    print("Hay ciclo!")
```

**Salida esperada:**

```
Hay ciclo!
```

**Explicacion:**
El algoritmo de Kahn (`get_sort`) solo puede procesar nodos cuyo in-degree
llega a 0. En un ciclo, todos los nodos involucrados siempre mantienen al
menos un in-degree > 0 (porque se apuntan entre si), asi que nunca entran a
la cola. Al final, `len(result) != len(graph)` y se lanza `RuntimeError`.

En este ejemplo, A -> B -> C -> A forma un ciclo de longitud 3. Ningun nodo
tiene in-degree 0, asi que la cola empieza vacia y el resultado queda vacio.

Esta es la forma mas directa de detectar ciclos en grafos dirigidos usando
las funciones disponibles.

---

## Ejercicio 7: Componentes conexas (BFS multiple)

**Problema:**
Encuentra todos los grupos de nodos conectados en un grafo no dirigido.
Cada grupo es una componente conexa.

**Codigo:**

```python
from graph import UndirectedGraph
from graph_algorithms import GraphTraversals

def compute_connected_components(graph):
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            comp = []
            GraphTraversals.traverse_bfs(graph, node, lambda n: comp.append(n))
            visited.update(comp)
            components.append([n.value for n in comp])
    return components

graph = UndirectedGraph()
a = graph.add_node_by_value("A")
b = graph.add_node_by_value("B")
c = graph.add_node_by_value("C")
d = graph.add_node_by_value("D")
e = graph.add_node_by_value("E")

graph.add_arc(a, b, 0.0)
graph.add_arc(c, d, 0.0)

components = compute_connected_components(graph)
print("Componentes conexas:", components)
```

**Salida esperada:**

```
Componentes conexas: [['A', 'B'], ['C', 'D'], ['E']]
```

**Explicacion:**
La idea es lanzar un BFS (o DFS) desde cada nodo que aun no ha sido visitado.
Cada BFS descubre todos los nodos de una componente conexa porque en un grafo
no dirigido, si puedes llegar de X a Y tambien puedes llegar de Y a X.

El algoritmo:
1. Itera sobre todos los nodos del grafo.
2. Si un nodo no ha sido visitado, lanza BFS desde el. Todos los nodos que
   visita forman una componente.
3. Marca esos nodos como visitados para no volver a procesarlos.
4. Repite hasta cubrir todos los nodos.

En este ejemplo hay 3 componentes: {A, B}, {C, D} y {E} (aislado, sin aristas).
La complejidad total sigue siendo O(V + E) porque cada nodo y arista se
procesa exactamente una vez sumando todos los BFS.

---

## Tabla resumen: Problema -> Algoritmo -> Funcion

| Problema | Algoritmo | Funcion |
|---|---|---|
| Camino mas corto (sin pesos) | BFS + predecessors | `GraphTraversals.find_shortest_path_bfs(g, start, end)` |
| Recorrer todos los alcanzables | BFS o DFS | `GraphTraversals.traverse_bfs(g, start, op)` / `traverse_dfs` |
| Arbol de expansion | DFS o BFS | `GraphTraversals.build_spanning_tree_dfs(g, start)` |
| Orden de ejecucion (dependencias) | Kahn (topo sort) | `GraphTopological.get_sort(g)` |
| Nivel/semestre de cada tarea | Kahn + rangos | `GraphTopological.get_ranks(g)` |
| Detectar ciclo en DAG | Kahn (falla si ciclo) | `GraphTopological.get_sort(g)` con try/except |
| Componentes conexas | BFS/DFS multiple | `traverse_bfs` en loop sobre nodos no visitados |
