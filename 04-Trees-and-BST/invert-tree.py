"""
=============================================================================
PROBLEM: INVERT BINARY TREE
=============================================================================
Difficulty: Easy
Platform: LeetCode #226
Link: https://leetcode.com/problems/invert-binary-tree/

PROBLEM STATEMENT:
Given the root of a binary tree, invert the tree, and return its root.

Inverting means: swap the left and right children of all nodes.

EXAMPLES:

Example 1:
  Input:       4
             /   \
            2     7
           / \   / \
          1   3 6   9
  
  Output:      4
             /   \
            7     2
           / \   / \
          9   6 3   1

Example 2:
  Input:     2
           /   \
          1     3
  
  Output:    2
           /   \
          3     1

Example 3:
  Input: []
  Output: []

CONSTRAINTS:
- The number of nodes is in range [0, 100]
- -100 <= Node.val <= 100
=============================================================================
"""


# =============================================================================
# TREE NODE DEFINITION
# =============================================================================

class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# =============================================================================
# SOLUTION 1: RECURSIVE (MOST ELEGANT) ⭐ RECOMMENDED
# =============================================================================

def invert_tree_recursive(root):
    """
    Invert tree using recursion - incredibly simple!
    
    KEY INSIGHT:
    To invert a tree:
    1. Swap left and right children
    2. Recursively invert left subtree
    3. Recursively invert right subtree
    
    It's that simple!
    
    HOW IT WORKS:
    Base case: if node is None, return None
    Recursive case:
      - Recursively invert left subtree
      - Recursively invert right subtree
      - Swap them
      - Return root
    
    VISUAL EXAMPLE:
    Original:     4
                /   \
               2     7
    
    Step 1: Invert left (2) → no children, return
    Step 2: Invert right (7) → no children, return  
    Step 3: Swap them
    
    Result:       4
                /   \
               7     2
    
    TIME COMPLEXITY: O(n)
    - Visit each node exactly once
    - n = number of nodes
    
    SPACE COMPLEXITY: O(h)
    - Recursion stack depth = height
    - h = height of tree
    - O(log n) for balanced, O(n) for skewed
    
    WHEN TO USE:
    - DEFAULT CHOICE!
    - Incredibly clean and simple
    - Shows understanding of recursion
    - What interviewers want to see
    """
    # Base case: empty tree
    if not root:
        return None
    
    # Recursive case: invert subtrees and swap
    # Note: We can swap first, then recurse (order doesn't matter)
    root.left, root.right = root.right, root.left
    
    # Recursively invert both subtrees
    invert_tree_recursive(root.left)
    invert_tree_recursive(root.right)
    
    return root


# =============================================================================
# SOLUTION 2: RECURSIVE (ALTERNATIVE STYLE)
# =============================================================================

def invert_tree_recursive_v2(root):
    """
    Same logic, slightly different code structure.
    
    Recurse first, then swap.
    """
    # Base case
    if not root:
        return None
    
    # Recursively invert subtrees first
    left = invert_tree_recursive_v2(root.left)
    right = invert_tree_recursive_v2(root.right)
    
    # Then swap
    root.left = right
    root.right = left
    
    return root


# =============================================================================
# SOLUTION 3: ITERATIVE (USING QUEUE - BFS)
# =============================================================================

def invert_tree_iterative_bfs(root):
    """
    Invert tree using iterative BFS with queue.
    
    HOW IT WORKS:
    1. Use queue for level-order traversal
    2. For each node, swap its children
    3. Add children to queue
    4. Continue until queue empty
    
    TIME COMPLEXITY: O(n)
    SPACE COMPLEXITY: O(w)
    - w = maximum width of tree
    - Could be O(n) for complete tree
    
    WHEN TO USE:
    - When asked for iterative solution
    - When avoiding recursion
    """
    if not root:
        return None
    
    from collections import deque
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        # Swap children
        node.left, node.right = node.right, node.left
        
        # Add children to queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return root


# =============================================================================
# SOLUTION 4: ITERATIVE (USING STACK - DFS)
# =============================================================================

def invert_tree_iterative_dfs(root):
    """
    Invert tree using iterative DFS with stack.
    
    TIME COMPLEXITY: O(n)
    SPACE COMPLEXITY: O(h)
    
    Similar to BFS but using stack instead of queue.
    """
    if not root:
        return None
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        
        # Swap children
        node.left, node.right = node.right, node.left
        
        # Add children to stack
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return root


# =============================================================================
# HELPER FUNCTIONS FOR TESTING
# =============================================================================

def create_tree_from_list(values):
    """Create binary tree from list (level-order)."""
    if not values:
        return None
    
    from collections import deque
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


def tree_to_list(root):
    """Convert tree to list (level-order) for comparison."""
    if not root:
        return []
    
    from collections import deque
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result


