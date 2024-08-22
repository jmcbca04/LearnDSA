graph_quiz = [
    {
        "question": "What is the time complexity of a breadth-first search (BFS) on a graph with V vertices and E edges?",
        "options": ["O(V)", "O(E)", "O(V + E)", "O(V * E)"],
        "correct_answer": "O(V + E)",
        "explanation": "The time complexity of BFS is O(V + E). This is because BFS visits each vertex once (O(V)) and explores every edge once (O(E)). In the worst case, when the graph is fully connected, E can be up to V^2, but the complexity is still expressed as O(V + E)."
    },
    {
        "question": "Which data structure is typically used to implement a breadth-first search?",
        "options": ["Stack", "Queue", "Heap", "Array"],
        "correct_answer": "Queue",
        "explanation": "A queue is typically used to implement breadth-first search. The queue helps maintain the order of vertices to be explored, ensuring that vertices are visited level by level, which is characteristic of BFS."
    },
    {
        "question": "What is a directed acyclic graph (DAG)?",
        "options": ["A graph with no cycles and directed edges", "A graph with cycles and undirected edges", "A graph with no edges", "A graph with only self-loops"],
        "correct_answer": "A graph with no cycles and directed edges",
        "explanation": "A directed acyclic graph (DAG) is a graph that has directed edges and no cycles. This means you can't start at a vertex and follow a sequence of edges that leads back to the same vertex. DAGs are often used to represent dependencies or hierarchical structures."
    },
    {
        "question": "Which algorithm is used to find the shortest path in a weighted graph?",
        "options": ["Depth-First Search", "Breadth-First Search", "Dijkstra's Algorithm", "Binary Search"],
        "correct_answer": "Dijkstra's Algorithm",
        "explanation": "Dijkstra's Algorithm is used to find the shortest path in a weighted graph. It works by iteratively selecting the unvisited vertex with the smallest tentative distance, updating the distances to its neighbors, and marking it as visited."
    },
    {
        "question": "What is the time complexity of Dijkstra's algorithm using a binary heap?",
        "options": ["O(V)", "O(E log V)", "O(V^2)", "O(E + V log V)"],
        "correct_answer": "O(E + V log V)",
        "explanation": "The time complexity of Dijkstra's algorithm using a binary heap is O(E + V log V). Each vertex is extracted from the heap once (O(V log V)), and each edge is examined once to update distances (O(E log V)). Since E can be at most V^2, this simplifies to O(E + V log V)."
    },
    {
        "question": "What is a minimum spanning tree?",
        "options": ["A tree with the least number of edges", "A tree with the maximum total edge weight", "A tree connecting all vertices with minimum total edge weight", "A tree with no cycles"],
        "correct_answer": "A tree connecting all vertices with minimum total edge weight",
        "explanation": "A minimum spanning tree is a subset of edges in a weighted, undirected graph that connects all vertices together with the minimum total edge weight, without creating any cycles. It's a way to find the most efficient way to connect all points in a graph."
    },
    {
        "question": "Which algorithm is used to find strongly connected components in a directed graph?",
        "options": ["Prim's Algorithm", "Kruskal's Algorithm", "Kosaraju's Algorithm", "Floyd-Warshall Algorithm"],
        "correct_answer": "Kosaraju's Algorithm",
        "explanation": "Kosaraju's Algorithm is used to find strongly connected components in a directed graph. It performs two depth-first searches: one on the original graph and one on the transposed graph, allowing it to identify groups of vertices where every vertex is reachable from every other vertex in the group."
    },
    {
        "question": "What is the time complexity of the Floyd-Warshall algorithm for finding all-pairs shortest paths?",
        "options": ["O(V^2)", "O(V^3)", "O(E log V)", "O(V + E)"],
        "correct_answer": "O(V^3)",
        "explanation": "The Floyd-Warshall algorithm has a time complexity of O(V^3). It uses three nested loops to consider all possible intermediate vertices for each pair of vertices, resulting in V^3 operations. This algorithm is efficient for dense graphs and when all-pairs shortest paths are needed."
    },
    {
        "question": "In a graph, what is the degree of a vertex?",
        "options": ["The number of edges connected to it", "The number of vertices in the graph", "The length of the longest path from it", "The number of cycles it's part of"],
        "correct_answer": "The number of edges connected to it",
        "explanation": "The degree of a vertex in a graph is the number of edges connected to it. In a directed graph, we distinguish between in-degree (number of incoming edges) and out-degree (number of outgoing edges)."
    },
    {
        "question": "What is a bipartite graph?",
        "options": ["A graph with exactly two vertices", "A graph whose vertices can be divided into two disjoint sets such that every edge connects vertices in different sets", "A graph with no edges", "A graph with only self-loops"],
        "correct_answer": "A graph whose vertices can be divided into two disjoint sets such that every edge connects vertices in different sets",
        "explanation": "A bipartite graph is a graph whose vertices can be divided into two disjoint sets such that every edge connects a vertex in one set to a vertex in the other set. No edge connects vertices within the same set. Bipartite graphs are useful in many applications, including matching problems."
    },
    {
        "question": "Which algorithm is used to find the maximum flow in a flow network?",
        "options": ["Depth-First Search", "Breadth-First Search", "Ford-Fulkerson Algorithm", "Bellman-Ford Algorithm"],
        "correct_answer": "Ford-Fulkerson Algorithm",
        "explanation": "The Ford-Fulkerson Algorithm is used to find the maximum flow in a flow network. It works by repeatedly finding augmenting paths from source to sink and increasing the flow along these paths until no more augmenting paths can be found."
    },
    {
        "question": "What is the time complexity of topological sorting using DFS?",
        "options": ["O(V)", "O(E)", "O(V + E)", "O(V * E)"],
        "correct_answer": "O(V + E)",
        "explanation": "The time complexity of topological sorting using DFS is O(V + E). This is because the algorithm performs a DFS traversal of the graph, which visits each vertex once and explores each edge once. Topological sorting is only possible on directed acyclic graphs (DAGs)."
    },
    {
        "question": "What is an Eulerian path in a graph?",
        "options": ["A path that visits every vertex exactly once", "A path that visits every edge exactly once", "A path that starts and ends at the same vertex", "A path with minimum total edge weight"],
        "correct_answer": "A path that visits every edge exactly once",
        "explanation": "An Eulerian path in a graph is a path that visits every edge exactly once. If the path starts and ends at the same vertex, it's called an Eulerian circuit. A graph has an Eulerian path if and only if it has at most two vertices with odd degree."
    },
    {
        "question": "Which of the following is NOT a property of a tree?",
        "options": ["Connected", "Acyclic", "Has n-1 edges for n vertices", "Contains cycles"],
        "correct_answer": "Contains cycles",
        "explanation": "Containing cycles is not a property of a tree. Trees are, by definition, connected, acyclic graphs. They have exactly n-1 edges for n vertices, which is the minimum number of edges needed to keep all vertices connected without forming any cycles."
    },
    {
        "question": "What is the chromatic number of a graph?",
        "options": ["The number of vertices in the graph", "The number of edges in the graph", "The minimum number of colors needed to color the vertices such that no two adjacent vertices have the same color", "The maximum degree of any vertex in the graph"],
        "correct_answer": "The minimum number of colors needed to color the vertices such that no two adjacent vertices have the same color",
        "explanation": "The chromatic number of a graph is the minimum number of colors needed to color the vertices such that no two adjacent vertices have the same color. This concept is important in graph theory and has applications in scheduling, register allocation in compilers, and other optimization problems."
    }
]