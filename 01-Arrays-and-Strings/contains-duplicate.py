"""
=============================================================================
PROBLEM: CONTAINS DUPLICATE
=============================================================================
Difficulty: Easy
Platform: LeetCode #217
Link: https://leetcode.com/problems/contains-duplicate/

PROBLEM STATEMENT:
Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.

EXAMPLES:

Example 1:
  Input: nums = [1,2,3,1]
  Output: true
  Explanation: The number 1 appears twice

Example 2:
  Input: nums = [1,2,3,4]
  Output: false
  Explanation: All numbers are unique

Example 3:
  Input: nums = [1,1,1,3,3,4,3,2,4,2]
  Output: true
  Explanation: Multiple numbers appear more than once

CONSTRAINTS:
- 1 <= nums.length <= 100,000
- -1,000,000,000 <= nums[i] <= 1,000,000,000
=============================================================================
"""


# =============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# =============================================================================

def contains_duplicate_brute_force(nums):
    """
    Check every pair of numbers to see if any are equal.
    
    HOW IT WORKS:
    1. Take each number
    2. Compare it with all numbers after it
    3. If we find a match, return True
    4. If no matches found after checking everything, return False
    
    STEP-BY-STEP EXAMPLE:
    nums = [1, 2, 3, 1]
    
    Step 1: Check 1 (index 0) against 2, 3, 1
      - 1 vs 2? No
      - 1 vs 3? No
      - 1 vs 1? YES! Return True ✓
    
    TIME COMPLEXITY: O(n²)
    - For each number (n), we check against all others (n-1)
    - Total comparisons: n × (n-1) / 2
    
    SPACE COMPLEXITY: O(1)
    - Only using loop variables i and j
    
    WHEN TO USE:
    - Very small arrays (less than 100 elements)
    - When memory is extremely limited
    - Usually NOT the right choice for interviews
    """
    n = len(nums)
    
    # Outer loop: pick first number
    for i in range(n):
        # Inner loop: compare with all following numbers
        for j in range(i + 1, n):
            # If we find two numbers that are the same
            if nums[i] == nums[j]:
                return True  # Found a duplicate!
    
    # Checked everything, no duplicates found
    return False


# =============================================================================
# SOLUTION 2: SORTING APPROACH
# =============================================================================

def contains_duplicate_sorting(nums):
    """
    Sort the array first, then check adjacent elements.
    
    HOW IT WORKS:
    1. Sort the array
    2. After sorting, duplicates will be next to each other
    3. Check each adjacent pair
    4. If any pair is equal, return True
    
    STEP-BY-STEP EXAMPLE:
    nums = [3, 1, 2, 1]
    
    After sorting: [1, 1, 2, 3]
    
    Check adjacent pairs:
    - 1 vs 1? YES! Return True ✓
    
    TIME COMPLEXITY: O(n log n)
    - Sorting takes O(n log n)
    - Checking adjacent pairs takes O(n)
    - Total: O(n log n) dominates
    
    SPACE COMPLEXITY: O(1) or O(n)
    - Depends on sorting algorithm
    - Some sorts are in-place O(1)
    - Python's sort uses O(n) space
    
    WHEN TO USE:
    - When you can't use extra space for a hash set
    - When you need to modify the array anyway
    - Good middle-ground solution
    """
    # Make a copy so we don't modify original
    # Remove this line if modifying original is okay
    nums_copy = nums.copy()
    
    # Sort the array
    nums_copy.sort()
    
    # Check adjacent elements
    for i in range(len(nums_copy) - 1):
        # If current element equals next element
        if nums_copy[i] == nums_copy[i + 1]:
            return True  # Found a duplicate!
    
    # No adjacent duplicates found
    return False


# =============================================================================
# SOLUTION 3: HASH SET (OPTIMIZED) ⭐ RECOMMENDED
# =============================================================================

