string_algo_questions = [
    {
        "question": "What is the time complexity of the naive string matching algorithm?",
        "choices": ["O(n)", "O(m)", "O(n+m)", "O(n*m)"],
        "correct_answer": "O(n*m)",
        "explanation": "The naive string matching algorithm has a time complexity of O(n*m), where n is the length of the text and m is the length of the pattern. In the worst case, it compares each character of the pattern with each character of the text."
    },
    {
        "question": "Which string matching algorithm uses a prefix function to avoid unnecessary comparisons?",
        "choices": ["Naive algorithm", "Rabin-Karp algorithm", "KMP algorithm", "Boyer-Moore algorithm"],
        "correct_answer": "KMP algorithm",
        "explanation": "The Knuth-Morris-Pratt (KMP) algorithm uses a prefix function to avoid unnecessary comparisons. It preprocesses the pattern to create a failure function that allows it to skip characters intelligently when a mismatch occurs."
    },
    {
        "question": "What is the time complexity of the KMP (Knuth-Morris-Pratt) algorithm?",
        "choices": ["O(n)", "O(m)", "O(n+m)", "O(n*m)"],
        "correct_answer": "O(n+m)",
        "explanation": "The KMP algorithm has a time complexity of O(n+m), where n is the length of the text and m is the length of the pattern. It preprocesses the pattern in O(m) time and then performs the search in O(n) time."
    },
    {
        "question": "Which string matching algorithm uses rolling hash functions?",
        "choices": ["KMP algorithm", "Boyer-Moore algorithm", "Rabin-Karp algorithm", "Aho-Corasick algorithm"],
        "correct_answer": "Rabin-Karp algorithm",
        "explanation": "The Rabin-Karp algorithm uses rolling hash functions to efficiently compute hash values for substrings of the text. This allows it to quickly compare the hash of the pattern with the hash of substrings in the text."
    },
    {
        "question": "What is the average-case time complexity of the Rabin-Karp algorithm?",
        "choices": ["O(n)", "O(m)", "O(n+m)", "O(n*m)"],
        "correct_answer": "O(n+m)",
        "explanation": "The average-case time complexity of the Rabin-Karp algorithm is O(n+m), where n is the length of the text and m is the length of the pattern. However, its worst-case time complexity is O(n*m)."
    },
    {
        "question": "Which string matching algorithm uses bad character and good suffix heuristics?",
        "choices": ["KMP algorithm", "Boyer-Moore algorithm", "Rabin-Karp algorithm", "Aho-Corasick algorithm"],
        "correct_answer": "Boyer-Moore algorithm",
        "explanation": "The Boyer-Moore algorithm uses both bad character and good suffix heuristics to skip unnecessary comparisons. These heuristics allow it to achieve sublinear time complexity in the average case."
    },
    {
        "question": "What is the best-case time complexity of the Boyer-Moore algorithm?",
        "choices": ["O(n)", "O(m)", "O(n/m)", "O(n+m)"],
        "correct_answer": "O(n/m)",
        "explanation": "The best-case time complexity of the Boyer-Moore algorithm is O(n/m), where n is the length of the text and m is the length of the pattern. This occurs when the pattern appears at the end of the text and there are no partial matches."
    },
    {
        "question": "Which string algorithm is used for finding the longest common subsequence of two strings?",
        "choices": ["KMP algorithm", "Dynamic Programming", "Rabin-Karp algorithm", "Boyer-Moore algorithm"],
        "correct_answer": "Dynamic Programming",
        "explanation": "Dynamic Programming is used to find the longest common subsequence of two strings. It builds a table of optimal subproblems and uses it to construct the final solution."
    },
    {
        "question": "What is the time complexity of finding the longest common subsequence using dynamic programming?",
        "choices": ["O(n)", "O(m)", "O(n+m)", "O(n*m)"],
        "correct_answer": "O(n*m)",
        "explanation": "The time complexity of finding the longest common subsequence using dynamic programming is O(n*m), where n and m are the lengths of the two strings. This is due to the construction of a 2D table of size n*m."
    },
    {
        "question": "Which algorithm is used for finding all occurrences of a set of patterns in a text?",
        "choices": ["KMP algorithm", "Boyer-Moore algorithm", "Rabin-Karp algorithm", "Aho-Corasick algorithm"],
        "correct_answer": "Aho-Corasick algorithm",
        "explanation": "The Aho-Corasick algorithm is used for finding all occurrences of a set of patterns in a text. It constructs a finite state machine from the patterns and uses it to efficiently search for multiple patterns simultaneously."
    },
    {
        "question": "What is the time complexity of the Aho-Corasick algorithm for pattern matching?",
        "choices": ["O(n)", "O(m)", "O(n+m)", "O(n*m)"],
        "correct_answer": "O(n+m)",
        "explanation": "The time complexity of the Aho-Corasick algorithm is O(n+m), where n is the length of the text and m is the total length of all patterns. It preprocesses the patterns in O(m) time and then searches the text in O(n) time."
    },
    {
        "question": "Which algorithm is used for finding the longest palindromic substring in linear time?",
        "choices": ["Naive algorithm", "Dynamic Programming", "Manacher's algorithm", "KMP algorithm"],
        "correct_answer": "Manacher's algorithm",
        "explanation": "Manacher's algorithm is used for finding the longest palindromic substring in linear time. It uses clever techniques to avoid redundant comparisons and achieves O(n) time complexity."
    },
    {
        "question": "What is the time complexity of Manacher's algorithm for finding the longest palindromic substring?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(2^n)"],
        "correct_answer": "O(n)",
        "explanation": "The time complexity of Manacher's algorithm is O(n), where n is the length of the string. It processes each character only a constant number of times, resulting in linear time complexity."
    },
    {
        "question": "Which data structure is commonly used in the implementation of the Aho-Corasick algorithm?",
        "choices": ["Binary Search Tree", "Hash Table", "Trie", "Heap"],
        "correct_answer": "Trie",
        "explanation": "The Aho-Corasick algorithm commonly uses a Trie (prefix tree) data structure to represent the set of patterns. This allows for efficient pattern matching and failure function computation."
    },
    {
        "question": "What is the main advantage of the Z algorithm over the KMP algorithm for string matching?",
        "choices": ["Lower time complexity", "Simpler implementation", "Handles multiple patterns", "Works with compressed strings"],
        "correct_answer": "Simpler implementation",
        "explanation": "The main advantage of the Z algorithm over the KMP algorithm is its simpler implementation. Both algorithms have the same linear time complexity, but the Z algorithm is often easier to understand and implement."
    },
    {
        "question": "Which string algorithm is used for finding the lexicographically minimal string rotation?",
        "choices": ["Booth's algorithm", "KMP algorithm", "Rabin-Karp algorithm", "Boyer-Moore algorithm"],
        "correct_answer": "Booth's algorithm",
        "explanation": "Booth's algorithm is used for finding the lexicographically minimal string rotation. It efficiently computes the minimal rotation in linear time by using techniques similar to those in the KMP algorithm."
    },
    {
        "question": "What is the time complexity of Booth's algorithm for finding the minimal string rotation?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(2^n)"],
        "correct_answer": "O(n)",
        "explanation": "The time complexity of Booth's algorithm is O(n), where n is the length of the string. It processes the string in a single pass, using an auxiliary array to store information about rotations."
    },
    {
        "question": "Which algorithm is used for constructing the suffix array of a string in O(n log n) time?",
        "choices": ["Naive algorithm", "KMP algorithm", "Manber-Myers algorithm", "Ukkonen's algorithm"],
        "correct_answer": "Manber-Myers algorithm",
        "explanation": "The Manber-Myers algorithm is used for constructing the suffix array of a string in O(n log n) time. It uses a divide-and-conquer approach and employs techniques from the KMP algorithm."
    },
    {
        "question": "What is the space complexity of the suffix array data structure?",
        "choices": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
        "correct_answer": "O(n)",
        "explanation": "The space complexity of the suffix array data structure is O(n), where n is the length of the string. It stores the starting positions of all suffixes in sorted order, requiring linear space."
    },
    {
        "question": "Which string algorithm is used for finding the longest repeated substring?",
        "choices": ["KMP algorithm", "Suffix Array", "Rabin-Karp algorithm", "Boyer-Moore algorithm"],
        "correct_answer": "Suffix Array",
        "explanation": "The Suffix Array data structure can be used to efficiently find the longest repeated substring. By constructing the suffix array and the LCP (Longest Common Prefix) array, we can identify the longest repeated substring in linear time."
    },
    {
        "question": "What is the time complexity of finding the longest repeated substring using a suffix array?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(2^n)"],
        "correct_answer": "O(n)",
        "explanation": "The time complexity of finding the longest repeated substring using a suffix array is O(n), where n is the length of the string. This assumes that the suffix array and LCP array have already been constructed."
    },
    {
        "question": "Which algorithm is used for online string matching?",
        "choices": ["KMP algorithm", "Boyer-Moore algorithm", "Rabin-Karp algorithm", "Aho-Corasick algorithm"],
        "correct_answer": "KMP algorithm",
        "explanation": "The KMP (Knuth-Morris-Pratt) algorithm is well-suited for online string matching. It can process the text character by character as it arrives, without needing to store the entire text in memory."
    },
    {
        "question": "What is the main advantage of the Rabin-Karp algorithm over other string matching algorithms?",
        "choices": ["Lower time complexity", "Simpler implementation", "Handles multiple patterns", "Efficient for two-dimensional pattern matching"],
        "correct_answer": "Efficient for two-dimensional pattern matching",
        "explanation": "The main advantage of the Rabin-Karp algorithm is its efficiency for two-dimensional pattern matching. Its use of rolling hash functions makes it well-suited for problems like finding a submatrix within a larger matrix."
    },
    {
        "question": "Which data structure is used in the Ukkonen's algorithm for suffix tree construction?",
        "choices": ["Binary Search Tree", "Hash Table", "Trie", "Heap"],
        "correct_answer": "Trie",
        "explanation": "Ukkonen's algorithm for suffix tree construction uses a Trie (prefix tree) data structure. It builds the suffix tree incrementally, adding suffixes one by one while maintaining efficiency through clever techniques."
    },
    {
        "question": "What is the time complexity of Ukkonen's algorithm for suffix tree construction?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(2^n)"],
        "correct_answer": "O(n)",
        "explanation": "The time complexity of Ukkonen's algorithm for suffix tree construction is O(n), where n is the length of the string. Despite its complex implementation, it achieves linear time complexity through the use of suffix links and other optimizations."
    },
    {
        "question": "Which string algorithm is used for finding the longest common substring of two strings?",
        "choices": ["KMP algorithm", "Suffix Array", "Dynamic Programming", "Boyer-Moore algorithm"],
        "correct_answer": "Suffix Array",
        "explanation": "The Suffix Array data structure can be used to efficiently find the longest common substring of two strings. By constructing a generalized suffix array for both strings and using the LCP array, we can find the longest common substring in linear time."
    },
    {
        "question": "What is the time complexity of finding the longest common substring using a suffix array?",
        "choices": ["O(n)", "O(n+m)", "O(n*m)", "O(n log n)"],
        "correct_answer": "O(n+m)",
        "explanation": "The time complexity of finding the longest common substring using a suffix array is O(n+m), where n and m are the lengths of the two strings. This assumes that the generalized suffix array and LCP array have already been constructed."
    },
    {
        "question": "Which algorithm is used for approximate string matching with k mismatches?",
        "choices": ["KMP algorithm", "Boyer-Moore algorithm", "Rabin-Karp algorithm", "Bitap algorithm"],
        "correct_answer": "Bitap algorithm",
        "explanation": "The Bitap algorithm (also known as the Shift-Or or Shift-And algorithm) is used for approximate string matching with k mismatches. It uses bitwise operations to efficiently handle mismatches and can be extended to support insertions and deletions."
    },
    {
        "question": "What is the time complexity of the Bitap algorithm for approximate string matching?",
        "choices": ["O(n)", "O(m*n)", "O(m*n/w)", "O(2^m*n)"],
        "correct_answer": "O(m*n/w)",
        "explanation": "The time complexity of the Bitap algorithm is O(m*n/w), where m is the length of the pattern, n is the length of the text, and w is the word size of the machine (typically 32 or 64 bits). The algorithm uses bitwise operations to process multiple characters in parallel."
    },
    {
        "question": "Which string algorithm is used for finding all palindromic substrings in linear time?",
        "choices": ["Naive algorithm", "Dynamic Programming", "Manacher's algorithm", "KMP algorithm"],
        "correct_answer": "Manacher's algorithm",
        "explanation": "Manacher's algorithm can be used to find all palindromic substrings in linear time. It computes the longest palindrome centered at each character, which can be used to enumerate all palindromic substrings."
    },
    {
        "question": "What is the space complexity of Manacher's algorithm for finding all palindromic substrings?",
        "choices": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
        "correct_answer": "O(n)",
        "explanation": "The space complexity of Manacher's algorithm for finding all palindromic substrings is O(n), where n is the length of the string. It uses an auxiliary array to store the lengths of palindromes centered at each character."
    },
    {
        "question": "Which data structure is used in the implementation of the Z algorithm?",
        "choices": ["Binary Search Tree", "Hash Table", "Array", "Heap"],
        "correct_answer": "Array",
        "explanation": "The Z algorithm uses an array (often called the Z array) to store the length of the longest substring starting from each position that is also a prefix of the string. This array is the key data structure in the algorithm's implementation."
    },
    {
        "question": "What is the time complexity of the Z algorithm for string matching?",
        "choices": ["O(n)", "O(m)", "O(n+m)", "O(n*m)"],
        "correct_answer": "O(n+m)",
        "explanation": "The time complexity of the Z algorithm for string matching is O(n+m), where n is the length of the text and m is the length of the pattern. It preprocesses the pattern and text in linear time and performs the matching in linear time as well."
    },
    {
        "question": "Which string algorithm is used for finding the lexicographically smallest cyclic rotation of a string?",
        "choices": ["KMP algorithm", "Booth's algorithm", "Rabin-Karp algorithm", "Boyer-Moore algorithm"],
        "correct_answer": "Booth's algorithm",
        "explanation": "Booth's algorithm is used for finding the lexicographically smallest cyclic rotation of a string. It can efficiently compute this rotation in linear time by using techniques similar to those in the KMP algorithm."
    },
    {
        "question": "What is the main advantage of using a suffix tree over a suffix array?",
        "choices": ["Lower space complexity", "Faster construction time", "More versatile for string operations", "Simpler implementation"],
        "correct_answer": "More versatile for string operations",
        "explanation": "The main advantage of using a suffix tree over a suffix array is that it's more versatile for various string operations. Suffix trees allow for efficient implementation of complex string algorithms and can answer queries like longest common substring in constant time after construction."
    },
    {
        "question": "Which algorithm is used for constructing a suffix tree in linear time?",
        "choices": ["Naive algorithm", "KMP algorithm", "Ukkonen's algorithm", "Manber-Myers algorithm"],
        "correct_answer": "Ukkonen's algorithm",
        "explanation": "Ukkonen's algorithm is used for constructing a suffix tree in linear time. It builds the suffix tree incrementally, processing the string from left to right and using suffix links to achieve linear time complexity."
    },
    {
        "question": "What is the space complexity of a suffix tree?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(2^n)"],
        "correct_answer": "O(n)",
        "explanation": "The space complexity of a suffix tree is O(n), where n is the length of the string. Although the constant factor can be high (up to 20 times the string length), it's still linear in terms of asymptotic complexity."
    },
    {
        "question": "Which string matching algorithm is most suitable for searching for multiple patterns simultaneously?",
        "choices": ["KMP algorithm", "Boyer-Moore algorithm", "Rabin-Karp algorithm", "Aho-Corasick algorithm"],
        "correct_answer": "Aho-Corasick algorithm",
        "explanation": "The Aho-Corasick algorithm is most suitable for searching for multiple patterns simultaneously. It constructs a finite state machine from the patterns, allowing for efficient matching of multiple patterns in a single pass through the text."
    },
    {
        "question": "What is the primary use of the Burrows-Wheeler Transform in string algorithms?",
        "choices": ["Pattern matching", "Data compression", "Sorting suffixes", "Palindrome detection"],
        "correct_answer": "Data compression",
        "explanation": "The primary use of the Burrows-Wheeler Transform in string algorithms is for data compression. It rearranges a character string into runs of similar characters, which can then be compressed more efficiently using techniques like move-to-front transform and run-length encoding."
    },
    {
        "question": "Which of the following is NOT a typical application of the Longest Common Subsequence (LCS) algorithm?",
        "choices": ["Diff tools for version control", "DNA sequence alignment", "Spell checking", "File compression"],
        "correct_answer": "File compression",
        "explanation": "File compression is not a typical application of the Longest Common Subsequence (LCS) algorithm. LCS is commonly used in diff tools, DNA sequence alignment, and can be adapted for spell checking, but it's not directly used for file compression."
    },
    {
        "question": "What is the time complexity of the naive algorithm for finding the Longest Common Subsequence of two strings?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(2^n)"],
        "correct_answer": "O(2^n)",
        "explanation": "The time complexity of the naive recursive algorithm for finding the Longest Common Subsequence of two strings is O(2^n). This is because for each character, we have two choices: either include it in the LCS or not, leading to an exponential number of recursive calls."
    },
    {
        "question": "Which data structure is used in the implementation of the Aho-Corasick algorithm for failure links?",
        "choices": ["Stack", "Queue", "Linked List", "Trie"],
        "correct_answer": "Trie",
        "explanation": "In the Aho-Corasick algorithm, failure links are implemented using a Trie data structure. These links connect nodes in the trie to the longest proper suffix that is also a prefix of some pattern, allowing for efficient transitions when a mismatch occurs."
    },
    {
        "question": "What is the main advantage of the Boyer-Moore algorithm over the KMP algorithm?",
        "choices": ["Lower worst-case time complexity", "Simpler implementation", "Better average-case performance", "Handles multiple patterns"],
        "correct_answer": "Better average-case performance",
        "explanation": "The main advantage of the Boyer-Moore algorithm over the KMP algorithm is its better average-case performance. Boyer-Moore can skip characters in the text, often resulting in sublinear time complexity in practice, especially for large alphabets."
    },
    {
        "question": "Which string matching algorithm is most suitable for searching in compressed text without decompression?",
        "choices": ["KMP algorithm", "Boyer-Moore algorithm", "Rabin-Karp algorithm", "Compressed Pattern Matching algorithms"],
        "correct_answer": "Compressed Pattern Matching algorithms",
        "explanation": "Compressed Pattern Matching algorithms are most suitable for searching in compressed text without decompression. These specialized algorithms can perform pattern matching directly on compressed representations of text, such as LZ-compressed files."
    },
    {
        "question": "What is the primary purpose of the Longest Palindromic Subsequence algorithm?",
        "choices": ["Find the longest substring that reads the same forwards and backwards", "Find the longest subsequence that reads the same forwards and backwards", "Find all palindromes in a string", "Check if a string is a palindrome"],
        "correct_answer": "Find the longest subsequence that reads the same forwards and backwards",
        "explanation": "The primary purpose of the Longest Palindromic Subsequence algorithm is to find the longest subsequence of characters that reads the same forwards and backwards, not necessarily consecutive in the original string."
    },
    {
        "question": "Which of the following is true about the relationship between the Longest Common Subsequence (LCS) and the Edit Distance problems?",
        "choices": ["They are unrelated problems", "LCS is a special case of Edit Distance", "Edit Distance is a special case of LCS", "They are the same problem with different names"],
        "correct_answer": "LCS is a special case of Edit Distance",
        "explanation": "The Longest Common Subsequence (LCS) problem can be seen as a special case of the Edit Distance problem. If we only allow insertions and deletions (no substitutions) in the Edit Distance problem, the number of operations is equal to the sum of the lengths of the two strings minus twice the length of their LCS."
    },
    {
        "question": "What is the main idea behind the Knuth-Morris-Pratt (KMP) algorithm?",
        "choices": ["Use rolling hash functions", "Preprocess the pattern to compute a failure function", "Compare characters from right to left", "Use a suffix tree for matching"],
        "correct_answer": "Preprocess the pattern to compute a failure function",
        "explanation": "The main idea behind the Knuth-Morris-Pratt (KMP) algorithm is to preprocess the pattern to compute a failure function. This function allows the algorithm to skip characters in the text when a mismatch occurs, avoiding unnecessary comparisons."
    }
]