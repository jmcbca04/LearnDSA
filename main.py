from fastapi import FastAPI, Request, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from auth import router as auth_router
from array_quiz_data import array_quiz
from linked_list_quiz_data import linked_list_quiz
from stack_quiz_data import stack_quiz
from queue_quiz_data import queue_quiz
from hash_table_quiz_data import hash_table_quiz
from tree_quiz_data import tree_quiz
from graph_quiz_data import graph_quiz
from heap_quiz_data import heap_quiz
from trie_quiz_data import trie_quiz
from sorting_algo_quiz_data import sorting_algo_questions
from searching_algo_quiz_data import searching_algo_questions
from dynamic_programming_quiz_data import dynamic_programming_questions
from greedy_algo_quiz_data import greedy_algo_questions
from divide_and_conquer_quiz_data import divide_and_conquer_questions
from backtracking_quiz_data import backtracking_questions
from graph_algo_quiz_data import graph_algo_questions
from recursive_algo_quiz_data import recursive_algo_questions
from string_algo_quiz_data import string_algo_questions
import random
import base64
import json
from shared import logger, get_optional_user, get_current_user, get_user_count, get_total_logins, test_db_connection, init_db
from fastapi.security import OAuth2PasswordBearer
from contextlib import asynccontextmanager
from typing import Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Testing database connection")
    test_db_connection()
    logger.info("Initializing database")
    init_db()
    logger.info("Database initialized")
    yield


app = FastAPI(lifespan=lifespan)


templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(auth_router)


@app.get("/profile", response_class=HTMLResponse)
async def profile(request: Request, user: Optional[dict] = Depends(get_optional_user)):
    if not user:
        logger.info("User not authenticated, redirecting to login")
        return RedirectResponse(url="/login")
    logger.info(f"User accessing profile: {user}")
    return templates.TemplateResponse("profile.html", {"request": request, "user": user})


@app.get("/user-stats")
async def user_stats():
    user_count = await get_user_count()
    total_logins = await get_total_logins()
    logger.info(f"User stats: count={user_count}, total_logins={total_logins}")
    return {"total_users": user_count, "total_logins": total_logins}


@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request, user: Optional[dict] = Depends(get_optional_user)):
    return templates.TemplateResponse("home.html", {"request": request, "user": user})


@app.get("/login-modal", response_class=HTMLResponse)
async def login_modal(request: Request):
    return templates.TemplateResponse("login_modal.html", {"request": request})


@app.get("/protected")
async def protected_route(user: dict = Depends(get_current_user)):
    return {"message": "This is a protected route", "user": user}


