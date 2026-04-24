"""
Ejercicios de práctica para el examen de AYDA — Grafos.

Cubre los algoritmos:
  - BFS                         (GraphTraversals.traverse_bfs)
  - DFS                         (GraphTraversals.traverse_dfs)
  - Camino más corto (BFS)      (GraphTraversals.find_shortest_path_bfs)
  - Ordenamiento topológico     (GraphTopological.get_sort)

Cada ejercicio tiene:
  1. Un docstring con la descripción del problema y el grafo.
  2. El grafo ya construido (no necesitas tocarlo).
  3. Un `raise NotImplementedError` que debes REEMPLAZAR con tu solución.

Debes resolver cada ejercicio usando las funciones de `graph_algorithms.py`.

Para verificar tus respuestas, ejecuta:
    python ejercicios_examen.py

El juez mostrará PASSED / FAILED / PENDING / ERROR para cada ejercicio.

Las soluciones correctas están en `ejercicios_examen_soluciones.py`.
"""
from graph import DirectedGraph, UndirectedGraph
from graph_algorithms import GraphTraversals, GraphTopological


# ============================================================================
# Juez (inspirado en main_tests.py)
# ============================================================================

def run_test(test_name: str, test_func) -> None:
    """Ejecuta un test y muestra PASSED / FAILED / PENDING / ERROR."""
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
    """
    BFS #1 — Contar nodos alcanzables.

    Grafo NO dirigido con nodos "A","B","C","D","E","F".
    Aristas: A-B, A-C, B-D, E-F.
    (E y F forman un componente separado)

    Usa traverse_bfs desde "A" y devuelve cuántos nodos fueron visitados.

    Returns:
        int: cantidad de nodos alcanzables desde "A".
    """
    graph = UndirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")
    d = graph.add_node_by_value("D")
    e = graph.add_node_by_value("E")
    f = graph.add_node_by_value("F")
    graph.add_arc(a, b, 0.0); graph.add_arc(a, c, 0.0); graph.add_arc(b, d, 0.0)
    graph.add_arc(e, f, 0.0)  # Componente separado

    # TODO: usa GraphTraversals.traverse_bfs desde 'a' y cuenta los visitados
    raise NotImplementedError("ejercicio_bfs_1")


def ejercicio_bfs_2():
    """
    BFS #2 — Lista de valores visitados en orden BFS.

    Grafo NO dirigido con nodos "1","2","3","4","5".
    Aristas: 1-2, 1-3, 2-4, 3-5.

    Usa traverse_bfs desde "1" y devuelve una lista con los VALORES
    de los nodos en el orden en que fueron visitados.

    Returns:
        list[str]: valores visitados, empezando por "1".
    """
    graph = UndirectedGraph()
    n1 = graph.add_node_by_value("1")
    n2 = graph.add_node_by_value("2")
    n3 = graph.add_node_by_value("3")
    n4 = graph.add_node_by_value("4")
    n5 = graph.add_node_by_value("5")
    graph.add_arc(n1, n2, 0.0); graph.add_arc(n1, n3, 0.0)
    graph.add_arc(n2, n4, 0.0); graph.add_arc(n3, n5, 0.0)

    # TODO: usa traverse_bfs y recolecta los valores visitados en orden BFS
    raise NotImplementedError("ejercicio_bfs_2")


def ejercicio_bfs_3():
    """
    BFS #3 — ¿Es "Z" alcanzable desde "A"?

    Grafo DIRIGIDO con nodos "A","B","C","Z".
    Aristas: A->B, B->C, C->Z.

    Usa traverse_bfs desde "A" y devuelve True si el nodo "Z" fue
    visitado, False en caso contrario.

    Returns:
        bool
    """
    graph = DirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")
    z = graph.add_node_by_value("Z")
    graph.add_arc(a, b, 0.0); graph.add_arc(b, c, 0.0); graph.add_arc(c, z, 0.0)

    # TODO: usa traverse_bfs desde 'a' y comprueba si "Z" está entre los visitados
    raise NotImplementedError("ejercicio_bfs_3")