def contains_duplicate_optimal(nums):
    """
    Use a hash set to track numbers we've seen.
    
    HOW IT WORKS:
    1. Create an empty set (like a bag to store numbers)
    2. For each number in the array:
       - Check if it's already in the set
       - If yes: We found a duplicate! Return True
       - If no: Add it to the set for future checks
    3. If we finish the loop: No duplicates found
    
    STEP-BY-STEP EXAMPLE:
    nums = [1, 2, 3, 1]
    
    Start with empty set: {}
    
    Step 1: Look at 1
      - Is 1 in set? No
      - Add 1 to set: {1}
    
    Step 2: Look at 2
      - Is 2 in set? No
      - Add 2 to set: {1, 2}
    
    Step 3: Look at 3
      - Is 3 in set? No
      - Add 3 to set: {1, 2, 3}
    
    Step 4: Look at 1
      - Is 1 in set? YES! ✓
      - Return True (found duplicate!)
    
    TIME COMPLEXITY: O(n)
    - Single pass through array
    - Set lookup is O(1) on average
    - n elements × O(1) lookup = O(n)
    
    SPACE COMPLEXITY: O(n)
    - In worst case (no duplicates), set stores all n elements
    
    WHY THIS IS BEST:
    - Fastest approach: O(n) time
    - One pass through array
    - Early termination when duplicate found
    - Clean and simple code
    
    WHEN TO USE:
    - Almost always! (unless space is very limited)
    - This is what interviewers want to see
    - Industry standard approach
    """
    # Create empty set to track seen numbers
    seen = set()
    
    # Check each number
    for num in nums:
        # If we've seen this number before
        if num in seen:
            return True  # Found a duplicate!
        
        # Haven't seen this number yet, remember it
        seen.add(num)
    
    # Checked all numbers, no duplicates
    return False


# =============================================================================
# SOLUTION 4: PYTHON ONE-LINER (BONUS)
# =============================================================================

def contains_duplicate_pythonic(nums):
    """
    Elegant Python solution using set comparison.
    
    HOW IT WORKS:
    - Set automatically removes duplicates
    - If set length < array length, there were duplicates
    
    Example: [1, 2, 3, 1]
    - Array length: 4
    - Set: {1, 2, 3} → length 3
    - 3 < 4, so there are duplicates!
    
    TIME COMPLEXITY: O(n)
    SPACE COMPLEXITY: O(n)
    
    This is the same as Solution 3, just more concise.
    """
    return len(nums) != len(set(nums))


# =============================================================================
# TEST CASES
# =============================================================================