@app.get("/lesson/{lesson_id}", response_class=HTMLResponse)
async def read_lesson(request: Request, lesson_id: int, user: Optional[dict] = Depends(get_optional_user)):
    lessons = {
        1: {
            "title": "Arrays",
            "description": "A collection of elements identified by index or key, stored in contiguous memory locations.",
            "key_points": [
                "Arrays store elements in contiguous memory locations.",
                "Elements are accessed using an index, typically starting from 0.",
                "Arrays have a fixed size in many programming languages.",
                "Dynamic arrays (like Python lists) can grow or shrink in size."
            ],
            "operations": [
                {"name": "Access", "time_complexity": "O(1)", "description": "Retrieve an element at a given index."},
                {"name": "Search", "time_complexity": "O(n)", "description": "Find a specific element in the array."},
                {"name": "Insert", "time_complexity": "O(n)", "description": "Add an element at a specific position."},
                {"name": "Delete", "time_complexity": "O(n)", "description": "Remove an element from a specific position."}
            ],
            "use_cases": [
                "Storing and accessing sequential data",
                "Temporary storage of objects",
                "Implementing other data structures like stacks, queues, and heaps",
                "Buffering data for I/O operations"
            ],
            "code_example": """
# Python example of array operations
numbers = [1, 2, 3, 4, 5]  # Creating an array

# Accessing elements
print(numbers[0])  # Output: 1

# Searching
if 3 in numbers:
    print("3 is in the array")

# Inserting (at the end)
numbers.append(6)

# Inserting (at a specific position)
numbers.insert(2, 10)

# Deleting
numbers.pop(1)  # Remove element at index 1

print(numbers)  # Output: [1, 10, 3, 4, 5, 6]
            """
        },
        2: {
            "title": "Linked Lists",
            "description": "A linear data structure where elements are stored in nodes, and each node points to the next node in the sequence.",
            "key_points": [
                "Linked Lists consist of nodes, where each node contains data and a reference (or link) to the next node.",
                "The first node is called the head, and the last node typically points to None.",
                "Linked Lists can be singly linked (each node points to the next), doubly linked (each node points to both next and previous), or circular.",
                "They allow for efficient insertion and deletion of elements, especially at the beginning of the list.",
                "Unlike arrays, Linked Lists do not require contiguous memory allocation."
            ],
            "operations": [
                {"name": "Access", "time_complexity": "O(n)", "description": "Traverse the list to reach a specific element."},
                {"name": "Search", "time_complexity": "O(n)", "description": "Traverse the list to find a specific element."},
                {"name": "Insert", "time_complexity": "O(1) or O(n)", "description": "O(1) at the beginning, O(n) if inserting at a specific position."},
                {"name": "Delete", "time_complexity": "O(1) or O(n)", "description": "O(1) at the beginning, O(n) if deleting from a specific position."}
            ],
            "use_cases": [
                "Implementing other data structures like stacks, queues, and hash tables",
                "Managing dynamic memory allocation",
                "Creating music playlists",
                "Implementing undo functionality in applications",
                "Representing sparse matrices"
            ],
            "code_example": """
# Python example of a singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
print(ll.display())  # Output: [1, 2, 3]
            """
        },
        3: {
            "title": "Stacks",
            "description": "A linear data structure that follows the Last In, First Out (LIFO) principle. Elements are added and removed from the same end, called the 'top' of the stack.",
            "key_points": [
                "Stacks follow the Last In, First Out (LIFO) principle.",
                "The main operations are push (add an element) and pop (remove the top element).",
                "Stacks can be implemented using arrays or linked lists.",
                "They have a 'top' pointer that keeps track of the last inserted element.",
                "Stacks have a limited access pattern - only the top element can be accessed directly."
            ],
            "operations": [
                {"name": "Push", "time_complexity": "O(1)", "description": "Add an element to the top of the stack."},
                {"name": "Pop", "time_complexity": "O(1)", "description": "Remove and return the top element from the stack."},
                {"name": "Peek/Top", "time_complexity": "O(1)", "description": "Return the top element without removing it."},
                {"name": "IsEmpty", "time_complexity": "O(1)", "description": "Check if the stack is empty."}
            ],
            "use_cases": [
                "Function call management (call stack) in programming languages",
                "Undo mechanisms in text editors and other applications",
                "Expression evaluation and syntax parsing",
                "Backtracking algorithms",
                "Browser history (back button functionality)"
            ],
            "code_example": """
# Python example of a stack implementation

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.peek())  # Output: 2
print(stack.size())  # Output: 2
print(stack.is_empty())  # Output: False
            """
        },
        4: {
            "title": "Queues",
            "description": "A linear data structure that follows the First In, First Out (FIFO) principle. Elements are added at one end (rear) and removed from the other end (front).",
            "key_points": [
                "Queues follow the First In, First Out (FIFO) principle.",
                "The main operations are enqueue (add an element) and dequeue (remove the front element).",
                "Queues can be implemented using arrays or linked lists.",
                "They have 'front' and 'rear' pointers to keep track of the ends of the queue.",
                "Variations include circular queues, double-ended queues (deques), and priority queues."
            ],
            "operations": [
                {"name": "Enqueue", "time_complexity": "O(1)", "description": "Add an element to the rear of the queue."},
                {"name": "Dequeue", "time_complexity": "O(1)", "description": "Remove and return the front element from the queue."},
                {"name": "Front", "time_complexity": "O(1)", "description": "Return the front element without removing it."},
                {"name": "IsEmpty", "time_complexity": "O(1)", "description": "Check if the queue is empty."},
                {"name": "Size", "time_complexity": "O(1)", "description": "Return the number of elements in the queue."}
            ],
            "use_cases": [
                "Task scheduling in operating systems",
                "Breadth-First Search (BFS) algorithm in graph traversal",
                "Print job spooling",
                "Handling of requests in web servers",
                "Buffering in data streams"
            ],
            "code_example": """
# Python example of a queue implementation

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.front())    # Output: 2
print(queue.size())     # Output: 2
print(queue.is_empty()) # Output: False
            """
        },
        5: {
            "title": "Hash Tables",
            "description": "A data structure that implements an associative array abstract data type, a structure that can map keys to values. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.",
            "key_points": [
                "Hash tables provide efficient insertion, deletion, and lookup operations.",
                "They use a hash function to convert keys into array indices.",
                "Collisions occur when two keys hash to the same index and are resolved using techniques like chaining or open addressing.",
                "The average time complexity for basic operations is O(1), but can degrade to O(n) in worst-case scenarios.",
                "Load factor (number of entries / number of buckets) affects performance and needs to be balanced."
            ],
            "operations": [
                {"name": "Insert", "time_complexity": "O(1) average", "description": "Add a key-value pair to the hash table."},
                {"name": "Delete", "time_complexity": "O(1) average", "description": "Remove a key-value pair from the hash table."},
                {"name": "Lookup", "time_complexity": "O(1) average", "description": "Retrieve the value associated with a given key."},
                {"name": "Resize", "time_complexity": "O(n)", "description": "Increase or decrease the size of the hash table and rehash all entries."}
            ],
            "use_cases": [
                "Implementing associative arrays (dictionaries in Python, objects in JavaScript)",
                "Database indexing for faster data retrieval",
                "Caching mechanisms in various applications",
                "Symbol tables in compilers and interpreters",
                "Implementing sets with fast membership testing"
            ],
            "code_example": """
# Python example of a simple hash table implementation

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return
        raise KeyError(key)

# Usage
ht = HashTable()
ht.insert("apple", 5)
ht.insert("banana", 7)
print(ht.get("apple"))  # Output: 5
ht.remove("apple")
try:
    print(ht.get("apple"))
except KeyError:
    print("Key not found")  # This will be printed
            """
        },
        6: {
            "title": "Trees",
            "description": "A hierarchical data structure consisting of nodes connected by edges. Each tree has a root node, and every node can have child nodes, forming a parent-child relationship.",
            "key_points": [
                "Trees have a root node and each node can have multiple child nodes.",
                "Nodes with no children are called leaf nodes.",
                "The depth of a node is the number of edges from the root to that node.",
                "The height of a tree is the maximum depth of any node.",
                "Common types include binary trees, binary search trees (BST), AVL trees, and B-trees.",
                "Trees are used to represent hierarchical relationships and for efficient searching and sorting."
            ],
            "operations": [
                {"name": "Insert", "time_complexity": "O(log n) for balanced trees", "description": "Add a new node to the tree."},
                {"name": "Delete", "time_complexity": "O(log n) for balanced trees", "description": "Remove a node from the tree."},
                {"name": "Search", "time_complexity": "O(log n) for balanced trees", "description": "Find a specific node in the tree."},
                {"name": "Traversal", "time_complexity": "O(n)", "description": "Visit all nodes in the tree (e.g., in-order, pre-order, post-order)."}
            ],
            "use_cases": [
                "File systems in operating systems",
                "DOM (Document Object Model) in web browsers",
                "Decision trees in machine learning",
                "Syntax trees in compilers",
                "Hierarchical data representation (e.g., organizational structures)"
            ],
            "code_example": """
# Python example of a binary search tree implementation

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

# Usage
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(9)

print(bst.inorder_traversal())  # Output: [1, 3, 5, 7, 9]
print(bst.search(7).value)  # Output: 7
print(bst.search(10))  # Output: None
            """
        },
        7: {
            "title": "Graphs",
            "description": "A non-linear data structure consisting of vertices (or nodes) and edges that connect these vertices. Graphs are used to represent networks of communication, data organization, computational devices, flow of computation, etc.",
            "key_points": [
                "Graphs consist of vertices (nodes) and edges connecting these vertices.",
                "Graphs can be directed (edges have direction) or undirected.",
                "Graphs can be weighted (edges have values) or unweighted.",
                "Common representations include adjacency matrix and adjacency list.",
                "Graphs can be cyclic or acyclic.",
                "Special types include trees, DAGs (Directed Acyclic Graphs), and bipartite graphs."
            ],
            "operations": [
                {"name": "Add Vertex", "time_complexity": "O(1)", "description": "Add a new vertex to the graph."},
                {"name": "Add Edge", "time_complexity": "O(1)", "description": "Add a new edge between two vertices."},
                {"name": "Remove Vertex", "time_complexity": "O(|V| + |E|)", "description": "Remove a vertex and all its incident edges."},
                {"name": "Remove Edge", "time_complexity": "O(1)", "description": "Remove an edge between two vertices."},
                {"name": "DFS Traversal", "time_complexity": "O(|V| + |E|)", "description": "Depth-First Search traversal of the graph."},
                {"name": "BFS Traversal", "time_complexity": "O(|V| + |E|)", "description": "Breadth-First Search traversal of the graph."}
            ],
            "use_cases": [
                "Social networks (friends connections)",
                "Map applications (cities and roads)",
                "Recommendation systems",
                "Network routing protocols",
                "Dependency resolution in software packages",
                "Analyzing chemical compounds in chemistry"
            ],
            "code_example": """
# Python example of a simple undirected graph using adjacency list

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1] = [v for v in self.graph[vertex1] if v != vertex2]
            self.graph[vertex2] = [v for v in self.graph[vertex2] if v != vertex1]

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for adj_vertex in self.graph[vertex]:
                self.graph[adj_vertex] = [v for v in self.graph[adj_vertex] if v != vertex]
            del self.graph[vertex]

    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_vertex)
        print(start_vertex, end=' ')
        for adj_vertex in self.graph[start_vertex]:
            if adj_vertex not in visited:
                self.dfs(adj_vertex, visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')
            for adj_vertex in self.graph[vertex]:
                if adj_vertex not in visited:
                    visited.add(adj_vertex)
                    queue.append(adj_vertex)

# Usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("DFS starting from vertex 0:")
g.dfs(0)
print("\\nBFS starting from vertex 0:")
g.bfs(0)
            """
        },
        8: {
            "title": "Heaps",
            "description": "A complete binary tree that satisfies the heap property. Heaps can be either max-heaps or min-heaps.",
            "key_points": [
                "Heaps are complete binary trees.",
                "Max-heaps: the key at the root must be greater than or equal to the keys at its children.",
                "Min-heaps: the key at the root must be less than or equal to the keys at its children.",
                "Heaps are used to implement priority queues and for sorting algorithms like HeapSort.",
                "Common operations include insertion, deletion, and extracting the maximum/minimum element."
            ],
            "operations": [
                {"name": "Insert", "time_complexity": "O(log n)", "description": "Add a new element to the heap."},
                {"name": "Delete", "time_complexity": "O(log n)", "description": "Remove an element from the heap."},
                {"name": "Extract Max/Min", "time_complexity": "O(log n)", "description": "Remove and return the maximum/minimum element from the heap."},
                {"name": "Heapify", "time_complexity": "O(log n)", "description": "Restore the heap property after insertion or deletion."}
            ],
            "use_cases": [
                "Implementing priority queues",
                "HeapSort algorithm",
                "Dijkstra's algorithm for shortest path",
                "Huffman coding for data compression",
                "OS scheduling and job scheduling"
            ],
            "code_example": """
# Python example of a max-heap implementation

class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._heapify_up(parent)

    def extract_max(self):
        if not self.heap:
            return None
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return max_value

    def _heapify_down(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        largest = i
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)

# Usage
max_heap = MaxHeap()
max_heap.insert(5)
max_heap.insert(3)
max_heap.insert(7)
max_heap.insert(1)
max_heap.insert(9)

print(max_heap.extract_max())  # Output: 9
print(max_heap.extract_max())  # Output: 7
print(max_heap.extract_max())  # Output: 5
            """
        },
        9: {
            "title": "Tries",
            "description": "A tree-like data structure that stores a dynamic set or associative array where the keys are usually strings. Tries are used to efficiently search for a key in a collection of strings.",
            "key_points": [
                "Tries are used for efficient string searching and retrieval.",
                "Each node in a trie represents a character in a string.",
                "The root node represents an empty string.",
                "Tries are used in applications like autocomplete suggestions, spell checkers, and routing algorithms.",
                "Tries can be implemented using arrays or linked lists."
            ],
            "operations": [
                {"name": "Insert", "time_complexity": "O(m)", "description": "Add a new string to the trie, where m is the length of the string."},
                {"name": "Search", "time_complexity": "O(m)", "description": "Check if a string is present in the trie."},
                {"name": "Delete", "time_complexity": "O(m)", "description": "Remove a string from the trie."},
                {"name": "Prefix Search", "time_complexity": "O(m)", "description": "Find all strings in the trie that have a given prefix."}
            ],
            "use_cases": [
                "Implementing autocomplete suggestions",
                "Spell checking in text editors",
                "Routing algorithms in routers",
                "Implementing dictionaries and word suggestions",
                "Solving word games like Scrabble"
            ],
            "code_example": """
# Python example of a trie implementation

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Usage
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("banana")

print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: True
print(trie.search("ban"))    # Output: False
print(trie.starts_with("app"))  # Output: True
            """
        },
        10: {
            "title": "Sorting Algorithms",
            "description": "Sorting algorithms are used to rearrange a given array or list of elements into a certain order. The order can be numerical order (ascending or descending), lexicographical order, or based on custom criteria.",
            "key_points": [
                "Sorting algorithms are used to arrange data in a specific order.",
                "Common sorting algorithms include bubble sort, selection sort, insertion sort, merge sort, quick sort, heap sort, and radix sort.",
                "Sorting algorithms have different time complexities for best, average, and worst cases.",
                "The choice of sorting algorithm depends on the size of the data, the nature of the data, and the required time complexity."
            ],
            "operations": [
                {"name": "Bubble Sort", "time_complexity": "O(n^2)", "description": "Compare adjacent elements and swap them if they are in the wrong order."},
                {"name": "Selection Sort", "time_complexity": "O(n^2)", "description": "Find the minimum element from the unsorted part and swap it with the first element."},
                {"name": "Insertion Sort", "time_complexity": "O(n^2)", "description": "Insert each element from the unsorted part into its correct position in the sorted part."},
                {"name": "Merge Sort", "time_complexity": "O(n log n)", "description": "Divide the array into two halves, sort them recursively, and merge them."},
                {"name": "Quick Sort", "time_complexity": "O(n log n) average, O(n^2) worst case", "description": "Choose a pivot element, partition the array around the pivot, and recursively sort the sub-arrays."},
                {"name": "Heap Sort", "time_complexity": "O(n log n)", "description": "Build a max heap from the array, repeatedly remove the maximum element, and place it at the end."},
                {"name": "Radix Sort", "time_complexity": "O(nk)", "description": "Sort the elements based on individual digits or characters, starting from the least significant digit/character."}
            ],
            "use_cases": [
                "Sorting data for display or analysis",
                "Implementing data structures like priority queues",
                "Solving problems related to searching and ordering",
                "Optimizing algorithms for better performance",
                "Working with large datasets that don't fit in memory"
            ],
            "code_example": """
# Python example of bubble sort implementation

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)  # Output: [11, 12, 22, 25, 34, 64, 90]
            """
        },
        11: {
            "title": "Searching Algorithms",
            "description": "Searching algorithms are used to find a specific element or value in a given data structure. The goal is to locate the target element efficiently and return its index or position.",
            "key_points": [
                "Searching algorithms are used to find elements in a data structure.",
                "Common searching algorithms include linear search, binary search, and hash table search.",
                "Searching algorithms have different time complexities for best, average, and worst cases.",
                "The choice of searching algorithm depends on the size of the data, the nature of the data, and the required time complexity."
            ],
            "operations": [
                {"name": "Linear Search", "time_complexity": "O(n)", "description": "Sequentially search for the target element in the data structure."},
                {"name": "Binary Search", "time_complexity": "O(log n)", "description": "Divide the sorted data structure into halves and search in the appropriate half."},
                {"name": "Hash Table Search", "time_complexity": "O(1) average", "description": "Use a hash function to compute the index of the target element in the hash table."}
            ],
            "use_cases": [
                "Searching for elements in a database",
                "Implementing search functionality in applications",
                "Solving problems related to searching and retrieval",
                "Optimizing algorithms for better performance",
                "Working with large datasets that don't fit in memory"
            ],
            "code_example": """
# Python example of linear search implementation

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Usage
arr = [64, 34, 25, 12, 22, 11, 90]
target = 22
index = linear_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print("Element not found")
            """
        },
        12: {
            "title": "Dynamic Programming",
            "description": "Dynamic programming is an algorithmic technique that solves a complex problem by breaking it down into simpler subproblems and solving each subproblem only once, storing their solutions in a table for future reference.",
            "key_points": [
                "Dynamic programming is used to solve optimization problems.",
                "It involves solving subproblems and combining their solutions to solve the original problem.",
                "Dynamic programming algorithms have overlapping subproblems and optimal substructure properties.",
                "The solutions to subproblems are stored in a table to avoid redundant computations."
            ],
            "operations": [
                {"name": "Tabulation", "time_complexity": "O(n)", "description": "Build a table in bottom-up manner and fill it up in a way that each entry depends on previously computed entries."},
                {"name": "Memoization", "time_complexity": "O(n)", "description": "Store the results of expensive function calls and return the cached result when the same inputs occur again."}
            ],
            "use_cases": [
                "Solving optimization problems like knapsack, longest common subsequence, and shortest path",
                "Implementing algorithms like Bellman-Ford and Floyd-Warshall for shortest path",
                "Solving problems related to combinatorics and probability",
                "Optimizing algorithms for better performance",
                "Working with large datasets that don't fit in memory"
            ],
            "code_example": """
# Python example of dynamic programming (tabulation) for fibonacci sequence

def fibonacci(n):
    fib = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

# Usage
n = 10
print(fibonacci(n))  # Output: 55
            """
        },
        13: {
            "title": "Greedy Algorithms",
            "description": "Greedy algorithms are a class of algorithms that make the locally optimal choice at each stage with the hope of finding a global optimum. They are used to solve optimization problems where the optimal solution can be reached by making a series of greedy choices.",
            "key_points": [
                "Greedy algorithms make locally optimal choices at each stage.",
                "They are used to solve optimization problems where a global optimum can be reached by making greedy choices.",
                "Greedy algorithms may not always produce the optimal solution, but they are efficient and easy to implement.",
                "Common greedy algorithms include Kruskal's algorithm for minimum spanning tree, Dijkstra's algorithm for shortest path, and Huffman coding."
            ],
            "operations": [
                {"name": "Kruskal's Algorithm", "time_complexity": "O(E log E)", "description": "Find the minimum spanning tree of a graph by repeatedly adding the smallest weight edge that does not form a cycle."},
                {"name": "Dijkstra's Algorithm", "time_complexity": "O((V + E) log V)", "description": "Find the shortest path from a source vertex to all other vertices in a weighted graph."},
                {"name": "Huffman Coding", "time_complexity": "O(n log n)", "description": "Generate a prefix code for a given set of characters based on their frequencies."}
            ],
            "use_cases": [
                "Solving optimization problems like minimum spanning tree, shortest path, and data compression",
                "Implementing algorithms like Kruskal's algorithm, Dijkstra's algorithm, and Huffman coding",
                "Solving problems related to network design and resource allocation",
                "Optimizing algorithms for better performance",
                "Working with large datasets that don't fit in memory"
            ],
            "code_example": """
# Python example of greedy algorithm (Dijkstra's algorithm) for shortest path

import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)
print(f"Shortest distances from vertex {start_vertex}: {shortest_distances}")
            """
        },
        14: {
            "title": "Divide and Conquer",
            "description": "Divide and conquer is an algorithmic technique that involves breaking down a problem into smaller subproblems, solving them independently, and combining their solutions to solve the original problem.",
            "key_points": [
                "Divide and conquer algorithms divide the problem into smaller subproblems.",
                "They solve each subproblem independently and combine their solutions.",
                "Common divide and conquer algorithms include binary search, merge sort, quick sort, and fast Fourier transform.",
                "Divide and conquer algorithms have a time complexity of O(n log n) for many problems."
            ],
            "operations": [
                {"name": "Binary Search", "time_complexity": "O(log n)", "description": "Divide the sorted array into halves and search in the appropriate half."},
                {"name": "Merge Sort", "time_complexity": "O(n log n)", "description": "Divide the array into two halves, sort them recursively, and merge them."},
                {"name": "Quick Sort", "time_complexity": "O(n log n) average, O(n^2) worst case", "description": "Choose a pivot element, partition the array around the pivot, and recursively sort the sub-arrays."},
                {"name": "Fast Fourier Transform", "time_complexity": "O(n log n)", "description": "Compute the discrete Fourier transform of a sequence using a divide and conquer approach."}
            ],
            "use_cases": [
                "Solving problems that can be divided into smaller subproblems",
                "Implementing algorithms like binary search, merge sort, quick sort, and fast Fourier transform",
                "Solving problems related to searching, sorting, and numerical analysis",
                "Optimizing algorithms for better performance",
                "Working with large datasets that don't fit in memory"
            ],
            "code_example": """
# Python example of divide and conquer (merge sort)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

# Usage
arr = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(arr))  # Output: [11, 12, 22, 25, 34, 64, 90]
            """
        },
        15: {
            "title": "Backtracking",
            "description": "Backtracking is an algorithmic technique that involves exploring all possible solutions to a problem by trying out different options and undoing choices that lead to a dead end.",
            "key_points": [
                "Backtracking algorithms explore all possible solutions to a problem.",
                "They try out different options and undo choices that lead to a dead end.",
                "Common backtracking problems include the N-Queens problem, the Knight's tour problem, and the Sudoku puzzle.",
                "Backtracking algorithms have an exponential time complexity in the worst case."
            ],
            "operations": [
                {"name": "N-Queens Problem", "time_complexity": "O(n!)", "description": "Place N queens on an NxN chessboard such that no two queens threaten each other."},
                {"name": "Knight's Tour Problem", "time_complexity": "O(8^n)", "description": "Find a closed tour for a knight on an NxN chessboard that visits every square exactly once."},
                {"name": "Sudoku Puzzle", "time_complexity": "O(9^n)", "description": "Fill a 9x9 grid with digits so that each column, row, and 3x3 subgrid contains all digits from 1 to 9."}
            ],
            "use_cases": [
                "Solving problems that involve exploring all possible solutions",
                "Implementing algorithms like the N-Queens problem, the Knight's tour problem, and the Sudoku puzzle",
                "Solving problems related to combinatorics and game theory",
                "Optimizing algorithms for better performance",
                "Working with large datasets that don't fit in memory"
            ],
            "code_example": """
# Python example of backtracking (N-Queens problem)

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_n_queens(board, row + 1, n):
                return True

            board[row][col] = 0

    return False

def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

# Usage
n = 4
board = [[0] * n for _ in range(n)]

if solve_n_queens(board, 0, n):
    print_board(board)
else:
    print("No solution exists.")
            """
        },
        16: {
            "title": "Graph Algorithms",
            "description": "Graph algorithms are used to solve problems related to graphs, which are abstract data structures that represent relationships between objects. Graph algorithms can be used for various applications such as network analysis, routing, and optimization.",
            "key_points": [
                "Graph algorithms are used to solve problems related to graphs.",
                "Common graph algorithms include breadth-first search (BFS), depth-first search (DFS), Dijkstra's algorithm, Bellman-Ford algorithm, and Kruskal's algorithm.",
                "Graph algorithms have different time complexities for different scenarios.",
                "The choice of graph algorithm depends on the problem at hand and the characteristics of the graph."
            ],
            "operations": [
                {"name": "Breadth-First Search (BFS)", "time_complexity": "O(|V| + |E|)", "description": "Explore all vertices of a graph in breadth-first order, starting from a given source vertex."},
                {"name": "Depth-First Search (DFS)", "time_complexity": "O(|V| + |E|)", "description": "Explore as far as possible along each branch before backtracking, starting from a given source vertex."},
                {"name": "Dijkstra's Algorithm", "time_complexity": "O((|V| + |E|) log |V|)", "description": "Find the shortest path from a source vertex to all other vertices in a weighted graph."},
                {"name": "Bellman-Ford Algorithm", "time_complexity": "O(|V| * |E|)", "description": "Find the shortest path from a source vertex to all other vertices in a weighted graph, even if there are negative weights."},
                {"name": "Kruskal's Algorithm", "time_complexity": "O(|E| log |E|)", "description": "Find the minimum spanning tree of a connected, undirected graph."}
            ],
            "use_cases": [
                "Network analysis and routing",
                "Optimization problems like shortest path and minimum spanning tree",
                "Solving problems related to connectivity and reachability",
                "Implementing algorithms like BFS, DFS, Dijkstra's algorithm, Bellman-Ford algorithm, and Kruskal's algorithm",
                "Working with large datasets that don't fit in memory"
            ],
            "code_example": """
# Python example of graph algorithm (Breadth-First Search)

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_vertex = 'A'
print(f"BFS traversal starting from vertex {start_vertex}:")
bfs(graph, start_vertex)
            """
        },
        17: {
            "title": "Recursive Algorithms",
            "description": "Recursive algorithms are algorithms that solve a problem by breaking it down into smaller subproblems and solving each subproblem recursively. Recursive algorithms are often simpler and more elegant than iterative algorithms.",
            "key_points": [
                "Recursive algorithms solve a problem by breaking it down into smaller subproblems.",
                "They solve each subproblem recursively until a base case is reached.",
                "Common recursive algorithms include factorial, Fibonacci, and Tower of Hanoi.",
                "Recursive algorithms have a time complexity of O(2^n) in the worst case."
            ],
            "operations": [
                {"name": "Factorial", "time_complexity": "O(n)", "description": "Calculate the factorial of a non-negative integer n."},
                {"name": "Fibonacci", "time_complexity": "O(2^n)", "description": "Calculate the nth Fibonacci number."},
                {"name": "Tower of Hanoi", "time_complexity": "O(2^n)", "description": "Move a stack of disks from one peg to another, with the constraint that smaller disks must always be on top of larger ones."}
            ],
            "use_cases": [
                "Solving problems that can be broken down into smaller subproblems",
                "Implementing algorithms like factorial, Fibonacci, and Tower of Hanoi",
                "Solving problems related to combinatorics and recursion",
                "Optimizing algorithms for better performance",
                "Working with large datasets that don't fit in memory"
            ],
            "code_example": """
# Python example of recursive algorithm (Factorial)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Usage
n = 5
print(f"Factorial of {n} is: {factorial(n)}")
            """
        },
        18: {
            "title": "String Algorithms",
            "description": "String algorithms are used to manipulate and process strings, which are sequences of characters. String algorithms can be used for various applications such as text editing, pattern matching, and data compression.",
            "key_points": [
                "String algorithms are used to manipulate and process strings.",
                "Common string algorithms include string matching (Knuth-Morris-Pratt, Boyer-Moore), string searching (Rabin-Karp), and string manipulation (substring search, string concatenation).",
                "String algorithms have different time complexities for different scenarios.",
                "The choice of string algorithm depends on the problem at hand and the characteristics of the strings."
            ],
            "operations": [
                {"name": "Knuth-Morris-Pratt (KMP) Algorithm", "time_complexity": "O(n + m)", "description": "Find the first occurrence of a pattern in a text."},
                {"name": "Boyer-Moore Algorithm", "time_complexity": "O(n/m) average, O(nm) worst case", "description": "Find the first occurrence of a pattern in a text."},
                {"name": "Rabin-Karp Algorithm", "time_complexity": "O(nm) average, O(n^2) worst case", "description": "Find the first occurrence of a pattern in a text."},
                {"name": "Substring Search", "time_complexity": "O(nm)", "description": "Find all occurrences of a substring in a string."},
                {"name": "String Concatenation", "time_complexity": "O(n + m)", "description": "Concatenate two strings."}
            ],
            "use_cases": [
                "Text editing and manipulation",
                "Pattern matching and searching",
                "Data compression and encoding",
                "Implementing algorithms like KMP, Boyer-Moore, Rabin-Karp, and string manipulation",
                "Working with large datasets that don't fit in memory"
            ],
            "code_example": """
# Python example of string algorithm (Knuth-Morris-Pratt)

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = [0] * m
    j = 0

    compute_lps(pattern, m, lps)

    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            print(f"Pattern found at index {i-j}")
            j = lps[j-1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

def compute_lps(pattern, m, lps):
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1

# Usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
kmp_search(text, pattern)
            """
        }
    }
    lesson = lessons.get(lesson_id)
    if lesson is None:
        return HTMLResponse("<p>Lesson not found.</p>")
    return templates.TemplateResponse("lesson_content.html", {"request": request, "lesson": lesson, "user": user})