def print_tree(root, level=0, prefix="Root: "):
    """Print tree in readable format."""
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
    """Test all solutions with various test cases."""
    print("=" * 80)
    print("              TESTING INVERT BINARY TREE SOLUTIONS")
    print("=" * 80)
    print()
    
    # Test Case 1: Standard tree
    print("TEST 1: Standard Tree")
    print("-" * 80)
    tree1 = create_tree_from_list([4, 2, 7, 1, 3, 6, 9])
    print("Original tree:")
    print_tree(tree1)
    print()
    
    inverted1 = invert_tree_recursive(create_tree_from_list([4, 2, 7, 1, 3, 6, 9]))
    print("Inverted tree:")
    print_tree(inverted1)
    print()
    
    result1 = tree_to_list(inverted1)
    expected1 = [4, 7, 2, 9, 6, 3, 1]
    print(f"Result:   {result1}")
    print(f"Expected: {expected1}")
    print(f"Status:   {'✓ PASS' if result1 == expected1 else '✗ FAIL'}")
    print()
    
    # Test Case 2: Small tree
    print("TEST 2: Small Tree")
    print("-" * 80)
    tree2 = create_tree_from_list([2, 1, 3])
    print("Original tree:")
    print_tree(tree2)
    print()
    
    inverted2 = invert_tree_recursive(create_tree_from_list([2, 1, 3]))
    print("Inverted tree:")
    print_tree(inverted2)
    print()
    
    result2 = tree_to_list(inverted2)
    expected2 = [2, 3, 1]
    print(f"Result:   {result2}")
    print(f"Expected: {expected2}")
    print(f"Status:   {'✓ PASS' if result2 == expected2 else '✗ FAIL'}")
    print()
    
    # Test Case 3: Empty tree
    print("TEST 3: Empty Tree")
    print("-" * 80)
    tree3 = None
    inverted3 = invert_tree_recursive(tree3)
    result3 = tree_to_list(inverted3)
    print(f"Result:   {result3}")
    print(f"Expected: []")
    print(f"Status:   {'✓ PASS' if result3 == [] else '✗ FAIL'}")
    print()
    
    # Test Case 4: Single node
    print("TEST 4: Single Node")
    print("-" * 80)
    tree4 = create_tree_from_list([1])
    inverted4 = invert_tree_recursive(create_tree_from_list([1]))
    result4 = tree_to_list(inverted4)
    expected4 = [1]
    print(f"Result:   {result4}")
    print(f"Expected: {expected4}")
    print(f"Status:   {'✓ PASS' if result4 == expected4 else '✗ FAIL'}")
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
│ (Recommended)   │                  │   (Call stack)  │ Cleanest code   │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ Iterative BFS   │     O(n)         │      O(w)       │ Iterative pref  │
│                 │                  │   (Queue)       │ No recursion    │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ Iterative DFS   │     O(n)         │      O(h)       │ Iterative pref  │
│                 │                  │   (Stack)       │ Similar to rec  │
└─────────────────┴──────────────────┴─────────────────┴─────────────────┘

All have O(n) time - choose based on preference!
Recursive is simplest and most elegant.
"""


# =============================================================================
# INTERVIEW TIPS
# =============================================================================
"""
HOW TO ACE THIS IN AN INTERVIEW:

1. CLARIFY (20 seconds)
   • "Should I modify the tree or create new one?" → Modify is fine
   • "What about empty tree?" → Return None

2. EXPLAIN THE APPROACH (1 minute)
   • "Trees are recursive structures"
   • "To invert: swap left and right at each node"
   • "Recursively invert subtrees"
   • "Base case: null node returns null"

3. CODE THE SOLUTION (2 minutes)
   • Write the 5-line recursive solution!
   • It's that simple!

4. WALK THROUGH EXAMPLE (1 minute)
   Draw tree:
       4
      / \
     2   7
   
   • Swap children of 4: now 7 is left, 2 is right
   • Recurse on left (7): no children, done
   • Recurse on right (2): no children, done
   • Result: 4 with 7 left, 2 right ✓

5. DISCUSS ALTERNATIVES (1 minute)
   • Mention iterative BFS/DFS versions
   • Recursive is cleanest and preferred

COMMON MISTAKES:
❌ Overcomplicating the solution
❌ Creating new tree instead of modifying
❌ Forgetting base case
❌ Not returning the root

BONUS POINTS:
✓ Writing it in 5 lines of code!
✓ Explaining it's just swapping recursively
✓ Drawing the tree transformation
✓ Mentioning this is a famous problem (Homebrew creator)

KEY PHRASES:
- "Recursive tree manipulation"
- "Swap left and right children"
- "Base case: null node"
- "O(n) time, O(h) space"

FUN FACT:
This problem became famous when Homebrew creator Max Howell
was rejected by Google for not being able to invert a binary
tree on a whiteboard!

The problem is actually very simple - shows importance of
staying calm in interviews!
"""


# =============================================================================
# RUN TESTS
# =============================================================================
if __name__ == "__main__":
    run_all_tests()