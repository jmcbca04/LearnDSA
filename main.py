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
from shared import logger, get_current_user, get_optional_user, oauth2_scheme, init_db, get_user_count, get_total_logins, test_db_connection
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
async def read_lesson(request: Request, lesson_id: int):
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
                {"name": "Access", "time_complexity":
                    "O(1)", "description": "Retrieve an element at a given index."},
                {"name": "Search", "time_complexity":
                    "O(n)", "description": "Find a specific element in the array."},
                {"name": "Insert", "time_complexity":
                    "O(n)", "description": "Add an element at a specific position."},
                {"name": "Delete", "time_complexity":
                    "O(n)", "description": "Remove an element from a specific position."}
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
                {"name": "Access", "time_complexity":
                    "O(n)", "description": "Traverse the list to reach a specific element."},
                {"name": "Search", "time_complexity":
                    "O(n)", "description": "Traverse the list to find a specific element."},
                {"name": "Insert", "time_complexity": "O(1) or O(n)",
                 "description": "O(1) at the beginning, O(n) if inserting at a specific position."},
                {"name": "Delete", "time_complexity": "O(1) or O(n)",
                 "description": "O(1) at the beginning, O(n) if deleting from a specific position."}
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
                {"name": "Push", "time_complexity":
                    "O(1)", "description": "Add an element to the top of the stack."},
                {"name": "Pop", "time_complexity":
                    "O(1)", "description": "Remove and return the top element from the stack."},
                {"name": "Peek/Top", "time_complexity":
                    "O(1)", "description": "Return the top element without removing it."},
                {"name": "IsEmpty",
                    "time_complexity": "O(1)", "description": "Check if the stack is empty."}
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
                {"name": "Enqueue", "time_complexity":
                    "O(1)", "description": "Add an element to the rear of the queue."},
                {"name": "Dequeue", "time_complexity":
                    "O(1)", "description": "Remove and return the front element from the queue."},
                {"name": "Front", "time_complexity":
                    "O(1)", "description": "Return the front element without removing it."},
                {"name": "IsEmpty",
                    "time_complexity": "O(1)", "description": "Check if the queue is empty."},
                {"name": "Size", "time_complexity":
                    "O(1)", "description": "Return the number of elements in the queue."}
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
                {"name": "Insert", "time_complexity": "O(1) average",
                 "description": "Add a key-value pair to the hash table."},
                {"name": "Delete", "time_complexity": "O(1) average",
                 "description": "Remove a key-value pair from the hash table."},
                {"name": "Lookup", "time_complexity": "O(1) average",
                 "description": "Retrieve the value associated with a given key."},
                {"name": "Resize", "time_complexity":
                    "O(n)", "description": "Increase or decrease the size of the hash table and rehash all entries."}
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
                {"name": "Insert", "time_complexity": "O(log n) for balanced trees",
                 "description": "Add a new node to the tree."},
                {"name": "Delete", "time_complexity": "O(log n) for balanced trees",
                 "description": "Remove a node from the tree."},
                {"name": "Search", "time_complexity": "O(log n) for balanced trees",
                 "description": "Find a specific node in the tree."},
                {"name": "Traversal", "time_complexity":
                    "O(n)", "description": "Visit all nodes in the tree (e.g., in-order, pre-order, post-order)."}
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
                {"name": "Add Vertex",
                    "time_complexity": "O(1)", "description": "Add a new vertex to the graph."},
                {"name": "Add Edge", "time_complexity":
                    "O(1)", "description": "Add a new edge between two vertices."},
                {"name": "Remove Vertex", "time_complexity":
                    "O(|V| + |E|)", "description": "Remove a vertex and all its incident edges."},
                {"name": "Remove Edge", "time_complexity":
                    "O(1)", "description": "Remove an edge between two vertices."},
                {"name": "DFS Traversal", "time_complexity":
                    "O(|V| + |E|)", "description": "Depth-First Search traversal of the graph."},
                {"name": "BFS Traversal", "time_complexity":
                    "O(|V| + |E|)", "description": "Breadth-First Search traversal of the graph."}
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
                {"name": "Insert",
                    "time_complexity": "O(log n)", "description": "Add a new element to the heap."},
                {"name": "Delete", "time_complexity":
                    "O(log n)", "description": "Remove an element from the heap."},
                {"name": "Extract Max/Min", "time_complexity":
                    "O(log n)", "description": "Remove and return the maximum/minimum element from the heap."},
                {"name": "Heapify", "time_complexity":
                    "O(log n)", "description": "Restore the heap property after insertion or deletion."}
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

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        max_value = self.heap[0]
        last_value = self.heap.pop()
        if self.heap:
            self.heap[0] = last_value
            self._heapify_down(0)
        return max_value

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[parent_index] < self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index
        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
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
            """
        },
        9: {
            "title": "Tries (Prefix Trees)",
            "description": "A tree-like data structure that stores a dynamic set or associative array where the keys are usually strings. Tries are used to efficiently search for words in a dictionary, provide autocomplete suggestions, and implement routing algorithms.",
            "key_points": [
                "Tries are tree-like data structures that store strings.",
                "Each node in a trie represents a character in a string.",
                "The root node represents an empty string.",
                "Tries are used for efficient string searching and autocomplete suggestions.",
                "Common operations include insertion, deletion, and searching for a string."
            ],
            "operations": [
                {"name": "Insert", "time_complexity":
                    "O(m)", "description": "Add a new string to the trie, where m is the length of the string."},
                {"name": "Delete", "time_complexity":
                    "O(m)", "description": "Remove a string from the trie, where m is the length of the string."},
                {"name": "Search", "time_complexity":
                    "O(m)", "description": "Check if a string is in the trie, where m is the length of the string."},
                {"name": "Autocomplete", "time_complexity":
                    "O(m)", "description": "Find all strings in the trie that start with a given prefix."}
            ],
            "use_cases": [
                "Implementing dictionaries and autocomplete suggestions",
                "Routing algorithms in routers and network devices",
                "Spell checkers and word processors",
                "Implementing T9 (predictive text) on mobile phones",
                "Search engines and indexing"
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

    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._get_words(node, prefix)

    def _get_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child_node in node.children.items():
            words.extend(self._get_words(child_node, prefix + char))
        return words

# Usage
trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("app")

print(trie.search("apple"))  # Output: True
print(trie.search("ban"))    # Output: False
print(trie.autocomplete("app"))  # Output: ['app', 'apple']
            """
        },
        # Algorithms
        10: {
            "title": "Sorting Algorithms",
            "description": "Sorting algorithms are used to rearrange a given set of data elements in a particular order. The order can be numerical or lexicographical.",
            "key_points": [
                "Sorting algorithms arrange data elements in a specific order.",
                "Common sorting algorithms include Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, Heap Sort, and Radix Sort.",
                "The efficiency of sorting algorithms is measured by their time complexity.",
                "Stable sorting algorithms maintain the relative order of equal elements.",
                "In-place sorting algorithms use a small amount of additional memory."
            ],
            "operations": [
                {"name": "Bubble Sort", "time_complexity":
                    "O(n^2)", "description": "Repeatedly swapping adjacent elements if they are in the wrong order."},
                {"name": "Selection Sort", "time_complexity":
                    "O(n^2)", "description": "Selecting the smallest (or largest) element and swapping it with the first unsorted element."},
                {"name": "Insertion Sort", "time_complexity":
                    "O(n^2)", "description": "Inserting each element into its correct position in the sorted portion of the array."},
                {"name": "Merge Sort", "time_complexity":
                    "O(n log n)", "description": "Dividing the array into two halves, sorting them recursively, and merging them."},
                {"name": "Quick Sort", "time_complexity": "O(n log n) average, O(n^2) worst case",
                 "description": "Selecting a 'pivot' element and partitioning the array around it."},
                {"name": "Heap Sort", "time_complexity":
                    "O(n log n)", "description": "Building a max-heap from the array and repeatedly extracting the maximum element."},
                {"name": "Radix Sort", "time_complexity":
                    "O(nk)", "description": "Sorting integers by grouping them by individual digits."}
            ],
            "use_cases": [
                "Sorting data for display or analysis",
                "Implementing data structures like priority queues",
                "Database indexing and query optimization",
                "Cryptography and encryption algorithms",
                "Numerical simulations and scientific computing"
            ],
            "code_example": """
# Python example of Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Usage
```
        }
    }

    return lessons[lesson_id]


@app.get("/lessons", response_class=HTMLResponse)
async def list_lessons(request: Request, user: Optional[dict] = Depends(get_optional_user)):
    return templates.TemplateResponse("lessons.html", {"request": request, "user": user})


@app.get("/quiz/{quiz_id}", response_class=HTMLResponse)
async def quiz(request: Request, quiz_id: int, user: Optional[dict] = Depends(get_optional_user)):
    quiz_data = {
        1: array_quiz,
        2: linked_list_quiz,
        3: stack_quiz,
        4: queue_quiz,
        5: hash_table_quiz,
        6: tree_quiz,
        7: graph_quiz,
        8: heap_quiz,
        9: trie_quiz,
        10: sorting_algo_questions,
        11: searching_algo_questions,
        12: dynamic_programming_questions,
        13: greedy_algo_questions,
        14: divide_and_conquer_questions,
        15: backtracking_questions,
        16: graph_algo_questions,
        17: recursive_algo_questions,
        18: string_algo_questions
    }

    if quiz_id in quiz_data:
        quiz = quiz_data[quiz_id]
        random.shuffle(quiz["questions"])
        return templates.TemplateResponse("quiz.html", {"request": request, "quiz": quiz, "user": user})
    else:
        raise HTTPException(status_code=404, detail="Quiz not found")


@app.post("/submit-quiz")
async def submit_quiz(request: Request, answers: dict = Form(...), user: Optional[dict] = Depends(get_optional_user)):
    quiz_id = int(answers.pop("quiz_id"))
    quiz_data = {
        1: array_quiz,
        2: linked_list_quiz,
        3: stack_quiz,
        4: queue_quiz,
        5: hash_table_quiz,
        6: tree_quiz,
        7: graph_quiz,
        8: heap_quiz,
        9: trie_quiz,
        10: sorting_algo_questions,
        11: searching_algo_questions,
        12: dynamic_programming_questions,
        13: greedy_algo_questions,
        14: divide_and_conquer_questions,
        15: backtracking_questions,
        16: graph_algo_questions,
        17: recursive_algo_questions,
        18: string_algo_questions
    }

    if quiz_id in quiz_data:
        quiz = quiz_data[quiz_id]
        correct_answers = {q["id"]: q["correct_answer"] for q in quiz["questions"]}
        score = sum(correct_answers[int(q_id)] == answers[q_id] for q_id in answers)
        return templates.TemplateResponse("quiz_results.html", {"request": request, "score": score, "total": len(quiz["questions"]), "user": user})
    else:
        raise HTTPException(status_code=404, detail="Quiz not found")


@app.get("/quizzes", response_class=HTMLResponse)
async def quizzes(request: Request, user: Optional[dict] = Depends(get_optional_user)):
    return templates.TemplateResponse("quizzes.html", {"request": request, "user": user})


@app.get("/algorithms", response_class=HTMLResponse)
async def algorithms(request: Request, user: Optional[dict] = Depends(get_optional_user)):
    return templates.TemplateResponse("algorithms.html", {"request": request, "user": user})


@app.get("/data-structures", response_class=HTMLResponse)
async def data_structures(request: Request, user: Optional[dict] = Depends(get_optional_user)):
    return templates.TemplateResponse("data_structures.html", {"request": request, "user": user})


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request, user: Optional[dict] = Depends(get_optional_user)):
    return templates.TemplateResponse("about.html", {"request": request, "user": user})


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request, user: Optional[dict] = Depends(get_optional_user)):
    return templates.TemplateResponse("contact.html", {"request": request, "user": user})


@app.get("/resources", response_class=HTMLResponse)
async def resources(request: Request, user: Optional[dict] = Depends(get_optional_user)):
    return templates.TemplateResponse("resources.html", {"request": request, "user": user})


@app.get("/faq", response_class=HTMLResponse)
async def faq(request: Request, user: Optional[dict] = Depends(get_optional_user)):
    return templates.TemplateResponse("faq.html", {"request": request, "user": user})


@app.get("/privacy-policy", response_class=HTMLResponse)
async def privacy_policy(request: Request, user: Optional[dict] = Depends(get_optional_user)):
    return templates.TemplateResponse("privacy_policy.html", {"request": request, "user": user})


@app.get("/terms-of-service", response_class=HTMLResponse)
async def terms_of_service(request: Request, user: Optional[dict] = Depends(get_optional_user)):
    return templates.TemplateResponse("terms_of_service.html", {"request": request, "user": user})


@app.get("/cookie-policy", response_class=HTMLResponse)
async def cookie_policy(request: Request, user: Optional[dict] = Depends(get_optional_user)):
    return templates.TemplateResponse("cookie_policy.html", {"request": request, "user": user})


@app.get("/accessibility-statement", response_class=HTMLResponse)
async def accessibility_statement(request: Request, user: Optional[dict] = Depends(get_optional_user)):
    return templates.TemplateResponse("accessibility_statement.html", {"request": request, "user": user})


@app.get("/sitemap", response_class=HTMLResponse)
async def sitemap(request: Request, user: Optional[dict] = Depends(get_optional_user)):
    return templates.TemplateResponse("sitemap.html", {"request": request, "user": user})


@app.get("/robots.txt")
async def robots_txt():
    return "User-agent: *\nDisallow: /"


@app.get("/favicon.ico")
async def favicon():
    return RedirectResponse(url="/static/favicon.ico")


@app.get("/ads.txt")
async def ads_txt():
    return "google.com, pub-1234567890, DIRECT, f08c47fec0942fa0"


@app.get("/manifest.json")
async def manifest():
    return {
        "name": "LearnDSA",
        "short_name": "LearnDSA",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#ffffff",
        "theme_color": "#000000",
        "icons": [
            {
                "src": "/static/favicon.ico",
                "sizes": "192x192",
                "type": "image/png"
            }
        ]
    }


@app.get("/service-worker.js")
async def service_worker():
    return FileResponse("static/service-worker.js", media_type="application/javascript")


@app.get("/offline.html")
async def offline():
    return FileResponse("static/offline.html")


@app.get("/api/data")
async def get_data():
    data = {"message": "Hello, World!"}
    return data


@app.post("/api/data")
async def post_data(data: dict):
    return {"received": data}


@app.get("/api/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/api/users/{user_id}")
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
                "Backtracking explores all possible solutions to a problem.",
                "It tries out different options and undoes choices that lead to a dead end.",
                "Common backtracking problems include the N-Queens Problem, the Knight's Tour Problem, and the Traveling Salesman Problem.",
                "Backtracking often has a recursive implementation.",
                "It is suitable for problems with a large search space and a small solution space."
            ],
            "operations": [
                {"name": "N-Queens Problem", "time_complexity":
                    "O(n!)", "description": "Placing n queens on an n x n chessboard such that no two queens threaten each other."},
                {"name": "Knight's Tour Problem", "time_complexity":
                    "O(8^(n^2))", "description": "Finding a closed tour for a knight on an n x n chessboard that visits every square exactly once."},
                {"name": "Traveling Salesman Problem", "time_complexity":
                    "O(n!)", "description": "Finding the shortest possible tour that visits a given set of cities and returns to the starting city."}
            ],
            "use_cases": [
                "Solving combinatorial problems in computer science",
                "Implementing game-playing algorithms",
                "Solving optimization problems in computer networks and telecommunications",
                "Implementing algorithms for machine learning and artificial intelligence",
                "Solving puzzles and problems in mathematics and science"
            ],
            "code_example": """
# Python example of Backtracking (N-Queens Problem)

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
        print(' '.join(['Q' if cell == 1 else '.' for cell in row]))

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
            "description": "Graph algorithms are used to solve problems related to graphs, which are abstract data structures consisting of vertices (or nodes) and edges that connect these vertices.",
            "key_points": [
                "Graph algorithms are used to solve problems related to graphs.",
                "Common graph algorithms include Breadth-First Search (BFS), Depth-First Search (DFS), Dijkstra's Algorithm, Bellman-Ford Algorithm, and Kruskal's Algorithm.",
                "Graph algorithms are used in various applications, including network analysis, route planning, and social network analysis.",
                "They are also used in computer science for solving optimization problems and implementing data structures.",
                "Graph algorithms can be implemented using various data structures, such as adjacency matrices and adjacency lists."
            ],
            "operations": [
                {"name": "Breadth-First Search (BFS)", "time_complexity": "O(V + E)",
                 "description": "Exploring all vertices at the current depth before moving to the next depth."},
                {"name": "Depth-First Search (DFS)", "time_complexity": "O(V + E)",
                 "description": "Exploring as far as possible along each branch before backtracking."},
                {"name": "Dijkstra's Algorithm", "time_complexity":
                    "O(E log V)", "description": "Finding the shortest path from a source vertex to all other vertices in a weighted graph."},
                {"name": "Bellman-Ford Algorithm", "time_complexity":
                    "O(VE)", "description": "Finding the shortest path from a source vertex to all other vertices in a weighted graph, even if there are negative weights."},
                {"name": "Kruskal's Algorithm", "time_complexity":
                    "O(E log E)", "description": "Finding the minimum spanning tree of a connected, undirected graph."}
            ],
            "use_cases": [
                "Network analysis and routing",
                "Social network analysis and recommendation systems",
                "Pathfinding and route planning",
                "Optimization problems in computer networks and telecommunications",
                "Implementing data structures like disjoint sets and priority queues"
            ],
            "code_example": """
# Python example of Graph Algorithm (Breadth-First Search)

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
print("BFS traversal starting from vertex", start_vertex)
bfs(graph, start_vertex)  # Output: A B C D E F
            """
        },
        17: {
            "title": "Recursive Algorithms",
            "description": "Recursive algorithms are algorithms that solve problems by breaking them down into smaller subproblems and solving each subproblem recursively.",
            "key_points": [
                "Recursive algorithms solve problems by breaking them down into smaller subproblems.",
                "They solve each subproblem recursively and combine their solutions to solve the original problem.",
                "Common recursive algorithms include Factorial, Fibonacci, Tower of Hanoi, and Quick Sort.",
                "Recursive algorithms often have a simple and elegant implementation.",
                "They are suitable for problems that can be divided into independent subproblems."
            ],
            "operations": [
                {"name": "Factorial", "time_complexity":
                    "O(n)", "description": "Calculating the factorial of a non-negative integer n."},
                {"name": "Fibonacci", "time_complexity":
                    "O(2^n)", "description": "Calculating the nth Fibonacci number."},
                {"name": "Tower of Hanoi", "time_complexity":
                    "O(2^n)", "description": "Solving the Tower of Hanoi problem with n disks."},
                {"name": "Quick Sort", "time_complexity": "O(n log n) average, O(n^2) worst case",
                 "description": "Sorting an array by selecting a 'pivot' element and partitioning the array around it."}
            ],
            "use_cases": [
                "Solving mathematical and scientific problems",
                "Implementing efficient sorting and searching algorithms",
                "Solving optimization problems in computer networks and telecommunications",
                "Implementing algorithms for machine learning and artificial intelligence",
                "Solving combinatorial problems in computer science"
            ],
            "code_example": """
# Python example of Recursive Algorithm (Factorial)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Usage
n = 5
print(factorial(n))  # Output: 120
            """
        },
        18: {
            "title": "String Algorithms",
            "description": "String algorithms are used to manipulate and process strings, which are sequences of characters.",
            "key_points": [
                "String algorithms manipulate and process strings.",
                "Common string algorithms include string matching (e.g., Knuth-Morris-Pratt, Boyer-Moore), string searching (e.g., Rabin-Karp), and regular expressions.",
                "String algorithms are used in various applications, including text editing, data compression, and natural language processing.",
                "They are also used in computer science for implementing data structures like tries and suffix arrays.",
                "String algorithms can be implemented using various techniques, such as brute force, dynamic programming, and finite automata."
            ],
            "operations": [
                {"name": "Knuth-Morris-Pratt (KMP)", "time_complexity": "O(n + m)",
                 "description": "Finding the first occurrence of a pattern in a text."},
                {"name": "Boyer-Moore", "time_complexity": "O(n/m) average, O(nm) worst case",
                 "description": "Finding the first occurrence of a pattern in a text."},
                {"name": "Rabin-Karp", "time_complexity": "O(nm) average, O(n^2) worst case",
                 "description": "Finding the first occurrence of a pattern in a text."},
                {"name": "Regular Expressions", "time_complexity": "O(nm) average, O(n^2) worst case",
                 "description": "Matching patterns in strings using regular expressions."}
            ],
            "use_cases": [
                "Text editing and processing",
                "Data compression and encoding",
                "Natural language processing and information retrieval",
                "Implementing data structures like tries and suffix arrays",
                "Pattern matching and searching in strings"
            ],
            "code_example": """
# Python example of String Algorithm (Knuth-Morris-Pratt)

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
                print("Pattern found at index", i-j)
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
kmp_search(text, pattern)  # Output: Pattern found at index 10
            """
        }
    }
    lesson = lessons.get(lesson_id)
    if lesson is None:
        return HTMLResponse("<p>Lesson not found.</p>")
    return templates.TemplateResponse("lesson_content.html", {"request": request, "lesson": lesson, "user": user})


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
