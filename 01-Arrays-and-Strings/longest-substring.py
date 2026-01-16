"""
=============================================================================
PROBLEM: LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
=============================================================================
Difficulty: Medium
Platform: LeetCode #3
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

PROBLEM STATEMENT:
Given a string s, find the length of the longest substring without 
repeating characters.

EXAMPLES:

Example 1:
  Input: s = "abcabcbb"
  Output: 3
  Explanation: The answer is "abc", with length 3

Example 2:
  Input: s = "bbbbb"
  Output: 1
  Explanation: The answer is "b", with length 1

Example 3:
  Input: s = "pwwkew"
  Output: 3
  Explanation: The answer is "wke", with length 3
  Note: "pwke" is a subsequence, not a substring

Example 4:
  Input: s = ""
  Output: 0

CONSTRAINTS:
- 0 <= s.length <= 50,000
- s consists of English letters, digits, symbols and spaces
=============================================================================
"""


# =============================================================================
# SOLUTION 1: SLIDING WINDOW WITH HASH SET ⭐ RECOMMENDED
# =============================================================================

def length_of_longest_substring_optimal(s):
    """
    Sliding window with hash set - O(n) solution!
    
    KEY INSIGHT:
    Use a sliding window with two pointers (left, right).
    Expand right to add characters.
    Shrink left when we find a duplicate.
    Track maximum window size.
    
    HOW IT WORKS:
    1. Use a set to track characters in current window
    2. Expand right pointer, adding characters to set
    3. If character already in set (duplicate):
       - Shrink from left until duplicate is removed
    4. Track maximum window size seen
    
    VISUAL EXAMPLE:
    s = "abcabcbb"
    
    Step 1: right=0, left=0, window="a", max=1
            set = {a}
    
    Step 2: right=1, left=0, window="ab", max=2
            set = {a,b}
    
    Step 3: right=2, left=0, window="abc", max=3
            set = {a,b,c}
    
    Step 4: right=3, 'a' is duplicate!
            Remove from left: left=1, window="bca"
            set = {b,c,a}
            max=3
    
    Step 5: right=4, 'b' is duplicate!
            Remove 'b': left=2, window="cab"
            set = {c,a,b}
            max=3
    
    Continue... max stays 3
    
    TIME COMPLEXITY: O(n)
    - Each character visited at most twice (once by right, once by left)
    - n = length of string
    
    SPACE COMPLEXITY: O(min(n, m))
    - Set stores unique characters
    - m = size of character set (26 for lowercase, 128 for ASCII)
    - At most min(n, m) characters in set
    
    WHEN TO USE:
    - DEFAULT CHOICE for substring problems
    - Classic sliding window pattern
    - Optimal time and space
    """
    # Edge case: empty string
    if not s:
        return 0
    
    # Sliding window boundaries
    left = 0
    max_length = 0
    
    # Set to track characters in current window
    char_set = set()
    
    # Expand right pointer
    for right in range(len(s)):
        # If character is duplicate, shrink from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character to window
        char_set.add(s[right])
        
        # Update maximum length
        max_length = max(max_length, right - left + 1)
    
    return max_length


# =============================================================================
# SOLUTION 2: SLIDING WINDOW WITH HASH MAP (OPTIMIZED)
# =============================================================================

def length_of_longest_substring_hashmap(s):
    """
    Sliding window with hash map - can skip characters!
    
    KEY OPTIMIZATION:
    Instead of removing characters one by one from left,
    we can jump left pointer directly to the position after
    the duplicate character.
    
    HOW IT WORKS:
    1. Use hash map to store: {character: last_seen_index}
    2. When we find duplicate, jump left pointer to:
       max(left, last_seen_index + 1)
    3. Update last seen index for current character
    4. Track maximum window size
    
    VISUAL EXAMPLE:
    s = "abcabcbb"
    
    Step 1-3: Build "abc", max=3
              map = {a:0, b:1, c:2}
    
    Step 4: right=3, s[3]='a', 'a' seen at index 0
            Jump left from 0 to 1 (0+1)
            window="bca", max=3
            map = {a:3, b:1, c:2}
    
    This is faster than removing one by one!
    
    TIME COMPLEXITY: O(n)
    - Single pass through string
    - Left pointer can skip multiple positions
    
    SPACE COMPLEXITY: O(min(n, m))
    - Hash map stores unique characters
    
    WHEN TO USE:
    - When you want to optimize further
    - Shows deeper understanding
    - Slightly faster in practice
    """
    if not s:
        return 0
    
    # Hash map: {character: last_seen_index}
    char_index = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # If character seen before and is in current window
        if s[right] in char_index and char_index[s[right]] >= left:
            # Jump left pointer past the duplicate
            left = char_index[s[right]] + 1
        
        # Update last seen index
        char_index[s[right]] = right
        
        # Update maximum length
        max_length = max(max_length, right - left + 1)
    
    return max_length


