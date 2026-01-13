"""
=============================================================================
PROBLEM: BINARY SEARCH
=============================================================================
Difficulty: Easy
Platform: LeetCode #704
Link: https://leetcode.com/problems/binary-search/

PROBLEM STATEMENT:
Given an array of integers nums which is sorted in ascending order, and an 
integer target, write a function to search target in nums. If target exists, 
then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

EXAMPLES:

Example 1:
  Input: nums = [-1,0,3,5,9,12], target = 9
  Output: 4
  Explanation: 9 exists in nums and its index is 4

Example 2:
  Input: nums = [-1,0,3,5,9,12], target = 2
  Output: -1
  Explanation: 2 does not exist in nums so return -1

CONSTRAINTS:
- 1 <= nums.length <= 10,000
- -10,000 < nums[i], target < 10,000
- All integers in nums are unique
- nums is sorted in ascending order
=============================================================================
"""


# =============================================================================
# SOLUTION 1: BINARY SEARCH (ITERATIVE) ⭐ RECOMMENDED
# =============================================================================

def binary_search_iterative(nums, target):
    """
    Classic binary search - divide and conquer!
    
    KEY INSIGHT:
    Array is sorted → we can eliminate half the elements at each step!
    
    If middle element is:
    - Equal to target → found it!
    - Less than target → target must be in right half
    - Greater than target → target must be in left half
    
    HOW IT WORKS:
    1. Start with left=0, right=len-1
    2. Calculate mid = (left + right) // 2
    3. Compare nums[mid] with target:
       - If equal: return mid
       - If nums[mid] < target: search right half (left = mid + 1)
       - If nums[mid] > target: search left half (right = mid - 1)
    4. Repeat until found or left > right
    
    VISUAL EXAMPLE:
    nums = [-1, 0, 3, 5, 9, 12], target = 9
    
    Step 1: left=0, right=5, mid=2
            [-1, 0, |3|, 5, 9, 12]
            nums[2]=3 < 9 → search right half
    
    Step 2: left=3, right=5, mid=4
            [-1, 0, 3, 5, |9|, 12]
            nums[4]=9 == 9 → FOUND! Return 4 ✓
    
    TIME COMPLEXITY: O(log n) ✓✓✓
    - Each step eliminates half the remaining elements
    - After k steps: n → n/2 → n/4 → ... → 1
    - Solve n / 2^k = 1 → k = log n
    
    Example: 1,000,000 elements → only 20 comparisons!
    
    SPACE COMPLEXITY: O(1)
    - Only using 3 variables (left, right, mid)
    
    WHEN TO USE:
    - DEFAULT CHOICE for searching sorted arrays
    - Industry standard
    - Much faster than linear search for large arrays
    """
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        # Calculate middle index
        # Use (left + right) // 2 but avoid overflow in other languages
        mid = left + (right - left) // 2
        
        # Check if target found
        if nums[mid] == target:
            return mid
        
        # Target is in right half
        elif nums[mid] < target:
            left = mid + 1
        
        # Target is in left half
        else:
            right = mid - 1
    
    # Target not found
    return -1


# =============================================================================
# SOLUTION 2: BINARY SEARCH (RECURSIVE)
# =============================================================================

def binary_search_recursive(nums, target, left=0, right=None):
    """
    Binary search using recursion.
    
    HOW IT WORKS:
    Same logic as iterative, but using recursion:
    - Base case: left > right → not found
    - Recursive case: search left or right half
    
    TIME COMPLEXITY: O(log n)
    SPACE COMPLEXITY: O(log n)
    - Recursion stack depth = log n
    
    WHEN TO USE:
    - When asked for recursive solution
    - Cleaner for certain variations
    - Iterative is usually preferred (less space)
    """
    # Initialize right on first call
    if right is None:
        right = len(nums) - 1
    
    # Base case: not found
    if left > right:
        return -1
    
    # Calculate mid
    mid = left + (right - left) // 2
    
    # Found target
    if nums[mid] == target:
        return mid
    
    # Search right half
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    
    # Search left half
    else:
        return binary_search_recursive(nums, target, left, mid - 1)