# ... rest of the code ...

def format_title(quiz_id: str) -> str:
    return ' '.join(word.capitalize() for word in quiz_id.replace('_', ' ').split())


@app.get("/quiz/{quiz_id}", response_class=HTMLResponse)
async def read_quiz(request: Request, quiz_id: str, user: Optional[dict] = Depends(get_optional_user)):
    formatted_title = format_title(quiz_id)
    quiz_data = {
        "arrays": array_quiz,
        "linked_lists": linked_list_quiz,
        "stacks": stack_quiz,
        "queues": queue_quiz,
        "hash_tables": hash_table_quiz,
        "trees": tree_quiz,
        "graphs": graph_quiz,
        "heaps": heap_quiz,
        "tries": trie_quiz,
        "sorting_algorithms": sorting_algo_questions,
        "searching_algorithms": searching_algo_questions,
        "dynamic_programming": dynamic_programming_questions,
        "greedy_algorithms": greedy_algo_questions,
        "divide_and_conquer": divide_and_conquer_questions,
        "backtracking": backtracking_questions,
        "graph_algorithms": graph_algo_questions,
        "recursive_algorithms": recursive_algo_questions,
        "string_algorithms": string_algo_questions
    }

    if quiz_id in quiz_data:
        questions = random.sample(
            quiz_data[quiz_id], min(10, len(quiz_data[quiz_id])))
        encoded_questions = base64.b64encode(
            json.dumps(questions).encode()).decode()
        quiz = {
            "title": f"Quiz on {formatted_title}",
            "description": f"Test your knowledge on {formatted_title}!",
            "questions": questions
        }
    else:
        quiz = {
            "title": f"Quiz on {formatted_title}",
            "description": f"Quiz not available for {formatted_title} yet.",
            "questions": []
        }
        encoded_questions = ""

    return templates.TemplateResponse("quiz_template.html", {
        "request": request,
        "quiz": quiz,
        "quiz_id": quiz_id,
        "encoded_questions": encoded_questions,
        "user": user
    })


