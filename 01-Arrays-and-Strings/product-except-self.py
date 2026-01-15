"""
=============================================================================
PROBLEM: PRODUCT OF ARRAY EXCEPT SELF
=============================================================================
Difficulty: Medium
Platform: LeetCode #238
Link: https://leetcode.com/problems/product-of-array-except-self/

PROBLEM STATEMENT:
Given an integer array nums, return an array answer such that answer[i] is 
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the 
division operation.

EXAMPLES:

Example 1:
  Input: nums = [1,2,3,4]
  Output: [24,12,8,6]
  Explanation:
    answer[0] = 2*3*4 = 24
    answer[1] = 1*3*4 = 12
    answer[2] = 1*2*4 = 8
    answer[3] = 1*2*3 = 6

Example 2:
  Input: nums = [-1,1,0,-3,3]
  Output: [0,0,9,0,0]

CONSTRAINTS:
- 2 <= nums.length <= 100,000
- -30 <= nums[i] <= 30
- The product of any prefix or suffix fits in 32-bit integer

FOLLOW-UP:
- Can you solve it in O(1) extra space? (Output array doesn't count)
=============================================================================
"""


# =============================================================================
# SOLUTION 1: BRUTE FORCE (TOO SLOW - FOR UNDERSTANDING)
# =============================================================================

def product_except_self_brute(nums):
    """
    Brute force: For each position, multiply all others.
    
    TIME COMPLEXITY: O(n²) ❌ Too slow!
    - For each element, iterate through all others
    
    SPACE COMPLEXITY: O(1)
    - Only output array (doesn't count)
    
    WHEN TO USE:
    - Never in interviews!
    - Just for understanding the problem
    """
    n = len(nums)
    result = []
    
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result.append(product)
    
    return result


# =============================================================================
# SOLUTION 2: USING DIVISION (NOT ALLOWED!)
# =============================================================================

def product_except_self_division(nums):
    """
    Calculate total product, then divide by each element.
    
    PROBLEM: This uses division - not allowed!
    Also fails when there are zeros.
    
    TIME COMPLEXITY: O(n)
    SPACE COMPLEXITY: O(1)
    
    WHEN TO USE:
    - Never! Problem explicitly forbids division
    - Shown here just to explain why it's not allowed
    """
    total_product = 1
    for num in nums:
        total_product *= num
    
    result = []
    for num in nums:
        result.append(total_product // num)  # Not allowed!
    
    return result


# =============================================================================
# SOLUTION 3: LEFT AND RIGHT PRODUCTS (OPTIMAL) ⭐
# =============================================================================

def product_except_self_optimal(nums):
    """
    Use left and right product arrays - O(n) time!
    
    KEY INSIGHT:
    For each position i, the product except self is:
    (product of all elements to the left) × (product of all elements to the right)
    
    HOW IT WORKS:
    1. Create left array: left[i] = product of all elements before i
    2. Create right array: right[i] = product of all elements after i
    3. Result[i] = left[i] × right[i]
    
    VISUAL EXAMPLE:
    nums = [1, 2, 3, 4]
    
    Left products (product before each position):
    left[0] = 1 (nothing before)
    left[1] = 1 (just 1)
    left[2] = 1*2 = 2 (1 and 2)
    left[3] = 1*2*3 = 6 (1, 2, and 3)
    left = [1, 1, 2, 6]
    
    Right products (product after each position):
    right[0] = 2*3*4 = 24 (2, 3, and 4)
    right[1] = 3*4 = 12 (3 and 4)
    right[2] = 4 (just 4)
    right[3] = 1 (nothing after)
    right = [24, 12, 4, 1]
    
    Result:
    result[0] = left[0] * right[0] = 1 * 24 = 24
    result[1] = left[1] * right[1] = 1 * 12 = 12
    result[2] = left[2] * right[2] = 2 * 4 = 8
    result[3] = left[3] * right[3] = 6 * 1 = 6
    result = [24, 12, 8, 6] ✓
    
    TIME COMPLEXITY: O(n)
    - Three passes through array (left, right, result)
    - 3n = O(n)
    
    SPACE COMPLEXITY: O(n)
    - left and right arrays each O(n)
    - Not including output array
    
    WHEN TO USE:
    - Good solution for interviews
    - Easy to understand and explain
    - Can be optimized further (see next solution)
    """
    n = len(nums)
    
    # Build left products
    left = [1] * n
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]
    
    # Build right products
    right = [1] * n
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]
    
    # Combine left and right
    result = []
    for i in range(n):
        result.append(left[i] * right[i])
    
    return result


