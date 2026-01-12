"""
=============================================================================
PROBLEM: CLIMBING STAIRS
=============================================================================
Difficulty: Easy
Platform: LeetCode #70
Link: https://leetcode.com/problems/climbing-stairs/

PROBLEM STATEMENT:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways 
can you climb to the top?

EXAMPLES:

Example 1:
  Input: n = 2
  Output: 2
  Explanation: Two ways: 1+1, or 2

Example 2:
  Input: n = 3
  Output: 3
  Explanation: Three ways: 1+1+1, 1+2, or 2+1

Example 3:
  Input: n = 4
  Output: 5
  Explanation: Five ways: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2

CONSTRAINTS:
- 1 <= n <= 45
=============================================================================
"""


# =============================================================================
# SOLUTION 1: DYNAMIC PROGRAMMING - SPACE OPTIMIZED (RECOMMENDED) ⭐
# =============================================================================

def climb_stairs_optimized(n):
    """
    Find number of ways using DP with O(1) space.
    
    KEY INSIGHT:
    This is a Fibonacci sequence!
    - To reach step n, you came from step (n-1) or (n-2)
    - ways(n) = ways(n-1) + ways(n-2)
    
    WHY IT'S FIBONACCI:
    - Step 1: 1 way  (just 1)
    - Step 2: 2 ways (1+1 or 2)
    - Step 3: 3 ways (ways to reach 2 + ways to reach 1)
    - Step 4: 5 ways (3 + 2)
    - Step 5: 8 ways (5 + 3)
    - Pattern: 1, 2, 3, 5, 8, 13, 21...
    
    HOW IT WORKS:
    Instead of storing all values, just keep last two:
    - prev2 = ways to reach (n-2)
    - prev1 = ways to reach (n-1)
    - current = prev1 + prev2
    
    VISUAL EXAMPLE (n=5):
    Step 1: prev2=1, prev1=2, current=3
    Step 2: prev2=2, prev1=3, current=5
    Step 3: prev2=3, prev1=5, current=8
    Result: 8 ways
    
    TIME COMPLEXITY: O(n)
    - Single pass through n steps
    
    SPACE COMPLEXITY: O(1)
    - Only 2 variables regardless of n
    - BEST SPACE EFFICIENCY!
    
    WHEN TO USE:
    - DEFAULT CHOICE for interviews
    - Best balance of clarity and efficiency
    - Shows understanding of space optimization
    """
    # Edge cases
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # Initialize for Fibonacci sequence
    # prev2 represents ways(n-2), prev1 represents ways(n-1)
    prev2 = 1  # ways to reach step 1
    prev1 = 2  # ways to reach step 2
    
    # Build up from step 3 to n
    for i in range(3, n + 1):
        current = prev1 + prev2
        # Slide the window forward
        prev2 = prev1
        prev1 = current
    
    return prev1


# =============================================================================
# SOLUTION 2: DYNAMIC PROGRAMMING - TABULATION
# =============================================================================

