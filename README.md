# Graph Traversal in Python: BFS and DFS by Aditya

This repository demonstrates **Graph Traversal** using two fundamental algorithms:  
1. **Breadth-First Search (BFS)**  
2. **Depth-First Search (DFS)**  

### Graph Representation
The graph is represented as an adjacency list. Below is the structure of the example graph used in this implementation:

```
Graph:
0 -> [1, 2]
1 -> [0, 3, 4]
2 -> [0, 5, 6]
3 -> [1]
4 -> [1]
5 -> [2]
6 -> [2]
```

### Algorithms

#### Breadth-First Search (BFS)
BFS explores all nodes at the present depth before moving to nodes at the next depth level. It uses a **queue** to keep track of nodes to visit.

#### Depth-First Search (DFS)
DFS explores as far as possible along each branch before backtracking. It uses **recursion** or a **stack** to manage the traversal.

---

### Code Example

#### BFS and DFS Implementation

```python
from collections import deque

# Adjacency list representation of the graph
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1],
    4: [1],
    5: [2],
    6: [2],
}

# Breadth-First Search (BFS)
def ar_bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Use a queue for BFS
    result = []  # To store the traversal order
    
    while queue:
        node = queue.popleft()  # Pop from the front of the queue
        if node not in visited:
            visited.add(node)
            result.append(node)
            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return result

# Depth-First Search (DFS)
def ar_dfs(graph, start, visited=None, result=None):
    if visited is None:
        visited = set()  # To keep track of visited nodes
    if result is None:
        result = []  # To store the traversal order
    
    visited.add(start)  # Mark the current node as visited
    result.append(start)
    
    # Recursively visit all unvisited neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            ar_dfs(graph, neighbor, visited, result)
    return result

# Starting node
start_node = 0

# Perform BFS and DFS
bfs_result = ar_bfs(graph, start_node)
dfs_result = ar_dfs(graph, start_node)

# Print results
print("Breadth-First Search (BFS):", bfs_result)
print("Depth-First Search (DFS):", dfs_result)
```

---

### Output

For the graph provided above, the traversal outputs are:

```plaintext
Breadth-First Search (BFS): [0, 1, 2, 3, 4, 5, 6]
Depth-First Search (DFS): [0, 1, 3, 4, 2, 5, 6]
```

---

### Key Points

1. **BFS Characteristics**:
   - Explores nodes layer by layer.
   - Uses a queue for traversal.
   - Suitable for finding the shortest path in an unweighted graph.

2. **DFS Characteristics**:
   - Explores as deep as possible before backtracking.
   - Uses recursion or a stack.
   - Can be used to detect cycles or paths in a graph.

---

### How to Run

1. Clone the repository:
   ```bash
   git clone git@github.com:bfouzder/Python-Graph-Traversal-BFS-DFS.git
   ```
2. Navigate to the project directory:
   ```bash
   cd graph-traversal
   ```
3. Run the Python script:
   ```bash
   python graph_traversal.py
   ```

---

### Why Used deque Instead of list?
---
1. Performance:
- list.append() is fast, but inserting or deleting at the start (list.insert(0, ...) or list.pop(0)) is slow because it shifts all elements.
- deque is optimized for such operations and handles them in constant time.
2. Convenience:
- deque provides methods like appendleft and popleft, which are not available in list.


### Future Enhancements
- Implement weighted graph traversal algorithms such as **Dijkstra's** or **A* Search**.
- Add examples of graph traversal in a directed graph.
- Provide visualization for BFS and DFS.

---

### Contributing
Feel free to fork the repository, add new features, and submit a pull request. Contributions are always welcome!

---

### License
This project is licensed under the MIT License. See the `LICENSE` file for details.