def ejercicio_bfs_4():
    """
    BFS #4 — Suma de valores enteros alcanzables.

    Grafo NO dirigido con nodos enteros 10, 20, 30, 40, 50.
    Aristas: 10-20, 10-30, 30-40.
    (El nodo 50 está aislado — sin aristas)

    Usa traverse_bfs desde el nodo 10 y devuelve la suma de los
    valores de los nodos visitados.

    Returns:
        int: suma de los valores alcanzables desde 10.
    """
    graph = UndirectedGraph()
    n10 = graph.add_node_by_value(10)
    n20 = graph.add_node_by_value(20)
    n30 = graph.add_node_by_value(30)
    n40 = graph.add_node_by_value(40)
    n50 = graph.add_node_by_value(50)  # aislado
    graph.add_arc(n10, n20, 0.0); graph.add_arc(n10, n30, 0.0)
    graph.add_arc(n30, n40, 0.0)

    # TODO: usa traverse_bfs desde n10 y devuelve la suma de los valores visitados
    raise NotImplementedError("ejercicio_bfs_4")


def ejercicio_bfs_5():
    """
    BFS #5 — Contar nodos cuyo valor empieza por 'C'.

    Grafo NO dirigido con nodos "Casa","Coche","Perro","Calle","Árbol".
    Aristas: Casa-Coche, Casa-Perro, Perro-Calle.
    ("Árbol" está aislado)

    Usa traverse_bfs desde "Casa" y devuelve cuántos nodos visitados
    tienen un valor que empieza por la letra 'C'.

    Returns:
        int
    """
    graph = UndirectedGraph()
    casa = graph.add_node_by_value("Casa")
    coche = graph.add_node_by_value("Coche")
    perro = graph.add_node_by_value("Perro")
    calle = graph.add_node_by_value("Calle")
    arbol = graph.add_node_by_value("Árbol")  # aislado
    graph.add_arc(casa, coche, 0.0); graph.add_arc(casa, perro, 0.0)
    graph.add_arc(perro, calle, 0.0)

    # TODO: usa traverse_bfs desde 'casa' y cuenta los visitados que empiezan por 'C'
    raise NotImplementedError("ejercicio_bfs_5")


# ============================================================================
# DFS — GraphTraversals.traverse_dfs
# ============================================================================

def ejercicio_dfs_1():
    """
    DFS #1 — Contar nodos visitados desde el origen.

    Grafo NO dirigido con nodos "A","B","C","D","E".
    Aristas: A-B, B-C, C-D, A-E.

    Usa traverse_dfs desde "A" y devuelve el número de nodos visitados.

    Returns:
        int
    """
    graph = UndirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")
    d = graph.add_node_by_value("D")
    e = graph.add_node_by_value("E")
    graph.add_arc(a, b, 0.0); graph.add_arc(b, c, 0.0)
    graph.add_arc(c, d, 0.0); graph.add_arc(a, e, 0.0)

    # TODO: usa traverse_dfs desde 'a' y cuenta los nodos visitados
    raise NotImplementedError("ejercicio_dfs_1")


def ejercicio_dfs_2():
    """
    DFS #2 — Lista de valores en orden de visita (cadena lineal).

    Grafo DIRIGIDO con nodos "1","2","3","4".
    Aristas: 1->2, 2->3, 3->4.

    Usa traverse_dfs desde "1" y devuelve la lista de VALORES de los
    nodos en el orden en que fueron visitados.

    Returns:
        list[str]: debe ser ["1","2","3","4"].
    """
    graph = DirectedGraph()
    n1 = graph.add_node_by_value("1")
    n2 = graph.add_node_by_value("2")
    n3 = graph.add_node_by_value("3")
    n4 = graph.add_node_by_value("4")
    graph.add_arc(n1, n2, 0.0); graph.add_arc(n2, n3, 0.0); graph.add_arc(n3, n4, 0.0)

    # TODO: usa traverse_dfs desde n1 y devuelve la lista de valores visitados
    raise NotImplementedError("ejercicio_dfs_2")


def ejercicio_dfs_3():
    """
    DFS #3 — ¿Existe un nodo "FIN" alcanzable?

    Grafo DIRIGIDO con nodos "INICIO","P1","P2","FIN".
    Aristas: INICIO->P1, P1->P2, P2->FIN.

    Usa traverse_dfs desde "INICIO" y devuelve True si "FIN" fue
    visitado durante el recorrido.

    Returns:
        bool
    """
    graph = DirectedGraph()
    inicio = graph.add_node_by_value("INICIO")
    p1 = graph.add_node_by_value("P1")
    p2 = graph.add_node_by_value("P2")
    fin = graph.add_node_by_value("FIN")
    graph.add_arc(inicio, p1, 0.0); graph.add_arc(p1, p2, 0.0); graph.add_arc(p2, fin, 0.0)

    # TODO: usa traverse_dfs desde 'inicio' y detecta si "FIN" fue visitado
    raise NotImplementedError("ejercicio_dfs_3")


