"""
=============================================================================
PROBLEM: VALID PARENTHESES
=============================================================================
Difficulty: Easy
Platform: LeetCode #20
Link: https://leetcode.com/problems/valid-parentheses/

PROBLEM STATEMENT:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

EXAMPLES:

Example 1:
  Input: s = "()"
  Output: true

Example 2:
  Input: s = "()[]{}"
  Output: true

Example 3:
  Input: s = "(]"
  Output: false
  Explanation: ( must close with ), not ]

Example 4:
  Input: s = "([)]"
  Output: false
  Explanation: Brackets are not in correct order

Example 5:
  Input: s = "{[]}"
  Output: true
  Explanation: Properly nested

CONSTRAINTS:
- 1 <= s.length <= 10,000
- s consists of parentheses only '()[]{}'
=============================================================================
"""


# =============================================================================
# SOLUTION 1: STACK APPROACH (OPTIMAL) ⭐ RECOMMENDED
# =============================================================================

def is_valid_stack(s):
    """
    Use a stack to match opening and closing brackets.
    
    KEY INSIGHT:
    - When we see an opening bracket: ( [ {
      → Push it onto stack (we'll need to match it later)
    
    - When we see a closing bracket: ) ] }
      → Check if stack top matches
      → If yes: pop and continue
      → If no: invalid!
    
    HOW IT WORKS:
    1. Create empty stack
    2. For each character:
       - If opening bracket: push to stack
       - If closing bracket: check if it matches stack top
    3. At end, stack should be empty (all matched)
    
    STEP-BY-STEP EXAMPLE:
    s = "([)]"
    
    Step 1: See '(' → push to stack
            Stack: ['(']
    
    Step 2: See '[' → push to stack
            Stack: ['(', '[']
    
    Step 3: See ')' → closing bracket
            Top of stack is '[' → doesn't match '('!
            Return False ✗
    
    ANOTHER EXAMPLE:
    s = "{[]}"
    
    Step 1: See '{' → push
            Stack: ['{']
    
    Step 2: See '[' → push
            Stack: ['{', '[']
    
    Step 3: See ']' → closing bracket
            Top is '[' → matches!
            Pop it. Stack: ['{']
    
    Step 4: See '}' → closing bracket
            Top is '{' → matches!
            Pop it. Stack: []
    
    Stack is empty → Return True ✓
    
    TIME COMPLEXITY: O(n)
    - Visit each character once
    - Stack operations (push/pop) are O(1)
    
    SPACE COMPLEXITY: O(n)
    - In worst case, all opening brackets
    - Stack stores n/2 elements
    - O(n/2) = O(n)
    
    WHEN TO USE:
    - This is THE standard solution
    - What interviewers expect
    - Clean and efficient
    """
    # Edge case: odd length can't be valid
    if len(s) % 2 != 0:
        return False
    
    # Create empty stack (use Python list)
    stack = []
    
    # Dictionary to map closing brackets to opening brackets
    # Makes it easy to check if brackets match
    bracket_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    # Go through each character
    for char in s:
        # If it's a closing bracket
        if char in bracket_map:
            # Pop from stack (or use dummy value if stack empty)
            # Get the top element, or '#' if stack is empty
            top_element = stack.pop() if stack else '#'
            
            # Check if it matches the expected opening bracket
            if bracket_map[char] != top_element:
                return False  # Mismatch!
        
        else:
            # It's an opening bracket - push to stack
            stack.append(char)
    
    # Valid only if stack is empty (all brackets matched)
    return len(stack) == 0


# =============================================================================
# SOLUTION 2: CLEANER VERSION
# =============================================================================

def is_valid_clean(s):
    """
    Same logic as above, slightly different implementation.
    
    TIME COMPLEXITY: O(n)
    SPACE COMPLEXITY: O(n)
    """
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        # If opening bracket
        if char in pairs:
            stack.append(char)
        # If closing bracket
        else:
            # Stack empty or top doesn't match
            if not stack or pairs[stack.pop()] != char:
                return False
    
    # All matched if stack is empty
    return not stack


# =============================================================================
# SOLUTION 3: USING REPLACE (NOT RECOMMENDED - Educational Only)
# =============================================================================

def is_valid_replace(s):
    """
    Keep removing matched pairs until string is empty or no more matches.
    
    HOW IT WORKS:
    - Replace "()" with ""
    - Replace "[]" with ""
    - Replace "{}" with ""
    - Repeat until no more replacements possible
    - If string becomes empty → valid
    
    EXAMPLE:
    s = "([{}])"
    → "([  ])" (remove {})
    → "(    )" (remove [])
    → "      " (remove ())
    → ""      (empty → valid!)
    
    TIME COMPLEXITY: O(n²)
    - Each replace scans entire string: O(n)
    - May need n/2 replacements
    - Total: O(n²) - inefficient!
    
    SPACE COMPLEXITY: O(n)
    - Creating new strings at each step
    
    WHEN TO USE:
    - DON'T use in interviews!
    - Shown here just to understand alternatives
    - Stack solution is much better
    """
    # Keep removing matched pairs
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "")
        s = s.replace("[]", "")
        s = s.replace("{}", "")
    
    # If empty, all brackets were matched
    return s == ""


# =============================================================================
# TEST CASES
# =============================================================================

