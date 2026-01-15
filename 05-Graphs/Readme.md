# 🕸️ Graphs

Master graph algorithms - essential for complex problem-solving.

## 📋 Problems in This Section

| # | Problem | Difficulty | Time | Space | Key Technique | Status |
|---|---------|-----------|------|-------|---------------|--------|
| 1 | [Number of Islands](./number-of-islands.py) | Medium | O(m×n) | O(m×n) | DFS/BFS | ✅ |
| 2 | [Clone Graph](./clone-graph.py) | Medium | O(n) | O(n) | DFS/BFS | ⏳ |
| 3 | [Course Schedule](./course-schedule.py) | Medium | O(V+E) | O(V+E) | Topological Sort | ⏳ |
| 4 | [Pacific Atlantic Water Flow](./water-flow.py) | Medium | O(m×n) | O(m×n) | DFS | ⏳ |

## 🎯 Key Concepts Covered

### Graph Basics
- **Vertices (Nodes)**: Points in the graph
- **Edges**: Connections between vertices
- **Directed vs Undirected**: One-way vs two-way edges
- **Weighted vs Unweighted**: Edges with/without values
- **Connected Components**: Separate graph sections

### Graph Representations
1. **Adjacency Matrix**: 2D array
   - grid[i][j] = 1 if edge exists
   - Good for dense graphs
   - O(V²) space

2. **Adjacency List**: Dictionary of lists
   - {node: [neighbors]}
   - Good for sparse graphs
   - O(V+E) space

3. **2D Grid**: Special case
   - Each cell connects to neighbors
   - Common in interviews

### Graph Traversal Algorithms

**Depth-First Search (DFS):**
- Go as deep as possible first
- Uses stack (or recursion)
- Good for: paths, cycles, connected components

**Breadth-First Search (BFS):**
- Explore level by level
- Uses queue
- Good for: shortest paths, nearest neighbors

### Important Patterns
1. **DFS/BFS Traversal** - Visit all nodes
2. **Cycle Detection** - Find loops
3. **Shortest Path** - BFS in unweighted graphs
4. **Topological Sort** - Ordering with dependencies
5. **Connected Components** - Find separate groups

## 💡 Interview Tips

- Always ask: "Directed or undirected?"
- Clarify graph representation
- Draw the graph first!
- Track visited nodes (crucial!)
- Consider both DFS and BFS
- Watch for edge cases (cycles, disconnected)

## 📚 Essential Concepts

**DFS Template (Recursive):**
```python
def dfs(node, visited):
    if node in visited:
        return
    
    visited.add(node)
    
    for neighbor in graph[node]:
        dfs(neighbor, visited)
```

**BFS Template (Iterative):**
```python
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = {start}
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

**4-Directional Grid Navigation:**
```python
directions = [(0,1), (1,0), (0,-1), (-1,0)]  # right, down, left, up

for dr, dc in directions:
    new_row = row + dr
    new_col = col + dc
    # Check bounds and visit
```

---

**Graphs are everywhere in real problems! 🕸️**