# =============================================================================
# SOLUTION 3: BRUTE FORCE (FOR COMPARISON - TOO SLOW)
# =============================================================================

def length_of_longest_substring_brute(s):
    """
    Brute force: Check all possible substrings.
    
    TIME COMPLEXITY: O(n³)
    - O(n²) to generate all substrings
    - O(n) to check each for duplicates
    
    SPACE COMPLEXITY: O(min(n, m))
    
    WHEN TO USE:
    - Never in interviews!
    - Just for comparison
    """
    if not s:
        return 0
    
    max_length = 0
    
    # Try all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Check if substring s[i:j+1] has all unique characters
            substring = s[i:j+1]
            if len(substring) == len(set(substring)):
                max_length = max(max_length, len(substring))
    
    return max_length


# =============================================================================
# TEST CASES
# =============================================================================

def run_all_tests():
    """
    Test all solutions with various test cases.
    """
    print("=" * 80)
    print("     TESTING LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS")
    print("=" * 80)
    print()
    
    # Test Case 1: Standard example
    print("TEST 1: Standard Example \"abcabcbb\"")
    print("-" * 80)
    s1 = "abcabcbb"
    print(f"Input: '{s1}'")
    print(f"Explanation: Longest is 'abc' with length 3")
    print(f"Sliding Window (Set):  {length_of_longest_substring_optimal(s1)}")
    print(f"Sliding Window (Map):  {length_of_longest_substring_hashmap(s1)}")
    print(f"Brute Force:           {length_of_longest_substring_brute(s1)}")
    print(f"Expected:              3")
    result1 = length_of_longest_substring_optimal(s1)
    print(f"Status:                {'✓ PASS' if result1 == 3 else '✗ FAIL'}")
    print()
    
    # Test Case 2: All same characters
    print("TEST 2: All Same \"bbbbb\"")
    print("-" * 80)
    s2 = "bbbbb"
    print(f"Input: '{s2}'")
    print(f"Explanation: Longest is 'b' with length 1")
    print(f"Sliding Window (Set):  {length_of_longest_substring_optimal(s2)}")
    print(f"Sliding Window (Map):  {length_of_longest_substring_hashmap(s2)}")
    print(f"Brute Force:           {length_of_longest_substring_brute(s2)}")
    print(f"Expected:              1")
    result2 = length_of_longest_substring_optimal(s2)
    print(f"Status:                {'✓ PASS' if result2 == 1 else '✗ FAIL'}")
    print()
    
    # Test Case 3: With spaces
    print("TEST 3: With Spaces \"pwwkew\"")
    print("-" * 80)
    s3 = "pwwkew"
    print(f"Input: '{s3}'")
    print(f"Explanation: Longest is 'wke' with length 3")
    print(f"Sliding Window (Set):  {length_of_longest_substring_optimal(s3)}")
    print(f"Sliding Window (Map):  {length_of_longest_substring_hashmap(s3)}")
    print(f"Brute Force:           {length_of_longest_substring_brute(s3)}")
    print(f"Expected:              3")
    result3 = length_of_longest_substring_optimal(s3)
    print(f"Status:                {'✓ PASS' if result3 == 3 else '✗ FAIL'}")
    print()
    
    # Test Case 4: Empty string
    print("TEST 4: Empty String \"\"")
    print("-" * 80)
    s4 = ""
    print(f"Input: '{s4}'")
    print(f"Sliding Window (Set):  {length_of_longest_substring_optimal(s4)}")
    print(f"Sliding Window (Map):  {length_of_longest_substring_hashmap(s4)}")
    print(f"Expected:              0")
    result4 = length_of_longest_substring_optimal(s4)
    print(f"Status:                {'✓ PASS' if result4 == 0 else '✗ FAIL'}")
    print()
    
    # Test Case 5: Single character
    print("TEST 5: Single Character \"a\"")
    print("-" * 80)
    s5 = "a"
    print(f"Input: '{s5}'")
    print(f"Sliding Window (Set):  {length_of_longest_substring_optimal(s5)}")
    print(f"Sliding Window (Map):  {length_of_longest_substring_hashmap(s5)}")
    print(f"Expected:              1")
    result5 = length_of_longest_substring_optimal(s5)
    print(f"Status:                {'✓ PASS' if result5 == 1 else '✗ FAIL'}")
    print()
    
    # Test Case 6: All unique
    print("TEST 6: All Unique \"abcdef\"")
    print("-" * 80)
    s6 = "abcdef"
    print(f"Input: '{s6}'")
    print(f"Sliding Window (Set):  {length_of_longest_substring_optimal(s6)}")
    print(f"Sliding Window (Map):  {length_of_longest_substring_hashmap(s6)}")
    print(f"Expected:              6")
    result6 = length_of_longest_substring_optimal(s6)
    print(f"Status:                {'✓ PASS' if result6 == 6 else '✗ FAIL'}")
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
│ Brute Force     │     O(n³)        │    O(min(n,m))  │ Never!          │
│                 │  (Very slow!)    │                 │ Understanding   │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ Sliding Win ⭐   │     O(n)         │    O(min(n,m))  │ BEST CHOICE     │
│ (Set)           │   (Optimal!)     │                 │ Clean & simple  │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ Sliding Win ⭐⭐  │     O(n)         │    O(min(n,m))  │ Slightly better │
│ (HashMap)       │   (Optimal!)     │                 │ Can skip chars  │
└─────────────────┴──────────────────┴─────────────────┴─────────────────┘