@app.get("/quiz/{quiz_id}/question/{question_index}", response_class=HTMLResponse)
async def get_question(request: Request, quiz_id: str, question_index: int, encoded_questions: str = None, user: Optional[dict] = Depends(get_optional_user)):
    try:
        if encoded_questions:
            questions = json.loads(base64.b64decode(
                encoded_questions).decode('utf-8'))
        else:
            quiz_data = {
                "arrays": array_quiz,
                "linked_lists": linked_list_quiz,
                "stacks": stack_quiz,
                "queues": queue_quiz,
                "hash_tables": hash_table_quiz,
                "trees": tree_quiz,
                "graphs": graph_quiz,
                "heaps": heap_quiz,
                "tries": trie_quiz
            }
            questions = random.sample(
                quiz_data[quiz_id], min(10, len(quiz_data[quiz_id])))
            encoded_questions = base64.b64encode(
                json.dumps(questions).encode()).decode()

        if int(question_index) < len(questions):
            question = questions[int(question_index)]
            return templates.TemplateResponse("question.html", {
                "request": request,
                "question": question,
                "question_index": question_index,
                "quiz_id": quiz_id,
                "total_questions": len(questions),
                "encoded_questions": encoded_questions,
                "user": user
            })
        return HTMLResponse("Quiz completed.")
    except Exception as e:
        return HTMLResponse(f"An error occurred: {str(e)}", status_code=500)