def run_all_tests():
    """
    Test all solutions with various test cases.
    """
    print("=" * 80)
    print("              TESTING CONTAINS DUPLICATE SOLUTIONS")
    print("=" * 80)
    print()
    
    # Test Case 1: Simple duplicate
    print("TEST 1: Simple Duplicate")
    print("-" * 80)
    nums1 = [1, 2, 3, 1]
    print(f"Input:  {nums1}")
    print(f"Brute Force:  {contains_duplicate_brute_force(nums1)}")
    print(f"Sorting:      {contains_duplicate_sorting(nums1)}")
    print(f"Hash Set:     {contains_duplicate_optimal(nums1)}")
    print(f"Pythonic:     {contains_duplicate_pythonic(nums1)}")
    print(f"Expected:     True")
    print(f"Status:       {'✓ PASS' if contains_duplicate_optimal(nums1) == True else '✗ FAIL'}")
    print()
    
    # Test Case 2: No duplicates
    print("TEST 2: No Duplicates")
    print("-" * 80)
    nums2 = [1, 2, 3, 4]
    print(f"Input:  {nums2}")
    print(f"Brute Force:  {contains_duplicate_brute_force(nums2)}")
    print(f"Sorting:      {contains_duplicate_sorting(nums2)}")
    print(f"Hash Set:     {contains_duplicate_optimal(nums2)}")
    print(f"Pythonic:     {contains_duplicate_pythonic(nums2)}")
    print(f"Expected:     False")
    print(f"Status:       {'✓ PASS' if contains_duplicate_optimal(nums2) == False else '✗ FAIL'}")
    print()
    
    # Test Case 3: Multiple duplicates
    print("TEST 3: Multiple Duplicates")
    print("-" * 80)
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Input:  {nums3}")
    print(f"Brute Force:  {contains_duplicate_brute_force(nums3)}")
    print(f"Sorting:      {contains_duplicate_sorting(nums3)}")
    print(f"Hash Set:     {contains_duplicate_optimal(nums3)}")
    print(f"Pythonic:     {contains_duplicate_pythonic(nums3)}")
    print(f"Expected:     True")
    print(f"Status:       {'✓ PASS' if contains_duplicate_optimal(nums3) == True else '✗ FAIL'}")
    print()
    
    # Test Case 4: Single element
    print("TEST 4: Single Element")
    print("-" * 80)
    nums4 = [1]
    print(f"Input:  {nums4}")
    print(f"Brute Force:  {contains_duplicate_brute_force(nums4)}")
    print(f"Sorting:      {contains_duplicate_sorting(nums4)}")
    print(f"Hash Set:     {contains_duplicate_optimal(nums4)}")
    print(f"Pythonic:     {contains_duplicate_pythonic(nums4)}")
    print(f"Expected:     False")
    print(f"Status:       {'✓ PASS' if contains_duplicate_optimal(nums4) == False else '✗ FAIL'}")
    print()
    
    # Test Case 5: All duplicates
    print("TEST 5: All Same Numbers")
    print("-" * 80)
    nums5 = [5, 5, 5, 5, 5]
    print(f"Input:  {nums5}")
    print(f"Brute Force:  {contains_duplicate_brute_force(nums5)}")
    print(f"Sorting:      {contains_duplicate_sorting(nums5)}")
    print(f"Hash Set:     {contains_duplicate_optimal(nums5)}")
    print(f"Pythonic:     {contains_duplicate_pythonic(nums5)}")
    print(f"Expected:     True")
    print(f"Status:       {'✓ PASS' if contains_duplicate_optimal(nums5) == True else '✗ FAIL'}")
    print()
    
    # Test Case 6: Negative numbers
    print("TEST 6: Negative Numbers")
    print("-" * 80)
    nums6 = [-1, -2, -3, -1]
    print(f"Input:  {nums6}")
    print(f"Brute Force:  {contains_duplicate_brute_force(nums6)}")
    print(f"Sorting:      {contains_duplicate_sorting(nums6)}")
    print(f"Hash Set:     {contains_duplicate_optimal(nums6)}")
    print(f"Pythonic:     {contains_duplicate_pythonic(nums6)}")
    print(f"Expected:     True")
    print(f"Status:       {'✓ PASS' if contains_duplicate_optimal(nums6) == True else '✗ FAIL'}")
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
│ Brute Force     │     O(n²)        │      O(1)       │ Tiny arrays     │
│                 │   (Very Slow)    │                 │ Never use       │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ Sorting         │   O(n log n)     │    O(1)-O(n)    │ Medium choice   │
│                 │   (Medium)       │                 │ Space limited   │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ Hash Set ⭐      │     O(n)         │      O(n)       │ BEST CHOICE     │
│ (Recommended)   │   (Fastest!)     │                 │ Use by default  │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ Pythonic        │     O(n)         │      O(n)       │ Same as above   │
│                 │   (Fastest!)     │                 │ More concise    │
└─────────────────┴──────────────────┴─────────────────┴─────────────────┘

For 100,000 elements with duplicate at position 50,000:
  • Brute Force:  ~2,500,000,000 comparisons ❌ (minutes!)
  • Sorting:      ~1,660,000 operations ⚠️ (seconds)
  • Hash Set:     ~50,000 operations ✓ (milliseconds!)
"""


# =============================================================================
# INTERVIEW TIPS
# =============================================================================
"""
HOW TO APPROACH THIS IN AN INTERVIEW:

1. CLARIFY (30 seconds)
   • "Should I return true for any duplicate, or count how many?"
   • "Can I modify the original array?"
   • "What's the expected size of the array?"

2. DISCUSS APPROACHES (2 minutes)
   Mention all three:
   • "Brute force would be O(n²) - check all pairs"
   • "We could sort and check adjacent: O(n log n)"
   • "Best is hash set for O(n) time with O(n) space"

3. CHOOSE AND CODE (3-5 minutes)
   • Usually code the hash set solution
   • It's fastest and cleanest
   • Most interviewers expect this

4. OPTIMIZE IF ASKED (1-2 minutes)
   • "If space is limited, we could use sorting"
   • "Trade-off is O(n log n) time for O(1) space"

5. TEST (1 minute)
   Walk through: [1, 2, 3, 1]
   • Show how set tracks: {} → {1} → {1,2} → {1,2,3} → found 1!

COMMON MISTAKES:
❌ Not asking about array modification
❌ Forgetting the Pythonic one-liner
❌ Not mentioning the sorting alternative
❌ Saying hash table when you mean hash set

BONUS POINTS:
✓ Mention Python's `len(set(nums)) != len(nums)` one-liner
✓ Discuss early termination benefit of hash set
✓ Know when sorting is better (space constraints)
"""


# =============================================================================
# RUN TESTS
# =============================================================================
if __name__ == "__main__":
    run_all_tests()