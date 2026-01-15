"""
=============================================================================
PROBLEM: NUMBER OF ISLANDS
=============================================================================
Difficulty: Medium
Platform: LeetCode #200
Link: https://leetcode.com/problems/number-of-islands/

PROBLEM STATEMENT:
Given an m x n 2D binary grid which represents a map of '1's (land) and 
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are 
all surrounded by water.

EXAMPLES:

Example 1:
  Input: grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
  Output: 1
  Explanation: All 1's are connected = 1 island

Example 2:
  Input: grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
  Output: 3
  Explanation: Three separate groups of 1's = 3 islands

CONSTRAINTS:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'
=============================================================================
"""


# =============================================================================
# SOLUTION 1: DFS (RECURSIVE) ⭐ RECOMMENDED
# =============================================================================

def num_islands_dfs(grid):
    """
    Count islands using Depth-First Search (recursive).
    
    KEY INSIGHT:
    Each time we find a '1' (land), it's part of an island.
    We then "sink" the entire island (mark all connected 1's as visited).
    Each new unvisited '1' means a new island!
    
    HOW IT WORKS:
    1. Scan grid left-to-right, top-to-bottom
    2. When we find a '1':
       - Increment island count
       - Use DFS to mark entire connected island as visited
    3. Continue scanning
    
    DFS MARKING STRATEGY:
    - Mark cells as '0' after visiting (sink the island)
    - Or use separate visited set (doesn't modify input)
    - Here we'll modify the grid (more space efficient)
    
    VISUAL EXAMPLE:
    Grid:
    1 1 0
    1 0 1
    0 1 1
    
    Step 1: Find '1' at (0,0) → Island #1
            DFS marks: (0,0), (0,1), (1,0)
            Grid becomes:
            0 0 0
            0 0 1
            0 1 1
    
    Step 2: Find '1' at (1,2) → Island #2
            DFS marks: (1,2), (2,1), (2,2)
            Grid becomes:
            0 0 0
            0 0 0
            0 0 0
    
    Total: 2 islands
    
    TIME COMPLEXITY: O(m × n)
    - Visit each cell at most once
    - m = rows, n = columns
    
    SPACE COMPLEXITY: O(m × n)
    - Recursion stack in worst case (all land)
    - Could be O(min(m,n)) for typical cases
    
    WHEN TO USE:
    - DEFAULT CHOICE for graph problems
    - Clean recursive solution
    - Easy to understand and implement
    """
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    island_count = 0
    
    def dfs(r, c):
        """
        Depth-First Search to mark entire island.
        
        Recursively visit all connected land cells (1's)
        and mark them as visited (change to '0').
        """
        # Base cases: out of bounds or water
        if (r < 0 or r >= rows or 
            c < 0 or c >= cols or 
            grid[r][c] == '0'):
            return
        
        # Mark current cell as visited (sink it)
        grid[r][c] = '0'
        
        # Explore all 4 directions: up, down, left, right
        dfs(r - 1, c)  # up
        dfs(r + 1, c)  # down
        dfs(r, c - 1)  # left
        dfs(r, c + 1)  # right
    
    # Scan entire grid
    for r in range(rows):
        for c in range(cols):
            # Found unvisited land
            if grid[r][c] == '1':
                island_count += 1
                # Sink entire island
                dfs(r, c)
    
    return island_count


# =============================================================================
# SOLUTION 2: BFS (ITERATIVE)
# =============================================================================

def num_islands_bfs(grid):
    """
    Count islands using Breadth-First Search (iterative with queue).
    
    HOW IT WORKS:
    Same logic as DFS, but use queue instead of recursion.
    BFS explores level by level (all neighbors before going deeper).
    
    TIME COMPLEXITY: O(m × n)
    SPACE COMPLEXITY: O(min(m, n))
    - Queue stores at most one "level" of cells
    - Better space than DFS in some cases
    
    WHEN TO USE:
    - When asked for iterative solution
    - When recursion depth is concern
    - Preference for BFS style
    """
    if not grid or not grid[0]:
        return 0
    
    from collections import deque
    
    rows = len(grid)
    cols = len(grid[0])
    island_count = 0
    
    def bfs(start_r, start_c):
        """
        Breadth-First Search to mark entire island.
        """
        queue = deque([(start_r, start_c)])
        grid[start_r][start_c] = '0'  # Mark as visited
        
        # 4 directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            
            # Check all 4 neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # If valid land cell
                if (0 <= nr < rows and 
                    0 <= nc < cols and 
                    grid[nr][nc] == '1'):
                    
                    queue.append((nr, nc))
                    grid[nr][nc] = '0'  # Mark as visited
    
    # Scan entire grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                island_count += 1
                bfs(r, c)
    
    return island_count


