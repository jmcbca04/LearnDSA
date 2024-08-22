trie_quiz = [
    {
        "question": "What is the primary purpose of a Trie data structure?",
        "options": ["Sorting strings", "Efficient string search and prefix matching", "Balancing binary trees", "Graph traversal"],
        "correct_answer": "Efficient string search and prefix matching",
        "explanation": "The primary purpose of a Trie (prefix tree) is efficient string search and prefix matching. It excels at tasks like autocomplete, spell checking, and IP routing, where quick prefix lookups are crucial."
    },
    {
        "question": "What is the time complexity of inserting a word of length k into a Trie?",
        "options": ["O(1)", "O(k)", "O(log k)", "O(n)"],
        "correct_answer": "O(k)",
        "explanation": "Inserting a word of length k into a Trie has a time complexity of O(k). This is because we need to traverse or create one node for each character in the word, regardless of the total number of words in the Trie."
    },
    {
        "question": "Which of the following applications is NOT typically associated with Tries?",
        "options": ["Autocomplete suggestions", "Spell checkers", "IP routing tables", "Sorting algorithms"],
        "correct_answer": "Sorting algorithms",
        "explanation": "Sorting algorithms are not typically associated with Tries. While Tries are excellent for string-related operations like autocomplete, spell checking, and IP routing, they are not commonly used for sorting. Other data structures like arrays or trees are more suitable for sorting algorithms."
    },
    {
        "question": "In a Trie, what does each node typically represent?",
        "options": ["A complete word", "A character", "A prefix", "The length of a word"],
        "correct_answer": "A character",
        "explanation": "In a Trie, each node typically represents a single character. The path from the root to a node forms a prefix, and complete words are usually marked by a special flag or terminator in the corresponding node."
    },
    {
        "question": "What is the space complexity of a Trie in the worst case?",
        "options": ["O(n)", "O(k*n)", "O(2^n)", "O(log n)"],
        "correct_answer": "O(k*n)",
        "explanation": "The space complexity of a Trie in the worst case is O(k*n), where k is the length of the longest word and n is the number of words. This occurs when there is no common prefix among the words, causing each character of each word to require a separate node."
    },
    {
        "question": "Which operation is typically faster in a Trie compared to a hash table?",
        "options": ["Insertion", "Deletion", "Exact string matching", "Prefix matching"],
        "correct_answer": "Prefix matching",
        "explanation": "Prefix matching is typically faster in a Trie compared to a hash table. Tries can find all words with a given prefix in O(k + m) time, where k is the length of the prefix and m is the number of matches. Hash tables are not designed for efficient prefix matching."
    },
    {
        "question": "What is a common way to mark the end of a word in a Trie?",
        "options": ["Using a special character", "Setting a boolean flag in the node", "Removing the last node", "Adding a null pointer"],
        "correct_answer": "Setting a boolean flag in the node",
        "explanation": "A common way to mark the end of a word in a Trie is by setting a boolean flag in the node. This flag indicates that the path from the root to this node forms a complete word, while still allowing the node to be part of longer words."
    },
    {
        "question": "Which of the following is TRUE about Tries?",
        "options": ["They always have a fixed depth", "They can only store lowercase letters", "They can efficiently store and search unicode strings", "They require less memory than hash tables for storing strings"],
        "correct_answer": "They can efficiently store and search unicode strings",
        "explanation": "Tries can efficiently store and search unicode strings. They are not limited to a fixed depth or just lowercase letters, and can handle any character set. While they may use more memory than hash tables for some datasets, they offer efficient prefix-based operations."
    },
    {
        "question": "What is the time complexity of finding the longest common prefix of a set of strings using a Trie?",
        "options": ["O(1)", "O(m), where m is the length of the longest common prefix", "O(n), where n is the number of strings", "O(k*n), where k is the average string length"],
        "correct_answer": "O(m), where m is the length of the longest common prefix",
        "explanation": "Finding the longest common prefix of a set of strings using a Trie has a time complexity of O(m), where m is the length of the longest common prefix. This operation involves traversing the Trie from the root until a node with more than one child or a word ending is encountered."
    },
    {
        "question": "In a Trie, how many children can each node have in the worst case for an English dictionary?",
        "options": ["26", "52", "256", "Unlimited"],
        "correct_answer": "26",
        "explanation": "For an English dictionary, each node in a Trie can have up to 26 children in the worst case, corresponding to the 26 letters of the English alphabet. This assumes we're only storing lowercase letters; if we include uppercase, it would be 52."
    },
    {
        "question": "What is a radix tree (or Patricia trie)?",
        "options": ["A Trie with a radix sort algorithm", "A compressed version of a regular Trie", "A Trie that only stores numbers", "A balanced Trie"],
        "correct_answer": "A compressed version of a regular Trie",
        "explanation": "A radix tree, also known as a Patricia trie, is a compressed version of a regular Trie. It merges nodes that have only one child, thus reducing the space requirements and potentially speeding up operations on strings with long common prefixes."
    },
    {
        "question": "Which of the following operations is typically NOT O(k) in a Trie, where k is the length of the key?",
        "options": ["Insertion", "Deletion", "Search", "Finding all keys with a given prefix"],
        "correct_answer": "Finding all keys with a given prefix",
        "explanation": "Finding all keys with a given prefix is typically not O(k) in a Trie, where k is the length of the key. While finding the node corresponding to the prefix is O(k), collecting all keys below that node can take longer, depending on the number and length of matching keys."
    },
    {
        "question": "What is the main disadvantage of using a Trie?",
        "options": ["Slow insertion time", "High space complexity", "Difficulty in implementation", "Poor performance for long strings"],
        "correct_answer": "High space complexity",
        "explanation": "The main disadvantage of using a Trie is its high space complexity. Tries can consume a lot of memory, especially when storing a large number of strings with little common prefix. Each node typically requires space for multiple child pointers, which can add up quickly."
    },
    {
        "question": "In which scenario would a Trie be less efficient than a hash table?",
        "options": ["Prefix matching", "Storing a small set of very long strings", "Autocomplete functionality", "Spell checking"],
        "correct_answer": "Storing a small set of very long strings",
        "explanation": "A Trie would be less efficient than a hash table when storing a small set of very long strings. In this scenario, the Trie might use more memory due to storing each character separately, while a hash table would store each string as a single entity. Hash tables also provide O(1) average case lookup for exact matches."
    },
    {
        "question": "What modification can be made to a Trie to make it more memory-efficient?",
        "options": ["Using a balanced tree structure", "Implementing path compression", "Adding more child nodes", "Increasing the alphabet size"],
        "correct_answer": "Implementing path compression",
        "explanation": "Implementing path compression can make a Trie more memory-efficient. This technique, used in radix trees (Patricia tries), merges chains of nodes that have only one child. This reduces the number of nodes needed to store the same information, thus saving memory."
    }
]