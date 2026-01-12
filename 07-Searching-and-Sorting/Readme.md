# 🔍 Searching and Sorting

Master fundamental algorithms - building blocks for complex problems.

## 📋 Problems in This Section

| # | Problem | Difficulty | Time | Space | Key Technique | Status |
|---|---------|-----------|------|-------|---------------|--------|
| 1 | [Binary Search](./binary-search.py) | Easy | O(log n) | O(1) | Divide & Conquer | ⏳ |
| 2 | [Search Insert Position](./search-insert.py) | Easy | O(log n) | O(1) | Binary Search | ⏳ |
| 3 | [Merge Sort](./merge-sort.py) | Medium | O(n log n) | O(n) | Divide & Conquer | ⏳ |
| 4 | [Quick Sort](./quick-sort.py) | Medium | O(n log n) | O(log n) | Divide & Conquer | ⏳ |

## 🎯 Key Concepts Covered

### Searching Algorithms
- **Linear Search**: O(n) - check every element
- **Binary Search**: O(log n) - divide and conquer
- **Two Pointers**: O(n) - efficient array traversal

### Sorting Algorithms
- **Bubble Sort**: O(n²) - simple but slow
- **Insertion Sort**: O(n²) - good for small/nearly sorted
- **Merge Sort**: O(n log n) - stable, needs extra space
- **Quick Sort**: O(n log n) avg - in-place, not stable
- **Heap Sort**: O(n log n) - in-place

### Important Patterns
1. **Binary Search** - Sorted array requirement
2. **Divide & Conquer** - Break into smaller problems
3. **In-place vs Extra Space** - Memory trade-offs
4. **Stable vs Unstable** - Relative order preservation

## 💡 Interview Tips

- Binary search: array MUST be sorted
- Always check boundaries (left, right, mid)
- Draw out small examples
- Consider edge cases (empty, one element, duplicates)
- Know time/space complexity of standard sorts

## 📚 Essential Concepts

**Binary Search Template:**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found
```

**When to Use Which Sort:**
- Small arrays (< 50): Insertion sort
- Need stable sort: Merge sort
- Need in-place: Quick sort or Heap sort
- Nearly sorted: Insertion sort
- General purpose: Quick sort (Python's default)

---

**Binary search is O(log n) magic! 🔍**