def ejercicio_dfs_4():
    """
    DFS #4 — Valor máximo entre los nodos alcanzables.

    Grafo NO dirigido con nodos enteros 5, 3, 8, 1, 12.
    Aristas: 5-3, 5-8, 8-1.
    (El nodo 12 está aislado)

    Usa traverse_dfs desde el nodo 5 y devuelve el valor máximo
    entre los nodos visitados.

    Returns:
        int
    """
    graph = UndirectedGraph()
    n5 = graph.add_node_by_value(5)
    n3 = graph.add_node_by_value(3)
    n8 = graph.add_node_by_value(8)
    n1 = graph.add_node_by_value(1)
    n12 = graph.add_node_by_value(12)  # aislado
    graph.add_arc(n5, n3, 0.0); graph.add_arc(n5, n8, 0.0); graph.add_arc(n8, n1, 0.0)

    # TODO: usa traverse_dfs desde n5 y devuelve el valor máximo visitado
    raise NotImplementedError("ejercicio_dfs_4")


def ejercicio_dfs_5():
    """
    DFS #5 — Contar nodos NO visitados desde el origen.

    Grafo NO dirigido con nodos "A","B","C","D".
    Aristas: A-B.
    (Los nodos C y D están aislados)

    Usa traverse_dfs desde "A" y devuelve la cantidad de nodos del
    grafo que NO fueron visitados (total de nodos − visitados).

    Returns:
        int
    """
    graph = UndirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")  # aislado
    d = graph.add_node_by_value("D")  # aislado
    graph.add_arc(a, b, 0.0)

    # TODO: usa traverse_dfs desde 'a' y calcula (total de nodos − visitados)
    raise NotImplementedError("ejercicio_dfs_5")


# ============================================================================
# Shortest Path BFS — GraphTraversals.find_shortest_path_bfs
# ============================================================================

def ejercicio_sp_1():
    """
    SP #1 — Número de aristas del camino más corto.

    Grafo NO dirigido con nodos "A","B","C","D","E".
    Aristas: A-B, B-C, C-D, A-E, E-D.

    Usa find_shortest_path_bfs de "A" a "D" y devuelve el número de
    ARISTAS del camino más corto (es decir, len(path) - 1).

    Returns:
        int
    """
    graph = UndirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")
    d = graph.add_node_by_value("D")
    e = graph.add_node_by_value("E")
    graph.add_arc(a, b, 0.0); graph.add_arc(b, c, 0.0); graph.add_arc(c, d, 0.0)
    graph.add_arc(a, e, 0.0); graph.add_arc(e, d, 0.0)

    # TODO: usa find_shortest_path_bfs de 'a' a 'd' y devuelve len(path) - 1
    raise NotImplementedError("ejercicio_sp_1")


def ejercicio_sp_2():
    """
    SP #2 — Camino en la mansion.

    Grafo NO dirigido con nodos:
      "Entrada","Sala1","Sala2","Cocina","Salida".
    Aristas:
      Entrada-Sala1, Entrada-Sala2, Sala1-Cocina,
      Sala2-Cocina, Cocina-Salida.

    Usa find_shortest_path_bfs de "Entrada" a "Salida" y devuelve la
    lista con los VALORES del camino (en orden).

    Returns:
        list[str]: camino desde "Entrada" hasta "Salida".
    """
    graph = UndirectedGraph()
    entrada = graph.add_node_by_value("Entrada")
    sala1 = graph.add_node_by_value("Sala1")
    sala2 = graph.add_node_by_value("Sala2")
    cocina = graph.add_node_by_value("Cocina")
    salida = graph.add_node_by_value("Salida")
    graph.add_arc(entrada, sala1, 0.0); graph.add_arc(entrada, sala2, 0.0)
    graph.add_arc(sala1, cocina, 0.0); graph.add_arc(sala2, cocina, 0.0)
    graph.add_arc(cocina, salida, 0.0)

    # TODO: usa find_shortest_path_bfs y devuelve la lista de valores del camino
    raise NotImplementedError("ejercicio_sp_2")


