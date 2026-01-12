"""
=============================================================================
PROBLEM: MAXIMUM DEPTH OF BINARY TREE
=============================================================================
Difficulty: Easy
Platform: LeetCode #104
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

PROBLEM STATEMENT:
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest 
path from the root node down to the farthest leaf node.

EXAMPLES:

Example 1:
  Input: root = [3,9,20,null,null,15,7]
  Tree:      3
           /   \
          9    20
              /  \
             15   7
  Output: 3
  Explanation: Maximum depth is 3 (path: 3 → 20 → 15 or 3 → 20 → 7)

Example 2:
  Input: root = [1,null,2]
  Tree:    1
            \
             2
  Output: 2

Example 3:
  Input: root = []
  Output: 0

CONSTRAINTS:
- The number of nodes is in range [0, 10,000]
- -100 <= Node.val <= 100
=============================================================================
"""


# =============================================================================
# TREE NODE DEFINITION
# =============================================================================

class TreeNode:
    """
    Definition for a binary tree node.
    
    Each node contains:
    - val: the value stored in this node
    - left: reference to left child (or None)
    - right: reference to right child (or None)
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# =============================================================================
# SOLUTION 1: RECURSIVE DFS (RECOMMENDED) ⭐
# =============================================================================

def max_depth_recursive(root):
    """
    Find maximum depth using recursive Depth-First Search.
    
    KEY INSIGHT:
    The depth of a tree is:
    - 0 if tree is empty
    - 1 + max(depth of left subtree, depth of right subtree)
    
    This is a natural recursive definition!
    
    HOW IT WORKS:
    1. Base case: if node is None, depth is 0
    2. Recursively find depth of left subtree
    3. Recursively find depth of right subtree
    4. Return 1 (current node) + max of the two depths
    
    VISUAL EXAMPLE:
    Tree:      3
             /   \
            9    20
                /  \
               15   7
    
    maxDepth(3):
      left = maxDepth(9):
               left = maxDepth(None) = 0
               right = maxDepth(None) = 0
               return 1 + max(0, 0) = 1
      
      right = maxDepth(20):
                left = maxDepth(15):
                         left = maxDepth(None) = 0
                         right = maxDepth(None) = 0
                         return 1 + max(0, 0) = 1
                
                right = maxDepth(7):
                          left = maxDepth(None) = 0
                          right = maxDepth(None) = 0
                          return 1 + max(0, 0) = 1
                
                return 1 + max(1, 1) = 2
      
      return 1 + max(1, 2) = 3 ✓
    
    TIME COMPLEXITY: O(n)
    - Visit each node exactly once
    - n = number of nodes in tree
    
    SPACE COMPLEXITY: O(h)
    - Recursion stack depth = height of tree
    - h = height (worst case: O(n) for skewed tree)
    - Best case: O(log n) for balanced tree
    
    WHEN TO USE:
    - DEFAULT CHOICE for tree problems
    - Clean and intuitive
    - Matches the recursive nature of trees
    """
    # Base case: empty tree has depth 0
    if not root:
        return 0
    
    # Recursive case:
    # Find depth of left subtree
    left_depth = max_depth_recursive(root.left)
    
    # Find depth of right subtree
    right_depth = max_depth_recursive(root.right)
    
    # Current depth = 1 (current node) + max of subtree depths
    return 1 + max(left_depth, right_depth)


# =============================================================================
# SOLUTION 2: ITERATIVE BFS (Level Order)
# =============================================================================

def max_depth_bfs(root):
    """
    Find maximum depth using iterative Breadth-First Search.
    
    HOW IT WORKS:
    1. Use a queue to process nodes level by level
    2. Count the number of levels
    3. Depth = number of levels
    
    VISUAL EXAMPLE:
    Tree:      3         Level 1 (depth = 1)
             /   \
            9    20      Level 2 (depth = 2)
                /  \
               15   7    Level 3 (depth = 3)
    
    Process:
    Queue: [(3, level=1)]
    Queue: [(9, level=2), (20, level=2)]
    Queue: [(20, level=2), (15, level=3), (7, level=3)]
    Max level seen = 3 → return 3
    
    TIME COMPLEXITY: O(n)
    - Visit each node once
    
    SPACE COMPLEXITY: O(w)
    - Queue stores at most one level
    - w = maximum width of tree
    - Worst case: O(n) for complete tree
    
    WHEN TO USE:
    - When asked for iterative solution
    - When you need level-order processing
    - Good for very deep trees (no recursion stack)
    """
    if not root:
        return 0
    
    from collections import deque
    
    # Queue stores (node, depth) pairs
    queue = deque([(root, 1)])
    max_depth = 0
    
    while queue:
        node, depth = queue.popleft()
        
        # Update max depth
        max_depth = max(max_depth, depth)
        
        # Add children with incremented depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return max_depth


# =============================================================================
# SOLUTION 3: ITERATIVE DFS (Using Stack)
# =============================================================================

def max_depth_dfs_iterative(root):
    """
    Find maximum depth using iterative DFS with stack.
    
    HOW IT WORKS:
    - Use stack instead of recursion
    - Track (node, current_depth) pairs
    - Update maximum depth as we go
    
    TIME COMPLEXITY: O(n)
    SPACE COMPLEXITY: O(h) - stack depth
    
    This mimics the recursive approach but uses explicit stack.
    """
    if not root:
        return 0
    
    # Stack stores (node, depth) pairs
    stack = [(root, 1)]
    max_depth = 0
    
    while stack:
        node, depth = stack.pop()
        
        # Update max depth
        max_depth = max(max_depth, depth)
        
        # Add children with incremented depth
        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))
    
    return max_depth


# =============================================================================
# HELPER FUNCTIONS FOR TESTING
# =============================================================================

def create_tree_from_list(values):
    """
    Create binary tree from list (level-order).
    None represents missing node.
    
    Example: [3,9,20,None,None,15,7]
         3
       /   \
      9    20
          /  \
         15   7
    """
    if not values:
        return None
    
    from collections import deque
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Add left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Add right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


def print_tree(root, level=0, prefix="Root: "):
    """
    Print tree in a readable format.
    """
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")


# =============================================================================
# TEST CASES
# =============================================================================

def run_all_tests():
    """
    Test all solutions with various test cases.
    """
    print("=" * 80)
    print("          TESTING MAXIMUM DEPTH OF BINARY TREE SOLUTIONS")
    print("=" * 80)
    print()
    
    # Test Case 1: Standard tree
    print("TEST 1: Standard Tree [3,9,20,null,null,15,7]")
    print("-" * 80)
    tree1 = create_tree_from_list([3, 9, 20, None, None, 15, 7])
    print("Tree structure:")
    print_tree(tree1)
    print()
    print(f"Recursive DFS:    {max_depth_recursive(tree1)}")
    print(f"Iterative BFS:    {max_depth_bfs(tree1)}")
    print(f"Iterative DFS:    {max_depth_dfs_iterative(tree1)}")
    print(f"Expected:         3")
    result1 = max_depth_recursive(tree1)
    print(f"Status:           {'✓ PASS' if result1 == 3 else '✗ FAIL'}")
    print()
    
    # Test Case 2: Right-skewed tree
    print("TEST 2: Right-Skewed Tree [1,null,2]")
    print("-" * 80)
    tree2 = create_tree_from_list([1, None, 2])
    print("Tree structure:")
    print_tree(tree2)
    print()
    print(f"Recursive DFS:    {max_depth_recursive(tree2)}")
    print(f"Iterative BFS:    {max_depth_bfs(tree2)}")
    print(f"Iterative DFS:    {max_depth_dfs_iterative(tree2)}")
    print(f"Expected:         2")
    result2 = max_depth_recursive(tree2)
    print(f"Status:           {'✓ PASS' if result2 == 2 else '✗ FAIL'}")
    print()
    
    # Test Case 3: Empty tree
    print("TEST 3: Empty Tree []")
    print("-" * 80)
    tree3 = None
    print("Tree structure: None")
    print()
    print(f"Recursive DFS:    {max_depth_recursive(tree3)}")
    print(f"Iterative BFS:    {max_depth_bfs(tree3)}")
    print(f"Iterative DFS:    {max_depth_dfs_iterative(tree3)}")
    print(f"Expected:         0")
    result3 = max_depth_recursive(tree3)
    print(f"Status:           {'✓ PASS' if result3 == 0 else '✗ FAIL'}")
    print()
    
    # Test Case 4: Single node
    print("TEST 4: Single Node [1]")
    print("-" * 80)
    tree4 = create_tree_from_list([1])
    print("Tree structure:")
    print_tree(tree4)
    print()
    print(f"Recursive DFS:    {max_depth_recursive(tree4)}")
    print(f"Iterative BFS:    {max_depth_bfs(tree4)}")
    print(f"Iterative DFS:    {max_depth_dfs_iterative(tree4)}")
    print(f"Expected:         1")
    result4 = max_depth_recursive(tree4)
    print(f"Status:           {'✓ PASS' if result4 == 1 else '✗ FAIL'}")
    print()
    
    # Test Case 5: Deeper tree
    print("TEST 5: Deeper Tree [1,2,3,4,5,6,7,8]")
    print("-" * 80)
    tree5 = create_tree_from_list([1, 2, 3, 4, 5, 6, 7, 8])
    print("Tree structure:")
    print_tree(tree5)
    print()
    print(f"Recursive DFS:    {max_depth_recursive(tree5)}")
    print(f"Iterative BFS:    {max_depth_bfs(tree5)}")
    print(f"Iterative DFS:    {max_depth_dfs_iterative(tree5)}")
    print(f"Expected:         4")
    result5 = max_depth_recursive(tree5)
    print(f"Status:           {'✓ PASS' if result5 == 4 else '✗ FAIL'}")
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
│ Recursive ⭐     │     O(n)         │      O(h)       │ BEST CHOICE     │
│ (Recommended)   │                  │   (Call stack)  │ Most intuitive  │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ BFS (Iterative) │     O(n)         │      O(w)       │ Level-order     │
│                 │                  │   (Queue)       │ processing      │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ DFS (Iterative) │     O(n)         │      O(h)       │ Avoid recursion │
│                 │                  │   (Stack)       │ Deep trees      │
└─────────────────┴──────────────────┴─────────────────┴─────────────────┘

All have O(n) time, but space differs:
- h = height (log n for balanced, n for skewed)
- w = width (n/2 for complete tree)
"""


