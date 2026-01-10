"""
=============================================================================
PROBLEM: VALID ANAGRAM
=============================================================================
Difficulty: Easy
Platform: LeetCode #242
Link: https://leetcode.com/problems/valid-anagram/

PROBLEM STATEMENT:
Given two strings s and t, return true if t is an anagram of s, and false 
otherwise.

An Anagram is a word formed by rearranging the letters of a different word,
using all the original letters exactly once.

EXAMPLES:

Example 1:
  Input: s = "anagram", t = "nagaram"
  Output: true
  Explanation: Both have same letters: a(3), n(1), g(1), r(1), m(1)

Example 2:
  Input: s = "rat", t = "car"
  Output: false
  Explanation: Different letters

Example 3:
  Input: s = "listen", t = "silent"
  Output: true
  Explanation: Same letters, different order

CONSTRAINTS:
- 1 <= s.length, t.length <= 50,000
- s and t consist of lowercase English letters
=============================================================================
"""


# =============================================================================
# SOLUTION 1: SORTING APPROACH
# =============================================================================

def is_anagram_sorting(s, t):
    """
    Sort both strings and compare them.
    
    HOW IT WORKS:
    1. If they're anagrams, sorting will make them identical
    2. Sort both strings
    3. Compare if they're equal
    
    STEP-BY-STEP EXAMPLE:
    s = "anagram", t = "nagaram"
    
    After sorting:
    s_sorted = "aaagmnr"
    t_sorted = "aaagmnr"
    
    They're equal! → Return True ✓
    
    TIME COMPLEXITY: O(n log n)
    - Sorting takes O(n log n) where n is string length
    - Comparison takes O(n)
    - Total: O(n log n) dominates
    
    SPACE COMPLEXITY: O(1) or O(n)
    - Depends on sorting implementation
    - Python's sorted() creates new list: O(n)
    
    WHEN TO USE:
    - Simplest approach to understand
    - Good for interviews if you mention the hash map approach too
    - Clean, short code
    """
    # Quick check: different lengths can't be anagrams
    if len(s) != len(t):
        return False
    
    # Sort both strings and compare
    # sorted() converts string to list of characters, then sorts them
    return sorted(s) == sorted(t)


# =============================================================================
# SOLUTION 2: HASH MAP / COUNTER (OPTIMAL) ⭐ RECOMMENDED
# =============================================================================

def is_anagram_hashmap(s, t):
    """
    Count character frequencies and compare.
    
    HOW IT WORKS:
    1. If different lengths → not anagrams
    2. Count frequency of each character in both strings
    3. If frequencies match → anagrams!
    
    STEP-BY-STEP EXAMPLE:
    s = "anagram", t = "nagaram"
    
    Count characters in s:
    {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
    
    Count characters in t:
    {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}
    
    Same frequencies! → Return True ✓
    
    TIME COMPLEXITY: O(n)
    - Count characters in s: O(n)
    - Count characters in t: O(n)
    - Compare dictionaries: O(n)
    - Total: O(n) linear time!
    
    SPACE COMPLEXITY: O(1) or O(26)
    - At most 26 letters in English alphabet
    - Dictionary stores up to 26 entries
    - O(26) = O(1) constant space!
    
    WHY THIS IS BETTER:
    - Faster than sorting: O(n) vs O(n log n)
    - More efficient for large strings
    - Early termination possible
    
    WHEN TO USE:
    - Default choice for interviews
    - Best time complexity
    - Shows understanding of hash maps
    """
    # Quick check: different lengths can't be anagrams
    if len(s) != len(t):
        return False
    
    # Create dictionaries to count character frequencies
    count_s = {}
    count_t = {}
    
    # Count characters in s
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    
    # Count characters in t
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1
    
    # Compare the frequency dictionaries
    return count_s == count_t


# =============================================================================
# SOLUTION 3: PYTHON COUNTER (MOST ELEGANT)
# =============================================================================

def is_anagram_counter(s, t):
    """
    Use Python's built-in Counter for character counting.
    
    HOW IT WORKS:
    - Counter is a special dictionary for counting
    - Automatically counts character frequencies
    - Clean one-liner solution
    
    TIME COMPLEXITY: O(n)
    SPACE COMPLEXITY: O(1) → at most 26 letters
    
    This is the same as Solution 2, just using Python's library.
    """
    from collections import Counter
    
    # Counter automatically counts all characters
    # Compare the two counters
    return Counter(s) == Counter(t)