def ejercicio_sp_3():
    """
    SP #3 — ¿Existe camino entre dos nodos?

    Grafo DIRIGIDO con nodos "A","B","C","D".
    Aristas: A->B, B->C.
    ("D" está aislado — sin aristas)

    Usa find_shortest_path_bfs de "A" a "D" y devuelve True si existe
    un camino, False en caso contrario.

    Pista: find_shortest_path_bfs retorna [] cuando no hay camino.

    Returns:
        bool
    """
    graph = DirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")
    d = graph.add_node_by_value("D")  # aislado
    graph.add_arc(a, b, 0.0); graph.add_arc(b, c, 0.0)

    # TODO: usa find_shortest_path_bfs de 'a' a 'd' y devuelve True si hay camino
    raise NotImplementedError("ejercicio_sp_3")


def ejercicio_sp_4():
    """
    SP #4 — Número de nodos intermedios.

    Grafo NO dirigido con nodos "1","2","3","4","5".
    Aristas: 1-2, 2-3, 3-4, 4-5.

    Usa find_shortest_path_bfs de "1" a "5" y devuelve el número de
    nodos INTERMEDIOS (sin contar inicio ni fin).

    Returns:
        int: len(path) - 2
    """
    graph = UndirectedGraph()
    n1 = graph.add_node_by_value("1")
    n2 = graph.add_node_by_value("2")
    n3 = graph.add_node_by_value("3")
    n4 = graph.add_node_by_value("4")
    n5 = graph.add_node_by_value("5")
    graph.add_arc(n1, n2, 0.0); graph.add_arc(n2, n3, 0.0)
    graph.add_arc(n3, n4, 0.0); graph.add_arc(n4, n5, 0.0)

    # TODO: usa find_shortest_path_bfs de n1 a n5 y devuelve len(path) - 2
    raise NotImplementedError("ejercicio_sp_4")


def ejercicio_sp_5():
    """
    SP #5 — Longitudes de dos caminos más cortos.

    Grafo NO dirigido con nodos "A","B","C","D","E".
    Aristas: A-B, B-C, A-D, D-E, C-E.

    Usa find_shortest_path_bfs para calcular:
      - len_ac: longitud (número de nodos) del camino más corto A→C
      - len_ae: longitud (número de nodos) del camino más corto A→E

    Devuelve una tupla (len_ac, len_ae).

    Returns:
        tuple[int, int]
    """
    graph = UndirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")
    d = graph.add_node_by_value("D")
    e = graph.add_node_by_value("E")
    graph.add_arc(a, b, 0.0); graph.add_arc(b, c, 0.0)
    graph.add_arc(a, d, 0.0); graph.add_arc(d, e, 0.0)
    graph.add_arc(c, e, 0.0)

    # TODO: calcula ambos caminos más cortos y devuelve (len(path_ac), len(path_ae))
    raise NotImplementedError("ejercicio_sp_5")


# ============================================================================
# Topological Sort — GraphTopological.get_sort (3 ejercicios)
# ============================================================================

def ejercicio_sort_1():
    """
    SORT #1 — Orden topológico de una cadena lineal.

    DAG con nodos "Compilar","Testear","Desplegar","Release".
    Aristas: Compilar->Testear, Testear->Desplegar, Desplegar->Release.

    Usa get_sort y devuelve la lista de VALORES en orden topológico.

    Returns:
        list[str]
    """
    graph = DirectedGraph()
    comp = graph.add_node_by_value("Compilar")
    test = graph.add_node_by_value("Testear")
    depl = graph.add_node_by_value("Desplegar")
    rel = graph.add_node_by_value("Release")
    graph.add_arc(comp, test, 0.0)
    graph.add_arc(test, depl, 0.0)
    graph.add_arc(depl, rel, 0.0)

    # TODO: usa get_sort y devuelve la lista de valores en orden topológico
    raise NotImplementedError("ejercicio_sort_1")


def ejercicio_sort_2():
    """
    SORT #2 — Primera tarea del orden topológico.

    DAG con nodos "A","B","C","D".
    Aristas: A->B, A->C, B->D, C->D.

    Usa get_sort y devuelve el VALOR del primer nodo del orden.

    Returns:
        str
    """
    graph = DirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")
    d = graph.add_node_by_value("D")
    graph.add_arc(a, b, 0.0); graph.add_arc(a, c, 0.0)
    graph.add_arc(b, d, 0.0); graph.add_arc(c, d, 0.0)

    # TODO: usa get_sort y devuelve el valor del primer nodo del orden
    raise NotImplementedError("ejercicio_sort_2")