def run_all_tests():
    """
    Test all solutions with various test cases.
    """
    print("=" * 80)
    print("              TESTING VALID PARENTHESES SOLUTIONS")
    print("=" * 80)
    print()
    
    # Test Case 1: Simple valid
    print("TEST 1: Simple Valid \"()\"")
    print("-" * 80)
    s1 = "()"
    print(f"Input: '{s1}'")
    print(f"Stack Solution: {is_valid_stack(s1)}")
    print(f"Clean Solution: {is_valid_clean(s1)}")
    print(f"Replace Solution: {is_valid_replace(s1)}")
    print(f"Expected: True")
    print(f"Status: {'✓ PASS' if is_valid_stack(s1) == True else '✗ FAIL'}")
    print()
    
    # Test Case 2: Multiple types
    print("TEST 2: Multiple Types \"()[]{}\"")
    print("-" * 80)
    s2 = "()[]{}"
    print(f"Input: '{s2}'")
    print(f"Stack Solution: {is_valid_stack(s2)}")
    print(f"Clean Solution: {is_valid_clean(s2)}")
    print(f"Replace Solution: {is_valid_replace(s2)}")
    print(f"Expected: True")
    print(f"Status: {'✓ PASS' if is_valid_stack(s2) == True else '✗ FAIL'}")
    print()
    
    # Test Case 3: Wrong type
    print("TEST 3: Wrong Type \"(]\"")
    print("-" * 80)
    s3 = "(]"
    print(f"Input: '{s3}'")
    print(f"Stack Solution: {is_valid_stack(s3)}")
    print(f"Clean Solution: {is_valid_clean(s3)}")
    print(f"Replace Solution: {is_valid_replace(s3)}")
    print(f"Expected: False")
    print(f"Status: {'✓ PASS' if is_valid_stack(s3) == False else '✗ FAIL'}")
    print()
    
    # Test Case 4: Wrong order
    print("TEST 4: Wrong Order \"([)]\"")
    print("-" * 80)
    s4 = "([)]"
    print(f"Input: '{s4}'")
    print(f"Explanation: Brackets interleaved incorrectly")
    print(f"Stack Solution: {is_valid_stack(s4)}")
    print(f"Clean Solution: {is_valid_clean(s4)}")
    print(f"Replace Solution: {is_valid_replace(s4)}")
    print(f"Expected: False")
    print(f"Status: {'✓ PASS' if is_valid_stack(s4) == False else '✗ FAIL'}")
    print()
    
    # Test Case 5: Nested valid
    print("TEST 5: Nested Valid \"{[]}\"")
    print("-" * 80)
    s5 = "{[]}"
    print(f"Input: '{s5}'")
    print(f"Stack Solution: {is_valid_stack(s5)}")
    print(f"Clean Solution: {is_valid_clean(s5)}")
    print(f"Replace Solution: {is_valid_replace(s5)}")
    print(f"Expected: True")
    print(f"Status: {'✓ PASS' if is_valid_stack(s5) == True else '✗ FAIL'}")
    print()
    
    # Test Case 6: Only opening
    print("TEST 6: Only Opening \"(((\"")
    print("-" * 80)
    s6 = "((("
    print(f"Input: '{s6}'")
    print(f"Stack Solution: {is_valid_stack(s6)}")
    print(f"Clean Solution: {is_valid_clean(s6)}")
    print(f"Replace Solution: {is_valid_replace(s6)}")
    print(f"Expected: False")
    print(f"Status: {'✓ PASS' if is_valid_stack(s6) == False else '✗ FAIL'}")
    print()
    
    # Test Case 7: Only closing
    print("TEST 7: Only Closing \")))\"")
    print("-" * 80)
    s7 = ")))"
    print(f"Input: '{s7}'")
    print(f"Stack Solution: {is_valid_stack(s7)}")
    print(f"Clean Solution: {is_valid_clean(s7)}")
    print(f"Replace Solution: {is_valid_replace(s7)}")
    print(f"Expected: False")
    print(f"Status: {'✓ PASS' if is_valid_stack(s7) == False else '✗ FAIL'}")
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
│ Stack ⭐         │     O(n)         │      O(n)       │ BEST CHOICE     │
│ (Recommended)   │   (Optimal!)     │                 │ Standard answer │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ Replace         │     O(n²)        │      O(n)       │ Never use!      │
│                 │   (Too slow)     │                 │ Just for fun    │
└─────────────────┴──────────────────┴─────────────────┴─────────────────┘

Stack solution is the industry standard!
"""


# =============================================================================
# INTERVIEW TIPS
# =============================================================================
"""
HOW TO ACE THIS IN AN INTERVIEW:

1. CLARIFY (30 seconds)
   • "Only these 3 types of brackets?" → Yes
   • "Can there be other characters?" → No (usually)
   • "Is empty string valid?" → Yes

2. EXPLAIN THE APPROACH (2 minutes)
   • "I'll use a stack"
   • "Opening brackets get pushed"
   • "Closing brackets must match stack top"
   • "At the end, stack should be empty"

3. WHY STACK? (Important to explain!)
   • "Stack is LIFO - Last In, First Out"
   • "Perfect for matching pairs"
   • "Most recent opening must match first"

4. CODE (5 minutes)
   • Write the stack solution
   • Use dictionary for clean bracket mapping
   • Handle edge cases (empty stack, odd length)

5. WALK THROUGH EXAMPLE (2 minutes)
   Use "{[()]}":
   • Show stack state after each character
   • { → push
   • [ → push
   • ( → push
   • ) → pop and match ( ✓
   • ] → pop and match [ ✓
   • } → pop and match { ✓
   • Stack empty → valid!

COMMON MISTAKES:
❌ Not checking if stack is empty before popping
❌ Forgetting to check if stack is empty at end
❌ Wrong bracket map direction
❌ Not handling edge cases

BONUS POINTS:
✓ Explaining why stack is perfect for this
✓ Mentioning LIFO property
✓ Showing the bracket map approach
✓ Handling odd-length string early

KEY PHRASES:
- "Stack for matching pairs"
- "LIFO structure"
- "Most recent opening bracket"
- "O(n) time and space"
"""


# =============================================================================
# RUN TESTS
# =============================================================================
if __name__ == "__main__":
    run_all_tests()