# =============================================================================
# SOLUTION 4: SINGLE HASH MAP (SPACE OPTIMIZED)
# =============================================================================

def is_anagram_optimized(s, t):
    """
    Use one hash map - increment for s, decrement for t.
    
    HOW IT WORKS:
    1. If different lengths → not anagrams
    2. For characters in s: increment count
    3. For characters in t: decrement count
    4. If all counts are 0 → anagrams!
    
    STEP-BY-STEP EXAMPLE:
    s = "anagram", t = "nagaram"
    
    After processing s:
    {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
    
    After processing t (decrementing):
    {'a': 0, 'n': 0, 'g': 0, 'r': 0, 'm': 0}
    
    All zeros! → Return True ✓
    
    TIME COMPLEXITY: O(n)
    SPACE COMPLEXITY: O(1) → at most 26 letters
    
    ADVANTAGES:
    - Uses only one dictionary instead of two
    - Slightly more space efficient
    - Same time complexity
    """
    # Quick check: different lengths can't be anagrams
    if len(s) != len(t):
        return False
    
    # Single dictionary for counting
    count = {}
    
    # Increment for characters in s
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    # Decrement for characters in t
    for char in t:
        count[char] = count.get(char, 0) - 1
    
    # Check if all counts are zero
    for val in count.values():
        if val != 0:
            return False
    
    return True


# =============================================================================
# SOLUTION 5: ARRAY COUNTING (FOR LOWERCASE LETTERS ONLY)
# =============================================================================

def is_anagram_array(s, t):
    """
    Use array of 26 for counting lowercase letters.
    
    HOW IT WORKS:
    1. Create array of size 26 (for a-z)
    2. Increment for characters in s
    3. Decrement for characters in t
    4. Check if all positions are 0
    
    TIME COMPLEXITY: O(n)
    SPACE COMPLEXITY: O(1) → fixed 26-element array
    
    WHEN TO USE:
    - When guaranteed only lowercase English letters
    - Maximum space efficiency
    - Slight performance edge over dictionaries
    """
    # Quick check: different lengths can't be anagrams
    if len(s) != len(t):
        return False
    
    # Array of 26 for lowercase letters a-z
    count = [0] * 26
    
    # Process both strings
    for i in range(len(s)):
        # Increment for s, decrement for t
        # ord('a') = 97, so ord(char) - ord('a') gives 0-25
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    
    # Check if all counts are zero
    return all(c == 0 for c in count)


# =============================================================================
# TEST CASES
# =============================================================================