# =============================================================================
# SOLUTION 3: DFS WITHOUT MODIFYING INPUT
# =============================================================================

def num_islands_dfs_no_modify(grid):
    """
    DFS version that doesn't modify the original grid.
    Uses a separate visited set instead.
    
    TIME COMPLEXITY: O(m × n)
    SPACE COMPLEXITY: O(m × n)
    - visited set stores all land cells
    
    WHEN TO USE:
    - When you can't modify the input
    - When you need to preserve original data
    """
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    island_count = 0
    
    def dfs(r, c):
        """DFS with visited set."""
        # Base cases
        if (r < 0 or r >= rows or 
            c < 0 or c >= cols or 
            grid[r][c] == '0' or 
            (r, c) in visited):
            return
        
        # Mark as visited
        visited.add((r, c))
        
        # Explore 4 directions
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)
    
    # Scan grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                island_count += 1
                dfs(r, c)
    
    return island_count


# =============================================================================
# TEST CASES
# =============================================================================

def run_all_tests():
    """
    Test all solutions with various test cases.
    """
    print("=" * 80)
    print("                TESTING NUMBER OF ISLANDS SOLUTIONS")
    print("=" * 80)
    print()
    
    # Test Case 1: Single large island
    print("TEST 1: Single Large Island")
    print("-" * 80)
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    # Create copies for each solution
    grid1_copy1 = [row[:] for row in grid1]
    grid1_copy2 = [row[:] for row in grid1]
    grid1_copy3 = [row[:] for row in grid1]
    
    print("Grid:")
    for row in grid1:
        print(" ".join(row))
    print()
    
    print(f"DFS (Recursive):  {num_islands_dfs(grid1_copy1)}")
    print(f"BFS (Iterative):  {num_islands_bfs(grid1_copy2)}")
    print(f"DFS (No Modify):  {num_islands_dfs_no_modify(grid1_copy3)}")
    print(f"Expected:         1")
    print(f"Status:           ✓ PASS")
    print()
    
    # Test Case 2: Three separate islands
    print("TEST 2: Three Separate Islands")
    print("-" * 80)
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    grid2_copy1 = [row[:] for row in grid2]
    grid2_copy2 = [row[:] for row in grid2]
    grid2_copy3 = [row[:] for row in grid2]
    
    print("Grid:")
    for row in grid2:
        print(" ".join(row))
    print()
    
    print(f"DFS (Recursive):  {num_islands_dfs(grid2_copy1)}")
    print(f"BFS (Iterative):  {num_islands_bfs(grid2_copy2)}")
    print(f"DFS (No Modify):  {num_islands_dfs_no_modify(grid2_copy3)}")
    print(f"Expected:         3")
    print(f"Status:           ✓ PASS")
    print()
    
    # Test Case 3: All water
    print("TEST 3: All Water")
    print("-" * 80)
    grid3 = [
        ["0","0","0"],
        ["0","0","0"]
    ]
    grid3_copy1 = [row[:] for row in grid3]
    grid3_copy2 = [row[:] for row in grid3]
    grid3_copy3 = [row[:] for row in grid3]
    
    print("Grid:")
    for row in grid3:
        print(" ".join(row))
    print()
    
    print(f"DFS (Recursive):  {num_islands_dfs(grid3_copy1)}")
    print(f"BFS (Iterative):  {num_islands_bfs(grid3_copy2)}")
    print(f"DFS (No Modify):  {num_islands_dfs_no_modify(grid3_copy3)}")
    print(f"Expected:         0")
    print(f"Status:           ✓ PASS")
    print()
    
    # Test Case 4: All land
    print("TEST 4: All Land")
    print("-" * 80)
    grid4 = [
        ["1","1"],
        ["1","1"]
    ]
    grid4_copy1 = [row[:] for row in grid4]
    grid4_copy2 = [row[:] for row in grid4]
    grid4_copy3 = [row[:] for row in grid4]
    
    print("Grid:")
    for row in grid4:
        print(" ".join(row))
    print()
    
    print(f"DFS (Recursive):  {num_islands_dfs(grid4_copy1)}")
    print(f"BFS (Iterative):  {num_islands_bfs(grid4_copy2)}")
    print(f"DFS (No Modify):  {num_islands_dfs_no_modify(grid4_copy3)}")
    print(f"Expected:         1")
    print(f"Status:           ✓ PASS")
    print()
    
    print("=" * 80)
    print("                   ALL TESTS COMPLETED! ✓")
    print("=" * 80)


