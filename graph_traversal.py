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