# =============================================================================
# INTERVIEW TIPS
# =============================================================================
"""
HOW TO ACE THIS IN AN INTERVIEW:

1. CLARIFY (30 seconds)
   • "Is it a binary tree or BST?" → Binary tree
   • "Can nodes have negative values?" → Yes
   • "What's the depth of empty tree?" → 0

2. EXPLAIN THE INSIGHT (Important!)
   • "Trees are naturally recursive"
   • "Depth = 1 + max depth of subtrees"
   • "This matches the recursive definition"

3. CODE THE SOLUTION (3 minutes)
   • Write recursive solution (simplest)
   • Handle base case (null node)
   • Recursive case (1 + max of children)

4. WALK THROUGH EXAMPLE (2 minutes)
   Draw tree and show recursion:
         3
       /   \
      9    20
          /  \
         15   7
   
   • maxDepth(3) needs maxDepth(9) and maxDepth(20)
   • maxDepth(9) = 1 (leaf node)
   • maxDepth(20) = 1 + max(1, 1) = 2
   • Final: 1 + max(1, 2) = 3

5. DISCUSS ALTERNATIVES (1 minute)
   • Mention BFS approach (level-order)
   • Mention DFS with stack (iterative)
   • Recursive is cleanest for interviews

COMMON MISTAKES:
❌ Forgetting base case (null node)
❌ Not adding 1 for current node
❌ Confusing depth with height
❌ Not considering empty tree

BONUS POINTS:
✓ Explaining recursive nature of trees
✓ Drawing the tree structure
✓ Mentioning space complexity (call stack)
✓ Discussing balanced vs skewed trees

KEY PHRASES:
- "Trees are recursive data structures"
- "Base case: null node returns 0"
- "Depth = 1 plus max of children"
- "DFS traversal"
"""


# =============================================================================
# RUN TESTS
# =============================================================================
if __name__ == "__main__":
    run_all_tests()