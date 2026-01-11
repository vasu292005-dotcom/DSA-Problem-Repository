# 📚 Stacks and Queues

Master stack and queue data structures - essential for many algorithm problems.

## 📋 Problems in This Section

| # | Problem | Difficulty | Time | Space | Key Technique | Status |
|---|---------|-----------|------|-------|---------------|--------|
| 1 | [Valid Parentheses](./valid-parentheses.py) | Easy | O(n) | O(n) | Stack | ✅ |
| 2 | [Implement Queue Using Stacks](./queue-using-stacks.py) | Easy | O(1) | O(n) | Two Stacks | ⏳ |
| 3 | [Min Stack](./min-stack.py) | Medium | O(1) | O(n) | Auxiliary Stack | ⏳ |
| 4 | [Daily Temperatures](./daily-temperatures.py) | Medium | O(n) | O(n) | Monotonic Stack | ⏳ |

## 🎯 Key Concepts Covered

### Stack Operations
- Push: Add to top - O(1)
- Pop: Remove from top - O(1)
- Peek: View top - O(1)
- LIFO: Last In, First Out

### Queue Operations
- Enqueue: Add to rear - O(1)
- Dequeue: Remove from front - O(1)
- FIFO: First In, First Out

### Important Patterns
1. **Matching Pairs** - Parentheses, brackets
2. **Monotonic Stack** - Next greater/smaller element
3. **Two Stacks** - Implement queue
4. **Min/Max Tracking** - Constant time min/max

## 💡 Interview Tips

- Stacks: Think about reversing or matching
- Queues: Think about order processing
- Draw the stack state at each step
- Consider what gets pushed and when to pop
- Edge cases: empty stack, single element

## 📚 Essential Concepts

**Stack Implementation:**
```python
stack = []
stack.append(x)   # Push
stack.pop()       # Pop
stack[-1]         # Peek
```

**Queue Implementation:**
```python
from collections import deque
queue = deque()
queue.append(x)    # Enqueue
queue.popleft()    # Dequeue
```

**Common Use Cases:**
- Parentheses matching
- Expression evaluation
- Backtracking
- BFS (using queue)
- DFS (using stack)

---

**Stacks and queues are fundamental! 📚**