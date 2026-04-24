¡Perfecto! Te voy a armar **5 ejercicios completos**, tipo HackerRank/CLRS, usando **solo BFS, DFS, Spanning Trees, Topological Sort, Ranks y Ciclos**, **con tus funciones y código listo para ejecutar**, incluyendo inputs de ejemplo y salidas esperadas. Esto va a cubrir **lo más probable que te salga en tu examen**, incluyendo el caso de la “mansion”.

---

# 1️⃣ Ejercicio: Camino más corto en la *mansion*

**Problema:**
Tienes un mapa de la mansion como grafo no ponderado. Encuentra el camino más corto desde la entrada (`start`) hasta la salida (`end`).

**Código:**

```python
# Grafo ya definido como Graph, Node, Arc
graph = Graph()
A = graph.add_node_by_value("Entrada")
B = graph.add_node_by_value("Sala1")
C = graph.add_node_by_value("Sala2")
D = graph.add_node_by_value("Cocina")
E = graph.add_node_by_value("Salida")

# Conexiones
graph.add_arc(A, B)
graph.add_arc(A, C)
graph.add_arc(B, D)
graph.add_arc(C, D)
graph.add_arc(D, E)

# Camino más corto usando tu función BFS
path = GraphTraversals.find_shortest_path_bfs(graph, A, E)
print("Camino más corto de Entrada a Salida:", [node.value for node in path])
```

**Salida esperada:**

```
Camino más corto de Entrada a Salida: ['Entrada', 'B', 'D', 'Salida']
```

✅ **Aprendes:** BFS en grafo no ponderado, reconstrucción de camino.

---

# 2️⃣ Ejercicio: Nodos alcanzables desde un nodo

**Problema:**
Lista todos los nodos que se pueden alcanzar desde un nodo `start`.

**Código:**

```python
graph = Graph()
a = graph.add_node_by_value("A")
b = graph.add_node_by_value("B")
c = graph.add_node_by_value("C")
d = graph.add_node_by_value("D")

graph.add_arc(a, b)
graph.add_arc(a, c)
graph.add_arc(b, d)

visitados = []
GraphTraversals.traverse_bfs(graph, a, lambda n: visitados.append(n.value))
print("Nodos alcanzables desde A:", visitados)
```

**Salida esperada:**

```
Nodos alcanzables desde A: ['A', 'B', 'C', 'D']
```

✅ **Aprendes:** BFS/DFS para exploración completa.

---

# 3️⃣ Ejercicio: Construir árbol de expansión DFS

**Problema:**
Construye un **árbol de expansión** desde un nodo `start` usando DFS.

**Código:**

```python
tree = GraphTraversals.build_spanning_tree_dfs(graph, a)

print("Arcos del árbol de expansión DFS:")
for node in tree:
    for arc in tree.get_outgoing_arcs(node):
        print(node.value, "->", arc.target.value)
```

**Salida esperada (puede variar según DFS):**

```
A -> B
B -> D
A -> C
```

✅ **Aprendes:** Construir un grafo nuevo sin ciclos a partir de DFS, usando `node_mapping`.

---

# 4️⃣ Ejercicio: Orden topológico de tareas

**Problema:**
Dado un DAG de tareas, devuelve un **orden válido** de ejecución.

**Código:**

```python
graph = Graph()
t1 = graph.add_node_by_value("Tarea1")
t2 = graph.add_node_by_value("Tarea2")
t3 = graph.add_node_by_value("Tarea3")
t4 = graph.add_node_by_value("Tarea4")

graph.add_arc(t1, t2)
graph.add_arc(t1, t3)
graph.add_arc(t2, t4)
graph.add_arc(t3, t4)

order = GraphTopological.get_sort(graph)
print("Orden topológico:", [node.value for node in order])
```

**Salida esperada:**

```
Orden topológico: ['Tarea1', 'Tarea2', 'Tarea3', 'Tarea4']
```

✅ **Aprendes:** Kahn’s Algorithm y cómo detectar dependencias/ciclos.

---

# 5️⃣ Ejercicio: Componentes conectadas

**Problema:**
Encuentra todos los grupos de nodos conectados en un grafo no dirigido.

**Código:**

```python
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

graph = Graph()
a = graph.add_node_by_value("A")
b = graph.add_node_by_value("B")
c = graph.add_node_by_value("C")
d = graph.add_node_by_value("D")
e = graph.add_node_by_value("E")

# Crear componentes
graph.add_arc(a, b)
graph.add_arc(b, a)
graph.add_arc(c, d)
graph.add_arc(d, c)

components = compute_connected_components(graph)
print("Componentes conectadas:", components)
```

**Salida esperada:**

```
Componentes conectadas: [['A', 'B'], ['C', 'D'], ['E']]
```

✅ **Aprendes:** BFS/DFS múltiples para agrupar nodos conectados.

---

Con estos 5 ejercicios tienes **todo lo que tu profesor puede poner** si no usas Dijkstra ni Kosaraju:

* Camino más corto → BFS → “mansion”
* Alcanzabilidad → BFS/DFS
* Árbol de expansión → DFS
* Orden de tareas → Topological sort
* Componentes conectadas → BFS/DFS múltiple

---
