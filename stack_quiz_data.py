stack_quiz = [
    {
        "question": "What is the primary characteristic of a stack data structure?",
        "options": ["FIFO (First In, First Out)", "LIFO (Last In, First Out)", "Random Access", "Sorted Order"],
        "correct_answer": "LIFO (Last In, First Out)",
        "explanation": "The primary characteristic of a stack is LIFO (Last In, First Out). This means that the last element added to the stack is the first one to be removed. This behavior is similar to a stack of plates where you add and remove plates from the top."
    },
    {
        "question": "What is the time complexity of pushing an element onto a stack?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": "O(1)",
        "explanation": "Pushing an element onto a stack is an O(1) operation. This is because adding an element to the top of the stack is a constant time operation, regardless of the number of elements already in the stack."
    },
    {
        "question": "Which operation is NOT typically associated with a stack?",
        "options": ["Push", "Pop", "Peek", "Insert at middle"],
        "correct_answer": "Insert at middle",
        "explanation": "Inserting at the middle is not typically associated with a stack. The main operations of a stack are push (add to top), pop (remove from top), and peek (view top element without removing). Inserting at the middle would violate the LIFO principle of a stack."
    },
    {
        "question": "What happens when you try to pop an element from an empty stack?",
        "options": ["Returns null", "Throws an exception", "Returns the last pushed element", "Adds a new element"],
        "correct_answer": "Throws an exception",
        "explanation": "When you try to pop an element from an empty stack, it typically throws an exception. This is because there are no elements to remove, and it's considered an error condition. The exact type of exception may vary depending on the programming language or implementation."
    },
    {
        "question": "Which data structure is often used to implement a stack?",
        "options": ["Array", "Binary Tree", "Hash Table", "Graph"],
        "correct_answer": "Array",
        "explanation": "An array is often used to implement a stack. This is because arrays allow for easy addition and removal of elements at one end (usually the end with the highest index), which aligns well with the LIFO behavior of a stack."
    },
    {
        "question": "What is the primary advantage of using a stack?",
        "options": ["Random access", "Constant time insertion and deletion", "Sorting elements", "Searching elements"],
        "correct_answer": "Constant time insertion and deletion",
        "explanation": "The primary advantage of using a stack is constant time insertion and deletion. Both push and pop operations on a stack are O(1), making it very efficient for scenarios where you need to add or remove elements in a Last In, First Out manner."
    },
    {
        "question": "In which scenario would a stack be most appropriate?",
        "options": ["Implementing a queue", "Undo functionality in a text editor", "Storing a phone book", "Implementing a priority queue"],
        "correct_answer": "Undo functionality in a text editor",
        "explanation": "A stack would be most appropriate for implementing undo functionality in a text editor. Each action can be pushed onto the stack, and when the user wants to undo, the most recent action can be popped off the stack and reversed."
    },
    {
        "question": "What is the time complexity of accessing the middle element of a stack?",
        "options": ["O(1)", "O(n)", "O(log n)", "Not possible without destroying the stack"],
        "correct_answer": "Not possible without destroying the stack",
        "explanation": "Accessing the middle element of a stack is not possible without destroying the stack. Stacks only allow access to the top element. To reach the middle element, you would need to pop off half the elements, which would alter the stack's state."
    },
    {
        "question": "Which of the following is true about the 'peek' operation on a stack?",
        "options": ["It removes the top element", "It adds a new element", "It returns the top element without removing it", "It reverses the stack"],
        "correct_answer": "It returns the top element without removing it",
        "explanation": "The 'peek' operation on a stack returns the top element without removing it. This allows you to inspect the next element that would be popped, without actually modifying the stack."
    },
    {
        "question": "What is a common use of stacks in programming languages?",
        "options": ["Heap memory allocation", "Function call management", "Garbage collection", "Multi-threading"],
        "correct_answer": "Function call management",
        "explanation": "Stacks are commonly used for function call management in programming languages. When a function is called, a new frame is pushed onto the call stack. When the function returns, its frame is popped off the stack. This manages the execution context of nested function calls."
    },
    {
        "question": "Which of these algorithms typically uses a stack in its implementation?",
        "options": ["Breadth-First Search", "Bubble Sort", "Depth-First Search", "Binary Search"],
        "correct_answer": "Depth-First Search",
        "explanation": "Depth-First Search (DFS) typically uses a stack in its implementation. The stack is used to keep track of the vertices to be explored next, allowing the algorithm to backtrack when it reaches a dead end in its search."
    },
    {
        "question": "What is the space complexity of a stack containing n elements?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": "O(n)",
        "explanation": "The space complexity of a stack containing n elements is O(n). This is because each element in the stack occupies space, and the total space used grows linearly with the number of elements."
    },
    {
        "question": "In the context of stack operations, what does 'overflow' refer to?",
        "options": ["Popping from an empty stack", "Pushing onto a full stack", "Peeking at an empty stack", "Reversing the stack"],
        "correct_answer": "Pushing onto a full stack",
        "explanation": "In the context of stack operations, 'overflow' refers to pushing onto a full stack. This occurs when trying to add an element to a stack that has already reached its maximum capacity, typically in implementations with a fixed size."
    },
    {
        "question": "Which of the following problems can be efficiently solved using a stack?",
        "options": ["Finding the shortest path in a graph", "Balancing parentheses in an expression", "Sorting an array", "Finding the minimum element in constant time"],
        "correct_answer": "Balancing parentheses in an expression",
        "explanation": "Balancing parentheses in an expression can be efficiently solved using a stack. As you iterate through the expression, you push opening parentheses onto the stack and pop when you encounter closing parentheses. If the stack is empty at the end and all parentheses were matched, the expression is balanced."
    },
    {
        "question": "What is the result of pushing elements 1, 2, 3 onto a stack and then popping twice?",
        "options": ["Stack contains: [1]", "Stack contains: [3]", "Stack contains: [1, 2]", "Stack contains: [1, 3]"],
        "correct_answer": "Stack contains: [1]",
        "explanation": "After pushing 1, 2, 3 onto a stack and popping twice, the stack will contain [1]. The stack would look like [1, 2, 3] after pushing, and then popping removes 3 and 2, leaving only 1 in the stack."
    }
]