tree_quiz = [
    {
        "question": "What is the maximum number of children a node can have in a binary tree?",
        "options": ["1", "2", "3", "Unlimited"],
        "correct_answer": "2",
        "explanation": "In a binary tree, each node can have at most two children. This is the defining characteristic of a binary tree, which distinguishes it from other types of trees that may have more than two children per node."
    },
    {
        "question": "Which traversal visits the root node first?",
        "options": ["In-order", "Pre-order", "Post-order", "Level-order"],
        "correct_answer": "Pre-order",
        "explanation": "Pre-order traversal visits the root node first, then the left subtree, and finally the right subtree. The order is: root, left, right. This is in contrast to in-order (left, root, right) and post-order (left, right, root) traversals."
    },
    {
        "question": "What is the time complexity of inserting a node into a binary search tree in the worst case?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
        "correct_answer": "O(n)",
        "explanation": "In the worst case, when the binary search tree is completely unbalanced (essentially a linked list), inserting a node takes O(n) time. This occurs when elements are inserted in sorted order, creating a skewed tree."
    },
    {
        "question": "Which data structure is commonly used to implement a level-order traversal?",
        "options": ["Stack", "Queue", "Linked List", "Array"],
        "correct_answer": "Queue",
        "explanation": "A queue is commonly used to implement level-order traversal (also known as breadth-first traversal). The queue helps in processing nodes level by level, ensuring that nodes at each level are visited before moving to the next level."
    },
    {
        "question": "What is the height of a complete binary tree with n nodes?",
        "options": ["log n", "n", "n/2", "2^n"],
        "correct_answer": "log n",
        "explanation": "The height of a complete binary tree with n nodes is logarithmic, specifically floor(log2(n)). This is because a complete binary tree is balanced, with all levels fully filled except possibly the last level."
    },
    {
        "question": "In a binary search tree, where is the smallest element located?",
        "options": ["Root node", "Leftmost node", "Rightmost node", "Random location"],
        "correct_answer": "Leftmost node",
        "explanation": "In a binary search tree, the smallest element is always located at the leftmost node. This is because, in a BST, all elements in the left subtree are smaller than the root, and this property recursively applies to all subtrees."
    },
    {
        "question": "What is a full binary tree?",
        "options": ["A tree where every node has 0 or 2 children", "A tree where every level is completely filled", "A tree with the maximum number of nodes", "A tree with only leaf nodes"],
        "correct_answer": "A tree where every node has 0 or 2 children",
        "explanation": "A full binary tree is a tree where every node has either 0 children (leaf nodes) or 2 children. There are no nodes with only one child in a full binary tree."
    },
    {
        "question": "Which tree traversal would visit the nodes in sorted order for a binary search tree?",
        "options": ["Pre-order", "In-order", "Post-order", "Level-order"],
        "correct_answer": "In-order",
        "explanation": "In-order traversal of a binary search tree visits the nodes in sorted order. This is because in-order traversal follows the pattern: left subtree, root, right subtree, which aligns with the BST property where left < root < right."
    },
    {
        "question": "What is the time complexity of searching for an element in a balanced binary search tree?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
        "correct_answer": "O(log n)",
        "explanation": "Searching in a balanced binary search tree takes O(log n) time. In each step, the search space is halved, leading to a logarithmic time complexity. This is why balanced BSTs are efficient for search operations."
    },
    {
        "question": "Which of the following is NOT a type of balanced binary search tree?",
        "options": ["AVL tree", "Red-Black tree", "B-tree", "Linked tree"],
        "correct_answer": "Linked tree",
        "explanation": "A 'Linked tree' is not a type of balanced binary search tree. AVL trees, Red-Black trees, and B-trees are all self-balancing data structures, while 'Linked tree' is not a standard term in tree data structures."
    },
    {
        "question": "What is the maximum number of nodes in a binary tree of height h?",
        "options": ["2^h", "2^(h+1) - 1", "h^2", "2h"],
        "correct_answer": "2^(h+1) - 1",
        "explanation": "The maximum number of nodes in a binary tree of height h is 2^(h+1) - 1. This occurs when the tree is a perfect binary tree, where all internal nodes have two children and all leaves are at the same level."
    },
    {
        "question": "Which tree traversal is commonly used to evaluate postfix expressions?",
        "options": ["In-order", "Pre-order", "Post-order", "Level-order"],
        "correct_answer": "Post-order",
        "explanation": "Post-order traversal is commonly used to evaluate postfix expressions. In postfix notation, operators appear after their operands, which aligns with post-order traversal where children are visited before the parent node."
    },
    {
        "question": "What is the time complexity of deleting a node from a binary search tree in the average case?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
        "correct_answer": "O(log n)",
        "explanation": "In the average case, deleting a node from a binary search tree takes O(log n) time. This assumes the tree is relatively balanced. The operation involves searching for the node (O(log n)) and then restructuring the tree, which is typically O(log n) in the average case."
    },
    {
        "question": "In a max heap, what is true about the root node?",
        "options": ["It's the smallest element", "It's the largest element", "It's always a leaf node", "It has no children"],
        "correct_answer": "It's the largest element",
        "explanation": "In a max heap, the root node is always the largest element. This is the defining property of a max heap, where each parent node is greater than or equal to its children."
    },
    {
        "question": "What is the space complexity of a binary tree with n nodes?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
        "correct_answer": "O(n)",
        "explanation": "The space complexity of a binary tree with n nodes is O(n). Each node in the tree occupies a constant amount of space, and there are n nodes in total, leading to linear space complexity."
    }
]