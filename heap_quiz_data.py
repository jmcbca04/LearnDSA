heap_quiz = [
    {
        "question": "What is the time complexity of inserting an element into a binary heap?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
        "correct_answer": "O(log n)",
        "explanation": "Inserting an element into a binary heap takes O(log n) time. After adding the element to the end, we perform the 'bubble up' operation, which in the worst case moves the element to the root, traversing the height of the heap, which is log n."
    },
    {
        "question": "Which of the following is NOT a property of a max heap?",
        "options": ["The root is the maximum element", "Every node is greater than its children", "The tree is balanced", "The tree is complete"],
        "correct_answer": "Every node is greater than its children",
        "explanation": "In a max heap, every node is greater than or equal to its children, not strictly greater. The root is the maximum element, the tree is balanced and complete, but a parent can be equal to its children."
    },
    {
        "question": "What is the time complexity of extracting the maximum element from a max heap?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
        "correct_answer": "O(log n)",
        "explanation": "Extracting the maximum element (root) from a max heap takes O(log n) time. We remove the root, replace it with the last element, and then 'bubble down' this element, which takes at most the height of the heap, log n."
    },
    {
        "question": "In a binary heap implemented as an array, where is the parent of the element at index i located?",
        "options": ["(i-1)/2", "i/2", "2i", "2i+1"],
        "correct_answer": "(i-1)/2",
        "explanation": "In a binary heap implemented as an array, the parent of an element at index i is located at index (i-1)/2 (integer division). This formula is derived from the relationship between parent and child indices in a complete binary tree."
    },
    {
        "question": "What is the space complexity of a binary heap with n elements?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
        "correct_answer": "O(n)",
        "explanation": "The space complexity of a binary heap with n elements is O(n). A heap is typically implemented as an array, and it requires space proportional to the number of elements it contains."
    },
    {
        "question": "Which of the following operations is typically faster in a heap compared to a sorted array?",
        "options": ["Finding the minimum element", "Finding the maximum element", "Inserting a new element", "Deleting an arbitrary element"],
        "correct_answer": "Inserting a new element",
        "explanation": "Inserting a new element is typically faster in a heap (O(log n)) compared to a sorted array (O(n)). In a heap, we add the element at the end and bubble up, while in a sorted array, we need to find the correct position and shift elements."
    },
    {
        "question": "What is the primary advantage of using a heap over a sorted array for implementing a priority queue?",
        "options": ["Faster access to all elements", "Lower memory usage", "Faster insertion of new elements", "Easier implementation"],
        "correct_answer": "Faster insertion of new elements",
        "explanation": "The primary advantage of using a heap over a sorted array for a priority queue is faster insertion of new elements. Heap insertion is O(log n), while inserting into a sorted array to maintain order is O(n)."
    },
    {
        "question": "In a min heap, what is true about the root node?",
        "options": ["It's the largest element", "It's the smallest element", "It's always a leaf node", "It has no children"],
        "correct_answer": "It's the smallest element",
        "explanation": "In a min heap, the root node is always the smallest element. This is the defining property of a min heap, where each parent node is smaller than or equal to its children."
    },
    {
        "question": "What is the time complexity of building a heap from an unsorted array?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
        "correct_answer": "O(n)",
        "explanation": "Building a heap from an unsorted array can be done in O(n) time. This is achieved by starting from the last non-leaf node and performing 'bubble down' operations. While it might seem like O(n log n), a more detailed analysis shows it's actually O(n)."
    },
    {
        "question": "Which of the following algorithms typically uses a heap as its core data structure?",
        "options": ["Quicksort", "Mergesort", "Heapsort", "Insertion sort"],
        "correct_answer": "Heapsort",
        "explanation": "Heapsort typically uses a heap as its core data structure. It works by building a max heap from the input array and then repeatedly extracting the maximum element to sort the array in ascending order."
    },
    {
        "question": "What is the maximum number of elements in a binary heap of height h?",
        "options": ["2^h", "2^(h+1) - 1", "h^2", "2h"],
        "correct_answer": "2^(h+1) - 1",
        "explanation": "The maximum number of elements in a binary heap of height h is 2^(h+1) - 1. This is because a binary heap is a complete binary tree, and this formula represents the maximum number of nodes in a complete binary tree of height h."
    },
    {
        "question": "Which of the following is NOT an application of heaps?",
        "options": ["Priority queues", "Sorting algorithms", "Graph algorithms (e.g., Dijkstra's)", "Balanced search trees"],
        "correct_answer": "Balanced search trees",
        "explanation": "Balanced search trees are not an application of heaps. While heaps are used in priority queues, sorting algorithms (heapsort), and some graph algorithms (like Dijkstra's), balanced search trees (like AVL or Red-Black trees) are a separate data structure with different properties and use cases."
    },
    {
        "question": "In a binary heap implemented as an array, where are the children of the element at index i located?",
        "options": ["2i and 2i+1", "i/2 and i/2+1", "i-1 and i+1", "2i-1 and 2i"],
        "correct_answer": "2i+1 and 2i+2",
        "explanation": "In a binary heap implemented as an array (with 0-based indexing), the children of the element at index i are located at indices 2i+1 and 2i+2. This formula maintains the complete binary tree structure in the array representation."
    },
    {
        "question": "What is the time complexity of decreasing the key of an element in a binary min-heap?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
        "correct_answer": "O(log n)",
        "explanation": "Decreasing the key of an element in a binary min-heap takes O(log n) time. After decreasing the key, we need to 'bubble up' the element to maintain the heap property, which in the worst case traverses the height of the heap, which is log n."
    },
    {
        "question": "Which of the following is true about a complete binary tree?",
        "options": ["All levels are fully filled", "The last level is fully filled or filled from left to right", "It has the maximum possible number of nodes", "It is always balanced"],
        "correct_answer": "The last level is fully filled or filled from left to right",
        "explanation": "In a complete binary tree, all levels are fully filled except possibly the last level, which is filled from left to right. This property allows for efficient array representation and is crucial for the implementation of binary heaps."
    }
]