@app.post("/quiz/{quiz_id}/submit/{question_index}", response_class=HTMLResponse)
async def submit_quiz(request: Request, quiz_id: str, question_index: int, answer: str = Form(None), encoded_questions: str = Form(None), user: Optional[dict] = Depends(get_optional_user)):
    logger.debug(
        f"Received submission for quiz {quiz_id}, question {question_index}")
    logger.debug(f"Answer: {answer}")
    logger.debug(f"Encoded questions: {encoded_questions}")

    if answer is None or encoded_questions is None:
        raise HTTPException(
            status_code=422, detail="Missing required form data")

    try:
        questions = json.loads(base64.b64decode(
            encoded_questions).decode('utf-8'))
        current_question = questions[int(question_index)]
        is_correct = answer == current_question["correct_answer"]
        next_question_index = int(question_index) + 1
        total_questions = len(questions)

        feedback_html = templates.TemplateResponse("feedback.html", {
            "request": request,
            "is_correct": is_correct,
            "correct_answer": current_question["correct_answer"],
            "explanation": current_question.get("explanation", "No explanation provided."),
            "next_question_index": next_question_index,
            "total_questions": total_questions,
            "quiz_id": quiz_id,
            "encoded_questions": encoded_questions,
            "user": user
        })

        response = f"""
        <div id="question-container">
            {feedback_html.body.decode()}
        </div>
        """

        return HTMLResponse(content=response)
    except Exception as e:
        logger.error(f"Error processing quiz submission: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.post("/quiz/{quiz_id}")
async def submit_quiz(request: Request, quiz_id: int, answer: str = Form(...), user: Optional[dict] = Depends(get_optional_user)):
    correct_answers = {
        1: "O(1)",  # Expected answer for quiz 1
        2: "Linked List",  # Expected answer for quiz 2
    }
    correct_answer = correct_answers.get(quiz_id, None)
    if answer.strip().lower() == correct_answer.lower():
        feedback = "Correct!"
    else:
        feedback = "That's not right. Review the lesson on " + (
            "Arrays" if quiz_id == 1 else "Linked Lists"
        ) + " and try again."
    question = correct_answers.get(quiz_id, "Quiz question not found.")
    return templates.TemplateResponse("quiz.html", {"request": request, "quiz_id": quiz_id, "question": question, "feedback": feedback, "user": user})


@app.get("/lessons", response_class=HTMLResponse)
async def list_lessons(request: Request, user: Optional[dict] = Depends(get_optional_user)):
    return templates.TemplateResponse("lessons.html", {"request": request, "user": user})


@app.get("/quizzes", response_class=HTMLResponse)
async def list_quizzes(request: Request, user: Optional[dict] = Depends(get_optional_user)):
    return templates.TemplateResponse("quizzes.html", {"request": request, "user": user})
