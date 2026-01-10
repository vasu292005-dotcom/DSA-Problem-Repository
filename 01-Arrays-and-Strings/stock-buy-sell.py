"""
=============================================================================
PROBLEM: BEST TIME TO BUY AND SELL STOCK
=============================================================================
Difficulty: Easy
Platform: LeetCode #121
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

PROBLEM STATEMENT:
You are given an array prices where prices[i] is the price of a given 
stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you 
cannot achieve any profit, return 0.

EXAMPLES:

Example 1:
  Input: prices = [7,1,5,3,6,4]
  Output: 5
  Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6)
               Profit = 6 - 1 = 5

Example 2:
  Input: prices = [7,6,4,3,1]
  Output: 0
  Explanation: Prices always decrease, no profit possible

CONSTRAINTS:
- 1 <= prices.length <= 100,000
- 0 <= prices[i] <= 10,000
- You must buy before you sell (can't sell then buy)
=============================================================================
"""


# =============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# =============================================================================

def max_profit_brute_force(prices):
    """
    Check every possible buy-sell pair.
    
    HOW IT WORKS:
    1. Try buying on each day
    2. Try selling on each future day
    3. Calculate profit for each pair
    4. Return maximum profit found
    
    STEP-BY-STEP EXAMPLE:
    prices = [7, 1, 5, 3, 6, 4]
    
    Buy day 0 (7): sell day 1(1)→-6, day 2(5)→-2, day 3(3)→-4...
    Buy day 1 (1): sell day 2(5)→4, day 3(3)→2, day 4(6)→5 ✓, day 5(4)→3
    Buy day 2 (5): sell day 3(3)→-2, day 4(6)→1, day 5(4)→-1
    ...
    Maximum profit: 5 (buy at 1, sell at 6)
    
    TIME COMPLEXITY: O(n²)
    - For each day (n), check all future days (n-1)
    - Total: n × (n-1) / 2 comparisons
    
    SPACE COMPLEXITY: O(1)
    - Only storing max_profit variable
    
    WHEN TO USE:
    - Never in real scenarios (too slow!)
    - Only mention in interviews to show you understand the problem
    """
    max_profit = 0
    n = len(prices)
    
    # Try each day as buy day
    for i in range(n):
        # Try each future day as sell day
        for j in range(i + 1, n):
            # Calculate profit
            profit = prices[j] - prices[i]
            # Update maximum
            max_profit = max(max_profit, profit)
    
    return max_profit


# =============================================================================
# SOLUTION 2: ONE PASS (OPTIMAL) ⭐ RECOMMENDED
# =============================================================================

def max_profit_optimal(prices):
    """
    Track minimum price seen so far and maximum profit.
    
    KEY INSIGHT:
    To maximize profit, we want to:
    - Buy at the LOWEST price we've seen
    - Sell at HIGHEST price after that
    
    We don't need to check all pairs!
    Just track the minimum price and calculate profit at each step.
    
    HOW IT WORKS:
    1. Start with min_price = infinity, max_profit = 0
    2. For each day:
       a. Update minimum price if current price is lower
       b. Calculate profit if we sold today (current - minimum)
       c. Update maximum profit if this profit is higher
    3. Return maximum profit
    
    STEP-BY-STEP EXAMPLE:
    prices = [7, 1, 5, 3, 6, 4]
    
    Day 0: price=7
      min_price = 7
      profit = 7-7 = 0
      max_profit = 0
    
    Day 1: price=1
      min_price = 1 (lower than 7!)
      profit = 1-1 = 0
      max_profit = 0
    
    Day 2: price=5
      min_price = 1 (still 1)
      profit = 5-1 = 4
      max_profit = 4 ✓
    
    Day 3: price=3
      min_price = 1
      profit = 3-1 = 2
      max_profit = 4
    
    Day 4: price=6
      min_price = 1
      profit = 6-1 = 5
      max_profit = 5 ✓
    
    Day 5: price=4
      min_price = 1
      profit = 4-1 = 3
      max_profit = 5
    
    Return 5!
    
    TIME COMPLEXITY: O(n)
    - Single pass through array
    - Constant time operations at each step
    
    SPACE COMPLEXITY: O(1)
    - Only two variables: min_price and max_profit
    
    WHY THIS WORKS:
    - We're doing a greedy approach
    - At each point, we know the best buy price so far
    - We calculate what profit we'd make selling today
    - This captures all possible profitable transactions!
    
    WHEN TO USE:
    - ALWAYS! This is the standard solution
    - O(n) time, O(1) space - perfect!
    - Clean and elegant
    """
    # Edge case: empty array
    if not prices:
        return 0
    
    # Initialize tracking variables
    min_price = float('inf')  # Lowest price seen so far
    max_profit = 0            # Best profit found so far
    
    # Go through each day
    for price in prices:
        # Update minimum price if we found a lower one
        if price < min_price:
            min_price = price
        
        # Calculate profit if we sold today
        # (current price - minimum price we've seen)
        profit = price - min_price
        
        # Update maximum profit if this is better
        if profit > max_profit:
            max_profit = profit
    
    return max_profit


