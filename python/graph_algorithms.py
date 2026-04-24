import heapq
from collections import deque
import queue
from typing import TypeVar, Dict, List, Set, Callable, Optional, Tuple
from unittest import result

from graph import Graph, Node, Arc

NodeType = TypeVar('NodeType')
WeightType = TypeVar('WeightType')
GraphType = TypeVar('GraphType', bound=Graph)

class AStar:
    """Implements the A* (A-Star) search algorithm."""

    @staticmethod
    def find_path(graph: GraphType, start: Node[NodeType], goal: Node[NodeType], heuristic: Callable[[Node[NodeType]], float]) -> List[Node[NodeType]]:
        """
        Finds the shortest path using a heuristic function.
        """
        if start not in graph or goal not in graph:
            raise ValueError("Start or Goal node not in graph.")

        # TODO: Implement A* search algorithm using Python's heapq.
        # HINT: Maintain a g_score (actual cost) and f_score (estimated total cost) for each node.
        raise NotImplementedError("AStar.find_path is not implemented yet!")

class BellmanFord:
    """Implements the Bellman-Ford algorithm for negative weights detection."""

    @staticmethod
    def get_minimum_paths_tree(graph: GraphType, source: Node[NodeType]) -> GraphType:
        """
        Computes the Shortest Paths Tree, detecting negative cycles.
        Raises RuntimeError if a negative cycle is detected.
        """
        if source not in graph: raise ValueError("Source node not in graph.")

        # TODO: Implement Bellman-Ford to find shortest paths and detect negative cycles.
        # HINT: Relax all edges |V| - 1 times. A final relaxation pass should detect cycles.
        raise NotImplementedError("BellmanFord.get_minimum_paths_tree is not implemented yet!")

class Prim:
    """Implements Prim's Algorithm for Minimum Spanning Trees."""

    @staticmethod
    def get_minimum_spanning_tree(graph: GraphType, start: Node[NodeType]) -> GraphType:
        # TODO: Implement Prim's algorithm using heapq.
        # HINT: Keep track of nodes already included in the MST to avoid cycles.
        raise NotImplementedError("Prim.get_minimum_spanning_tree is not implemented yet!")

class Kruskal:
    """Implements Kruskal's Algorithm for Minimum Spanning Trees."""

    @staticmethod
    def get_minimum_spanning_tree(graph: GraphType) -> GraphType:
        # TODO: Implement Kruskal's algorithm.
        # HINT: Sort all edges by weight. You will need to implement a Disjoint Set (Union-Find) helper.
        raise NotImplementedError("Kruskal.get_minimum_spanning_tree is not implemented yet!")

class Dijkstra:
    """Implements Dijkstra's algorithm for finding shortest paths in weighted graphs."""

    @staticmethod
    def get_minimum_paths_tree(graph: GraphType, source: Node[NodeType]) -> GraphType:
        """
        Computes the Shortest Paths Tree (SPT) from a source node using a Min-Heap.

        Args:
            graph (GraphType): The input weighted graph.
            source (Node[NodeType]): The source node for path computation.

        Returns:
            GraphType: A new graph containing only the arcs that form the shortest paths tree.

        Time complexity: O((V + E) log V)
        """
        if not isinstance(graph, Graph): raise TypeError("Expected a Graph instance.")
        if source not in graph: raise ValueError("Source node not in graph.")

        # TODO: Implement Dijkstra's Algorithm using Python's heapq.
        # Remember to handle ties in the priority queue properly (e.g., using id(node)).
        raise NotImplementedError("Dijkstra.get_minimum_paths_tree is not implemented yet!")


