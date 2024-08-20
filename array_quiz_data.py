array_quiz = [
    {
        "question": "What is the time complexity of accessing an element in an array by its index?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": 0
    },
    {
        "question": "Which of the following is NOT a characteristic of arrays?",
        "options": ["Fixed size", "Contiguous memory allocation", "Dynamic resizing", "Constant-time element access"],
        "correct_answer": 2
    },
    {
        "question": "What is the space complexity of an array with n elements?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": 1
    },
    {
        "question": "In most programming languages, array indices start at what number?",
        "options": ["-1", "0", "1", "Depends on the language"],
        "correct_answer": 1
    },
    {
        "question": "What is the time complexity of inserting an element at the end of an array (assuming there's space)?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": 0
    },
    {
        "question": "What is the time complexity of inserting an element at the beginning of an array?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": 1
    },
    {
        "question": "Which data structure is an array most similar to?",
        "options": ["Linked List", "Stack", "Queue", "Tree"],
        "correct_answer": 1
    },
    {
        "question": "What is the main advantage of using an array over a linked list?",
        "options": ["Dynamic size", "Faster insertion", "Constant-time access", "Less memory usage"],
        "correct_answer": 2
    },
    {
        "question": "In a zero-indexed array of size n, what is the index of the last element?",
        "options": ["n", "n-1", "n+1", "0"],
        "correct_answer": 1
    },
    {
        "question": "What is the time complexity of searching for an element in an unsorted array?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": 1
    },
    {
        "question": "What is the time complexity of searching for an element in a sorted array using binary search?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": 2
    },
    {
        "question": "Which sorting algorithm is typically used by programming languages to sort arrays?",
        "options": ["Bubble Sort", "Quick Sort", "Insertion Sort", "Selection Sort"],
        "correct_answer": 1
    },
    {
        "question": "What is the time complexity of reversing an array?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": 1
    },
    {
        "question": "In Java, what happens if you try to access an array index that is out of bounds?",
        "options": ["The program crashes", "It returns null", "ArrayIndexOutOfBoundsException is thrown", "It wraps around to the beginning of the array"],
        "correct_answer": 2
    },
    {
        "question": "What is the time complexity of finding the minimum element in an unsorted array?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": 1
    },
    {
        "question": "Which of the following operations is NOT typically O(1) for arrays?",
        "options": ["Accessing an element", "Updating an element", "Inserting an element at a given index", "Getting the length of the array"],
        "correct_answer": 2
    },
    {
        "question": "What is a jagged array?",
        "options": ["An array with non-contiguous memory allocation", "An array of arrays with different lengths", "An array with only prime number indices", "An array that can change size dynamically"],
        "correct_answer": 1
    },
    {
        "question": "In C, what does arr[i] typically translate to in pointer arithmetic?",
        "options": ["*(arr + i)", "*(arr - i)", "*(i + arr)", "&(arr + i)"],
        "correct_answer": 0
    },
    {
        "question": "What is the time complexity of concatenating two arrays of lengths m and n?",
        "options": ["O(1)", "O(m + n)", "O(m * n)", "O(max(m, n))"],
        "correct_answer": 1
    },
    {
        "question": "Which of the following is true about multi-dimensional arrays in most programming languages?",
        "options": ["They always have to be square matrices", "They are stored in row-major order", "They cannot be jagged", "They have O(1) access time for any dimension"],
        "correct_answer": 1
    },
    {
        "question": "What is the space complexity of creating a copy of an array?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": 1
    },
    {
        "question": "In Python, what is the difference between a list and an array?",
        "options": ["Lists are mutable, arrays are not", "Arrays are more memory-efficient", "Lists can hold different data types, arrays are homogeneous", "There is no difference"],
        "correct_answer": 2
    },
    {
        "question": "What is the time complexity of rotating an array by k positions?",
        "options": ["O(1)", "O(k)", "O(n)", "O(n + k)"],
        "correct_answer": 2
    },
    {
        "question": "Which of the following is NOT a common use case for arrays?",
        "options": ["Storing a list of items", "Implementing a stack", "Implementing a queue efficiently", "Matrix operations"],
        "correct_answer": 2
    },
    {
        "question": "What is the time complexity of finding the intersection of two unsorted arrays?",
        "options": ["O(n)", "O(n log n)", "O(n^2)", "O(n + m)"],
        "correct_answer": 2
    },
    {
        "question": "In most programming languages, can arrays hold elements of different data types?",
        "options": ["Yes, always", "No, never", "Depends on the language", "Only if explicitly declared as such"],
        "correct_answer": 2
    },
    {
        "question": "What is the primary advantage of using a dynamic array over a static array?",
        "options": ["Faster access time", "Ability to resize", "Less memory usage", "Better cache performance"],
        "correct_answer": 1
    },
    {
        "question": "What is the time complexity of finding the majority element in an array?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": 1
    },
    {
        "question": "Which sorting algorithm is in-place and does not require extra space for sorting an array?",
        "options": ["Merge Sort", "Quick Sort", "Heap Sort", "Radix Sort"],
        "correct_answer": 2
    },
    {
        "question": "What is the time complexity of the counting sort algorithm for sorting an array?",
        "options": ["O(n)", "O(n log n)", "O(n + k)", "O(n^2)"],
        "correct_answer": 2
    },
    {
        "question": "In C++, what is the difference between std::array and std::vector?",
        "options": ["std::array has fixed size, std::vector can grow", "std::vector is faster", "std::array uses less memory", "There is no difference"],
        "correct_answer": 0
    },
    {
        "question": "What is the time complexity of finding the kth smallest element in an unsorted array?",
        "options": ["O(n)", "O(n log n)", "O(k)", "O(n + k)"],
        "correct_answer": 0
    },
    {
        "question": "Which of the following is true about cache performance when working with arrays?",
        "options": ["Arrays have poor cache performance", "Accessing array elements sequentially is cache-friendly", "Cache performance is not affected by array operations", "Arrays always cause cache misses"],
        "correct_answer": 1
    },
    {
        "question": "What is the space complexity of the merge sort algorithm when sorting an array?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n log n)"],
        "correct_answer": 1
    },
    {
        "question": "In Java, what is the default value for elements in a newly created integer array?",
        "options": ["null", "0", "1", "-1"],
        "correct_answer": 1
    },
    {
        "question": "What is the time complexity of finding the longest increasing subsequence in an array?",
        "options": ["O(n)", "O(n log n)", "O(n^2)", "O(2^n)"],
        "correct_answer": 1
    },
    {
        "question": "Which of the following operations on an array typically requires O(n) time?",
        "options": ["Accessing an element", "Updating an element", "Finding the maximum element", "Getting the length of the array"],
        "correct_answer": 2
    },
    {
        "question": "What is the primary disadvantage of using arrays?",
        "options": ["Slow access time", "Fixed size in many languages", "High memory usage", "Poor cache performance"],
        "correct_answer": 1
    },
    {
        "question": "In Python, what is the time complexity of the 'in' operator when checking if an element exists in a list?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": 1
    },
    {
        "question": "What is the time complexity of the Boyer-Moore majority vote algorithm for finding the majority element in an array?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": 1
    },
    {
        "question": "Which of the following is NOT a valid way to initialize an array in C?",
        "options": ["int arr[] = {1, 2, 3};", "int arr[3] = {1, 2, 3};", "int arr[3]; arr = {1, 2, 3};", "int *arr = (int*)malloc(3 * sizeof(int));"],
        "correct_answer": 2
    },
    {
        "question": "What is the time complexity of finding the equilibrium index in an array?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": 1
    },
    {
        "question": "In Java, what happens if you try to store more elements than the declared size of an array?",
        "options": ["The array automatically resizes", "ArrayIndexOutOfBoundsException is thrown", "The extra elements are ignored", "The program crashes"],
        "correct_answer": 1
    },
    {
        "question": "What is the time complexity of the Dutch National Flag algorithm for sorting an array with three distinct elements?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n log n)"],
        "correct_answer": 1
    },
    {
        "question": "Which of the following is true about the memory allocation of multi-dimensional arrays in C?",
        "options": ["Always contiguous", "Never contiguous", "Contiguous only for 2D arrays", "Depends on the compiler"],
        "correct_answer": 0
    },
    {
        "question": "What is the time complexity of finding the median of two sorted arrays of equal length?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
        "correct_answer": 1
    },
    {
        "question": "In Python, what is the time complexity of list slicing (e.g., arr[1:n])?",
        "options": ["O(1)", "O(k) where k is the slice length", "O(n)", "O(n log n)"],
        "correct_answer": 1
    },
    {
        "question": "What is the space complexity of the quicksort algorithm in its typical implementation?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
        "correct_answer": 1
    },
    {
        "question": "Which of the following array operations typically has the worst time complexity?",
        "options": ["Accessing an element", "Inserting an element at the beginning", "Updating an element", "Finding the length of the array"],
        "correct_answer": 1
    }
]