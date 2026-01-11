"""
=============================================================================
PROBLEM: REVERSE LINKED LIST
=============================================================================
Difficulty: Easy
Platform: LeetCode #206
Link: https://leetcode.com/problems/reverse-linked-list/

PROBLEM STATEMENT:
Given the head of a singly linked list, reverse the list, and return the 
reversed list.

EXAMPLES:

Example 1:
  Input: head = [1,2,3,4,5]
  Output: [5,4,3,2,1]
  
  Visual:
  Before: 1 → 2 → 3 → 4 → 5 → None
  After:  5 → 4 → 3 → 2 → 1 → None

Example 2:
  Input: head = [1,2]
  Output: [2,1]

Example 3:
  Input: head = []
  Output: []

CONSTRAINTS:
- The number of nodes is in range [0, 5000]
- -5000 <= Node.val <= 5000
=============================================================================
"""


# =============================================================================
# LINKED LIST NODE DEFINITION
# =============================================================================

class ListNode:
    """
    Definition for singly-linked list node.
    
    Each node contains:
    - val: the value stored in this node
    - next: reference to the next node (or None if last node)
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# =============================================================================
# SOLUTION 1: ITERATIVE APPROACH (RECOMMENDED) ⭐
# =============================================================================

def reverse_list_iterative(head):
    """
    Reverse linked list using iterative approach with 3 pointers.
    
    HOW IT WORKS:
    We use three pointers to reverse the links one by one:
    1. prev: points to the previous node (starts at None)
    2. current: points to current node (starts at head)
    3. next_temp: temporarily stores the next node
    
    At each step:
    - Save the next node (so we don't lose it)
    - Reverse the current link (point current to prev)
    - Move prev and current one step forward
    
    VISUAL EXAMPLE:
    Original: 1 → 2 → 3 → None
    
    Step 0: prev=None, curr=1, next=2
            None ← 1   2 → 3 → None
    
    Step 1: prev=1, curr=2, next=3
            None ← 1 ← 2   3 → None
    
    Step 2: prev=2, curr=3, next=None
            None ← 1 ← 2 ← 3
    
    Step 3: prev=3, curr=None
            Return prev (which is 3, the new head)
    
    TIME COMPLEXITY: O(n)
    - Visit each node exactly once
    - n = number of nodes
    
    SPACE COMPLEXITY: O(1)
    - Only using 3 pointer variables
    - No recursion stack
    - No additional data structures
    
    WHEN TO USE:
    - Default choice for interviews
    - More space efficient than recursive
    - Easier to understand visually
    """
    # Edge case: empty list or single node
    if not head or not head.next:
        return head
    
    # Initialize three pointers
    prev = None        # Previous node (starts as None)
    current = head     # Current node we're processing
    
    # Traverse the list
    while current:
        # Step 1: Save the next node (we'll need it!)
        next_temp = current.next
        
        # Step 2: Reverse the link
        # Make current point backwards to prev
        current.next = prev
        
        # Step 3: Move prev and current one step forward
        prev = current
        current = next_temp
    
    # When loop ends, prev is at the old tail (new head)
    return prev


# =============================================================================
# SOLUTION 2: RECURSIVE APPROACH
# =============================================================================

def reverse_list_recursive(head):
    """
    Reverse linked list using recursion.
    
    HOW IT WORKS:
    The idea is to reverse from the end backwards:
    1. Recursively reverse everything after the first node
    2. Then attach the first node to the end
    
    VISUAL EXAMPLE:
    Original: 1 → 2 → 3 → None
    
    Call stack:
    reverse(1 → 2 → 3)
      → reverse(2 → 3)
        → reverse(3)
          → return 3
        ← now we have: 3 → None, and we're at node 2
        ← make 3 point to 2: 3 → 2 → None
        ← make 2's next None: 3 → 2 → None
      ← now we're at node 1
      ← make 2 point to 1: 3 → 2 → 1 → None
      ← make 1's next None: 3 → 2 → 1 → None
    
    TIME COMPLEXITY: O(n)
    - Visit each node once
    
    SPACE COMPLEXITY: O(n)
    - Recursion stack uses n space
    - Each recursive call adds to stack
    
    WHEN TO USE:
    - When asked specifically for recursive solution
    - When you want elegant, concise code
    - Not ideal for very long lists (stack overflow risk)
    """
    # Base case: empty list or single node
    if not head or not head.next:
        return head
    
    # Recursively reverse the rest of the list
    # This returns the new head (which is the old tail)
    new_head = reverse_list_recursive(head.next)
    
    # Now head.next is the last node of the reversed portion
    # Make it point back to head
    head.next.next = head
    
    # Make current head point to None (it's now the tail)
    head.next = None
    
    # Return the new head
    return new_head


# =============================================================================
# HELPER FUNCTIONS FOR TESTING
# =============================================================================

def create_linked_list(values):
    """
    Create a linked list from a list of values.
    
    Example: [1, 2, 3] → 1 → 2 → 3 → None
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


def linked_list_to_list(head):
    """
    Convert linked list to Python list for easy printing.
    
    Example: 1 → 2 → 3 → None → [1, 2, 3]
    """
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result


def print_linked_list(head, label=""):
    """
    Print linked list in a readable format.
    """
    values = linked_list_to_list(head)
    if label:
        print(f"{label}: {' → '.join(map(str, values))} → None")
    else:
        print(f"{' → '.join(map(str, values))} → None")


# =============================================================================
# TEST CASES
# =============================================================================

def run_all_tests():
    """
    Test both solutions with various test cases.
    """
    print("=" * 80)
    print("              TESTING REVERSE LINKED LIST SOLUTIONS")
    print("=" * 80)
    print()
    
    # Test Case 1: Standard list
    print("TEST 1: Standard List [1,2,3,4,5]")
    print("-" * 80)
    list1 = create_linked_list([1, 2, 3, 4, 5])
    print_linked_list(list1, "Original")
    
    reversed1_iter = reverse_list_iterative(create_linked_list([1, 2, 3, 4, 5]))
    print_linked_list(reversed1_iter, "Iterative Result")
    
    reversed1_rec = reverse_list_recursive(create_linked_list([1, 2, 3, 4, 5]))
    print_linked_list(reversed1_rec, "Recursive Result")
    
    expected1 = [5, 4, 3, 2, 1]
    result1 = linked_list_to_list(reversed1_iter)
    print(f"Expected: {expected1}")
    print(f"Status: {'✓ PASS' if result1 == expected1 else '✗ FAIL'}")
    print()
    
    # Test Case 2: Two nodes
    print("TEST 2: Two Nodes [1,2]")
    print("-" * 80)
    list2 = create_linked_list([1, 2])
    print_linked_list(list2, "Original")
    
    reversed2_iter = reverse_list_iterative(create_linked_list([1, 2]))
    print_linked_list(reversed2_iter, "Iterative Result")
    
    reversed2_rec = reverse_list_recursive(create_linked_list([1, 2]))
    print_linked_list(reversed2_rec, "Recursive Result")
    
    expected2 = [2, 1]
    result2 = linked_list_to_list(reversed2_iter)
    print(f"Expected: {expected2}")
    print(f"Status: {'✓ PASS' if result2 == expected2 else '✗ FAIL'}")
    print()
    
    # Test Case 3: Single node
    print("TEST 3: Single Node [1]")
    print("-" * 80)
    list3 = create_linked_list([1])
    print_linked_list(list3, "Original")
    
    reversed3_iter = reverse_list_iterative(create_linked_list([1]))
    print_linked_list(reversed3_iter, "Iterative Result")
    
    reversed3_rec = reverse_list_recursive(create_linked_list([1]))
    print_linked_list(reversed3_rec, "Recursive Result")
    
    expected3 = [1]
    result3 = linked_list_to_list(reversed3_iter)
    print(f"Expected: {expected3}")
    print(f"Status: {'✓ PASS' if result3 == expected3 else '✗ FAIL'}")
    print()
    
    # Test Case 4: Empty list
    print("TEST 4: Empty List []")
    print("-" * 80)
    list4 = create_linked_list([])
    print("Original: None")
    
    reversed4_iter = reverse_list_iterative(None)
    print(f"Iterative Result: {reversed4_iter}")
    
    reversed4_rec = reverse_list_recursive(None)
    print(f"Recursive Result: {reversed4_rec}")
    
    print(f"Expected: None")
    print(f"Status: {'✓ PASS' if reversed4_iter is None else '✗ FAIL'}")
    print()
    
    # Test Case 5: Longer list
    print("TEST 5: Longer List [1,2,3,4,5,6,7,8,9,10]")
    print("-" * 80)
    list5 = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print_linked_list(list5, "Original")
    
    reversed5_iter = reverse_list_iterative(create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print_linked_list(reversed5_iter, "Iterative Result")
    
    expected5 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    result5 = linked_list_to_list(reversed5_iter)
    print(f"Expected: {expected5}")
    print(f"Status: {'✓ PASS' if result5 == expected5 else '✗ FAIL'}")
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
│ Iterative ⭐     │     O(n)         │      O(1)       │ BEST CHOICE     │
│ (Recommended)   │                  │   (Constant)    │ Most efficient  │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ Recursive       │     O(n)         │      O(n)       │ Asked in        │
│                 │                  │   (Call stack)  │ follow-up       │
└─────────────────┴──────────────────┴─────────────────┴─────────────────┘

Both have same time complexity, but iterative is more space-efficient!
"""


# =============================================================================
# INTERVIEW TIPS
# =============================================================================
"""
HOW TO ACE THIS IN AN INTERVIEW:

1. CLARIFY (30 seconds)
   • "Is this singly or doubly linked?" → Singly
   • "Can I modify the original list?" → Yes
   • "What should I return for empty list?" → None/null

2. DRAW IT OUT (1 minute) - VERY IMPORTANT!
   • Draw 3-4 nodes with arrows
   • Show how pointers change
   • Interviewers LOVE seeing this

3. EXPLAIN APPROACH (2 minutes)
   • "I'll use 3 pointers: prev, current, next"
   • "At each step, reverse one link"
   • "Move all pointers forward"
   • Mention O(n) time, O(1) space

4. CODE (5 minutes)
   • Write iterative solution
   • Add comments as you go
   • Handle edge cases (null, single node)

5. TEST (2 minutes)
   Walk through with [1,2,3]:
   • Show each pointer position
   • Show link reversal
   • Verify final result

6. DISCUSS ALTERNATIVES (1 minute)
   • Mention recursive approach exists
   • Trade-off: cleaner code but uses O(n) space
   • Iterative is usually preferred

COMMON MISTAKES:
❌ Losing reference to next node (save it first!)
❌ Not handling empty list or single node
❌ Getting confused with pointer directions
❌ Forgetting to return the new head (prev)

BONUS POINTS:
✓ Drawing the pointers clearly
✓ Mentioning both iterative and recursive
✓ Discussing space complexity difference
✓ Handling edge cases without being prompted

KEY PHRASES:
- "Three pointer technique"
- "In-place reversal"
- "Constant space complexity"
- "Linear time complexity"
"""


# =============================================================================
# RUN TESTS
# =============================================================================
if __name__ == "__main__":
    run_all_tests()