def ejercicio_sort_3():
    """
    SORT #3 — Detección de ciclo con get_sort.

    Grafo DIRIGIDO con nodos "X","Y","Z".
    Aristas: X->Y, Y->Z, Z->X (ciclo!).

    Usa get_sort y devuelve True si el grafo tiene ciclo, False si no.

    Pista: get_sort lanza RuntimeError cuando hay ciclo — usa try/except.

    Returns:
        bool
    """
    graph = DirectedGraph()
    x = graph.add_node_by_value("X")
    y = graph.add_node_by_value("Y")
    z = graph.add_node_by_value("Z")
    graph.add_arc(x, y, 0.0); graph.add_arc(y, z, 0.0); graph.add_arc(z, x, 0.0)

    # TODO: intenta get_sort y captura RuntimeError para detectar ciclo
    raise NotImplementedError("ejercicio_sort_3")


# ============================================================================
# Topological Ranks — GraphTopological.get_ranks (3 ejercicios)
# ============================================================================

def ejercicio_rank_1():
    """
    RANK #1 — Rango del último nodo en cadena lineal.

    DAG con nodos "A","B","C","D".
    Aristas: A->B, B->C, C->D.

    Usa get_ranks y devuelve el rango del nodo cuyo valor es "D".

    Returns:
        int
    """
    graph = DirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")
    d = graph.add_node_by_value("D")
    graph.add_arc(a, b, 0.0); graph.add_arc(b, c, 0.0); graph.add_arc(c, d, 0.0)

    # TODO: usa get_ranks y devuelve el rango del nodo con valor "D"
    raise NotImplementedError("ejercicio_rank_1")


def ejercicio_rank_2():
    """
    RANK #2 — Contar nodos con rango 0 (sin dependencias).

    DAG con nodos "A","B","C","D","E".
    Aristas: A->C, B->D, D->E.
    ("A" y "B" no tienen predecesores → rango 0)

    Usa get_ranks y devuelve cuántos nodos tienen rango 0.

    Returns:
        int
    """
    graph = DirectedGraph()
    a = graph.add_node_by_value("A")
    b = graph.add_node_by_value("B")
    c = graph.add_node_by_value("C")
    d = graph.add_node_by_value("D")
    e = graph.add_node_by_value("E")
    graph.add_arc(a, c, 0.0); graph.add_arc(b, d, 0.0); graph.add_arc(d, e, 0.0)

    # TODO: usa get_ranks y cuenta cuántos nodos tienen rango == 0
    raise NotImplementedError("ejercicio_rank_2")


def ejercicio_rank_3():
    """
    RANK #3 — Rango máximo (profundidad del pipeline).

    DAG con nodos "Req","Design","Code","Test","Deploy".
    Aristas: Req->Design, Design->Code, Code->Test, Test->Deploy.

    Usa get_ranks y devuelve el valor del rango máximo en el DAG.
    (Indica cuántos pasos secuenciales tiene el pipeline)

    Returns:
        int
    """
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

    # TODO: usa get_ranks y devuelve el rango máximo (max de los valores del dict)
    raise NotImplementedError("ejercicio_rank_3")


def ejercicio_rank_4():
    """
    RANK #4 — Malla curricular: semestres mínimos.

    Eres un estudiante y necesitas planificar tu malla de materias.
    Cada materia tiene prerrequisitos que debes aprobar antes.
    El rango de cada materia indica el semestre más temprano (desde 0)
    en que la puedes cursar.

    DAG de prerrequisitos:
      "Cálculo I"  -> "Cálculo II"  -> "Ec. Diferenciales"
      "Prog I"     -> "Prog II"     -> "Estructuras"
      "Cálculo I"  -> "Física I"

    Usa get_ranks y devuelve cuántos SEMESTRES MÍNIMOS necesitas para
    completar TODAS las materias (es decir, max(ranks) + 1).

    Returns:
        int
    """
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

    # TODO: usa get_ranks y devuelve max(ranks.values()) + 1
    raise NotImplementedError("ejercicio_rank_4")


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
    print("    EJERCICIOS DE EXAMEN — AYDA GRAFOS    ")
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
