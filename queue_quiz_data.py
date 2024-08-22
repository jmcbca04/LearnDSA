queue_quiz = [
    {
        "question": "What is the primary characteristic of a queue data structure?",
        "options": ["LIFO (Last In, First Out)", "FIFO (First In, First Out)", "Random Access", "Sorted Order"],
        "correct_answer": "FIFO (First In, First Out)",
        "explanation": "The primary characteristic of a queue is FIFO (First In, First Out). This means that the first element added to the queue is the first one to be removed. This behavior is similar to a line of people waiting for a service, where the person who arrives first is served first."
    },
    {
        "question": "What is the time complexity of enqueuing an element into a queue?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": "O(1)",
        "explanation": "Enqueuing an element into a queue is an O(1) operation. This is because adding an element to the rear of the queue is a constant time operation, regardless of the number of elements already in the queue."
    },
    {
        "question": "Which operation is NOT typically associated with a queue?",
        "options": ["Enqueue", "Dequeue", "Peek", "Push"],
        "correct_answer": "Push",
        "explanation": "Push is not typically associated with a queue. The main operations of a queue are enqueue (add to rear), dequeue (remove from front), and peek (view front element without removing). Push is an operation associated with stacks, not queues."
    },
    {
        "question": "What happens when you try to dequeue an element from an empty queue?",
        "options": ["Returns null", "Throws an exception", "Returns the last enqueued element", "Adds a new element"],
        "correct_answer": "Throws an exception",
        "explanation": "When you try to dequeue an element from an empty queue, it typically throws an exception. This is because there are no elements to remove, and it's considered an error condition. The exact type of exception may vary depending on the programming language or implementation."
    },
    {
        "question": "Which data structure can be used to implement a queue?",
        "options": ["Array", "Linked List", "Both Array and Linked List", "Binary Tree"],
        "correct_answer": "Both Array and Linked List",
        "explanation": "Both arrays and linked lists can be used to implement a queue. Arrays can be used with a circular buffer implementation, while linked lists naturally support efficient insertion at one end and deletion at the other."
    },
    {
        "question": "What is the primary advantage of using a queue?",
        "options": ["Random access", "Constant time insertion and deletion at both ends", "Maintaining order of elements", "Sorting elements"],
        "correct_answer": "Maintaining order of elements",
        "explanation": "The primary advantage of using a queue is maintaining the order of elements. Queues preserve the order in which elements are added, which is useful for many applications like task scheduling, breadth-first search, or any scenario where first-come, first-served order is important."
    },
    {
        "question": "In which scenario would a queue be most appropriate?",
        "options": ["Undo functionality in a text editor", "Managing print job spooling", "Implementing a stack", "Depth-first search in a graph"],
        "correct_answer": "Managing print job spooling",
        "explanation": "A queue would be most appropriate for managing print job spooling. Print jobs are typically processed in the order they are received, which aligns perfectly with the FIFO nature of a queue."
    },
    {
        "question": "What is the time complexity of accessing the middle element of a queue?",
        "options": ["O(1)", "O(n)", "O(log n)", "Not possible without destroying the queue"],
        "correct_answer": "Not possible without destroying the queue",
        "explanation": "Accessing the middle element of a queue is not possible without destroying the queue. Queues only allow access to the front element. To reach the middle element, you would need to dequeue half the elements, which would alter the queue's state."
    },
    {
        "question": "Which of the following is true about the 'peek' operation on a queue?",
        "options": ["It removes the front element", "It adds a new element", "It returns the front element without removing it", "It reverses the queue"],
        "correct_answer": "It returns the front element without removing it",
        "explanation": "The 'peek' operation on a queue returns the front element without removing it. This allows you to inspect the next element that would be dequeued, without actually modifying the queue."
    },
    {
        "question": "What is a common use of queues in computer science?",
        "options": ["Memory management", "Breadth-first search", "Depth-first search", "Binary search"],
        "correct_answer": "Breadth-first search",
        "explanation": "Queues are commonly used in breadth-first search (BFS) algorithms. In BFS, a queue is used to keep track of the nodes to visit next, ensuring that nodes are explored level by level in a graph or tree."
    },
    {
        "question": "What is the space complexity of a queue containing n elements?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": "O(n)",
        "explanation": "The space complexity of a queue containing n elements is O(n). This is because each element in the queue occupies space, and the total space used grows linearly with the number of elements."
    },
    {
        "question": "In the context of queue operations, what does 'overflow' refer to?",
        "options": ["Dequeuing from an empty queue", "Enqueuing onto a full queue", "Peeking at an empty queue", "Reversing the queue"],
        "correct_answer": "Enqueuing onto a full queue",
        "explanation": "In the context of queue operations, 'overflow' refers to enqueuing onto a full queue. This occurs when trying to add an element to a queue that has already reached its maximum capacity, typically in implementations with a fixed size."
    },
    {
        "question": "Which of the following is a variation of a queue?",
        "options": ["Circular queue", "Square queue", "Triangular queue", "Pentagonal queue"],
        "correct_answer": "Circular queue",
        "explanation": "A circular queue is a variation of a queue. It's an efficient implementation using a fixed-size array where the front and rear of the queue wrap around to the beginning of the array when they reach the end, forming a circular structure."
    },
    {
        "question": "What is the result of enqueuing elements 1, 2, 3 into a queue and then dequeuing twice?",
        "options": ["Queue contains: [3]", "Queue contains: [1]", "Queue contains: [3, 2]", "Queue contains: [3, 1]"],
        "correct_answer": "Queue contains: [3]",
        "explanation": "After enqueuing 1, 2, 3 into a queue and dequeuing twice, the queue will contain [3]. The queue would look like [1, 2, 3] after enqueuing, and then dequeuing removes 1 and 2, leaving only 3 in the queue."
    },
    {
        "question": "Which of the following applications would NOT typically use a queue?",
        "options": ["CPU scheduling", "Disk scheduling", "Handling of interrupts in real-time systems", "Implementing undo functionality"],
        "correct_answer": "Implementing undo functionality",
        "explanation": "Implementing undo functionality would not typically use a queue. Undo functionality is better suited for a stack data structure, as it follows a Last-In-First-Out (LIFO) order. Queues are more appropriate for scenarios where first-come, first-served order is important, like CPU scheduling or handling interrupts."
    }
]