def climb_stairs_tabulation(n):
    """
    Find number of ways using DP table (bottom-up).
    
    HOW IT WORKS:
    1. Create array to store results for each step
    2. Fill base cases (steps 1 and 2)
    3. Build up: dp[i] = dp[i-1] + dp[i-2]
    
    VISUAL EXAMPLE (n=5):
    dp = [0, 1, 2, 0, 0, 0]  # base cases
    dp = [0, 1, 2, 3, 0, 0]  # dp[3] = dp[2] + dp[1] = 2 + 1 = 3
    dp = [0, 1, 2, 3, 5, 0]  # dp[4] = dp[3] + dp[2] = 3 + 2 = 5
    dp = [0, 1, 2, 3, 5, 8]  # dp[5] = dp[4] + dp[3] = 5 + 3 = 8
    
    TIME COMPLEXITY: O(n)
    SPACE COMPLEXITY: O(n) - dp array
    
    WHEN TO USE:
    - When you want to see all intermediate results
    - Learning DP concepts
    - Debugging purposes
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # Create DP table
    dp = [0] * (n + 1)
    
    # Base cases
    dp[1] = 1  # 1 way to reach step 1
    dp[2] = 2  # 2 ways to reach step 2
    
    # Fill the table
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


# =============================================================================
# SOLUTION 3: RECURSION WITH MEMOIZATION (Top-Down)
# =============================================================================

def climb_stairs_memoization(n, memo=None):
    """
    Find number of ways using recursion with memoization.
    
    HOW IT WORKS:
    1. Solve recursively: ways(n) = ways(n-1) + ways(n-2)
    2. Cache results to avoid recomputation
    3. Check cache before computing
    
    RECURSION TREE (without memo) for n=5:
                        f(5)
                    /          \
                f(4)              f(3)
              /      \           /     \
          f(3)       f(2)     f(2)    f(1)
         /   \        
      f(2)  f(1)     
    
    Notice: f(3) computed twice, f(2) computed 3 times!
    Memoization prevents recomputation.
    
    TIME COMPLEXITY: O(n)
    - Each subproblem computed once
    
    SPACE COMPLEXITY: O(n)
    - Memo dictionary + recursion stack
    
    WHEN TO USE:
    - When asked for recursive solution
    - To demonstrate memoization concept
    - Natural top-down thinking
    """
    # Initialize memo dictionary
    if memo is None:
        memo = {}
    
    # Base cases
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # Check if already computed
    if n in memo:
        return memo[n]
    
    # Recursive case with memoization
    memo[n] = climb_stairs_memoization(n - 1, memo) + climb_stairs_memoization(n - 2, memo)
    
    return memo[n]


# =============================================================================
# SOLUTION 4: PURE RECURSION (For Understanding Only)
# =============================================================================

def climb_stairs_recursive(n):
    """
    Pure recursive solution WITHOUT memoization.
    
    WARNING: This is VERY SLOW for large n!
    Time complexity: O(2^n) - exponential!
    
    Only use this to understand the problem,
    then optimize with memoization or DP.
    
    DO NOT USE IN INTERVIEWS (too slow)
    """
    # Base cases
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # Recursive case
    return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)


# =============================================================================
# SOLUTION 5: MATHEMATICAL FORMULA (Advanced)
# =============================================================================

def climb_stairs_formula(n):
    """
    Using Fibonacci formula (Binet's formula).
    
    Fibonacci: F(n) = (φ^n - ψ^n) / √5
    where φ = (1 + √5) / 2 (golden ratio)
          ψ = (1 - √5) / 2
    
    Since climbing stairs follows Fibonacci shifted by 1,
    we need the (n+1)th Fibonacci number.
    
    TIME COMPLEXITY: O(1)
    SPACE COMPLEXITY: O(1)
    
    NOTE: May have floating point precision issues
    Use only if interviewer asks for O(1) time
    """
    import math
    
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    
    # (n+1)th Fibonacci number
    result = (phi ** (n + 1) - psi ** (n + 1)) / sqrt5
    
    return int(round(result))


# =============================================================================
# TEST CASES
# =============================================================================

def run_all_tests():
    """
    Test all solutions with various test cases.
    """
    print("=" * 80)
    print("            TESTING CLIMBING STAIRS SOLUTIONS")
    print("=" * 80)
    print()
    
    test_cases = [
        (1, 1, "Single step"),
        (2, 2, "Two steps (base case)"),
        (3, 3, "Three steps"),
        (4, 5, "Four steps"),
        (5, 8, "Five steps"),
        (10, 89, "Ten steps"),
        (20, 10946, "Twenty steps"),
    ]
    
    for i, (n, expected, description) in enumerate(test_cases, 1):
        print(f"TEST {i}: {description} (n={n})")
        print("-" * 80)
        
        # Test all solutions
        result_optimized = climb_stairs_optimized(n)
        result_tabulation = climb_stairs_tabulation(n)
        result_memo = climb_stairs_memoization(n)
        result_formula = climb_stairs_formula(n)
        
        # Only test pure recursion for small n (it's too slow!)
        if n <= 10:
            result_recursive = climb_stairs_recursive(n)
        else:
            result_recursive = "Skipped (too slow)"
        
        print(f"DP Optimized (O(1) space): {result_optimized}")
        print(f"DP Tabulation (O(n) space): {result_tabulation}")
        print(f"Memoization:              {result_memo}")
        print(f"Pure Recursion:           {result_recursive}")
        print(f"Mathematical Formula:     {result_formula}")
        print(f"Expected:                 {expected}")
        
        passed = result_optimized == expected
        print(f"Status:                   {'✓ PASS' if passed else '✗ FAIL'}")
        print()
    
    print("=" * 80)
    print("                   ALL TESTS COMPLETED! ✓")
    print("=" * 80)


# =============================================================================
# STEP-BY-STEP EXAMPLE
# =============================================================================

def demonstrate_algorithm():
    """
    Show how the optimized algorithm works step-by-step.
    """
    print("=" * 80)
    print("        STEP-BY-STEP DEMONSTRATION: CLIMBING 5 STAIRS")
    print("=" * 80)
    print()
    
    n = 5
    print(f"Finding number of ways to climb {n} stairs...")
    print()
    
    print("Initial state:")
    print("  prev2 = 1 (ways to reach step 1)")
    print("  prev1 = 2 (ways to reach step 2)")
    print()
    
    prev2 = 1
    prev1 = 2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        print(f"Step {i}:")
        print(f"  current = prev1 + prev2 = {prev1} + {prev2} = {current}")
        print(f"  Update: prev2={prev1}, prev1={current}")
        print()
        
        prev2 = prev1
        prev1 = current
    
    print(f"Final answer: {prev1} ways to climb {n} stairs")
    print()
    
    print("The 5 ways are:")
    print("  1. 1+1+1+1+1")
    print("  2. 1+1+1+2")
    print("  3. 1+1+2+1")
    print("  4. 1+2+1+1")
    print("  5. 2+1+1+1")
    print("  6. 1+2+2")
    print("  7. 2+1+2")
    print("  8. 2+2+1")
    print()
    print("(Actually 8 ways - it's the 5th Fibonacci number!)")
    print()


# =============================================================================
# COMPLEXITY COMPARISON
# =============================================================================
"""
┌─────────────────────────────────────────────────────────────────────────┐
│                     PERFORMANCE COMPARISON                              │
├──────────────────┬──────────────────┬─────────────────┬────────────────┤
│    Approach      │  Time Complexity │ Space Complexity│  Recommend?    │
├──────────────────┼──────────────────┼─────────────────┼────────────────┤
│ DP Optimized ⭐   │     O(n)         │      O(1)       │ YES - BEST!    │
│                  │                  │                 │                │
├──────────────────┼──────────────────┼─────────────────┼────────────────┤
│ DP Tabulation    │     O(n)         │      O(n)       │ Good for       │
│                  │                  │                 │ learning       │
├──────────────────┼──────────────────┼─────────────────┼────────────────┤
│ Memoization      │     O(n)         │      O(n)       │ Good for       │
│                  │                  │                 │ recursive sols │
├──────────────────┼──────────────────┼─────────────────┼────────────────┤
│ Pure Recursion   │     O(2^n)       │      O(n)       │ NO - Too slow! │
│                  │                  │                 │                │
├──────────────────┼──────────────────┼─────────────────┼────────────────┤
│ Math Formula     │     O(1)         │      O(1)       │ Only if asked  │
│                  │                  │                 │ (precision!)   │
└──────────────────┴──────────────────┴─────────────────┴────────────────┘

For n=20:
- Pure recursion: ~21,000 operations (2^20)
- DP/Memoization: ~20 operations
- 1000x faster!
"""


# =============================================================================
# INTERVIEW TIPS
# =============================================================================
"""
HOW TO ACE THIS IN AN INTERVIEW:

1. RECOGNIZE THE PATTERN (Important!)
   • "This looks like a Fibonacci problem"
   • "To reach step n, I need ways(n-1) + ways(n-2)"
   • "Let me verify with small examples"

2. START WITH EXAMPLES (Draw it out!)
   n=1: [1] → 1 way
   n=2: [1,1], [2] → 2 ways
   n=3: [1,1,1], [1,2], [2,1] → 3 ways
   n=4: ... → 5 ways
   Pattern: 1, 2, 3, 5, 8... (Fibonacci!)

3. EXPLAIN YOUR APPROACH
   • "I'll use DP with O(1) space"
   • "Only need last two values, not whole array"
   • "Slide window forward: prev2 → prev1 → current"

4. CODE CLEANLY (5 minutes)
   • Handle edge cases (n=1, n=2)
   • Use clear variable names
   • Add comments for clarity

5. DISCUSS ALTERNATIVES
   • Mention memoization approach
   • Explain why O(1) space is better
   • Note that pure recursion is too slow

COMMON MISTAKES:
❌ Using pure recursion (O(2^n) - too slow!)
❌ Forgetting base cases
❌ Off-by-one errors in loop
❌ Not recognizing Fibonacci pattern

BONUS POINTS:
✓ Immediately recognizing Fibonacci
✓ Drawing small examples
✓ Explaining space optimization
✓ Mentioning time complexity improvement

KEY PHRASES TO SAY:
- "This is a classic DP problem"
- "Follows Fibonacci sequence"
- "Can optimize space to O(1)"
- "Previous two values determine current"

FOLLOW-UP QUESTIONS:
Q: What if you can climb 1, 2, or 3 steps?
A: Same pattern: ways(n) = ways(n-1) + ways(n-2) + ways(n-3)

Q: What's the maximum n you can handle?
A: Algorithm works for any n, but result might overflow
   For n=45, answer is ~1.8 billion (within int range)
"""


# =============================================================================
# RUN TESTS
# =============================================================================
if __name__ == "__main__":
    run_all_tests()
    print()
    demonstrate_algorithm()