# =============================================================================
# SOLUTION 4: SPACE OPTIMIZED O(1) SPACE! ⭐⭐ BEST
# =============================================================================

def product_except_self_space_optimized(nums):
    """
    O(1) space solution - use output array cleverly!
    
    KEY OPTIMIZATION:
    Instead of separate left and right arrays, we can:
    1. Build left products directly in result array
    2. Calculate right products on-the-fly and multiply
    
    This achieves O(1) extra space!
    (Output array doesn't count per problem rules)
    
    HOW IT WORKS:
    Pass 1: Fill result with left products
    Pass 2: Multiply by right products (calculated on-the-fly)
    
    VISUAL EXAMPLE:
    nums = [1, 2, 3, 4]
    
    Pass 1 (left products):
    result = [1, 1, 2, 6]
    
    Pass 2 (multiply by right products):
    Start with right = 1
    i=3: result[3] = 6 * 1 = 6, right = 1 * 4 = 4
    i=2: result[2] = 2 * 4 = 8, right = 4 * 3 = 12
    i=1: result[1] = 1 * 12 = 12, right = 12 * 2 = 24
    i=0: result[0] = 1 * 24 = 24, right = 24 * 1 = 24
    
    result = [24, 12, 8, 6] ✓
    
    TIME COMPLEXITY: O(n)
    - Two passes through array
    
    SPACE COMPLEXITY: O(1) ✓✓✓
    - Only one variable (right)
    - Output array doesn't count!
    
    WHEN TO USE:
    - BEST SOLUTION for interviews!
    - Shows optimization skills
    - What top candidates provide
    """
    n = len(nums)
    result = [1] * n
    
    # Pass 1: Build left products in result array
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]
    
    # Pass 2: Multiply by right products
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]
    
    return result


# =============================================================================
# TEST CASES
# =============================================================================

