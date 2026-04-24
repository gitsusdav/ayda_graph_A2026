"""
Soluciones de los ejercicios de examen — AYDA Grafos.

Este archivo contiene las respuestas correctas para cada ejercicio del
fichero `ejercicios_examen.py`. Todas las funciones se resuelven
exclusivamente con las funciones de `graph_algorithms.py`:

  - GraphTraversals.traverse_bfs
  - GraphTraversals.traverse_dfs
  - GraphTraversals.find_shortest_path_bfs
  - GraphTopological.get_sort

Para ejecutar y verificar:
    python ejercicios_examen_soluciones.py

Todos los tests deben salir en [PASSED].
"""
from graph import DirectedGraph, UndirectedGraph
from graph_algorithms import GraphTraversals, GraphTopological


# ============================================================================
# Juez
# ============================================================================

def run_test(test_name: str, test_func) -> None:
    print(f"Running {test_name.ljust(42)} ", end="")
    try:
        test_func()
        print("\033[32m[PASSED]\033[0m")
    except NotImplementedError as e:
        print(f"\033[33m[PENDING]\033[0m ({e})")
    except AssertionError as e:
        print(f"\033[31m[FAILED]\033[0m (Assertion: {e})")
    except Exception as e:
        print(f"\033[31m[ERROR]\033[0m ({type(e).__name__}: {e})")


# ============================================================================
# BFS — GraphTraversals.traverse_bfs
# ============================================================================

def ejercicio_bfs_1():
    """BFS #1 — Contar nodos alcanzables desde 'A'."""
    graph = UndirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")
    d = graph.add_node_by_value("D")
    e = graph.add_node_by_value("E")
    f = graph.add_node_by_value("F")
    graph.add_arc(a, b, 0.0); graph.add_arc(a, c, 0.0); graph.add_arc(b, d, 0.0)
    graph.add_arc(e, f, 0.0)

    # SOLUCIÓN: BFS con visitor que cuenta los nodos visitados
    visitados = []
    GraphTraversals.traverse_bfs(graph, a, lambda n: visitados.append(n))
    return len(visitados)


def ejercicio_bfs_2():
    """BFS #2 — Valores visitados en orden BFS."""
    graph = UndirectedGraph()
    n1 = graph.add_node_by_value("1")
    n2 = graph.add_node_by_value("2")
    n3 = graph.add_node_by_value("3")
    n4 = graph.add_node_by_value("4")
    n5 = graph.add_node_by_value("5")
    graph.add_arc(n1, n2, 0.0); graph.add_arc(n1, n3, 0.0)
    graph.add_arc(n2, n4, 0.0); graph.add_arc(n3, n5, 0.0)

    # SOLUCIÓN: BFS con visitor que recolecta los valores
    valores = []
    GraphTraversals.traverse_bfs(graph, n1, lambda n: valores.append(n.value))
    return valores


def ejercicio_bfs_3():
    """BFS #3 — ¿Es 'Z' alcanzable desde 'A'?"""
    graph = DirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")
    z = graph.add_node_by_value("Z")
    graph.add_arc(a, b, 0.0); graph.add_arc(b, c, 0.0); graph.add_arc(c, z, 0.0)

    # SOLUCIÓN: recolectar valores durante BFS y comprobar si "Z" está
    valores = []
    GraphTraversals.traverse_bfs(graph, a, lambda n: valores.append(n.value))
    return "Z" in valores


def ejercicio_bfs_4():
    """BFS #4 — Suma de valores enteros alcanzables desde 10."""
    graph = UndirectedGraph()
    n10 = graph.add_node_by_value(10)
    n20 = graph.add_node_by_value(20)
    n30 = graph.add_node_by_value(30)
    n40 = graph.add_node_by_value(40)
    n50 = graph.add_node_by_value(50)
    graph.add_arc(n10, n20, 0.0); graph.add_arc(n10, n30, 0.0)
    graph.add_arc(n30, n40, 0.0)

    # SOLUCIÓN: BFS recolectando valores y sumando
    valores = []
    GraphTraversals.traverse_bfs(graph, n10, lambda n: valores.append(n.value))
    return sum(valores)