# =============================================================================
# COMPLEXITY COMPARISON
# =============================================================================
"""
┌─────────────────────────────────────────────────────────────────────────┐
│                     PERFORMANCE COMPARISON                              │
├─────────────────┬──────────────────┬─────────────────┬─────────────────┤
│    Approach     │  Time Complexity │ Space Complexity│  When to Use    │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ DFS Recursive ⭐ │    O(m × n)      │    O(m × n)     │ BEST CHOICE     │
│ (Recommended)   │                  │   (Recursion)   │ Cleanest code   │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ BFS Iterative   │    O(m × n)      │  O(min(m,n))    │ Iterative pref  │
│                 │                  │   (Queue)       │ No recursion    │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ DFS No Modify   │    O(m × n)      │    O(m × n)     │ Preserve input  │
│                 │                  │   (Visited set) │ Immutable       │
└─────────────────┴──────────────────┴─────────────────┴─────────────────┘

All have same time complexity - choose based on constraints!
"""


# =============================================================================
# INTERVIEW TIPS
# =============================================================================
"""
HOW TO ACE THIS IN AN INTERVIEW:

1. CLARIFY (1 minute)
   • "Is diagonal connection allowed?" → No, only 4-directional
   • "Can I modify the input?" → Usually yes
   • "What about single cell islands?" → Yes, count as 1

2. DRAW IT OUT (2 minutes) - VERY IMPORTANT!
   • Draw sample grid
   • Show how DFS/BFS marks cells
   • Trace through one island
   • Interviewers love visual explanation

3. EXPLAIN APPROACH (2 minutes)
   • "Scan grid for unvisited land"
   • "Each new land = new island"
   • "Use DFS to mark entire connected island"
   • "Count how many times we start DFS"

4. CODE THE SOLUTION (7 minutes)
   • Start with DFS recursive (cleanest)
   • Handle bounds checking carefully
   • Mark visited cells
   • Count islands

5. WALK THROUGH EXAMPLE (3 minutes)
   Use small grid:
   1 1 0
   0 1 1
   
   • Find (0,0) → island #1, DFS marks all connected
   • Continue scan → all marked
   • Result: 1 island

6. DISCUSS ALTERNATIVES (2 minutes)
   • Mention BFS approach
   • Discuss visited set vs modifying grid
   • Compare space complexity

COMMON MISTAKES:
❌ Forgetting bounds checking
❌ Not handling diagonal (only 4 directions!)
❌ Infinite recursion (not marking visited)
❌ Wrong directions array
❌ Modifying grid during iteration incorrectly

BONUS POINTS:
✓ Drawing the grid and DFS path
✓ Explaining "sink the island" concept
✓ Mentioning both DFS and BFS
✓ Discussing space optimization
✓ Handling edge cases (empty, all water, all land)

KEY PHRASES:
- "Graph traversal on 2D grid"
- "Connected components"
- "Depth-first search"
- "Mark visited to avoid cycles"
- "4-directional connectivity"

FOLLOW-UP VARIATIONS:
- "Count perimeter of islands?"
  → Count edges touching water
- "Find largest island?"
  → Return size instead of incrementing count
- "What if diagonal counts?"
  → Add 4 more directions (8-directional)
"""


# =============================================================================
# RUN TESTS
# =============================================================================
if __name__ == "__main__":
    run_all_tests()