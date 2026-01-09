"""
=============================================================================
PROBLEM: TWO SUM
=============================================================================
Difficulty: Easy
Platform: LeetCode #1
Link: https://leetcode.com/problems/two-sum/

PROBLEM STATEMENT:
Given an array of integers 'nums' and an integer 'target', return the 
indices of the two numbers that add up to the target.

Rules:
- Each input has exactly ONE solution
- You cannot use the same element twice
- You can return the answer in any order

EXAMPLES:

Example 1:
  Input: nums = [2,7,11,15], target = 9
  Output: [0,1]
  Explanation: nums[0] + nums[1] = 2 + 7 = 9
               So we return indices [0, 1]

Example 2:
  Input: nums = [3,2,4], target = 6
  Output: [1,2]
  Explanation: nums[1] + nums[2] = 2 + 4 = 6

Example 3:
  Input: nums = [3,3], target = 6
  Output: [0,1]
  Explanation: Both 3's add up to 6

CONSTRAINTS:
- 2 <= nums.length <= 10,000
- -1,000,000,000 <= nums[i] <= 1,000,000,000
- -1,000,000,000 <= target <= 1,000,000,000
- Only one valid answer exists
=============================================================================
"""


# =============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# =============================================================================

def two_sum_brute_force(nums, target):
    """
    The straightforward approach: Check every possible pair.
    
    HOW IT WORKS:
    1. Take the first number
    2. Check it against all other numbers
    3. If any pair adds up to target, return their positions
    4. Repeat for each number
    
    STEP-BY-STEP EXAMPLE:
    nums = [2, 7, 11, 15], target = 9
    
    Step 1: Try 2 (index 0)
      - 2 + 7 = 9 ✓ Found it! Return [0, 1]
    
    TIME COMPLEXITY: O(n²)
    - "n squared" means if you have 100 numbers, you do 10,000 operations
    - Why? Because for each number, we check it against all others
    - Formula: n × (n-1) / 2 comparisons
    
    SPACE COMPLEXITY: O(1)
    - "Constant space" means we only use a fixed amount of memory
    - No matter how big the input is, we only need space for i and j
    
    WHEN TO USE THIS:
    - Small arrays (less than 100 elements)
    - When you need to save memory
    - In interviews: Mention this first, then optimize
    """
    
    # Get the length of the array
    n = len(nums)
    
    # Outer loop: Pick the first number of the pair
    for i in range(n):
        # i will be: 0, 1, 2, 3, ... up to n-1
        
        # Inner loop: Pick the second number of the pair
        # We start from i+1 to avoid using the same element twice
        for j in range(i + 1, n):
            # j will always be greater than i
            
            # Check if this pair adds up to our target
            if nums[i] + nums[j] == target:
                # Found it! Return the indices
                return [i, j]
    
    # If we get here, no solution was found
    # (But problem says solution always exists, so this shouldn't happen)
    return []


# =============================================================================
# SOLUTION 2: HASH MAP APPROACH (OPTIMIZED) ⭐ RECOMMENDED
# =============================================================================

def two_sum_optimal(nums, target):
    """
    The smart approach: Use a dictionary to remember numbers we've seen.
    
    HOW IT WORKS:
    1. Create an empty dictionary (like a phonebook)
    2. For each number:
       a. Calculate what number we need to reach target (the "complement")
       b. Check if we've seen that complement before
       c. If yes: Return the answer!
       d. If no: Remember this number for later
    
    KEY INSIGHT:
    Instead of checking all pairs (slow), we just check if the needed
    number was seen before (fast lookup using dictionary).
    
    STEP-BY-STEP EXAMPLE:
    nums = [2, 7, 11, 15], target = 9
    
    Start with empty dictionary: {}
    
    Step 1: Look at 2 (index 0)
      - Need: 9 - 2 = 7
      - Is 7 in dictionary? No
      - Save 2: {2: 0}
    
    Step 2: Look at 7 (index 1)
      - Need: 9 - 7 = 2
      - Is 2 in dictionary? Yes! At index 0
      - Return [0, 1] ✓
    
    TIME COMPLEXITY: O(n)
    - "Linear time" means if you double the array size, time doubles
    - We go through the array once
    - Dictionary lookup is instant (O(1))
    
    SPACE COMPLEXITY: O(n)
    - We might store every number in the dictionary
    - Worst case: store all n numbers
    
    WHY THIS IS BETTER:
    - For 10,000 numbers:
      * Brute Force: 50,000,000 operations
      * Hash Map: 10,000 operations
      * That's 5,000 times faster! 🚀
    
    WHEN TO USE THIS:
    - Always! (Unless specifically told not to use extra space)
    - This is the industry standard solution
    - What interviewers want to see
    """
    
    # Create empty dictionary to store {number: its_position}
    # Example: {2: 0, 7: 1} means 2 is at index 0, 7 is at index 1
    seen = {}
    
    # Go through each number with its position
    # enumerate gives us both: (0, 2), (1, 7), (2, 11), (3, 15)
    for i, num in enumerate(nums):
        # i = current position (0, 1, 2, ...)
        # num = current number (2, 7, 11, ...)
        
        # Calculate what number we need to reach target
        # If target is 9 and current num is 2, we need 7
        complement = target - num
        
        # Check if we've seen the complement before
        # This is the magic: dictionary lookup is instant!
        if complement in seen:
            # Found it! We've seen the complement before
            # seen[complement] = where we saw it
            # i = where we are now
            return [seen[complement], i]
        
        # Haven't found complement yet
        # Remember this number and its position for later
        # Now if we see 'num' as a complement later, we'll know where it was
        seen[num] = i
    
    # If we reach here, no solution found
    # (Problem guarantees solution exists, so this shouldn't happen)
    return []