def ejercicio_bfs_5():
    """BFS #5 — Nodos visitados cuyo valor empieza por 'C'."""
    graph = UndirectedGraph()
    casa = graph.add_node_by_value("Casa")
    coche = graph.add_node_by_value("Coche")
    perro = graph.add_node_by_value("Perro")
    calle = graph.add_node_by_value("Calle")
    arbol = graph.add_node_by_value("Árbol")
    graph.add_arc(casa, coche, 0.0); graph.add_arc(casa, perro, 0.0)
    graph.add_arc(perro, calle, 0.0)

    # SOLUCIÓN: BFS recolectando valores y filtrando por inicial 'C'
    valores = []
    GraphTraversals.traverse_bfs(graph, casa, lambda n: valores.append(n.value))
    return sum(1 for v in valores if v.startswith("C"))


# ============================================================================
# DFS — GraphTraversals.traverse_dfs
# ============================================================================

def ejercicio_dfs_1():
    """DFS #1 — Contar nodos visitados desde 'A'."""
    graph = UndirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")
    d = graph.add_node_by_value("D")
    e = graph.add_node_by_value("E")
    graph.add_arc(a, b, 0.0); graph.add_arc(b, c, 0.0)
    graph.add_arc(c, d, 0.0); graph.add_arc(a, e, 0.0)

    # SOLUCIÓN
    visitados = []
    GraphTraversals.traverse_dfs(graph, a, lambda n: visitados.append(n))
    return len(visitados)


def ejercicio_dfs_2():
    """DFS #2 — Lista de valores en orden DFS."""
    graph = DirectedGraph()
    n1 = graph.add_node_by_value("1")
    n2 = graph.add_node_by_value("2")
    n3 = graph.add_node_by_value("3")
    n4 = graph.add_node_by_value("4")
    graph.add_arc(n1, n2, 0.0); graph.add_arc(n2, n3, 0.0); graph.add_arc(n3, n4, 0.0)

    # SOLUCIÓN
    valores = []
    GraphTraversals.traverse_dfs(graph, n1, lambda n: valores.append(n.value))
    return valores


def ejercicio_dfs_3():
    """DFS #3 — ¿Se llega a 'FIN' desde 'INICIO'?"""
    graph = DirectedGraph()
    inicio = graph.add_node_by_value("INICIO")
    p1 = graph.add_node_by_value("P1")
    p2 = graph.add_node_by_value("P2")
    fin = graph.add_node_by_value("FIN")
    graph.add_arc(inicio, p1, 0.0); graph.add_arc(p1, p2, 0.0); graph.add_arc(p2, fin, 0.0)

    # SOLUCIÓN
    valores = []
    GraphTraversals.traverse_dfs(graph, inicio, lambda n: valores.append(n.value))
    return "FIN" in valores


def ejercicio_dfs_4():
    """DFS #4 — Máximo valor alcanzable desde 5."""
    graph = UndirectedGraph()
    n5 = graph.add_node_by_value(5)
    n3 = graph.add_node_by_value(3)
    n8 = graph.add_node_by_value(8)
    n1 = graph.add_node_by_value(1)
    n12 = graph.add_node_by_value(12)
    graph.add_arc(n5, n3, 0.0); graph.add_arc(n5, n8, 0.0); graph.add_arc(n8, n1, 0.0)

    # SOLUCIÓN
    valores = []
    GraphTraversals.traverse_dfs(graph, n5, lambda n: valores.append(n.value))
    return max(valores)


def ejercicio_dfs_5():
    """DFS #5 — Cantidad de nodos NO visitados desde 'A'."""
    graph = UndirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")
    d = graph.add_node_by_value("D")
    graph.add_arc(a, b, 0.0)

    # SOLUCIÓN: total de nodos − visitados
    visitados = []
    GraphTraversals.traverse_dfs(graph, a, lambda n: visitados.append(n))
    return len(graph) - len(visitados)


# ============================================================================
# Shortest Path BFS — GraphTraversals.find_shortest_path_bfs
# ============================================================================

def ejercicio_sp_1():
    """SP #1 — Número de aristas del camino más corto A→D."""
    graph = UndirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")
    d = graph.add_node_by_value("D")
    e = graph.add_node_by_value("E")
    graph.add_arc(a, b, 0.0); graph.add_arc(b, c, 0.0); graph.add_arc(c, d, 0.0)
    graph.add_arc(a, e, 0.0); graph.add_arc(e, d, 0.0)

    # SOLUCIÓN
    path = GraphTraversals.find_shortest_path_bfs(graph, a, d)
    return len(path) - 1