class GraphTraversals:
    """Provides graph traversal algorithms (BFS, DFS) and related operations."""

    @staticmethod
    def traverse_bfs(graph: GraphType, start: Node[NodeType], op: Callable[[Node[NodeType]], None]) -> None:
        """
        Performs a Breadth-First Search traversal starting from a given node.

        Args:
            graph (GraphType): The graph to traverse.
            start (Node[NodeType]): The starting node.
            op (Callable): Unary operation (Visitor pattern) invoked for each visited node.
        """
        if not isinstance(graph, Graph): raise TypeError("Expected a Graph instance.")
        if start not in graph: raise ValueError("Source node not in graph.")
        
        visited = set() # visited nodes
        q = deque([start]) 

        while q:
            u = q.popleft()
            if u in visited:
                continue
            visited.add(u)
            op(u)

            for arc in graph.get_outgoing_arcs(u):
                v = arc.target
                if v not in visited:
                    q.append(v)


        # HINT: Use graph.get_outgoing_arcs() and call op(current_node) when processed.
        # raise NotImplementedError("traverse_bfs is not implemented yet!")

    @staticmethod
    def find_shortest_path_bfs(graph: GraphType, start: Node[NodeType], end: Node[NodeType]) -> List[Node[NodeType]]:
        """
        Finds the shortest path between two nodes in an unweighted graph using BFS.
        """
        
        if not isinstance(graph, Graph): raise TypeError("Expected a Graph instance.")
        if start not in graph or end not in graph: raise ValueError("Start or End node not in graph.")

        q = deque([start])
        visited = set()
        predecessors = {start: None}

        while q:
            current_node = q.popleft()
            if current_node == end:
                break
            visited.add(current_node)

            for arc in graph.get_outgoing_arcs(current_node):
                neighbor = arc.target
                if neighbor not in visited and neighbor not in predecessors:
                    predecessors[neighbor] = current_node
                    q.append(neighbor)

        else:
            return []
        
        path = []

        while end is not None:
            path.append(end)
            end = predecessors[end]
        
        return path[::-1]
    


        # TODO: Implement shortest path finding using BFS and a predecessors tracking dictionary.
        #raise NotImplementedError("find_shortest_path_bfs is not implemented yet!")

    @staticmethod
    def traverse_dfs(graph: GraphType, start: Node[NodeType], op: Callable[[Node[NodeType]], None]) -> None:
        """
        Performs a Depth-First Search traversal starting from a node.
        """

        
        if not isinstance(graph, Graph): raise TypeError("Expected a Graph instance.")
        if start not in graph: raise ValueError("Source node not in graph.")
        
        visited = set()
        stack = [start]

        while stack:
            current_node = stack.pop()
            if current_node in visited:
                continue
            visited.add(current_node)
            op(current_node)

            for arc in graph.get_outgoing_arcs(current_node):
                neighbor = arc.target
                if neighbor not in visited:
                    stack.append(neighbor)

        # TODO: Implement DFS. (Hint: Create a private recursive helper method `_dfs_recursive`).
        # HINT: Use graph.get_outgoing_arcs() and call op(current_node) when processed.
        #raise NotImplementedError("traverse_dfs is not implemented yet!")

    @staticmethod
    def build_spanning_tree_dfs(graph: GraphType, start: Node[NodeType]) -> GraphType:
        """Builds a spanning tree using Depth-First Search traversal."""
        if not isinstance(graph, Graph): raise TypeError("Expected a Graph instance.")
        if start not in graph: raise ValueError("Source node not in graph.")

        tree = type(graph)()  # Create a new graph to hold the spanning tree
        visited = set()
        stack = [start]

        node_mapping = {}  # Maps original nodes to their counterparts in the spanning tree
        node_mapping[start] = tree.add_node_by_value(start.value)  # Add the start node to the spanning tree

        while stack:
                current_node = stack.pop()

                if current_node in visited:
                    continue

                visited.add(current_node)

                for arc in graph.get_outgoing_arcs(current_node):
                    neighbor = arc.target

                    if neighbor not in visited:
                        stack.append(neighbor)

                    # crear nodo si no existe en el árbol
                        if neighbor not in node_mapping:
                            node_mapping[neighbor] = tree.add_node_by_value(neighbor.value)

                     # usar el mapping (ESTA es la clave)
                        tree.add_arc(node_mapping[current_node],node_mapping[neighbor],arc.get_weight())  # Add the arc to the spanning tree
        return tree
        # TODO: Traverse the graph using DFS and build a new GraphType.
        #raise NotImplementedError("build_spanning_tree_dfs is not implemented yet!")


