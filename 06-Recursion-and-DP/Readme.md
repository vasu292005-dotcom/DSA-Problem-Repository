# 🔄 Recursion and Dynamic Programming

Master recursion and DP - essential for optimization problems.

## 📋 Problems in This Section

| # | Problem | Difficulty | Time | Space | Key Technique | Status |
|---|---------|-----------|------|-------|---------------|--------|
| 1 | [Climbing Stairs](./climbing-stairs.py) | Easy | O(n) | O(1) | DP/Fibonacci | ✅ |
| 2 | [Fibonacci Number](./fibonacci.py) | Easy | O(n) | O(1) | DP | ⏳ |
| 3 | [House Robber](./house-robber.py) | Medium | O(n) | O(1) | DP | ⏳ |
| 4 | [Coin Change](./coin-change.py) | Medium | O(n×m) | O(n) | DP | ⏳ |

## 🎯 Key Concepts Covered

### Recursion Basics
- Base case (stopping condition)
- Recursive case (self-reference)
- Call stack and stack overflow
- Tail recursion optimization

### Dynamic Programming (DP)
- **Overlapping Subproblems** - Same calculations repeated
- **Optimal Substructure** - Optimal solution uses optimal subsolutions
- **Memoization** - Top-down with caching
- **Tabulation** - Bottom-up with table

### DP Approaches
1. **Top-Down (Memoization)**
   - Start from problem
   - Recursively solve subproblems
   - Cache results in memo

2. **Bottom-Up (Tabulation)**
   - Start from base cases
   - Build up to solution
   - Fill DP table iteratively

### Common DP Patterns
- Fibonacci sequence
- Climbing stairs
- 0/1 Knapsack
- Longest common subsequence
- Coin change problem

## 💡 Interview Tips

- Identify if problem has overlapping subproblems
- Start with recursive solution (brute force)
- Add memoization to optimize
- Consider converting to tabulation for space
- Draw recursion tree to visualize

## 📚 Essential Concepts

**Recursion Template:**
```python
def recursive_function(n):
    # Base case
    if n == 0:
        return base_value
    
    # Recursive case
    return recursive_function(n-1) + something
```

**DP Memoization Template:**
```python
def dp_memo(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n == 0:
        return base_value
    
    memo[n] = dp_memo(n-1, memo) + something
    return memo[n]
```

**DP Tabulation Template:**
```python
def dp_table(n):
    dp = [0] * (n + 1)
    dp[0] = base_value
    
    for i in range(1, n + 1):
        dp[i] = dp[i-1] + something
    
    return dp[n]
```

---

**DP = Recursion + Memoization! 🔄**