def ejercicio_sp_2():
    """SP #2 — Camino más corto en la mansion."""
    graph = UndirectedGraph()
    entrada = graph.add_node_by_value("Entrada")
    sala1 = graph.add_node_by_value("Sala1")
    sala2 = graph.add_node_by_value("Sala2")
    cocina = graph.add_node_by_value("Cocina")
    salida = graph.add_node_by_value("Salida")
    graph.add_arc(entrada, sala1, 0.0); graph.add_arc(entrada, sala2, 0.0)
    graph.add_arc(sala1, cocina, 0.0); graph.add_arc(sala2, cocina, 0.0)
    graph.add_arc(cocina, salida, 0.0)

    # SOLUCIÓN
    path = GraphTraversals.find_shortest_path_bfs(graph, entrada, salida)
    return [node.value for node in path]


def ejercicio_sp_3():
    """SP #3 — ¿Existe camino de 'A' a 'D'?"""
    graph = DirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")
    d = graph.add_node_by_value("D")
    graph.add_arc(a, b, 0.0); graph.add_arc(b, c, 0.0)

    # SOLUCIÓN: lista vacía → no hay camino
    path = GraphTraversals.find_shortest_path_bfs(graph, a, d)
    return len(path) > 0


def ejercicio_sp_4():
    """SP #4 — Número de nodos intermedios de 1 a 5."""
    graph = UndirectedGraph()
    n1 = graph.add_node_by_value("1")
    n2 = graph.add_node_by_value("2")
    n3 = graph.add_node_by_value("3")
    n4 = graph.add_node_by_value("4")
    n5 = graph.add_node_by_value("5")
    graph.add_arc(n1, n2, 0.0); graph.add_arc(n2, n3, 0.0)
    graph.add_arc(n3, n4, 0.0); graph.add_arc(n4, n5, 0.0)

    # SOLUCIÓN
    path = GraphTraversals.find_shortest_path_bfs(graph, n1, n5)
    return len(path) - 2


def ejercicio_sp_5():
    """SP #5 — Longitudes de A→C y A→E."""
    graph = UndirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")
    d = graph.add_node_by_value("D")
    e = graph.add_node_by_value("E")
    graph.add_arc(a, b, 0.0); graph.add_arc(b, c, 0.0)
    graph.add_arc(a, d, 0.0); graph.add_arc(d, e, 0.0)
    graph.add_arc(c, e, 0.0)

    # SOLUCIÓN
    path_ac = GraphTraversals.find_shortest_path_bfs(graph, a, c)
    path_ae = GraphTraversals.find_shortest_path_bfs(graph, a, e)
    return (len(path_ac), len(path_ae))


# ============================================================================
# Topological Sort — GraphTopological.get_sort (3 ejercicios)
# ============================================================================

def ejercicio_sort_1():
    """SORT #1 — Orden topológico completo."""
    graph = DirectedGraph()
    comp = graph.add_node_by_value("Compilar")
    test = graph.add_node_by_value("Testear")
    depl = graph.add_node_by_value("Desplegar")
    rel = graph.add_node_by_value("Release")
    graph.add_arc(comp, test, 0.0)
    graph.add_arc(test, depl, 0.0)
    graph.add_arc(depl, rel, 0.0)

    # SOLUCIÓN
    orden = GraphTopological.get_sort(graph)
    return [node.value for node in orden]


def ejercicio_sort_2():
    """SORT #2 — Primera tarea del orden."""
    graph = DirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")
    d = graph.add_node_by_value("D")
    graph.add_arc(a, b, 0.0); graph.add_arc(a, c, 0.0)
    graph.add_arc(b, d, 0.0); graph.add_arc(c, d, 0.0)

    # SOLUCIÓN
    orden = GraphTopological.get_sort(graph)
    return orden[0].value


def ejercicio_sort_3():
    """SORT #3 — Detección de ciclo."""
    graph = DirectedGraph()
    x = graph.add_node_by_value("X")
    y = graph.add_node_by_value("Y")
    z = graph.add_node_by_value("Z")
    graph.add_arc(x, y, 0.0); graph.add_arc(y, z, 0.0); graph.add_arc(z, x, 0.0)

    # SOLUCIÓN: get_sort lanza RuntimeError si hay ciclo
    try:
        GraphTopological.get_sort(graph)
        return False
    except RuntimeError:
        return True