# =============================================================================
# SOLUTION 3: SIMPLIFIED VERSION
# =============================================================================

def max_profit_simple(prices):
    """
    Same algorithm as optimal, but more concise.
    
    TIME COMPLEXITY: O(n)
    SPACE COMPLEXITY: O(1)
    
    This is exactly the same logic, just written more compactly.
    """
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit


# =============================================================================
# TEST CASES
# =============================================================================

def run_all_tests():
    """
    Test all solutions with various test cases.
    """
    print("=" * 80)
    print("           TESTING BEST TIME TO BUY/SELL STOCK SOLUTIONS")
    print("=" * 80)
    print()
    
    # Test Case 1: Basic example with profit
    print("TEST 1: Standard Case With Profit")
    print("-" * 80)
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Input:  {prices1}")
    print(f"Explanation: Buy at 1, sell at 6 → Profit = 5")
    print(f"Brute Force: {max_profit_brute_force(prices1)}")
    print(f"Optimal:     {max_profit_optimal(prices1)}")
    print(f"Simple:      {max_profit_simple(prices1)}")
    print(f"Expected:    5")
    print(f"Status:      {'✓ PASS' if max_profit_optimal(prices1) == 5 else '✗ FAIL'}")
    print()
    
    # Test Case 2: Decreasing prices (no profit)
    print("TEST 2: Always Decreasing (No Profit)")
    print("-" * 80)
    prices2 = [7, 6, 4, 3, 1]
    print(f"Input:  {prices2}")
    print(f"Explanation: Prices always go down, can't make profit")
    print(f"Brute Force: {max_profit_brute_force(prices2)}")
    print(f"Optimal:     {max_profit_optimal(prices2)}")
    print(f"Simple:      {max_profit_simple(prices2)}")
    print(f"Expected:    0")
    print(f"Status:      {'✓ PASS' if max_profit_optimal(prices2) == 0 else '✗ FAIL'}")
    print()
    
    # Test Case 3: Buy and sell same day
    print("TEST 3: Two Days")
    print("-" * 80)
    prices3 = [1, 2]
    print(f"Input:  {prices3}")
    print(f"Explanation: Buy at 1, sell at 2 → Profit = 1")
    print(f"Brute Force: {max_profit_brute_force(prices3)}")
    print(f"Optimal:     {max_profit_optimal(prices3)}")
    print(f"Simple:      {max_profit_simple(prices3)}")
    print(f"Expected:    1")
    print(f"Status:      {'✓ PASS' if max_profit_optimal(prices3) == 1 else '✗ FAIL'}")
    print()
    
    # Test Case 4: Large profit at end
    print("TEST 4: Large Profit At End")
    print("-" * 80)
    prices4 = [2, 4, 1, 7]
    print(f"Input:  {prices4}")
    print(f"Explanation: Buy at 1, sell at 7 → Profit = 6")
    print(f"Brute Force: {max_profit_brute_force(prices4)}")
    print(f"Optimal:     {max_profit_optimal(prices4)}")
    print(f"Simple:      {max_profit_simple(prices4)}")
    print(f"Expected:    6")
    print(f"Status:      {'✓ PASS' if max_profit_optimal(prices4) == 6 else '✗ FAIL'}")
    print()
    
    # Test Case 5: Single day
    print("TEST 5: Single Day (Can't Trade)")
    print("-" * 80)
    prices5 = [5]
    print(f"Input:  {prices5}")
    print(f"Explanation: Only one day, can't buy and sell")
    print(f"Brute Force: {max_profit_brute_force(prices5)}")
    print(f"Optimal:     {max_profit_optimal(prices5)}")
    print(f"Simple:      {max_profit_simple(prices5)}")
    print(f"Expected:    0")
    print(f"Status:      {'✓ PASS' if max_profit_optimal(prices5) == 0 else '✗ FAIL'}")
    print()
    
    # Test Case 6: All same price
    print("TEST 6: All Same Price")
    print("-" * 80)
    prices6 = [3, 3, 3, 3]
    print(f"Input:  {prices6}")
    print(f"Explanation: Price never changes, no profit")
    print(f"Brute Force: {max_profit_brute_force(prices6)}")
    print(f"Optimal:     {max_profit_optimal(prices6)}")
    print(f"Simple:      {max_profit_simple(prices6)}")
    print(f"Expected:    0")
    print(f"Status:      {'✓ PASS' if max_profit_optimal(prices6) == 0 else '✗ FAIL'}")
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
│ Brute Force     │     O(n²)        │      O(1)       │ Never!          │
│                 │   (Too slow)     │                 │ Too inefficient │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ One Pass ⭐      │     O(n)         │      O(1)       │ ALWAYS          │
│ (Recommended)   │   (Optimal!)     │   (Perfect!)    │ Best solution   │
└─────────────────┴──────────────────┴─────────────────┴─────────────────┘

