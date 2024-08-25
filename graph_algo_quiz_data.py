graph_algo_questions = [
    {
        "question": "What is the time complexity of Breadth-First Search (BFS) on a graph with V vertices and E edges?",
        "options": ["O(V)", "O(E)", "O(V + E)", "O(V * E)"],
        "correct_answer": "O(V + E)",
        "explanation": "The time complexity of BFS is O(V + E). This is because BFS visits each vertex once (O(V)) and explores every edge once (O(E))."
    },
    {
        "question": "Which data structure is typically used to implement Breadth-First Search?",
        "options": ["Stack", "Queue", "Priority Queue", "Linked List"],
        "correct_answer": "Queue",
        "explanation": "A queue is typically used to implement Breadth-First Search. It helps maintain the order of vertices to be explored, ensuring that vertices are visited level by level."
    },
    {
        "question": "What is the time complexity of Depth-First Search (DFS) on a graph with V vertices and E edges?",
        "options": ["O(V)", "O(E)", "O(V + E)", "O(V * E)"],
        "correct_answer": "O(V + E)",
        "explanation": "The time complexity of DFS is O(V + E). Similar to BFS, DFS visits each vertex once and explores each edge once."
    },
    {
        "question": "Which data structure is typically used to implement Depth-First Search?",
        "options": ["Stack", "Queue", "Priority Queue", "Linked List"],
        "correct_answer": "Stack",
        "explanation": "A stack is typically used to implement Depth-First Search. It helps maintain the order of vertices to be explored, allowing backtracking when needed."
    },
    {
        "question": "What is the time complexity of Dijkstra's algorithm using a binary heap?",
        "options": ["O(V)", "O(E log V)", "O(V^2)", "O(E + V log V)"],
        "correct_answer": "O(E + V log V)",
        "explanation": "The time complexity of Dijkstra's algorithm using a binary heap is O(E + V log V). Each vertex is extracted from the heap once (O(V log V)), and each edge is examined once to update distances (O(E log V))."
    },
    {
        "question": "What is the main limitation of Dijkstra's algorithm?",
        "options": ["It doesn't work on directed graphs", "It can't handle negative edge weights", "It only works on trees", "It has high space complexity"],
        "correct_answer": "It can't handle negative edge weights",
        "explanation": "The main limitation of Dijkstra's algorithm is that it can't handle negative edge weights. The presence of negative edges can lead to incorrect results."
    },
    {
        "question": "Which algorithm is used to find the minimum spanning tree of a weighted, undirected graph?",
        "options": ["Dijkstra's algorithm", "Bellman-Ford algorithm", "Kruskal's algorithm", "Floyd-Warshall algorithm"],
        "correct_answer": "Kruskal's algorithm",
        "explanation": "Kruskal's algorithm is used to find the minimum spanning tree of a weighted, undirected graph. It works by sorting edges by weight and adding them to the tree if they don't create a cycle."
    },
    {
        "question": "What is the time complexity of Kruskal's algorithm?",
        "options": ["O(V)", "O(E log E)", "O(V^2)", "O(E + V log V)"],
        "correct_answer": "O(E log E)",
        "explanation": "The time complexity of Kruskal's algorithm is O(E log E), where E is the number of edges. This is due to the sorting of edges, which is the most time-consuming part of the algorithm."
    },
    {
        "question": "Which algorithm can detect negative cycles in a graph?",
        "options": ["Dijkstra's algorithm", "Bellman-Ford algorithm", "Kruskal's algorithm", "Prim's algorithm"],
        "correct_answer": "Bellman-Ford algorithm",
        "explanation": "The Bellman-Ford algorithm can detect negative cycles in a graph. It relaxes all edges V-1 times (where V is the number of vertices) and then checks if further relaxation is possible, indicating a negative cycle."
    },
    {
        "question": "What is the time complexity of the Bellman-Ford algorithm?",
        "options": ["O(V)", "O(E log V)", "O(V * E)", "O(V^2)"],
        "correct_answer": "O(V * E)",
        "explanation": "The time complexity of the Bellman-Ford algorithm is O(V * E), where V is the number of vertices and E is the number of edges. It relaxes all edges V-1 times."
    },
    {
        "question": "Which algorithm is used to find the shortest path between all pairs of vertices in a graph?",
        "options": ["Dijkstra's algorithm", "Bellman-Ford algorithm", "Floyd-Warshall algorithm", "A* search algorithm"],
        "correct_answer": "Floyd-Warshall algorithm",
        "explanation": "The Floyd-Warshall algorithm is used to find the shortest path between all pairs of vertices in a graph. It works by considering all vertices as intermediate vertices."
    },
    {
        "question": "What is the time complexity of the Floyd-Warshall algorithm?",
        "options": ["O(V^2)", "O(V^3)", "O(E log V)", "O(V * E)"],
        "correct_answer": "O(V^3)",
        "explanation": "The time complexity of the Floyd-Warshall algorithm is O(V^3), where V is the number of vertices. It uses three nested loops to consider all possible intermediate vertices for each pair of vertices."
    },
    {
        "question": "Which algorithm is used to find strongly connected components in a directed graph?",
        "options": ["Tarjan's algorithm", "Kruskal's algorithm", "Prim's algorithm", "A* search algorithm"],
        "correct_answer": "Tarjan's algorithm",
        "explanation": "Tarjan's algorithm is used to find strongly connected components in a directed graph. It performs a single depth-first search to identify strongly connected components."
    },
    {
        "question": "What is the time complexity of Tarjan's algorithm for finding strongly connected components?",
        "options": ["O(V)", "O(E)", "O(V + E)", "O(V * E)"],
        "correct_answer": "O(V + E)",
        "explanation": "The time complexity of Tarjan's algorithm for finding strongly connected components is O(V + E), where V is the number of vertices and E is the number of edges. It performs a single depth-first search of the graph."
    },
    {
        "question": "Which algorithm is used to find the maximum flow in a flow network?",
        "options": ["Dijkstra's algorithm", "Ford-Fulkerson algorithm", "Kruskal's algorithm", "A* search algorithm"],
        "correct_answer": "Ford-Fulkerson algorithm",
        "explanation": "The Ford-Fulkerson algorithm is used to find the maximum flow in a flow network. It works by repeatedly finding augmenting paths from source to sink and increasing the flow along these paths."
    },
    {
        "question": "What is the time complexity of the Ford-Fulkerson algorithm?",
        "options": ["O(V * E)", "O(E * max_flow)", "O(V^2 * E)", "O(V * E^2)"],
        "correct_answer": "O(E * max_flow)",
        "explanation": "The time complexity of the Ford-Fulkerson algorithm is O(E * max_flow), where E is the number of edges and max_flow is the maximum flow in the network. This is because each augmenting path can increase the flow by at least 1."
    },
    {
        "question": "Which algorithm is used to find a maximum matching in a bipartite graph?",
        "options": ["Kruskal's algorithm", "Prim's algorithm", "Hungarian algorithm", "A* search algorithm"],
        "correct_answer": "Hungarian algorithm",
        "explanation": "The Hungarian algorithm (also known as the Munkres algorithm) is used to find a maximum matching in a bipartite graph. It works by finding an augmenting path in each iteration."
    },
    {
        "question": "What is the time complexity of the Hungarian algorithm?",
        "options": ["O(V^2)", "O(V^3)", "O(V^4)", "O(V * E)"],
        "correct_answer": "O(V^3)",
        "explanation": "The time complexity of the Hungarian algorithm is O(V^3), where V is the number of vertices. This is because it may need to find up to V augmenting paths, each taking O(V^2) time."
    },
    {
        "question": "Which algorithm is used to find the shortest path in a graph with negative edge weights?",
        "options": ["Dijkstra's algorithm", "Bellman-Ford algorithm", "A* search algorithm", "Floyd-Warshall algorithm"],
        "correct_answer": "Bellman-Ford algorithm",
        "explanation": "The Bellman-Ford algorithm is used to find the shortest path in a graph with negative edge weights. It can handle negative edges as long as there are no negative cycles."
    },
    {
        "question": "What is the main advantage of the A* search algorithm over Dijkstra's algorithm?",
        "options": ["Lower time complexity", "Can handle negative edges", "More memory efficient", "Uses heuristics for better performance"],
        "correct_answer": "Uses heuristics for better performance",
        "explanation": "The main advantage of the A* search algorithm over Dijkstra's algorithm is that it uses heuristics for better performance. This allows it to find the shortest path more quickly in many cases by guiding the search towards the goal."
    },
    {
        "question": "Which algorithm is used to find a topological ordering of a directed acyclic graph (DAG)?",
        "options": ["Depth-First Search", "Breadth-First Search", "Kahn's algorithm", "Prim's algorithm"],
        "correct_answer": "Kahn's algorithm",
        "explanation": "Kahn's algorithm is used to find a topological ordering of a directed acyclic graph (DAG). It works by repeatedly removing nodes with no incoming edges and adding them to the result."
    },
    {
        "question": "What is the time complexity of Kahn's algorithm for topological sorting?",
        "options": ["O(V)", "O(E)", "O(V + E)", "O(V * E)"],
        "correct_answer": "O(V + E)",
        "explanation": "The time complexity of Kahn's algorithm for topological sorting is O(V + E), where V is the number of vertices and E is the number of edges. It processes each vertex and edge once."
    },
    {
        "question": "Which algorithm is used to find the lowest common ancestor (LCA) of two nodes in a tree?",
        "options": ["Depth-First Search", "Breadth-First Search", "Tarjan's off-line algorithm", "Floyd-Warshall algorithm"],
        "correct_answer": "Tarjan's off-line algorithm",
        "explanation": "Tarjan's off-line algorithm is used to find the lowest common ancestor (LCA) of two nodes in a tree. It can find LCAs for multiple pairs of nodes in a single traversal of the tree."
    },
    {
        "question": "What is the time complexity of Tarjan's off-line algorithm for finding LCAs?",
        "options": ["O(V)", "O(E)", "O(V + E)", "O(V * E)"],
        "correct_answer": "O(V + E)",
        "explanation": "The time complexity of Tarjan's off-line algorithm for finding LCAs is O(V + E), where V is the number of vertices and E is the number of edges. It performs a single depth-first search of the tree."
    },
    {
        "question": "Which algorithm is used to find the maximum flow in a flow network with multiple sources and sinks?",
        "options": ["Ford-Fulkerson algorithm", "Edmonds-Karp algorithm", "Dinic's algorithm", "Push-relabel algorithm"],
        "correct_answer": "Push-relabel algorithm",
        "explanation": "The Push-relabel algorithm is used to find the maximum flow in a flow network with multiple sources and sinks. It maintains a preflow and gradually converts it to a maximum flow by moving excess flow from vertices."
    },
    {
        "question": "What is the time complexity of the Push-relabel algorithm for maximum flow?",
        "options": ["O(V^2 * E)", "O(V^3)", "O(V * E * log(V))", "O(V * E^2)"],
        "correct_answer": "O(V^2 * E)",
        "explanation": "The time complexity of the Push-relabel algorithm for maximum flow is O(V^2 * E), where V is the number of vertices and E is the number of edges. This is for the basic implementation; more efficient variants exist."
    },
    {
        "question": "Which algorithm is used to find the minimum cut in a flow network?",
        "options": ["Dijkstra's algorithm", "Ford-Fulkerson algorithm", "Karger's algorithm", "Prim's algorithm"],
        "correct_answer": "Ford-Fulkerson algorithm",
        "explanation": "The Ford-Fulkerson algorithm can be used to find the minimum cut in a flow network. After finding the maximum flow, the minimum cut is determined by the set of vertices reachable from the source in the residual graph."
    },
    {
        "question": "What is the relationship between the maximum flow and the minimum cut in a flow network?",
        "options": ["They are always equal", "Maximum flow is always greater", "Minimum cut is always greater", "They are unrelated"],
        "correct_answer": "They are always equal",
        "explanation": "The maximum flow and minimum cut in a flow network are always equal. This is known as the max-flow min-cut theorem, which states that the maximum flow through a network is equal to the capacity of the minimum cut."
    },
    {
        "question": "Which algorithm is used to find the shortest path in a graph where edge weights represent probabilities?",
        "options": ["Dijkstra's algorithm", "Bellman-Ford algorithm", "Floyd-Warshall algorithm", "Viterbi algorithm"],
        "correct_answer": "Viterbi algorithm",
        "explanation": "The Viterbi algorithm is used to find the shortest path in a graph where edge weights represent probabilities. It is commonly used in hidden Markov models and communication systems."
    },
    {
        "question": "What is the time complexity of the Viterbi algorithm?",
        "options": ["O(V)", "O(E)", "O(V * E)", "O(V^2)"],
        "correct_answer": "O(V * E)",
        "explanation": "The time complexity of the Viterbi algorithm is O(V * E), where V is the number of vertices (states) and E is the number of edges (transitions). It processes each state and transition once."
    },
    {
        "question": "Which algorithm is used to find the maximum matching in a general graph?",
        "options": ["Hungarian algorithm", "Hopcroft-Karp algorithm", "Edmonds' Blossom algorithm", "Ford-Fulkerson algorithm"],
        "correct_answer": "Edmonds' Blossom algorithm",
        "explanation": "Edmonds' Blossom algorithm is used to find the maximum matching in a general graph. It can handle non-bipartite graphs by contracting odd-length cycles (blossoms) into single vertices."
    },
    {
        "question": "What is the time complexity of Edmonds' Blossom algorithm?",
        "options": ["O(V^2)", "O(V^3)", "O(V^4)", "O(V * E)"],
        "correct_answer": "O(V^4)",
        "explanation": "The time complexity of Edmonds' Blossom algorithm is O(V^4), where V is the number of vertices. This is for the basic implementation; more efficient variants exist with O(V^3) complexity."
    },
    {
        "question": "Which algorithm is used to find the strongly connected components in a directed graph in linear time?",
        "options": ["Kosaraju's algorithm", "Tarjan's algorithm", "Floyd-Warshall algorithm", "Prim's algorithm"],
        "correct_answer": "Kosaraju's algorithm",
        "explanation": "Kosaraju's algorithm is used to find the strongly connected components in a directed graph in linear time. It performs two depth-first searches: one on the original graph and one on the transposed graph."
    },
    {
        "question": "What is the time complexity of Kosaraju's algorithm?",
        "options": ["O(V)", "O(E)", "O(V + E)", "O(V * E)"],
        "correct_answer": "O(V + E)",
        "explanation": "The time complexity of Kosaraju's algorithm is O(V + E), where V is the number of vertices and E is the number of edges. It performs two depth-first searches, each taking O(V + E) time."
    },
    {
        "question": "Which algorithm is used to find the minimum spanning tree of a graph when edge weights are integers?",
        "options": ["Kruskal's algorithm", "Prim's algorithm", "Borůvka's algorithm", "Reverse-delete algorithm"],
        "correct_answer": "Borůvka's algorithm",
        "explanation": "Borůvka's algorithm is particularly efficient for finding the minimum spanning tree of a graph when edge weights are integers. It works by repeatedly adding the cheapest edge that connects a component to another component."
    },
    {
        "question": "What is the time complexity of Borůvka's algorithm?",
        "options": ["O(E log V)", "O(E log E)", "O(V^2)", "O(E log log V)"],
        "correct_answer": "O(E log log V)",
        "explanation": "The time complexity of Borůvka's algorithm is O(E log log V) when using a fast disjoint-set data structure, where V is the number of vertices and E is the number of edges."
    },
    {
        "question": "Which algorithm is used to find the maximum flow in a flow network with unit capacities?",
        "options": ["Ford-Fulkerson algorithm", "Edmonds-Karp algorithm", "Dinic's algorithm", "Hopcroft-Karp algorithm"],
        "correct_answer": "Hopcroft-Karp algorithm",
        "explanation": "The Hopcroft-Karp algorithm is used to find the maximum flow in a flow network with unit capacities. It's particularly efficient for bipartite matching problems."
    },
    {
        "question": "What is the time complexity of the Hopcroft-Karp algorithm?",
        "options": ["O(V^2)", "O(E sqrt(V))", "O(V * E)", "O(V^3)"],
        "correct_answer": "O(E sqrt(V))",
        "explanation": "The time complexity of the Hopcroft-Karp algorithm is O(E sqrt(V)), where V is the number of vertices and E is the number of edges. This makes it more efficient than the Ford-Fulkerson algorithm for sparse graphs."
    },
    {
        "question": "Which algorithm is used to find the shortest path in a graph with non-negative edge weights?",
        "options": ["Bellman-Ford algorithm", "Floyd-Warshall algorithm", "Dijkstra's algorithm", "A* search algorithm"],
        "correct_answer": "Dijkstra's algorithm",
        "explanation": "Dijkstra's algorithm is used to find the shortest path in a graph with non-negative edge weights. It works by greedily selecting the vertex with the smallest tentative distance."
    },
    {
        "question": "What is the time complexity of Dijkstra's algorithm using a binary heap?",
        "options": ["O(V^2)", "O(E log V)", "O(V + E)", "O(V * E)"],
        "correct_answer": "O(E log V)",
        "explanation": "The time complexity of Dijkstra's algorithm using a binary heap is O(E log V), where V is the number of vertices and E is the number of edges. This is because each edge relaxation takes O(log V) time."
    },
    {
        "question": "Which algorithm is used to find the articulation points (cut vertices) in a graph?",
        "options": ["Depth-First Search", "Breadth-First Search", "Tarjan's algorithm", "Kruskal's algorithm"],
        "correct_answer": "Tarjan's algorithm",
        "explanation": "Tarjan's algorithm is used to find the articulation points (cut vertices) in a graph. It performs a single depth-first search and uses low-link values to identify articulation points."
    },
    {
        "question": "What is the time complexity of Tarjan's algorithm for finding articulation points?",
        "options": ["O(V)", "O(E)", "O(V + E)", "O(V * E)"],
        "correct_answer": "O(V + E)",
        "explanation": "The time complexity of Tarjan's algorithm for finding articulation points is O(V + E), where V is the number of vertices and E is the number of edges. It performs a single depth-first search of the graph."
    },
    {
        "question": "Which algorithm is used to find the bridges in a graph?",
        "options": ["Depth-First Search", "Breadth-First Search", "Tarjan's algorithm", "Kruskal's algorithm"],
        "correct_answer": "Tarjan's algorithm",
        "explanation": "Tarjan's algorithm can also be used to find the bridges in a graph. Similar to finding articulation points, it uses a single depth-first search and low-link values to identify bridges."
    },
    {
        "question": "What is the difference between an articulation point and a bridge in a graph?",
        "options": ["They are the same", "Articulation point is a vertex, bridge is an edge", "Articulation point is an edge, bridge is a vertex", "They are unrelated concepts"],
        "correct_answer": "Articulation point is a vertex, bridge is an edge",
        "explanation": "An articulation point (or cut vertex) is a vertex whose removal increases the number of connected components in the graph. A bridge is an edge whose removal increases the number of connected components."
    },
    {
        "question": "Which algorithm is used to find the shortest path in a weighted graph with negative edge weights but no negative cycles?",
        "options": ["Dijkstra's algorithm", "Bellman-Ford algorithm", "Floyd-Warshall algorithm", "A* search algorithm"],
        "correct_answer": "Bellman-Ford algorithm",
        "explanation": "The Bellman-Ford algorithm is used to find the shortest path in a weighted graph with negative edge weights but no negative cycles. It can handle negative edges, unlike Dijkstra's algorithm."
    },
    {
        "question": "What happens if you run the Bellman-Ford algorithm on a graph with a negative cycle?",
        "options": ["It will crash", "It will return incorrect results", "It will detect the negative cycle", "It will run indefinitely"],
        "correct_answer": "It will detect the negative cycle",
        "explanation": "If the Bellman-Ford algorithm is run on a graph with a negative cycle, it will detect the presence of the negative cycle. This is because the distances will keep decreasing in the cycle after V-1 iterations."
    },
    {
        "question": "Which algorithm is used to find the maximum flow in a flow network in polynomial time?",
        "options": ["Ford-Fulkerson algorithm", "Edmonds-Karp algorithm", "Dinic's algorithm", "All of the above"],
        "correct_answer": "All of the above",
        "explanation": "All of these algorithms (Ford-Fulkerson, Edmonds-Karp, and Dinic's) can find the maximum flow in a flow network in polynomial time. Edmonds-Karp and Dinic's are specific implementations of the Ford-Fulkerson method with guaranteed polynomial time complexity."
    },
    {
        "question": "What is the time complexity of the Edmonds-Karp algorithm?",
        "options": ["O(V * E)", "O(V * E^2)", "O(V^2 * E)", "O(V^3)"],
        "correct_answer": "O(V * E^2)",
        "explanation": "The time complexity of the Edmonds-Karp algorithm is O(V * E^2), where V is the number of vertices and E is the number of edges. This is because it can perform at most O(V * E) augmentations, each taking O(E) time."
    },
    {
        "question": "Which algorithm is used to find all pairs shortest paths in a weighted graph?",
        "options": ["Dijkstra's algorithm", "Bellman-Ford algorithm", "Floyd-Warshall algorithm", "A* search algorithm"],
        "correct_answer": "Floyd-Warshall algorithm",
        "explanation": "The Floyd-Warshall algorithm is used to find all pairs shortest paths in a weighted graph. It works by considering all vertices as intermediate vertices and updates the shortest paths accordingly."
    },
    {
        "question": "What is the space complexity of the Floyd-Warshall algorithm?",
        "options": ["O(V)", "O(E)", "O(V^2)", "O(V^3)"],
        "correct_answer": "O(V^2)",
        "explanation": "The space complexity of the Floyd-Warshall algorithm is O(V^2), where V is the number of vertices. This is because it maintains a distance matrix of size V x V to store the shortest distances between all pairs of vertices."
    }
]