# ============================================================================
# Topological Ranks — GraphTopological.get_ranks (3 ejercicios)
# ============================================================================

def ejercicio_rank_1():
    """RANK #1 — Rango del último nodo en cadena lineal."""
    graph = DirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")
    d = graph.add_node_by_value("D")
    graph.add_arc(a, b, 0.0); graph.add_arc(b, c, 0.0); graph.add_arc(c, d, 0.0)

    # SOLUCIÓN: buscar el nodo "D" en el diccionario de rangos
    ranks = GraphTopological.get_ranks(graph)
    for node, rank in ranks.items():
        if node.value == "D":
            return rank


def ejercicio_rank_2():
    """RANK #2 — Contar nodos con rango 0."""
    graph = DirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")
    d = graph.add_node_by_value("D")
    e = graph.add_node_by_value("E")
    graph.add_arc(a, c, 0.0); graph.add_arc(b, d, 0.0); graph.add_arc(d, e, 0.0)

    # SOLUCIÓN: contar nodos cuyo rango es 0
    ranks = GraphTopological.get_ranks(graph)
    return sum(1 for r in ranks.values() if r == 0)


def ejercicio_rank_3():
    """RANK #3 — Rango máximo del pipeline."""
    graph = DirectedGraph()
    req = graph.add_node_by_value("Req")
    design = graph.add_node_by_value("Design")
    code = graph.add_node_by_value("Code")
    test = graph.add_node_by_value("Test")
    deploy = graph.add_node_by_value("Deploy")
    graph.add_arc(req, design, 0.0)
    graph.add_arc(design, code, 0.0)
    graph.add_arc(code, test, 0.0)
    graph.add_arc(test, deploy, 0.0)

    # SOLUCIÓN: el rango máximo indica la profundidad del pipeline
    ranks = GraphTopological.get_ranks(graph)
    return max(ranks.values())


def ejercicio_rank_4():
    """RANK #4 — Malla curricular: semestres mínimos."""
    graph = DirectedGraph()
    calc1 = graph.add_node_by_value("Cálculo I")
    calc2 = graph.add_node_by_value("Cálculo II")
    ecdif = graph.add_node_by_value("Ec. Diferenciales")
    prog1 = graph.add_node_by_value("Prog I")
    prog2 = graph.add_node_by_value("Prog II")
    estru = graph.add_node_by_value("Estructuras")
    fis1  = graph.add_node_by_value("Física I")
    graph.add_arc(calc1, calc2, 0.0); graph.add_arc(calc2, ecdif, 0.0)
    graph.add_arc(prog1, prog2, 0.0); graph.add_arc(prog2, estru, 0.0)
    graph.add_arc(calc1, fis1, 0.0)

    # SOLUCIÓN: max rank + 1 = semestres mínimos
    ranks = GraphTopological.get_ranks(graph)
    return max(ranks.values()) + 1


# ============================================================================
# Tests del juez
# ============================================================================

def test_bfs_1():
    assert ejercicio_bfs_1() == 4, "Desde A solo son alcanzables A, B, C y D"

def test_bfs_2():
    result = ejercicio_bfs_2()
    assert isinstance(result, list), "Debe retornar una lista"
    assert len(result) == 5, f"Debe visitar los 5 nodos, visitó {len(result)}"
    assert result[0] == "1", "El primer nodo visitado debe ser '1'"
    assert set(result) == {"1","2","3","4","5"}, "Debe visitar todos los nodos"

def test_bfs_3():
    assert ejercicio_bfs_3() is True, "'Z' es alcanzable desde 'A'"

def test_bfs_4():
    assert ejercicio_bfs_4() == 100, "10+20+30+40 = 100 (50 aislado)"

def test_bfs_5():
    assert ejercicio_bfs_5() == 3, "Casa, Coche y Calle empiezan por 'C'"


def test_dfs_1():
    assert ejercicio_dfs_1() == 5, "DFS debe visitar los 5 nodos conectados"

def test_dfs_2():
    result = ejercicio_dfs_2()
    assert isinstance(result, list), "Debe retornar una lista"
    assert result == ["1","2","3","4"], f"Orden DFS incorrecto: {result}"

def test_dfs_3():
    assert ejercicio_dfs_3() is True, "'FIN' es alcanzable desde 'INICIO'"

def test_dfs_4():
    assert ejercicio_dfs_4() == 8, "El máximo alcanzable desde 5 es 8 (12 aislado)"

