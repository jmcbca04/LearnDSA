hash_table_quiz = [
    {
        "question": "What is the average time complexity for insertion in a hash table?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": "O(1)",
        "explanation": "The average time complexity for insertion in a hash table is O(1). This is because a good hash function distributes keys uniformly, allowing for constant-time access to the correct bucket. However, this assumes that collisions are rare and handled efficiently."
    },
    {
        "question": "What is a collision in the context of hash tables?",
        "options": ["When two keys have the same hash value", "When the hash table is full", "When a key is not found", "When the hash function fails"],
        "correct_answer": "When two keys have the same hash value",
        "explanation": "A collision in hash tables occurs when two different keys produce the same hash value. This means they would be mapped to the same location in the hash table, requiring a collision resolution strategy to handle the situation."
    },
    {
        "question": "Which of the following is NOT a common method for handling collisions in hash tables?",
        "options": ["Chaining", "Open addressing", "Linear probing", "Binary search"],
        "correct_answer": "Binary search",
        "explanation": "Binary search is not a common method for handling collisions in hash tables. Chaining (using linked lists), open addressing, and linear probing are all common collision resolution techniques. Binary search is typically used for searching in sorted arrays, not for hash table collision resolution."
    },
    {
        "question": "What is the load factor of a hash table?",
        "options": ["The ratio of the number of stored elements to the size of the hash table", "The number of collisions", "The size of the hash table", "The number of empty slots"],
        "correct_answer": "The ratio of the number of stored elements to the size of the hash table",
        "explanation": "The load factor of a hash table is the ratio of the number of stored elements to the size of the hash table. It's a measure of how full the hash table is, and it affects the performance of hash table operations. A higher load factor increases the chance of collisions."
    },
    {
        "question": "Which of the following is a characteristic of a good hash function?",
        "options": ["It should be slow to compute", "It should cluster similar keys together", "It should distribute keys uniformly", "It should always produce prime numbers"],
        "correct_answer": "It should distribute keys uniformly",
        "explanation": "A good hash function should distribute keys uniformly across the hash table. This minimizes collisions and ensures that the hash table's performance remains close to O(1) for its operations. Clustering keys or always producing prime numbers would lead to more collisions."
    },
    {
        "question": "What is the purpose of rehashing in a hash table?",
        "options": ["To resolve collisions", "To improve the hash function", "To resize the hash table", "To delete all elements"],
        "correct_answer": "To resize the hash table",
        "explanation": "Rehashing is used to resize the hash table. When the load factor becomes too high, rehashing is performed to increase the size of the hash table, redistribute all existing elements, and maintain efficient performance. This helps to keep the number of collisions low as more elements are added to the hash table."
    },
    {
        "question": "In Python, which built-in data structure implements a hash table?",
        "options": ["List", "Tuple", "Set", "Dictionary"],
        "correct_answer": "Dictionary",
        "explanation": "In Python, the Dictionary (dict) data structure implements a hash table. It provides key-value pair storage with average O(1) time complexity for insertion, deletion, and lookup operations. Sets in Python also use hash table implementation internally."
    },
    {
        "question": "What is the worst-case time complexity for searching in a hash table?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "correct_answer": "O(n)",
        "explanation": "The worst-case time complexity for searching in a hash table is O(n). This occurs when all keys hash to the same bucket, essentially degenerating the hash table into a linked list. However, this is extremely rare with a good hash function and is why the average case is still considered O(1)."
    },
    {
        "question": "Which of the following is an advantage of hash tables over arrays?",
        "options": ["Constant time access to elements", "Lower memory usage", "Maintaining order of elements", "Better cache performance"],
        "correct_answer": "Constant time access to elements",
        "explanation": "A key advantage of hash tables over arrays is constant time (O(1)) access to elements on average. Unlike arrays where you need the index, hash tables allow you to access elements using keys, which can be of various data types, not just integers."
    },
    {
        "question": "What happens if you try to insert a key-value pair into a hash table where the key already exists?",
        "options": ["The operation fails", "The new value replaces the old value", "A collision occurs", "The key is duplicated"],
        "correct_answer": "The new value replaces the old value",
        "explanation": "When you insert a key-value pair into a hash table where the key already exists, the new value typically replaces the old value associated with that key. This behavior ensures that each key in the hash table is unique and associated with the most recently assigned value."
    },
    {
        "question": "Which of the following is NOT a common use case for hash tables?",
        "options": ["Implementing caches", "Storing database indexes", "Maintaining sorted data", "Detecting duplicates"],
        "correct_answer": "Maintaining sorted data",
        "explanation": "Maintaining sorted data is not a common use case for hash tables. Hash tables are unordered by nature and do not maintain any specific order of elements. For sorted data, other data structures like balanced binary search trees (e.g., Red-Black trees) are more appropriate."
    },
    {
        "question": "What is the primary advantage of using open addressing over chaining for collision resolution?",
        "options": ["It's easier to implement", "It uses less memory", "It's faster for insertions", "It handles collisions better"],
        "correct_answer": "It uses less memory",
        "explanation": "The primary advantage of using open addressing over chaining for collision resolution is that it uses less memory. Open addressing stores all elements directly in the hash table array, while chaining requires additional memory for linked list nodes. This makes open addressing more cache-friendly and memory-efficient."
    },
    {
        "question": "In the context of hash tables, what is meant by 'perfect hashing'?",
        "options": ["A hash function that never produces collisions", "A hash function that always produces prime numbers", "A hash table with no empty slots", "A hash table with O(1) worst-case lookup time"],
        "correct_answer": "A hash function that never produces collisions",
        "explanation": "Perfect hashing refers to a hash function that never produces collisions for a specific set of keys. This means each key in the set is mapped to a unique slot in the hash table. Perfect hashing can provide O(1) worst-case lookup time but is typically only feasible when the set of keys is known in advance and does not change."
    },
    {
        "question": "What is the time complexity of deleting an element from a hash table?",
        "options": ["O(1) average case", "O(n) average case", "O(log n) average case", "O(n^2) average case"],
        "correct_answer": "O(1) average case",
        "explanation": "The average time complexity of deleting an element from a hash table is O(1). This is because the hash function can directly compute the location of the element, allowing for constant-time access on average. However, in the worst case (rare), it could be O(n) if many elements have collided into a single bucket."
    },
    {
        "question": "Which of the following statements about hash tables is FALSE?",
        "options": ["They provide fast insertion and lookup", "They maintain the order of inserted elements", "They can have collisions", "They can be resized dynamically"],
        "correct_answer": "They maintain the order of inserted elements",
        "explanation": "The statement 'They maintain the order of inserted elements' is false for hash tables. Hash tables do not maintain the order of inserted elements. The position of an element in the hash table is determined by its hash value, not the order of insertion. If you need to maintain insertion order, you would need to use an additional data structure or a specialized implementation like Python's OrderedDict."
    }
]