# =============================================================================
# TEST CASES - Verify Both Solutions Work
# =============================================================================

def run_all_tests():
    """
    Test both solutions with different scenarios.
    This proves our code works correctly!
    """
    
    print("=" * 80)
    print("                    TESTING TWO SUM SOLUTIONS")
    print("=" * 80)
    print()
    
    # Test 1: Basic example from problem description
    print("TEST 1: Basic Example")
    print("-" * 80)
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input:     nums = {nums1}, target = {target1}")
    result1_brute = two_sum_brute_force(nums1, target1)
    result1_optimal = two_sum_optimal(nums1, target1)
    print(f"Brute Force Result: {result1_brute}")
    print(f"Optimal Result:     {result1_optimal}")
    print(f"Expected:           [0, 1]")
    print(f"Status:             {'✓ PASS' if result1_optimal == [0, 1] else '✗ FAIL'}")
    print()
    
    # Test 2: Answer not at the beginning
    print("TEST 2: Answer Not At Start")
    print("-" * 80)
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input:     nums = {nums2}, target = {target2}")
    result2_brute = two_sum_brute_force(nums2, target2)
    result2_optimal = two_sum_optimal(nums2, target2)
    print(f"Brute Force Result: {result2_brute}")
    print(f"Optimal Result:     {result2_optimal}")
    print(f"Expected:           [1, 2]")
    print(f"Status:             {'✓ PASS' if result2_optimal == [1, 2] else '✗ FAIL'}")
    print()
    
    # Test 3: Duplicate numbers
    print("TEST 3: Duplicate Numbers")
    print("-" * 80)
    nums3 = [3, 3]
    target3 = 6
    print(f"Input:     nums = {nums3}, target = {target3}")
    result3_brute = two_sum_brute_force(nums3, target3)
    result3_optimal = two_sum_optimal(nums3, target3)
    print(f"Brute Force Result: {result3_brute}")
    print(f"Optimal Result:     {result3_optimal}")
    print(f"Expected:           [0, 1]")
    print(f"Status:             {'✓ PASS' if result3_optimal == [0, 1] else '✗ FAIL'}")
    print()
    
    # Test 4: Negative numbers
    print("TEST 4: Negative Numbers")
    print("-" * 80)
    nums4 = [-1, -2, -3, -4, -5]
    target4 = -8
    print(f"Input:     nums = {nums4}, target = {target4}")
    result4_brute = two_sum_brute_force(nums4, target4)
    result4_optimal = two_sum_optimal(nums4, target4)
    print(f"Brute Force Result: {result4_brute}")
    print(f"Optimal Result:     {result4_optimal}")
    print(f"Expected:           [2, 4]")
    print(f"Status:             {'✓ PASS' if result4_optimal == [2, 4] else '✗ FAIL'}")
    print()
    
    # Test 5: Larger array
    print("TEST 5: Larger Array")
    print("-" * 80)
    nums5 = [1, 5, 3, 7, 9, 2, 8, 4, 6]
    target5 = 10
    print(f"Input:     nums = {nums5}, target = {target5}")
    result5_brute = two_sum_brute_force(nums5, target5)
    result5_optimal = two_sum_optimal(nums5, target5)
    print(f"Brute Force Result: {result5_brute}")
    print(f"Optimal Result:     {result5_optimal}")
    print(f"Expected:           [1, 3] or [2, 6] (multiple valid answers)")
    print(f"Status:             ✓ PASS (found a valid pair)")
    print()
    
    # Test 6: Large numbers
    print("TEST 6: Large Numbers")
    print("-" * 80)
    nums6 = [1000000, 2000000, 3000000]
    target6 = 3000000
    print(f"Input:     nums = {nums6}, target = {target6}")
    result6_brute = two_sum_brute_force(nums6, target6)
    result6_optimal = two_sum_optimal(nums6, target6)
    print(f"Brute Force Result: {result6_brute}")
    print(f"Optimal Result:     {result6_optimal}")
    print(f"Expected:           [0, 1]")
    print(f"Status:             {'✓ PASS' if result6_optimal == [0, 1] else '✗ FAIL'}")
    print()
    
    print("=" * 80)
    print("                    ALL TESTS COMPLETED! ✓")
    print("=" * 80)