def run_all_tests():
    """Test all solutions with various test cases."""
    print("=" * 80)
    print("           TESTING PRODUCT OF ARRAY EXCEPT SELF SOLUTIONS")
    print("=" * 80)
    print()
    
    # Test Case 1: Standard example
    print("TEST 1: Standard Example [1,2,3,4]")
    print("-" * 80)
    nums1 = [1, 2, 3, 4]
    print(f"Input: {nums1}")
    print(f"Explanation:")
    print(f"  result[0] = 2*3*4 = 24")
    print(f"  result[1] = 1*3*4 = 12")
    print(f"  result[2] = 1*2*4 = 8")
    print(f"  result[3] = 1*2*3 = 6")
    print()
    print(f"Brute Force:      {product_except_self_brute(nums1)}")
    print(f"Optimal (O(n)):   {product_except_self_optimal(nums1)}")
    print(f"Space Opt (O(1)): {product_except_self_space_optimized(nums1)}")
    print(f"Expected:         [24, 12, 8, 6]")
    result1 = product_except_self_space_optimized(nums1)
    print(f"Status:           {'✓ PASS' if result1 == [24, 12, 8, 6] else '✗ FAIL'}")
    print()
    
    # Test Case 2: With zeros
    print("TEST 2: With Zeros [-1,1,0,-3,3]")
    print("-" * 80)
    nums2 = [-1, 1, 0, -3, 3]
    print(f"Input: {nums2}")
    print(f"Brute Force:      {product_except_self_brute(nums2)}")
    print(f"Optimal (O(n)):   {product_except_self_optimal(nums2)}")
    print(f"Space Opt (O(1)): {product_except_self_space_optimized(nums2)}")
    print(f"Expected:         [0, 0, 9, 0, 0]")
    result2 = product_except_self_space_optimized(nums2)
    print(f"Status:           {'✓ PASS' if result2 == [0, 0, 9, 0, 0] else '✗ FAIL'}")
    print()
    
    # Test Case 3: All same numbers
    print("TEST 3: All Same [2,2,2,2]")
    print("-" * 80)
    nums3 = [2, 2, 2, 2]
    print(f"Input: {nums3}")
    result3 = product_except_self_space_optimized(nums3)
    print(f"Space Opt (O(1)): {result3}")
    print(f"Expected:         [8, 8, 8, 8]")
    print(f"Status:           {'✓ PASS' if result3 == [8, 8, 8, 8] else '✗ FAIL'}")
    print()
    
    # Test Case 4: Two elements
    print("TEST 4: Two Elements [3,5]")
    print("-" * 80)
    nums4 = [3, 5]
    print(f"Input: {nums4}")
    result4 = product_except_self_space_optimized(nums4)
    print(f"Space Opt (O(1)): {result4}")
    print(f"Expected:         [5, 3]")
    print(f"Status:           {'✓ PASS' if result4 == [5, 3] else '✗ FAIL'}")
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
│                 │   (Too slow!)    │                 │ Understanding   │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ Division        │     O(n)         │      O(1)       │ Not allowed!    │
│                 │                  │                 │ Fails w/ zeros  │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ Left/Right ⭐    │     O(n)         │      O(n)       │ Good solution   │
│                 │                  │   (2 arrays)    │ Easy to explain │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ Space Opt ⭐⭐    │     O(n)         │      O(1)       │ BEST!           │
│ (Recommended)   │                  │   (Optimal!)    │ Top answer      │
└─────────────────┴──────────────────┴─────────────────┴─────────────────┘

Space-optimized solution is what separates good from great candidates!
"""


# =============================================================================
# INTERVIEW TIPS
# =============================================================================
"""
HOW TO ACE THIS IN AN INTERVIEW:

1. CLARIFY (30 seconds)
   • "Can I use division?" → No!
   • "What about zeros in array?" → Handle them
   • "Does output array count for space?" → No

2. START WITH BRUTE FORCE (1 minute)
   • "Naive: for each position, multiply all others"
   • "That's O(n²) - too slow"
   • Shows you understand the problem

3. EXPLAIN LEFT/RIGHT INSIGHT (2 minutes)
   • "Product except self = left product × right product"
   • "Build left products, build right products"
   • "Multiply them together"
   • Draw example: [1,2,3,4]

4. CODE THE OPTIMAL SOLUTION (5 minutes)
   • Start with O(n) space version
   • If time, optimize to O(1)

5. OPTIMIZE TO O(1) SPACE (3 minutes)
   • "Can we use result array for left products?"
   • "Calculate right products on-the-fly"
   • This really impresses interviewers!

6. WALK THROUGH EXAMPLE (2 minutes)
   nums = [1,2,3,4]
   • Show left pass: [1,1,2,6]
   • Show right pass with multiplication
   • Final: [24,12,8,6] ✓

COMMON MISTAKES:
❌ Using division (explicitly forbidden!)
❌ Not handling zeros correctly
❌ Off-by-one errors in loops
❌ Forgetting to initialize result array
❌ Not considering space optimization

BONUS POINTS:
✓ Starting with brute force, then optimizing
✓ Explaining the left×right insight clearly
✓ Providing O(1) space solution
✓ Drawing the visualization
✓ Handling zeros correctly without division

KEY PHRASES:
- "Prefix and suffix products"
- "Left products and right products"
- "Two-pass algorithm"
- "O(1) extra space optimization"
- "Division not needed"

FOLLOW-UP VARIATIONS:
- "What if division was allowed?"
  → Calculate total product, divide by each element
  → But fails with zeros!
- "What if there could be multiple zeros?"
  → Track zero count and positions
"""


# =============================================================================
# RUN TESTS
# =============================================================================
if __name__ == "__main__":
    run_all_tests()