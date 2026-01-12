# 🌳 Trees and Binary Search Trees

Master tree data structures - fundamental for many advanced algorithms.

## 📋 Problems in This Section

| # | Problem | Difficulty | Time | Space | Key Technique | Status |
|---|---------|-----------|------|-------|---------------|--------|
| 1 | [Maximum Depth of Binary Tree](./max-depth-tree.py) | Easy | O(n) | O(h) | DFS/Recursion | ✅ |
| 2 | [Invert Binary Tree](./invert-tree.py) | Easy | O(n) | O(h) | Recursion | ⏳ |
| 3 | [Validate BST](./validate-bst.py) | Medium | O(n) | O(h) | Inorder Traversal | ⏳ |
| 4 | [Lowest Common Ancestor](./lca-bst.py) | Medium | O(h) | O(1) | BST Properties | ⏳ |

## 🎯 Key Concepts Covered

### Tree Basics
- Node structure (value, left, right)
- Root, leaves, height, depth
- Binary trees vs Binary Search Trees
- Balanced vs unbalanced trees

### Tree Traversals
- **Preorder**: Root → Left → Right
- **Inorder**: Left → Root → Right (sorted for BST!)
- **Postorder**: Left → Right → Root
- **Level Order**: BFS, level by level

### Important Patterns
1. **Recursion** - Most tree problems use recursion
2. **DFS** - Depth First Search (preorder, inorder, postorder)
3. **BFS** - Breadth First Search (level order)
4. **BST Properties** - Left < Root < Right

### Common Operations
- Finding height/depth
- Searching for values
- Inserting nodes
- Deleting nodes
- Validating BST property

## 💡 Interview Tips

- Always ask: "Is it a binary tree or BST?"
- Draw the tree on paper/whiteboard
- Recursion is your best friend for trees
- Think about base cases (null nodes, leaf nodes)
- Consider both recursive and iterative approaches

## 📚 Essential Concepts

**Tree Node Structure:**
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

**BST Property:**
- Left subtree values < root value
- Right subtree values > root value
- Both subtrees are also BSTs

**Height vs Depth:**
- Height: distance from node to deepest leaf
- Depth: distance from root to node

---

**Trees are recursive by nature! 🌳**