Both sliding window approaches are O(n) - choose based on preference!
HashMap version can be slightly faster in practice.
"""


# =============================================================================
# INTERVIEW TIPS
# =============================================================================
"""
HOW TO ACE THIS IN AN INTERVIEW:

1. CLARIFY (30 seconds)
   • "What characters can be in string?" → Any ASCII
   • "Is case sensitive?" → Yes
   • "What about empty string?" → Return 0

2. RECOGNIZE THE PATTERN (1 minute)
   • "This is a sliding window problem"
   • "We need to track a window of unique characters"
   • "Expand right, shrink left when duplicate found"

3. EXPLAIN APPROACH (2 minutes)
   • "Use two pointers: left and right"
   • "Use set to track characters in window"
   • "Expand right, shrink left on duplicates"
   • "Track maximum window size"

4. DRAW IT OUT (2 minutes) - IMPORTANT!
   Draw example: "abcabcbb"
   Show window expanding and shrinking
   Interviewers love visual explanations!

5. CODE THE SOLUTION (5 minutes)
   • Write sliding window with set
   • Clean, readable code
   • Handle edge cases

6. WALK THROUGH EXAMPLE (2 minutes)
   Use "abcabcbb":
   • Show window states: a, ab, abc
   • Show shrinking when 'a' repeats
   • Show final answer: 3

7. OPTIMIZE (2 minutes)
   • Mention hashmap optimization
   • Explain jumping left pointer
   • Shows deeper understanding

COMMON MISTAKES:
❌ Not handling empty string
❌ Forgetting to update max_length
❌ Wrong window size calculation (right - left + 1)
❌ Not removing from set when shrinking
❌ Infinite loop (not incrementing left)

BONUS POINTS:
✓ Recognizing it's sliding window immediately
✓ Drawing clear visualization
✓ Both set and hashmap approaches
✓ Discussing space complexity
✓ Mentioning character set size impact

KEY PHRASES:
- "Sliding window technique"
- "Two pointers"
- "Expand and shrink window"
- "Track unique characters"
- "O(n) time complexity"

FOLLOW-UP VARIATIONS:
- "Find the actual substring, not just length?"
  → Track start index when updating max
- "What if we want at most k distinct characters?"
  → Modify condition, allow up to k characters
- "Longest substring with at most 2 unique chars?"
  → Similar sliding window, different condition
"""


# =============================================================================
# RUN TESTS
# =============================================================================
if __name__ == "__main__":
    run_all_tests()