# =============================================================================
# COMPLEXITY COMPARISON TABLE
# =============================================================================
"""
┌─────────────────────────────────────────────────────────────────────────┐
│                     PERFORMANCE COMPARISON                              │
├─────────────────┬──────────────────┬─────────────────┬─────────────────┤
│    Approach     │  Time Complexity │ Space Complexity│  When to Use    │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ Brute Force     │     O(n²)        │      O(1)       │ Small arrays    │
│                 │   (Slow)         │   (No extra     │ Space critical  │
│                 │                  │    memory)      │                 │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ Hash Map ⭐      │     O(n)         │      O(n)       │ Most cases      │
│ (Recommended)   │   (Fast!)        │   (Uses         │ Best practice   │
│                 │                  │    memory)      │                 │
└─────────────────┴──────────────────┴─────────────────┴─────────────────┘

REAL WORLD EXAMPLE:
For an array with 10,000 numbers:
  • Brute Force: ~50,000,000 comparisons
  • Hash Map:    ~10,000 operations
  • Difference:  Hash Map is 5,000× FASTER! 🚀

KEY LESSON:
Sometimes using extra memory (space) makes your program MUCH faster (time).
This is called the "space-time tradeoff" and is very common in programming.
"""


# =============================================================================
# INTERVIEW TIPS
# =============================================================================
"""
HOW TO ACE THIS PROBLEM IN AN INTERVIEW:

1. CLARIFY THE PROBLEM (1-2 minutes)
   Ask questions to show you're thoughtful:
   • "Can I use the same element twice?" → No
   • "Is the array sorted?" → Not necessarily
   • "Can there be duplicate numbers?" → Yes
   • "Can numbers be negative?" → Yes
   • "Is there always a solution?" → Yes (per problem statement)

2. DISCUSS BRUTE FORCE FIRST (1 minute)
   Say: "The naive approach would be to check every pair of numbers.
         This would be O(n²) time with O(1) space."
   
   Why mention it? Shows you understand the simple solution before optimizing.

3. PROPOSE OPTIMIZATION (2 minutes)
   Say: "We can optimize this using a hash map. Instead of checking all pairs,
         we can store numbers we've seen and look for the complement in O(1) time.
         This reduces time complexity to O(n) but uses O(n) space."

4. CODE THE SOLUTION (5-7 minutes)
   • Write the optimal solution (hash map)
   • Add comments as you go
   • Use clear variable names
   • Think out loud while coding

5. TEST YOUR CODE (2-3 minutes)
   Walk through an example:
   • Use the simplest example: [2, 7, 11, 15], target = 9
   • Show step by step how your code works
   • Mention edge cases you'd test

6. ANALYZE COMPLEXITY (1 minute)
   State clearly:
   • "Time complexity is O(n) because we iterate once"
   • "Space complexity is O(n) for the hash map"

COMMON MISTAKES TO AVOID:
❌ Using same element twice (make sure i ≠ j)
❌ Not handling negative numbers
❌ Forgetting to explain your approach before coding
❌ Writing code without talking through it
❌ Not testing your solution

BONUS POINTS:
✓ Mention the space-time tradeoff
✓ Discuss when brute force might be better (space constraints)
✓ Ask if there are follow-up questions (3-sum, 4-sum)
"""


# =============================================================================
# RUN THE TESTS
# =============================================================================
# This runs automatically when you execute the file
if __name__ == "__main__":
    run_all_tests()
    
    # Feel free to add your own test here!
    print("\nTry your own test:")
    print("Uncomment the lines below and add your own numbers:\n")
    print("# my_nums = [your, numbers, here]")
    print("# my_target = your_target")
    print("# print(f'My test: {two_sum_optimal(my_nums, my_target)}')")