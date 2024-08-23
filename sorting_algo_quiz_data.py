sorting_algo_questions = [
    {
        "question": "Which sorting algorithm has the best average-case time complexity?",
        "choices": ["Bubble Sort", "Quick Sort", "Insertion Sort", "Selection Sort"],
        "correct_answer": "Quick Sort",
        "explanation": "Quick Sort has the best average-case time complexity of O(n log n). It uses a divide-and-conquer approach and performs well on most datasets, making it efficient for large-scale sorting tasks."
    },
    {
        "question": "What is the time complexity of Bubble Sort in the worst case?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
        "correct_answer": "O(n^2)",
        "explanation": "Bubble Sort has a worst-case time complexity of O(n^2). This occurs when the array is in reverse order, requiring the maximum number of comparisons and swaps for each element."
    },
    {
        "question": "Which sorting algorithm is known for its stability?",
        "choices": ["Quick Sort", "Heap Sort", "Merge Sort", "Shell Sort"],
        "correct_answer": "Merge Sort",
        "explanation": "Merge Sort is known for its stability, meaning it preserves the relative order of equal elements. This property is crucial in certain applications where maintaining the original order of equal elements is important."
    },
    {
        "question": "What is the space complexity of Merge Sort?",
        "choices": ["O(1)", "O(n)", "O(log n)", "O(n log n)"],
        "correct_answer": "O(n)",
        "explanation": "Merge Sort has a space complexity of O(n) because it requires additional space to merge the sorted subarrays. This extra space is proportional to the size of the input array."
    },
    {
        "question": "Which sorting algorithm is based on the divide-and-conquer paradigm?",
        "choices": ["Bubble Sort", "Insertion Sort", "Quick Sort", "Selection Sort"],
        "correct_answer": "Quick Sort",
        "explanation": "Quick Sort is based on the divide-and-conquer paradigm. It works by selecting a 'pivot' element and partitioning the array around the pivot, then recursively sorting the subarrays."
    },
    {
        "question": "What is the best-case time complexity of Insertion Sort?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(1)"],
        "correct_answer": "O(n)",
        "explanation": "The best-case time complexity of Insertion Sort is O(n), which occurs when the input array is already sorted. In this case, the algorithm only needs to compare each element once with its predecessor."
    },
    {
        "question": "Which sorting algorithm is most efficient for small datasets?",
        "choices": ["Merge Sort", "Quick Sort", "Insertion Sort", "Heap Sort"],
        "correct_answer": "Insertion Sort",
        "explanation": "Insertion Sort is most efficient for small datasets. It has low overhead and performs well when the input size is small, making it a good choice for sorting small arrays or as part of more complex algorithms."
    },
    {
        "question": "What is the average-case time complexity of Heap Sort?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
        "correct_answer": "O(n log n)",
        "explanation": "Heap Sort has an average-case time complexity of O(n log n). It works by building a max-heap and then repeatedly extracting the maximum element, which takes logarithmic time for each operation."
    },
    {
        "question": "Which sorting algorithm is in-place and does not require extra space?",
        "choices": ["Merge Sort", "Quick Sort", "Counting Sort", "Radix Sort"],
        "correct_answer": "Quick Sort",
        "explanation": "Quick Sort is an in-place sorting algorithm that does not require extra space proportional to the input size. It sorts the array by partitioning it around a pivot element and recursively sorting the subarrays."
    },
    {
        "question": "What is the worst-case time complexity of Quick Sort?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
        "correct_answer": "O(n^2)",
        "explanation": "The worst-case time complexity of Quick Sort is O(n^2). This occurs when the chosen pivot is always the smallest or largest element, leading to unbalanced partitions and maximum recursion depth."
    },
    {
        "question": "Which sorting algorithm is based on the heap data structure?",
        "choices": ["Merge Sort", "Quick Sort", "Heap Sort", "Bubble Sort"],
        "correct_answer": "Heap Sort",
        "explanation": "Heap Sort is based on the heap data structure, which is a complete binary tree that satisfies the heap property. It works by building a max-heap and then repeatedly extracting the maximum element."
    },
    {
        "question": "What is the time complexity of Counting Sort?",
        "choices": ["O(n+k)", "O(n log n)", "O(n^2)", "O(k log n)"],
        "correct_answer": "O(n+k)",
        "explanation": "Counting Sort has a time complexity of O(n+k), where n is the number of elements and k is the range of input values. It works by counting the number of occurrences of each value and then constructing the sorted array."
    },
    {
        "question": "Which sorting algorithm is most suitable for sorting strings?",
        "choices": ["Quick Sort", "Merge Sort", "Radix Sort", "Heap Sort"],
        "correct_answer": "Radix Sort",
        "explanation": "Radix Sort is most suitable for sorting strings. It works by sorting the characters of the strings from least significant to most significant, using a stable sorting algorithm for each character."
    },
    {
        "question": "What is the main advantage of Shell Sort over Insertion Sort?",
        "choices": ["Stability", "In-place sorting", "Better performance on partially sorted arrays", "Lower space complexity"],
        "correct_answer": "Better performance on partially sorted arrays",
        "explanation": "The main advantage of Shell Sort over Insertion Sort is that it performs better on partially sorted arrays. It works by sorting elements that are far apart first, then gradually reducing the gap size until it becomes 1, at which point it becomes equivalent to Insertion Sort."
    },
    {
        "question": "Which sorting algorithm is not comparison-based?",
        "choices": ["Merge Sort", "Bubble Sort", "Counting Sort", "Quick Sort"],
        "correct_answer": "Counting Sort",
        "explanation": "Counting Sort is not a comparison-based sorting algorithm. It works by counting the number of occurrences of each value and then constructing the sorted array. This makes it suitable for sorting integers within a known range."
    },
    {
        "question": "What is the best-case time complexity of Bubble Sort?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(1)"],
        "correct_answer": "O(n)",
        "explanation": "The best-case time complexity of Bubble Sort is O(n), which occurs when the input array is already sorted. In this case, the algorithm only needs to perform one pass through the array to confirm that it is sorted."
    },
    {
        "question": "Which sorting algorithm is most efficient for nearly sorted data?",
        "choices": ["Quick Sort", "Merge Sort", "Insertion Sort", "Heap Sort"],
        "correct_answer": "Insertion Sort",
        "explanation": "Insertion Sort is most efficient for nearly sorted data. It works by iterating through the array and inserting each element into its correct position, which is usually close to its current position. This results in fewer comparisons and swaps compared to other sorting algorithms."
    },
    {
        "question": "What is the space complexity of Quick Sort?",
        "choices": ["O(1)", "O(n)", "O(log n)", "O(n log n)"],
        "correct_answer": "O(log n)",
        "explanation": "The space complexity of Quick Sort is O(log n) in the average case, assuming that the recursive calls are balanced. This is because the maximum depth of the recursion tree is logarithmic in the number of elements."
    },
    {
        "question": "Which sorting algorithm is used in Python's built-in sort() function?",
        "choices": ["Merge Sort", "Quick Sort", "Timsort", "Heap Sort"],
        "correct_answer": "Timsort",
        "explanation": "Python's built-in sort() function uses the Timsort algorithm. Timsort is a hybrid sorting algorithm derived from Merge Sort and Insertion Sort, designed to perform well on many kinds of real-world data."
    },
    {
        "question": "What is the time complexity of Selection Sort?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
        "correct_answer": "O(n^2)",
        "explanation": "Selection Sort has a time complexity of O(n^2) in all cases. It works by repeatedly finding the minimum element from the unsorted part of the array and swapping it with the first element of the unsorted part."
    },
    {
        "question": "Which sorting algorithm is most suitable for sorting a linked list?",
        "choices": ["Quick Sort", "Merge Sort", "Heap Sort", "Radix Sort"],
        "correct_answer": "Merge Sort",
        "explanation": "Merge Sort is most suitable for sorting a linked list. It works by splitting the list into two halves, sorting them recursively, and then merging the sorted halves. This approach is efficient for linked lists because it does not require random access to the elements."
    },
    {
        "question": "What is the main disadvantage of Merge Sort?",
        "choices": ["High time complexity", "Not stable", "High space complexity", "Not in-place"],
        "correct_answer": "High space complexity",
        "explanation": "The main disadvantage of Merge Sort is its high space complexity. It requires additional space to merge the sorted subarrays, which can be a problem for large datasets that don't fit in memory."
    },
    {
        "question": "Which sorting algorithm is most efficient for sorting integers within a small range?",
        "choices": ["Quick Sort", "Merge Sort", "Counting Sort", "Heap Sort"],
        "correct_answer": "Counting Sort",
        "explanation": "Counting Sort is most efficient for sorting integers within a small range. It works by counting the number of occurrences of each value and then constructing the sorted array. This makes it suitable for sorting integers with a known range of values."
    },
    {
        "question": "What is the average-case time complexity of Bubble Sort?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
        "correct_answer": "O(n^2)",
        "explanation": "The average-case time complexity of Bubble Sort is O(n^2). This is because, on average, each element needs to be compared and swapped with its adjacent element in the worst case."
    },
    {
        "question": "Which sorting algorithm is most suitable for external sorting?",
        "choices": ["Quick Sort", "Merge Sort", "Insertion Sort", "Selection Sort"],
        "correct_answer": "Merge Sort",
        "explanation": "Merge Sort is most suitable for external sorting. It works by splitting the data into smaller chunks that can fit in memory, sorting them individually, and then merging them back together. This approach is efficient for large datasets that don't fit in memory."
    },
    {
        "question": "What is the worst-case time complexity of Merge Sort?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
        "correct_answer": "O(n log n)",
        "explanation": "The worst-case time complexity of Merge Sort is O(n log n). This occurs when the array is split into two equal halves at each step of the recursion. The merging step takes linear time, and there are log n levels of recursion."
    },
    {
        "question": "Which sorting algorithm is most efficient for sorting a small number of elements?",
        "choices": ["Quick Sort", "Merge Sort", "Insertion Sort", "Heap Sort"],
        "correct_answer": "Insertion Sort",
        "explanation": "Insertion Sort is most efficient for sorting a small number of elements. It works by iterating through the array and inserting each element into its correct position. This approach is simple and efficient for small arrays."
    },
    {
        "question": "What is the best-case time complexity of Quick Sort?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
        "correct_answer": "O(n log n)",
        "explanation": "The best-case time complexity of Quick Sort is O(n log n), which occurs when the chosen pivot divides the array into two equal halves at each step of the recursion. This results in a balanced recursion tree."
    },
    {
        "question": "Which sorting algorithm is most suitable for sorting data with many duplicate elements?",
        "choices": ["Quick Sort", "Merge Sort", "Counting Sort", "Heap Sort"],
        "correct_answer": "Counting Sort",
        "explanation": "Counting Sort is most suitable for sorting data with many duplicate elements. It works by counting the number of occurrences of each value and then constructing the sorted array. This makes it efficient for sorting data with a known range of values and a large number of duplicates."
    },
    {
        "question": "What is the space complexity of Bubble Sort?",
        "choices": ["O(1)", "O(n)", "O(log n)", "O(n log n)"],
        "correct_answer": "O(1)",
        "explanation": "Bubble Sort has a space complexity of O(1) because it sorts the array in-place, without requiring additional space proportional to the input size."
    },
    {
        "question": "Which sorting algorithm is most efficient for sorting a large dataset that doesn't fit in memory?",
        "choices": ["Quick Sort", "Merge Sort", "External Merge Sort", "Heap Sort"],
        "correct_answer": "External Merge Sort",
        "explanation": "External Merge Sort is most efficient for sorting a large dataset that doesn't fit in memory. It works by splitting the data into smaller chunks that can fit in memory, sorting them individually, and then merging them back together. This approach is efficient for large datasets that don't fit in memory."
    },
    {
        "question": "What is the time complexity of Radix Sort?",
        "choices": ["O(nk)", "O(n log n)", "O(n^2)", "O(k log n)"],
        "correct_answer": "O(nk)",
        "explanation": "Radix Sort has a time complexity of O(nk), where n is the number of elements and k is the number of digits in the maximum element. It works by sorting the elements based on their individual digits, starting from the least significant digit and moving to the most significant digit."
    },
    {
        "question": "Which sorting algorithm is most suitable for sorting floating-point numbers?",
        "choices": ["Counting Sort", "Radix Sort", "Quick Sort", "Bucket Sort"],
        "correct_answer": "Bucket Sort",
        "explanation": "Bucket Sort is most suitable for sorting floating-point numbers. It works by distributing the elements into a fixed number of buckets based on their values, then sorting the elements within each bucket using a different sorting algorithm, and finally concatenating the sorted buckets."
    },
    {
        "question": "What is the main advantage of Quick Sort over Merge Sort?",
        "choices": ["Stability", "In-place sorting", "Better worst-case performance", "Lower average-case time complexity"],
        "correct_answer": "In-place sorting",
        "explanation": "The main advantage of Quick Sort over Merge Sort is that it is an in-place sorting algorithm. This means that it sorts the array in-place, without requiring additional space proportional to the input size. This can be a significant advantage for large datasets."
    },
    {
        "question": "Which sorting algorithm is most efficient for sorting data with a known distribution?",
        "choices": ["Quick Sort", "Merge Sort", "Bucket Sort", "Heap Sort"],
        "correct_answer": "Bucket Sort",
        "explanation": "Bucket Sort is most efficient for sorting data with a known distribution. It works by distributing the elements into a fixed number of buckets based on their values, then sorting the elements within each bucket using a different sorting algorithm, and finally concatenating the sorted buckets."
    },
    {
        "question": "What is the time complexity of Shell Sort?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "Depends on the gap sequence"],
        "correct_answer": "Depends on the gap sequence",
        "explanation": "The time complexity of Shell Sort depends on the gap sequence used. A good gap sequence can result in a time complexity of O(n log n), while a poor gap sequence can result in a time complexity of O(n^2)."
    },
    {
        "question": "Which sorting algorithm is most suitable for sorting data with a high number of inversions?",
        "choices": ["Bubble Sort", "Insertion Sort", "Merge Sort", "Selection Sort"],
        "correct_answer": "Merge Sort",
        "explanation": "Merge Sort is most suitable for sorting data with a high number of inversions. It works by splitting the array into two halves, sorting them recursively, and then merging the sorted halves. This approach is efficient for data with a high number of inversions."
    },
    {
        "question": "What is the main advantage of Heap Sort over Quick Sort?",
        "choices": ["Better average-case performance", "Stability", "Guaranteed O(n log n) worst-case performance", "Lower space complexity"],
        "correct_answer": "Guaranteed O(n log n) worst-case performance",
        "explanation": "The main advantage of Heap Sort over Quick Sort is that it guarantees a worst-case time complexity of O(n log n). This is because it works by building a max-heap and then repeatedly extracting the maximum element, which takes logarithmic time for each operation."
    },
    {
        "question": "Which sorting algorithm is most efficient for sorting data with many repeated elements?",
        "choices": ["Quick Sort", "Merge Sort", "Counting Sort", "Heap Sort"],
        "correct_answer": "Counting Sort",
        "explanation": "Counting Sort is most efficient for sorting data with many repeated elements. It works by counting the number of occurrences of each value and then constructing the sorted array. This makes it efficient for sorting data with a known range of values and a large number of duplicates."
    },
    {
        "question": "What is the time complexity of Cocktail Sort?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
        "correct_answer": "O(n^2)",
        "explanation": "Cocktail Sort has a time complexity of O(n^2) in all cases. It works by repeatedly traversing the array in both directions, swapping adjacent elements if they are in the wrong order. This approach is similar to Bubble Sort, but it improves performance by reducing the number of passes through the array."
    },
    {
        "question": "Which sorting algorithm is most suitable for sorting data with a small range of possible values?",
        "choices": ["Quick Sort", "Merge Sort", "Counting Sort", "Heap Sort"],
        "correct_answer": "Counting Sort",
        "explanation": "Counting Sort is most suitable for sorting data with a small range of possible values. It works by counting the number of occurrences of each value and then constructing the sorted array. This makes it efficient for sorting data with a known range of values."
    },
    {
        "question": "What is the main advantage of Insertion Sort over Selection Sort?",
        "choices": ["Better worst-case performance", "Stability", "In-place sorting", "Lower average-case time complexity"],
        "correct_answer": "Stability",
        "explanation": "The main advantage of Insertion Sort over Selection Sort is that it is a stable sorting algorithm. This means that it preserves the relative order of equal elements. This property is crucial in certain applications where maintaining the original order of equal elements is important."
    },
    {
        "question": "Which sorting algorithm is most efficient for sorting data with a high percentage of elements already in their correct position?",
        "choices": ["Quick Sort", "Merge Sort", "Insertion Sort", "Heap Sort"],
        "correct_answer": "Insertion Sort",
        "explanation": "Insertion Sort is most efficient for sorting data with a high percentage of elements already in their correct position. It works by iterating through the array and inserting each element into its correct position. This approach is efficient when the input data is already partially sorted."
    },
    {
        "question": "What is the time complexity of Gnome Sort?",
        "choices": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
        "correct_answer": "O(n^2)",
        "explanation": "Gnome Sort has a time complexity of O(n^2) in all cases. It works by repeatedly swapping adjacent elements if they are in the wrong order, similar to Bubble Sort. However, it improves performance by moving the current element back to its correct position in each iteration."
    },
    {
        "question": "Which sorting algorithm is most suitable for sorting data with a large number of distinct elements?",
        "choices": ["Counting Sort", "Radix Sort", "Quick Sort", "Bucket Sort"],
        "correct_answer": "Quick Sort",
        "explanation": "Quick Sort is most suitable for sorting data with a large number of distinct elements. It works by selecting a 'pivot' element and partitioning the array around the pivot, then recursively sorting the subarrays. This approach is efficient for large datasets with a wide range of values."
    },
    {
        "question": "What is the main advantage of Merge Sort over Quick Sort?",
        "choices": ["Better average-case performance", "Stability", "In-place sorting", "Lower worst-case time complexity"],
        "correct_answer": "Stability",
        "explanation": "The main advantage of Merge Sort over Quick Sort is that it is a stable sorting algorithm. This means that it preserves the relative order of equal elements. This property is crucial in certain applications where maintaining the original order of equal elements is important."
    },
    {
        "question": "Which sorting algorithm is most efficient for sorting data with a small number of unique elements?",
        "choices": ["Quick Sort", "Merge Sort", "Counting Sort", "Heap Sort"],
        "correct_answer": "Counting Sort",
        "explanation": "Counting Sort is most efficient for sorting data with a small number of unique elements. It works by counting the number of occurrences of each value and then constructing the sorted array. This makes it efficient for sorting data with a known range of values and a small number of unique elements."
    },
    {
        "question": "What is the time complexity of Comb Sort?",
        "choices": ["O(n log n)", "O(n^2)", "O(n log^2 n)", "O(n^2 / 2^p)"],
        "correct_answer": "O(n^2 / 2^p)",
        "explanation": "Comb Sort has a time complexity of O(n^2 / 2^p) in the worst case, where p is the number of times the gap size is reduced by a factor of 1.3. It works by repeatedly traversing the array and swapping adjacent elements if they are in the wrong order, similar to Bubble Sort. However, it improves performance by using a gap sequence that reduces the number of comparisons and swaps."
    },
    {
        "question": "Which sorting algorithm is most suitable for sorting data with a large number of elements close to their final positions?",
        "choices": ["Quick Sort", "Merge Sort", "Insertion Sort", "Heap Sort"],
        "correct_answer": "Insertion Sort",
        "explanation": "Insertion Sort is most suitable for sorting data with a large number of elements close to their final positions. It works by iterating through the array and inserting each element into its correct position. This approach is efficient when the input data is already partially sorted."
    },
    {
        "question": "What is the main advantage of Selection Sort over Bubble Sort?",
        "choices": ["Better average-case performance", "Stability", "Fewer swaps", "Lower worst-case time complexity"],
        "correct_answer": "Fewer swaps",
        "explanation": "The main advantage of Selection Sort over Bubble Sort is that it performs fewer swaps. It works by repeatedly finding the minimum element from the unsorted part of the array and swapping it with the first element of the unsorted part. This results in fewer swaps compared to Bubble Sort, which swaps adjacent elements if they are in the wrong order."
    }
]