@staticmethod
def build_spanning_tree_bfs(graph: GraphType, start: Node[NodeType]) -> GraphType:
    if not isinstance(graph, Graph):
        raise TypeError("Expected a Graph instance.")
    if start not in graph:
        raise ValueError("Source node not in graph.")

    tree = type(graph)()
    visited = set()
    queue = deque([start])

    node_mapping = {}
    node_mapping[start] = tree.add_node_by_value(start.value)

    visited.add(start)

    while queue:
        current_node = queue.popleft()

        for arc in graph.get_outgoing_arcs(current_node):
            neighbor = arc.target

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

                if neighbor not in node_mapping:
                    node_mapping[neighbor] = tree.add_node_by_value(neighbor.value)

                tree.add_arc(
                    node_mapping[current_node],
                    node_mapping[neighbor],
                    arc.get_weight()
                )

    return tree

class GraphProperties:
    """Analyzes graph properties such as cycles, connected components, and dependencies."""

    @staticmethod
    def has_cycle(graph: GraphType) -> bool:
        """
        Detects cycles in a directed graph using Kahn's algorithm.
        Returns True if the graph contains at least one cycle, False otherwise.
        """
        if not isinstance(graph, Graph): raise TypeError("Expected a Graph instance.")

        # TODO: Implement cycle detection using in-degrees.
        # HINT: You can easily get in-degrees using graph.get_in_degree(node).
        raise NotImplementedError("has_cycle is not implemented yet!")

    @staticmethod
    def compute_connected_components(graph: GraphType) -> List[List[Node[NodeType]]]:
        """
        Groups nodes into connected components. Primarily designed for undirected graphs.
        """
        if not isinstance(graph, Graph): raise TypeError("Expected a Graph instance.")

        # TODO: Iterate over all nodes, launching a BFS/DFS for unvisited ones to form components.
        raise NotImplementedError("compute_connected_components is not implemented yet!")

    @staticmethod
    def compute_strongly_connected_components(graph: GraphType) -> List[List[Node[NodeType]]]:
        """
        Computes Strongly Connected Components (SCC) using Kosaraju's Algorithm.
        """
        if not isinstance(graph, Graph): raise TypeError("Expected a Graph instance.")

        # TODO: Implement Kosaraju's Algorithm (Requires reversing the graph).
        raise NotImplementedError("compute_strongly_connected_components is not implemented yet!")


class GraphTopological:
    """Provides topological sorting and ranking for directed acyclic graphs (DAGs)."""

    @staticmethod
    def get_sort(graph):
        if not isinstance(graph, Graph):
            raise TypeError("Expected a Graph instance.")

        in_degree = {}
        q = deque()
        result = []

        for node in graph:
            in_degree[node] = graph.get_in_degree(node)

        for node in graph:
            if in_degree[node] == 0:
                q.append(node)

        while q:
            current_node = q.popleft()
            result.append(current_node)

            for arc in graph.get_outgoing_arcs(current_node):
                neighbor = arc.target
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    q.append(neighbor)
                
        if len(result) != len(graph):
                raise RuntimeError("Graph has a cycle.")

        return result

    @staticmethod
    def get_ranks(graph: GraphType) -> Dict[Node[NodeType], int]:
    
        if not isinstance(graph, Graph):
            raise TypeError("Expected a Graph instance.")
    
        rank = {}
        q = deque()
        in_degree = {}

        # get indegree for every node
        for node in graph:
            in_degree[node] = graph.get_in_degree(node)

        # get rank zero
        for node in graph:
            if in_degree[node] == 0:
                q.append(node)
                rank[node] = 0

        # kahn
        while q:
            current_node = q.popleft()

            for arc in graph.get_outgoing_arcs(current_node):
                neighbor = arc.target
                in_degree[neighbor] -= 1 # substract current node indegree

                if neighbor not in rank:
                    rank[neighbor] = rank[current_node] + 1

                else:
                    rank[neighbor] = max(rank[current_node], rank[neighbor] +1)

                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        
        # Detección de ciclo
        if len(rank) != len(graph):
            raise RuntimeError("Graph has a cycle.")

        return rank