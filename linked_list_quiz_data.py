linked_list_quiz = [
    {
        "question": "What is the time complexity of accessing an element in a singly linked list?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": "O(n)",
        "explanation": "In a singly linked list, to access an element, we need to traverse the list from the head node until we reach the desired element. This operation takes linear time, O(n), in the worst case when the element is at the end of the list."
    },
    {
        "question": "Which of the following operations is typically O(1) for a singly linked list?",
        "options": ["Insertion at the beginning", "Insertion at the end", "Deletion from the middle", "Searching for an element"],
        "correct_answer": "Insertion at the beginning",
        "explanation": "Insertion at the beginning of a singly linked list is an O(1) operation because we only need to update the head pointer and the next pointer of the new node. This doesn't require traversing the list."
    },
    {
        "question": "What is the main advantage of a linked list over an array?",
        "options": ["Constant-time access to elements", "Dynamic size", "Better cache performance", "Lower memory usage"],
        "correct_answer": "Dynamic size",
        "explanation": "The main advantage of a linked list over an array is its dynamic size. Linked lists can grow or shrink dynamically as elements are added or removed, whereas arrays have a fixed size that must be specified at the time of creation."
    },
    {
        "question": "In a doubly linked list, each node contains:",
        "options": ["Only data", "Data and a pointer to the next node", "Data and a pointer to the previous node", "Data and pointers to both the next and previous nodes"],
        "correct_answer": "Data and pointers to both the next and previous nodes",
        "explanation": "In a doubly linked list, each node contains data and pointers to both the next and previous nodes. This allows for efficient traversal in both forward and backward directions."
    },
    {
        "question": "What is the space complexity of a linked list with n elements?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": "O(n)",
        "explanation": "The space complexity of a linked list with n elements is O(n) because each element requires a separate node in memory, and the number of nodes grows linearly with the number of elements."
    },
    {
        "question": "Which of the following is NOT a type of linked list?",
        "options": ["Singly linked list", "Doubly linked list", "Circular linked list", "Binary linked list"],
        "correct_answer": "Binary linked list",
        "explanation": "A binary linked list is not a standard type of linked list. The common types of linked lists are singly linked lists, doubly linked lists, and circular linked lists."
    },
    {
        "question": "What is the time complexity of inserting an element at the end of a singly linked list if we don't maintain a tail pointer?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": "O(n)",
        "explanation": "If we don't maintain a tail pointer in a singly linked list, inserting an element at the end requires traversing the entire list to find the last node, which takes O(n) time."
    },
    {
        "question": "In a circular linked list:",
        "options": ["The first node points to null", "The last node points to null", "The last node points to the first node", "There are no pointers"],
        "correct_answer": "The last node points to the first node",
        "explanation": "In a circular linked list, the last node points back to the first node, forming a circular structure. This allows for efficient traversal in a loop."
    },
    {
        "question": "Which data structure is typically used to implement a linked list?",
        "options": ["Array", "Tree", "Graph", "Node"],
        "correct_answer": "Node",
        "explanation": "A linked list is typically implemented using a Node data structure, where each node represents an element in the list and contains pointers to the next and previous nodes."
    },
    {
        "question": "What is the main disadvantage of a linked list compared to an array?",
        "options": ["Higher memory usage", "Slower insertion", "No random access", "Fixed size"],
        "correct_answer": "No random access",
        "explanation": "The main disadvantage of a linked list compared to an array is the lack of random access. In an array, we can access any element directly using its index, but in a linked list, we need to traverse the list from the beginning to access an element."
    },
    {
        "question": "In a doubly linked list, reversing the list requires:",
        "options": ["Only changing the head pointer", "Swapping next and previous pointers for each node", "Reallocating memory for all nodes", "Creating a new list"],
        "correct_answer": "Swapping next and previous pointers for each node",
        "explanation": "To reverse a doubly linked list, we need to swap the next and previous pointers for each node. This allows us to traverse the list in the reverse direction."
    },
    {
        "question": "What is the time complexity of deleting a node from the middle of a singly linked list?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": "O(n)",
        "explanation": "Deleting a node from the middle of a singly linked list requires traversing the list to find the node to be deleted, which takes O(n) time."
    },
    {
        "question": "Which of the following applications is best suited for a linked list?",
        "options": ["Storing a fixed-size array of integers", "Implementing a stack", "Binary search", "Random access to elements"],
        "correct_answer": "Implementing a stack",
        "explanation": "Linked lists are well-suited for implementing stacks because they allow for efficient insertion and deletion of elements at the beginning of the list, which is the primary operation in a stack."
    },
    {
        "question": "What is the primary advantage of a doubly linked list over a singly linked list?",
        "options": ["Lower memory usage", "Faster insertion at the beginning", "Ability to traverse in both directions", "Constant-time access to elements"],
        "correct_answer": "Ability to traverse in both directions",
        "explanation": "The primary advantage of a doubly linked list over a singly linked list is the ability to traverse the list in both forward and backward directions efficiently."
    },
    {
        "question": "In a linked list implementation, what does the 'head' typically refer to?",
        "options": ["The last node", "The middle node", "The first node", "A special node containing metadata"],
        "correct_answer": "The first node",
        "explanation": "In a linked list implementation, the 'head' typically refers to the first node in the list. It is the starting point for traversing the list."
    }
]