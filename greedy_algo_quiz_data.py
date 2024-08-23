greedy_algo_questions = [
    {
        "question": "What is the main characteristic of a greedy algorithm?",
        "choices": ["Always finds the global optimum", "Makes locally optimal choices at each step", "Uses dynamic programming", "Requires backtracking"],
        "correct_answer": "Makes locally optimal choices at each step",
        "explanation": "The main characteristic of a greedy algorithm is that it makes locally optimal choices at each step, hoping to find a global optimum. It makes the best immediate, or local, solution without considering the overall problem."
    },
    {
        "question": "Which of the following problems can be solved optimally using a greedy algorithm?",
        "choices": ["Traveling Salesman Problem", "0/1 Knapsack Problem", "Activity Selection Problem", "Longest Common Subsequence"],
        "correct_answer": "Activity Selection Problem",
        "explanation": "The Activity Selection Problem can be solved optimally using a greedy algorithm. By selecting activities that finish earliest, we can maximize the number of non-overlapping activities."
    },
    {
        "question": "What is the time complexity of Kruskal's algorithm for finding a minimum spanning tree?",
        "choices": ["O(V)", "O(E)", "O(E log V)", "O(V^2)"],
        "correct_answer": "O(E log V)",
        "explanation": "Kruskal's algorithm has a time complexity of O(E log V), where E is the number of edges and V is the number of vertices. The log V factor comes from the sorting of edges or the use of a disjoint-set data structure."
    },
    {
        "question": "Which data structure is commonly used in Kruskal's algorithm for efficient implementation?",
        "choices": ["Stack", "Queue", "Heap", "Disjoint Set (Union-Find)"],
        "correct_answer": "Disjoint Set (Union-Find)",
        "explanation": "Kruskal's algorithm commonly uses a Disjoint Set (Union-Find) data structure for efficient implementation. This allows for quick checking of whether adding an edge would create a cycle in the growing spanning tree."
    },
    {
        "question": "What is the main difference between Prim's and Kruskal's algorithms for minimum spanning trees?",
        "choices": ["Time complexity", "Space complexity", "Optimality", "Growth strategy"],
        "correct_answer": "Growth strategy",
        "explanation": "The main difference between Prim's and Kruskal's algorithms is their growth strategy. Prim's algorithm grows a single tree from a starting vertex, while Kruskal's algorithm builds a forest of trees and combines them."
    },
    {
        "question": "Which greedy algorithm is used for finding the shortest path in a weighted graph?",
        "choices": ["Kruskal's algorithm", "Prim's algorithm", "Dijkstra's algorithm", "Bellman-Ford algorithm"],
        "correct_answer": "Dijkstra's algorithm",
        "explanation": "Dijkstra's algorithm is a greedy algorithm used for finding the shortest path in a weighted graph with non-negative edge weights. It greedily selects the vertex with the smallest tentative distance at each step."
    },
    {
        "question": "What is the time complexity of the standard implementation of Dijkstra's algorithm using an adjacency matrix?",
        "choices": ["O(V)", "O(E)", "O(V^2)", "O(E log V)"],
        "correct_answer": "O(V^2)",
        "explanation": "The standard implementation of Dijkstra's algorithm using an adjacency matrix has a time complexity of O(V^2), where V is the number of vertices. This is due to the linear search for the minimum distance vertex in each iteration."
    },
    {
        "question": "Which of the following is NOT a characteristic of greedy algorithms?",
        "choices": ["Local optimization", "Irrevocable choices", "Polynomial time complexity", "Guaranteed global optimum"],
        "correct_answer": "Guaranteed global optimum",
        "explanation": "Greedy algorithms do not guarantee a global optimum. They make locally optimal choices at each step, which may not always lead to the best overall solution. The other characteristics listed are typical of greedy algorithms."
    },
    {
        "question": "What is the main advantage of greedy algorithms over dynamic programming?",
        "choices": ["Always finds the optimal solution", "Simpler implementation", "Lower time complexity", "Better space efficiency"],
        "correct_answer": "Simpler implementation",
        "explanation": "The main advantage of greedy algorithms over dynamic programming is often their simpler implementation. Greedy algorithms make decisions based on current information without the need to solve and store solutions to subproblems."
    },
    {
        "question": "Which greedy algorithm is used for data compression?",
        "choices": ["Kruskal's algorithm", "Huffman coding", "Dijkstra's algorithm", "Prim's algorithm"],
        "correct_answer": "Huffman coding",
        "explanation": "Huffman coding is a greedy algorithm used for data compression. It assigns variable-length codes to characters based on their frequencies, with more frequent characters getting shorter codes."
    },
    {
        "question": "What is the time complexity of Huffman coding algorithm?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(2^n)"],
        "correct_answer": "O(n log n)",
        "explanation": "The time complexity of Huffman coding algorithm is O(n log n), where n is the number of unique characters. This is due to the sorting of characters by frequency and the use of a priority queue to build the Huffman tree."
    },
    {
        "question": "Which problem does the greedy coin change algorithm solve optimally?",
        "choices": ["Minimizing the number of coins for any denomination set", "Maximizing the value of coins used", "Minimizing the number of coins for canonical denomination sets", "Finding the most valuable coin combination"],
        "correct_answer": "Minimizing the number of coins for canonical denomination sets",
        "explanation": "The greedy coin change algorithm solves optimally the problem of minimizing the number of coins for canonical denomination sets (like US coins). It may not work for arbitrary denomination sets."
    },
    {
        "question": "What is the main idea behind the greedy approach to the Fractional Knapsack problem?",
        "choices": ["Take whole items with highest value", "Take items with lowest weight", "Take items with highest value-to-weight ratio", "Take a fraction of each item"],
        "correct_answer": "Take items with highest value-to-weight ratio",
        "explanation": "The main idea behind the greedy approach to the Fractional Knapsack problem is to take items with the highest value-to-weight ratio. This maximizes the value per unit weight, allowing for optimal solution in the fractional case."
    },
    {
        "question": "Which of the following problems cannot be solved optimally using a greedy approach?",
        "choices": ["Minimum Spanning Tree", "Shortest Path in a weighted graph (non-negative edges)", "0/1 Knapsack Problem", "Huffman Coding"],
        "correct_answer": "0/1 Knapsack Problem",
        "explanation": "The 0/1 Knapsack Problem cannot be solved optimally using a greedy approach. It requires considering all possible combinations of items, which is better suited for dynamic programming or other techniques."
    },
    {
        "question": "What is the time complexity of the greedy algorithm for the Fractional Knapsack problem?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(2^n)"],
        "correct_answer": "O(n log n)",
        "explanation": "The time complexity of the greedy algorithm for the Fractional Knapsack problem is O(n log n), where n is the number of items. This is due to the sorting of items by their value-to-weight ratio."
    },
    {
        "question": "Which greedy algorithm is used for finding the minimum number of platforms required for a railway station?",
        "choices": ["Kruskal's algorithm", "Dijkstra's algorithm", "Activity Selection algorithm", "Interval Scheduling algorithm"],
        "correct_answer": "Interval Scheduling algorithm",
        "explanation": "The Interval Scheduling algorithm, a greedy approach, is used for finding the minimum number of platforms required for a railway station. It involves sorting arrival and departure times and keeping track of overlapping intervals."
    },
    {
        "question": "What is the key idea behind the greedy approach to the Job Sequencing problem with deadlines?",
        "choices": ["Schedule jobs in order of arrival", "Schedule highest profit jobs first", "Schedule shortest jobs first", "Schedule jobs as late as possible within their deadlines"],
        "correct_answer": "Schedule jobs as late as possible within their deadlines",
        "explanation": "The key idea behind the greedy approach to the Job Sequencing problem with deadlines is to schedule jobs as late as possible within their deadlines. This allows for maximizing the number of jobs that can be completed before their deadlines."
    },
    {
        "question": "Which of the following is a limitation of greedy algorithms?",
        "choices": ["High time complexity", "Difficult implementation", "May not always find the optimal solution", "Requires sorting in all cases"],
        "correct_answer": "May not always find the optimal solution",
        "explanation": "A limitation of greedy algorithms is that they may not always find the optimal solution. The locally optimal choices made at each step do not guarantee a globally optimal solution for all problems."
    },
    {
        "question": "What is the time complexity of Prim's algorithm for finding a minimum spanning tree using a binary heap?",
        "choices": ["O(V)", "O(E)", "O(V log V)", "O(E log V)"],
        "correct_answer": "O(E log V)",
        "explanation": "The time complexity of Prim's algorithm for finding a minimum spanning tree using a binary heap is O(E log V), where E is the number of edges and V is the number of vertices. This is due to the heap operations performed for each edge."
    },
    {
        "question": "Which greedy algorithm is used for task scheduling to minimize the total completion time?",
        "choices": ["Longest Processing Time (LPT)", "Shortest Processing Time (SPT)", "Earliest Deadline First (EDF)", "Round Robin (RR)"],
        "correct_answer": "Shortest Processing Time (SPT)",
        "explanation": "The Shortest Processing Time (SPT) algorithm is a greedy approach used for task scheduling to minimize the total completion time. It schedules tasks in order of increasing processing time."
    },
    {
        "question": "What is the main idea behind the greedy approach to the Egyptian Fraction problem?",
        "choices": ["Use the largest possible unit fraction at each step", "Use the smallest possible unit fraction at each step", "Use random unit fractions", "Use only even denominators"],
        "correct_answer": "Use the largest possible unit fraction at each step",
        "explanation": "The main idea behind the greedy approach to the Egyptian Fraction problem is to use the largest possible unit fraction at each step. This ensures that the number of fractions is minimized while representing the given rational number."
    },
    {
        "question": "Which of the following is NOT a typical application of greedy algorithms?",
        "choices": ["Huffman coding", "Dijkstra's shortest path", "Matrix chain multiplication", "Kruskal's minimum spanning tree"],
        "correct_answer": "Matrix chain multiplication",
        "explanation": "Matrix chain multiplication is not a typical application of greedy algorithms. It is usually solved using dynamic programming. The other options (Huffman coding, Dijkstra's shortest path, and Kruskal's minimum spanning tree) are classic applications of greedy algorithms."
    },
    {
        "question": "What is the time complexity of the greedy algorithm for the Activity Selection problem?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(2^n)"],
        "correct_answer": "O(n log n)",
        "explanation": "The time complexity of the greedy algorithm for the Activity Selection problem is O(n log n), where n is the number of activities. This is due to the sorting of activities by their finish times."
    },
    {
        "question": "Which data structure is commonly used in Prim's algorithm for efficient implementation?",
        "choices": ["Stack", "Queue", "Binary Heap", "Hash Table"],
        "correct_answer": "Binary Heap",
        "explanation": "A Binary Heap is commonly used in Prim's algorithm for efficient implementation. It allows for quick extraction of the minimum weight edge and updating of key values, leading to an O(E log V) time complexity."
    },
    {
        "question": "What is the main difference between a greedy algorithm and a dynamic programming approach?",
        "choices": ["Time complexity", "Space complexity", "Optimality guarantee", "Problem-solving strategy"],
        "correct_answer": "Problem-solving strategy",
        "explanation": "The main difference between a greedy algorithm and a dynamic programming approach is their problem-solving strategy. Greedy algorithms make locally optimal choices at each step, while dynamic programming solves and combines solutions to overlapping subproblems."
    },
    {
        "question": "Which of the following problems is solved using Kruskal's algorithm?",
        "choices": ["Shortest path", "Minimum spanning tree", "Maximum flow", "Longest path"],
        "correct_answer": "Minimum spanning tree",
        "explanation": "Kruskal's algorithm is used to solve the Minimum Spanning Tree problem. It builds the spanning tree by adding edges in order of increasing weight, avoiding cycles."
    },
    {
        "question": "What is the key idea behind the greedy approach to the Huffman coding problem?",
        "choices": ["Assign shorter codes to more frequent characters", "Assign longer codes to more frequent characters", "Assign equal-length codes to all characters", "Assign codes randomly"],
        "correct_answer": "Assign shorter codes to more frequent characters",
        "explanation": "The key idea behind the greedy approach to the Huffman coding problem is to assign shorter codes to more frequent characters. This minimizes the overall length of the encoded message."
    },
    {
        "question": "Which of the following is a characteristic of problems that can be solved optimally using greedy algorithms?",
        "choices": ["Overlapping subproblems", "Optimal substructure", "Greedy choice property", "Requires backtracking"],
        "correct_answer": "Greedy choice property",
        "explanation": "The greedy choice property is a characteristic of problems that can be solved optimally using greedy algorithms. It means that a globally optimal solution can be reached by making locally optimal choices."
    },
    {
        "question": "What is the time complexity of Dijkstra's algorithm using a Fibonacci heap?",
        "choices": ["O(V)", "O(E)", "O(V log V)", "O(E + V log V)"],
        "correct_answer": "O(E + V log V)",
        "explanation": "The time complexity of Dijkstra's algorithm using a Fibonacci heap is O(E + V log V), where E is the number of edges and V is the number of vertices. This is an improvement over the binary heap implementation for dense graphs."
    },
    {
        "question": "Which greedy algorithm is used for load balancing in distributed systems?",
        "choices": ["Round Robin", "Least Connection", "Weighted Round Robin", "All of the above"],
        "correct_answer": "All of the above",
        "explanation": "All of the mentioned algorithms (Round Robin, Least Connection, and Weighted Round Robin) are greedy approaches used for load balancing in distributed systems. They make locally optimal decisions to distribute incoming requests or tasks."
    },
    {
        "question": "What is the main idea behind the greedy approach to the Coin Change problem (when it works optimally)?",
        "choices": ["Use the largest denomination first", "Use the smallest denomination first", "Use random denominations", "Use only even-valued coins"],
        "correct_answer": "Use the largest denomination first",
        "explanation": "The main idea behind the greedy approach to the Coin Change problem (when it works optimally) is to use the largest denomination first. This minimizes the number of coins used, but only works for certain denomination systems (like US coins)."
    },
    {
        "question": "Which of the following is NOT a typical use case for greedy algorithms?",
        "choices": ["Huffman coding", "Dijkstra's shortest path", "Traveling Salesman Problem", "Activity Selection"],
        "correct_answer": "Traveling Salesman Problem",
        "explanation": "The Traveling Salesman Problem is not typically solved using greedy algorithms as they don't guarantee an optimal solution for this NP-hard problem. The other options are classic applications of greedy algorithms."
    },
    {
        "question": "What is the time complexity of the greedy algorithm for the Fractional Knapsack problem?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(2^n)"],
        "correct_answer": "O(n log n)",
        "explanation": "The time complexity of the greedy algorithm for the Fractional Knapsack problem is O(n log n), where n is the number of items. This is due to the sorting of items by their value-to-weight ratio."
    },
    {
        "question": "Which of the following statements about greedy algorithms is true?",
        "choices": ["They always find the optimal solution", "They never backtrack", "They are always faster than dynamic programming", "They may not work for all optimization problems"],
        "correct_answer": "They may not work for all optimization problems",
        "explanation": "Greedy algorithms may not work for all optimization problems. While they are efficient and simple, they don't guarantee optimal solutions for every problem and may fail in cases where global optimization is required."
    },
    {
        "question": "What is the main advantage of using a greedy algorithm for the Activity Selection problem?",
        "choices": ["It always finds the global optimum", "It has a simple implementation", "It works for any input", "It has constant time complexity"],
        "correct_answer": "It has a simple implementation",
        "explanation": "The main advantage of using a greedy algorithm for the Activity Selection problem is its simple implementation. It makes locally optimal choices by selecting activities that finish earliest, leading to an optimal solution efficiently."
    },
    {
        "question": "In the context of Huffman coding, what does a leaf node in the Huffman tree represent?",
        "choices": ["A bit", "A character", "A frequency", "A code"],
        "correct_answer": "A character",
        "explanation": "In Huffman coding, a leaf node in the Huffman tree represents a character from the input alphabet. The path from the root to this leaf node determines the binary code for that character."
    },
    {
        "question": "Which of the following is a key step in Kruskal's algorithm?",
        "choices": ["Sorting edges by weight", "Using a priority queue", "Performing DFS", "Relaxing edges"],
        "correct_answer": "Sorting edges by weight",
        "explanation": "A key step in Kruskal's algorithm is sorting edges by weight in non-decreasing order. This allows the algorithm to consider edges from lowest to highest weight when building the minimum spanning tree."
    }
]