# =============================================================================
# SOLUTION 3: LINEAR SEARCH (FOR COMPARISON - SLOW!)
# =============================================================================

def linear_search(nums, target):
    """
    Linear search - check every element.
    
    TIME COMPLEXITY: O(n)
    - Must check every element in worst case
    
    SPACE COMPLEXITY: O(1)
    
    WHY IT'S SLOWER:
    For 1,000,000 elements:
    - Linear: up to 1,000,000 checks
    - Binary: only 20 checks!
    
    Binary is 50,000× FASTER! 🚀
    
    WHEN TO USE:
    - Array is NOT sorted
    - Array is very small (< 10 elements)
    - Only need to search once
    """
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


# =============================================================================
# TEST CASES
# =============================================================================

def run_all_tests():
    """
    Test all solutions with various test cases.
    """
    print("=" * 80)
    print("                   TESTING BINARY SEARCH SOLUTIONS")
    print("=" * 80)
    print()
    
    # Test Case 1: Target exists
    print("TEST 1: Target Exists")
    print("-" * 80)
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Iterative:    {binary_search_iterative(nums1, target1)}")
    print(f"Recursive:    {binary_search_recursive(nums1, target1)}")
    print(f"Linear:       {linear_search(nums1, target1)}")
    print(f"Expected:     4")
    result1 = binary_search_iterative(nums1, target1)
    print(f"Status:       {'✓ PASS' if result1 == 4 else '✗ FAIL'}")
    print()
    
    # Test Case 2: Target doesn't exist
    print("TEST 2: Target Doesn't Exist")
    print("-" * 80)
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Iterative:    {binary_search_iterative(nums2, target2)}")
    print(f"Recursive:    {binary_search_recursive(nums2, target2)}")
    print(f"Linear:       {linear_search(nums2, target2)}")
    print(f"Expected:     -1")
    result2 = binary_search_iterative(nums2, target2)
    print(f"Status:       {'✓ PASS' if result2 == -1 else '✗ FAIL'}")
    print()
    
    # Test Case 3: Single element (found)
    print("TEST 3: Single Element (Found)")
    print("-" * 80)
    nums3 = [5]
    target3 = 5
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Iterative:    {binary_search_iterative(nums3, target3)}")
    print(f"Recursive:    {binary_search_recursive(nums3, target3)}")
    print(f"Linear:       {linear_search(nums3, target3)}")
    print(f"Expected:     0")
    result3 = binary_search_iterative(nums3, target3)
    print(f"Status:       {'✓ PASS' if result3 == 0 else '✗ FAIL'}")
    print()
    
    # Test Case 4: Target at beginning
    print("TEST 4: Target At Beginning")
    print("-" * 80)
    nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target4 = 1
    print(f"Input: nums = {nums4}, target = {target4}")
    print(f"Iterative:    {binary_search_iterative(nums4, target4)}")
    print(f"Recursive:    {binary_search_recursive(nums4, target4)}")
    print(f"Linear:       {linear_search(nums4, target4)}")
    print(f"Expected:     0")
    result4 = binary_search_iterative(nums4, target4)
    print(f"Status:       {'✓ PASS' if result4 == 0 else '✗ FAIL'}")
    print()
    
    # Test Case 5: Target at end
    print("TEST 5: Target At End")
    print("-" * 80)
    nums5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target5 = 10
    print(f"Input: nums = {nums5}, target = {target5}")
    print(f"Iterative:    {binary_search_iterative(nums5, target5)}")
    print(f"Recursive:    {binary_search_recursive(nums5, target5)}")
    print(f"Linear:       {linear_search(nums5, target5)}")
    print(f"Expected:     9")
    result5 = binary_search_iterative(nums5, target5)
    print(f"Status:       {'✓ PASS' if result5 == 9 else '✗ FAIL'}")
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
├─────────────────┼──────────────────┼─────────────────┼─────────