def test_dfs_5():
    assert ejercicio_dfs_5() == 2, "C y D no son alcanzables desde A"


def test_sp_1():
    assert ejercicio_sp_1() == 2, "El camino más corto A→D tiene 2 aristas (A-E-D)"

def test_sp_2():
    result = ejercicio_sp_2()
    assert isinstance(result, list), "Debe retornar una lista"
    assert len(result) == 4, f"El camino debe tener 4 nodos, tiene {len(result)}"
    assert result[0] == "Entrada", "Debe empezar en 'Entrada'"
    assert result[-1] == "Salida", "Debe terminar en 'Salida'"
    assert result[2] == "Cocina", "El tercer nodo debe ser 'Cocina'"
    assert result[1] in ("Sala1", "Sala2"), "El segundo nodo debe ser una sala"

def test_sp_3():
    assert ejercicio_sp_3() is False, "No existe camino de A a D (D está aislado)"

def test_sp_4():
    assert ejercicio_sp_4() == 3, "El camino 1→5 tiene 3 nodos intermedios (2,3,4)"

def test_sp_5():
    result = ejercicio_sp_5()
    assert result == (3, 3), f"Esperado (3, 3), obtuvo {result}"


def test_sort_1():
    result = ejercicio_sort_1()
    assert result == ["Compilar","Testear","Desplegar","Release"], \
        f"Orden incorrecto: {result}"

def test_sort_2():
    assert ejercicio_sort_2() == "A", "El primer nodo del orden debe ser 'A'"

def test_sort_3():
    assert ejercicio_sort_3() is True, "El grafo X->Y->Z->X tiene un ciclo"


def test_rank_1():
    assert ejercicio_rank_1() == 3, "El rango de D en A->B->C->D es 3"

def test_rank_2():
    assert ejercicio_rank_2() == 2, "A y B tienen rango 0 (2 nodos)"

def test_rank_3():
    assert ejercicio_rank_3() == 4, "El rango máximo (Deploy) es 4"

def test_rank_4():
    assert ejercicio_rank_4() == 3, "Se necesitan 3 semestres (rangos 0, 1, 2)"


# ============================================================================
# Main
# ============================================================================

def main() -> None:
    print("==========================================")
    print("  SOLUCIONES — EJERCICIOS AYDA GRAFOS     ")
    print("==========================================\n")

    print("--- BFS (GraphTraversals.traverse_bfs) ---")
    run_test("BFS #1 (contar alcanzables)", test_bfs_1)
    run_test("BFS #2 (orden de visita)", test_bfs_2)
    run_test("BFS #3 (alcanzabilidad)", test_bfs_3)
    run_test("BFS #4 (suma de valores)", test_bfs_4)
    run_test("BFS #5 (predicado sobre valor)", test_bfs_5)

    print("\n--- DFS (GraphTraversals.traverse_dfs) ---")
    run_test("DFS #1 (contar alcanzables)", test_dfs_1)
    run_test("DFS #2 (orden de visita)", test_dfs_2)
    run_test("DFS #3 (alcanzabilidad)", test_dfs_3)
    run_test("DFS #4 (máximo valor)", test_dfs_4)
    run_test("DFS #5 (no visitados)", test_dfs_5)

    print("\n--- Shortest Path (find_shortest_path_bfs) ---")
    run_test("SP  #1 (aristas del camino)", test_sp_1)
    run_test("SP  #2 (camino en mansion)", test_sp_2)
    run_test("SP  #3 (existe camino)", test_sp_3)
    run_test("SP  #4 (intermedios)", test_sp_4)
    run_test("SP  #5 (dos caminos)", test_sp_5)

    print("\n--- Topological Sort (GraphTopological.get_sort) ---")
    run_test("SORT #1 (orden completo)", test_sort_1)
    run_test("SORT #2 (primera tarea)", test_sort_2)
    run_test("SORT #3 (detección de ciclo)", test_sort_3)

    print("\n--- Topological Ranks (GraphTopological.get_ranks) ---")
    run_test("RANK #1 (rango de un nodo)", test_rank_1)
    run_test("RANK #2 (nodos sin dependencias)", test_rank_2)
    run_test("RANK #3 (rango máximo)", test_rank_3)
    run_test("RANK #4 (malla curricular)", test_rank_4)

    print("\n==========================================")


if __name__ == "__main__":
    main()
