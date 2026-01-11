# 🔗 Linked Lists

Master the fundamentals of linked list manipulation - a core data structure for interviews.

## 📋 Problems in This Section

| # | Problem | Difficulty | Time | Space | Key Technique | Status |
|---|---------|-----------|------|-------|---------------|--------|
| 1 | [Reverse Linked List](./reverse-linked-list.py) | Easy | O(n) | O(1) | Two Pointers | ✅ |
| 2 | [Merge Two Sorted Lists](./merge-sorted-lists.py) | Easy | O(n+m) | O(1) | Two Pointers | ✅ |
| 3 | [Detect Cycle](./detect-cycle.py) | Medium | O(n) | O(1) | Fast/Slow Pointers | ⏳ |
| 4 | [Remove Nth Node From End](./remove-nth-node.py) | Medium | O(n) | O(1) | Two Pointers | ⏳ |

## 🎯 Key Concepts Covered

### Linked List Basics
- Node structure (value + next pointer)
- Traversal techniques
- Pointer manipulation
- Edge cases (empty list, single node)

### Important Patterns
1. **Two Pointers** - Fast and slow pointers
2. **Dummy Node** - Simplify edge case handling
3. **In-place Reversal** - Reverse without extra space
4. **Cycle Detection** - Floyd's algorithm

### Common Operations
- Reversal (iterative and recursive)
- Merging sorted lists
- Detecting and removing cycles
- Finding middle node
- Removing nodes

## 💡 Interview Tips

- Always ask: "Is it singly or doubly linked?"
- Draw the pointers on paper/whiteboard
- Handle edge cases: null, single node, two nodes
- Practice pointer manipulation carefully
- Consider recursive vs iterative approaches

## 📚 Essential Concepts

**Node Structure:**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

**Common Patterns:**
- Dummy node: Simplifies head operations
- Runner technique: Fast/slow pointers
- Reverse in groups: Advanced pointer manipulation

---

**Let's master linked lists! 🔗**