For 100,000 stock prices:
  • Brute Force:  ~5,000,000,000 operations ❌ (minutes!)
  • One Pass:     ~100,000 operations ✓ (milliseconds!)
  
Speedup: 50,000× FASTER!
"""


# =============================================================================
# INTERVIEW TIPS
# =============================================================================
"""
HOW TO ACE THIS IN AN INTERVIEW:

1. CLARIFY (30 seconds)
   • "Can I buy and sell on the same day?" → No
   • "Can I make multiple transactions?" → No (just one buy, one sell)
   • "What if prices always decrease?" → Return 0

2. DISCUSS APPROACHES (2 minutes)
   • "Brute force: check all pairs - O(n²)"
   • "Better: track minimum price seen so far"
   • "At each day, calculate profit if we sold"
   • "This gives us O(n) time, O(1) space"

3. EXPLAIN THE INSIGHT (Important!)
   • "Key insight: we want to buy at minimum and sell at maximum AFTER"
   • "Don't need to check all pairs - just track the minimum"
   • "This is a greedy algorithm"

4. CODE (3-5 minutes)
   • Write the one-pass solution
   • Add comments explaining min_price and max_profit
   • Keep it clean and simple

5. WALK THROUGH EXAMPLE (2 minutes)
   Use [7, 1, 5, 3, 6, 4]:
   • Show how min_price updates
   • Show how max_profit gets calculated
   • Demonstrate the final answer is 5

FOLLOW-UP QUESTIONS:
Q: What if we can make multiple transactions?
A: Different problem (Stock II) - can buy/sell multiple times

Q: What if there's a transaction fee?
A: Subtract fee from each profit calculation

Q: How would you find the actual buy and sell days?
A: Store indices when we update max_profit

COMMON MISTAKES:
❌ Selling before buying (wrong order!)
❌ Trying dynamic programming (overkill for this)
❌ Not handling edge cases (single day, empty array)
❌ Forgetting that profit can be 0

BONUS POINTS:
✓ Mention this is a greedy algorithm
✓ Explain why we don't need to track buy day
✓ Discuss the follow-up problems (Stock II, III, IV)
✓ Note that O(1) space is optimal

KEY PHRASES TO USE:
- "Track the minimum price seen so far"
- "At each point, calculate potential profit"
- "Greedy approach - always use best buy price"
- "One pass through array is sufficient"
"""


# =============================================================================
# RUN TESTS
# =============================================================================
if __name__ == "__main__":
    run_all_tests()