def run_all_tests():
    """
    Test all solutions with various test cases.
    """
    print("=" * 80)
    print("                TESTING VALID ANAGRAM SOLUTIONS")
    print("=" * 80)
    print()
    
    # Test Case 1: Basic anagram
    print("TEST 1: Basic Anagram")
    print("-" * 80)
    s1, t1 = "anagram", "nagaram"
    print(f"Input:  s = '{s1}', t = '{t1}'")
    print(f"Sorting:    {is_anagram_sorting(s1, t1)}")
    print(f"Hash Map:   {is_anagram_hashmap(s1, t1)}")
    print(f"Counter:    {is_anagram_counter(s1, t1)}")
    print(f"Optimized:  {is_anagram_optimized(s1, t1)}")
    print(f"Array:      {is_anagram_array(s1, t1)}")
    print(f"Expected:   True")
    print(f"Status:     {'✓ PASS' if is_anagram_hashmap(s1, t1) == True else '✗ FAIL'}")
    print()
    
    # Test Case 2: Not an anagram
    print("TEST 2: Not An Anagram")
    print("-" * 80)
    s2, t2 = "rat", "car"
    print(f"Input:  s = '{s2}', t = '{t2}'")
    print(f"Sorting:    {is_anagram_sorting(s2, t2)}")
    print(f"Hash Map:   {is_anagram_hashmap(s2, t2)}")
    print(f"Counter:    {is_anagram_counter(s2, t2)}")
    print(f"Optimized:  {is_anagram_optimized(s2, t2)}")
    print(f"Array:      {is_anagram_array(s2, t2)}")
    print(f"Expected:   False")
    print(f"Status:     {'✓ PASS' if is_anagram_hashmap(s2, t2) == False else '✗ FAIL'}")
    print()
    
    # Test Case 3: Classic example
    print("TEST 3: Listen/Silent")
    print("-" * 80)
    s3, t3 = "listen", "silent"
    print(f"Input:  s = '{s3}', t = '{t3}'")
    print(f"Sorting:    {is_anagram_sorting(s3, t3)}")
    print(f"Hash Map:   {is_anagram_hashmap(s3, t3)}")
    print(f"Counter:    {is_anagram_counter(s3, t3)}")
    print(f"Optimized:  {is_anagram_optimized(s3, t3)}")
    print(f"Array:      {is_anagram_array(s3, t3)}")
    print(f"Expected:   True")
    print(f"Status:     {'✓ PASS' if is_anagram_hashmap(s3, t3) == True else '✗ FAIL'}")
    print()
    
    # Test Case 4: Different lengths
    print("TEST 4: Different Lengths")
    print("-" * 80)
    s4, t4 = "ab", "abc"
    print(f"Input:  s = '{s4}', t = '{t4}'")
    print(f"Sorting:    {is_anagram_sorting(s4, t4)}")
    print(f"Hash Map:   {is_anagram_hashmap(s4, t4)}")
    print(f"Counter:    {is_anagram_counter(s4, t4)}")
    print(f"Optimized:  {is_anagram_optimized(s4, t4)}")
    print(f"Array:      {is_anagram_array(s4, t4)}")
    print(f"Expected:   False")
    print(f"Status:     {'✓ PASS' if is_anagram_hashmap(s4, t4) == False else '✗ FAIL'}")
    print()
    
    # Test Case 5: Single character
    print("TEST 5: Single Character")
    print("-" * 80)
    s5, t5 = "a", "a"
    print(f"Input:  s = '{s5}', t = '{t5}'")
    print(f"Sorting:    {is_anagram_sorting(s5, t5)}")
    print(f"Hash Map:   {is_anagram_hashmap(s5, t5)}")
    print(f"Counter:    {is_anagram_counter(s5, t5)}")
    print(f"Optimized:  {is_anagram_optimized(s5, t5)}")
    print(f"Array:      {is_anagram_array(s5, t5)}")
    print(f"Expected:   True")
    print(f"Status:     {'✓ PASS' if is_anagram_hashmap(s5, t5) == True else '✗ FAIL'}")
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
│ Sorting         │   O(n log n)     │      O(n)       │ Simple/Quick    │
│                 │                  │                 │ Short strings   │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ Hash Map ⭐      │     O(n)         │      O(1)       │ BEST CHOICE     │
│ (Recommended)   │   (Fastest!)     │   (26 max)      │ Interviews      │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ Counter         │     O(n)         │      O(1)       │ Most Pythonic   │
│                 │                  │                 │ Clean code      │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ Array Counting  │     O(n)         │      O(1)       │ Maximum speed   │
│                 │                  │   (26 fixed)    │ Lowercase only  │
└─────────────────┴──────────────────┴─────────────────┴─────────────────┘
"""


# =============================================================================
# INTERVIEW TIPS
# =============================================================================
"""
HOW TO ACE THIS IN AN INTERVIEW:

1. CLARIFY (30 seconds)
   • "Are both strings lowercase only?" → Yes (usually)
   • "Do spaces and punctuation count?" → Not in this problem
   • "What about Unicode characters?" → Usually just a-z

2. DISCUSS APPROACHES (2 minutes)
   • "Simple approach: sort both and compare - O(n log n)"
   • "Better: count character frequencies - O(n)"
   • "Python has Counter for this - very clean"

3. CODE (3-5 minutes)
   Choose based on interviewer preference:
   • Hash map: Shows data structure knowledge
   • Counter: Shows Python proficiency
   • Array: Shows optimization skills

4. TEST (1 minute)
   Walk through "anagram" and "nagaram"
   • Show counting process
   • Verify frequencies match

FOLLOW-UP QUESTIONS:
Q: What if we need to handle Unicode?
A: Hash map/Counter still work! Array method only works for a-z.

Q: What if strings are huge (millions of characters)?
A: Hash map O(n) beats sorting O(n log n) significantly.

Q: Can we do better than O(n)?
A: No - we must read each character at least once.

COMMON MISTAKES:
❌ Forgetting to check if lengths are different
❌ Not handling empty strings
❌ Using == on sorted lists (works but mention it)
❌ Overthinking - it's simpler than it seems!

BONUS POINTS:
✓ Mention all approaches and trade-offs
✓ Show the Pythonic Counter solution
✓ Discuss when array method is best
✓ Know that O(26) = O(1) for space
"""


# =============================================================================
# RUN TESTS
# =============================================================================
if __name__ == "__main__":
    run_all_tests()