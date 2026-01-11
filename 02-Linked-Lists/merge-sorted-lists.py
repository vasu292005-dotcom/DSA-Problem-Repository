"""
=============================================================================
PROBLEM: MERGE TWO SORTED LISTS
=============================================================================
Difficulty: Easy
Platform: LeetCode #21
Link: https://leetcode.com/problems/merge-two-sorted-lists/

PROBLEM STATEMENT:
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by 
splicing together the nodes of the first two lists.

Return the head of the merged linked list.

EXAMPLES:

Example 1:
  Input: list1 = [1,2,4], list2 = [1,3,4]
  Output: [1,1,2,3,4,4]
  
  Visual:
  list1: 1 → 2 → 4
  list2: 1 → 3 → 4
  merged: 1 → 1 → 2 → 3 → 4 → 4

Example 2:
  Input: list1 = [], list2 = []
  Output: []

Example 3:
  Input: list1 = [], list2 = [0]
  Output: [0]

CONSTRAINTS:
- The number of nodes in both lists is in range [0, 50]
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order
=============================================================================
"""


# =============================================================================
# LINKED LIST NODE DEFINITION
# =============================================================================

class ListNode:
    """
    Definition for singly-linked list node.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# =============================================================================
# SOLUTION 1: ITERATIVE WITH DUMMY NODE (RECOMMENDED) ⭐
# =============================================================================

def merge_two_lists_iterative(list1, list2):
    """
    Merge two sorted linked lists using dummy node pattern.
    
    KEY TECHNIQUE: DUMMY NODE
    - Create a dummy node to simplify edge cases
    - Always have a "current" pointer
    - Return dummy.next (skip the dummy node)
    
    HOW IT WORKS:
    1. Create a dummy node (placeholder)
    2. Use "current" pointer starting at dummy
    3. Compare values from both lists:
       - Attach smaller value to current
       - Move that list's pointer forward
       - Move current forward
    4. Attach remaining nodes from non-empty list
    5. Return dummy.next (actual head)
    
    STEP-BY-STEP EXAMPLE:
    list1: 1 → 2 → 4
    list2: 1 → 3 → 4
    
    Start:
    dummy → None
    current = dummy
    
    Step 1: Compare 1 and 1 (equal, take from list1)
    dummy → 1
    current at 1, list1 at 2, list2 at 1
    
    Step 2: Compare 2 and 1 (1 smaller)
    dummy → 1 → 1
    current at second 1, list1 at 2, list2 at 3
    
    Step 3: Compare 2 and 3 (2 smaller)
    dummy → 1 → 1 → 2
    current at 2, list1 at 4, list2 at 3
    
    Step 4: Compare 4 and 3 (3 smaller)
    dummy → 1 → 1 → 2 → 3
    current at 3, list1 at 4, list2 at 4
    
    Step 5: Compare 4 and 4 (equal, take from list1)
    dummy → 1 → 1 → 2 → 3 → 4
    current at first 4, list1 at None, list2 at 4
    
    Step 6: list1 is empty, attach rest of list2
    dummy → 1 → 1 → 2 → 3 → 4 → 4
    
    Return dummy.next (skip dummy) = 1 → 1 → 2 → 3 → 4 → 4
    
    TIME COMPLEXITY: O(n + m)
    - n = length of list1
    - m = length of list2
    - Visit each node exactly once
    
    SPACE COMPLEXITY: O(1)
    - Only using pointers (dummy, current)
    - Not creating new nodes, just rearranging
    
    WHEN TO USE:
    - DEFAULT CHOICE for interviews
    - Clean and easy to understand
    - Handles all edge cases elegantly
    """
    # Create dummy node (makes code cleaner)
    dummy = ListNode(0)
    current = dummy
    
    # While both lists have nodes
    while list1 and list2:
        # Compare values
        if list1.val <= list2.val:
            # Attach list1's node
            current.next = list1
            list1 = list1.next
        else:
            # Attach list2's node
            current.next = list2
            list2 = list2.next
        
        # Move current forward
        current = current.next
    
    # Attach remaining nodes (one list is empty, other might have nodes)
    if list1:
        current.next = list1
    else:
        current.next = list2
    
    # Return actual head (skip dummy)
    return dummy.next


# =============================================================================
# SOLUTION 2: RECURSIVE APPROACH
# =============================================================================

def merge_two_lists_recursive(list1, list2):
    """
    Merge two sorted lists using recursion.
    
    HOW IT WORKS:
    - Base case: if one list is empty, return the other
    - Recursive case:
      1. Compare heads of both lists
      2. Choose smaller one
      3. Recursively merge rest with other list
      4. Return the chosen head
    
    EXAMPLE:
    list1: 1 → 2 → 4
    list2: 1 → 3 → 4
    
    merge(1→2→4, 1→3→4)
      → 1.next = merge(2→4, 1→3→4)
                  → 1.next = merge(2→4, 3→4)
                              → 2.next = merge(4, 3→4)
                                          → 3.next = merge(4, 4)
                                                      → 4.next = merge(None, 4)
                                                                  → return 4
    
    Builds: 1 → 1 → 2 → 3 → 4 → 4
    
    TIME COMPLEXITY: O(n + m)
    - Each node visited once
    
    SPACE COMPLEXITY: O(n + m)
    - Recursion stack depth = total nodes
    
    WHEN TO USE:
    - When asked for recursive solution
    - Elegant and concise code
    - Not ideal for very long lists (stack overflow risk)
    """
    # Base cases
    if not list1:
        return list2
    if not list2:
        return list1
    
    # Recursive case: choose smaller head
    if list1.val <= list2.val:
        # list1's head is smaller
        # Merge rest of list1 with list2
        list1.next = merge_two_lists_recursive(list1.next, list2)
        return list1
    else:
        # list2's head is smaller
        # Merge list1 with rest of list2
        list2.next = merge_two_lists_recursive(list1, list2.next)
        return list2


# =============================================================================
# HELPER FUNCTIONS FOR TESTING
# =============================================================================

def create_linked_list(values):
    """Create linked list from list of values."""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


def linked_list_to_list(head):
    """Convert linked list to Python list."""
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result


def print_linked_list(head, label=""):
    """Print linked list in readable format."""
    values = linked_list_to_list(head)
    if label:
        if values:
            print(f"{label}: {' → '.join(map(str, values))} → None")
        else:
            print(f"{label}: None")
    else:
        if values:
            print(f"{' → '.join(map(str, values))} → None")
        else:
            print("None")


# =============================================================================
# TEST CASES
# =============================================================================

def run_all_tests():
    """
    Test both solutions with various test cases.
    """
    print("=" * 80)
    print("            TESTING MERGE TWO SORTED LISTS SOLUTIONS")
    print("=" * 80)
    print()
    
    # Test Case 1: Standard merge
    print("TEST 1: Standard Merge [1,2,4] and [1,3,4]")
    print("-" * 80)
    list1_a = create_linked_list([1, 2, 4])
    list2_a = create_linked_list([1, 3, 4])
    print_linked_list(list1_a, "List 1")
    print_linked_list(list2_a, "List 2")
    
    merged1_iter = merge_two_lists_iterative(
        create_linked_list([1, 2, 4]),
        create_linked_list([1, 3, 4])
    )
    print_linked_list(merged1_iter, "Iterative Result")
    
    merged1_rec = merge_two_lists_recursive(
        create_linked_list([1, 2, 4]),
        create_linked_list([1, 3, 4])
    )
    print_linked_list(merged1_rec, "Recursive Result")
    
    expected1 = [1, 1, 2, 3, 4, 4]
    result1 = linked_list_to_list(merged1_iter)
    print(f"Expected: {expected1}")
    print(f"Status: {'✓ PASS' if result1 == expected1 else '✗ FAIL'}")
    print()
    
    # Test Case 2: Both empty
    print("TEST 2: Both Empty [] and []")
    print("-" * 80)
    list2_a = create_linked_list([])
    list2_b = create_linked_list([])
    print_linked_list(list2_a, "List 1")
    print_linked_list(list2_b, "List 2")
    
    merged2 = merge_two_lists_iterative(None, None)
    print_linked_list(merged2, "Iterative Result")
    
    expected2 = []
    result2 = linked_list_to_list(merged2)
    print(f"Expected: {expected2}")
    print(f"Status: {'✓ PASS' if result2 == expected2 else '✗ FAIL'}")
    print()
    
    # Test Case 3: One empty
    print("TEST 3: One Empty [] and [0]")
    print("-" * 80)
    list3_a = create_linked_list([])
    list3_b = create_linked_list([0])
    print_linked_list(list3_a, "List 1")
    print_linked_list(list3_b, "List 2")
    
    merged3 = merge_two_lists_iterative(None, create_linked_list([0]))
    print_linked_list(merged3, "Iterative Result")
    
    expected3 = [0]
    result3 = linked_list_to_list(merged3)
    print(f"Expected: {expected3}")
    print(f"Status: {'✓ PASS' if result3 == expected3 else '✗ FAIL'}")
    print()
    
    # Test Case 4: Different lengths
    print("TEST 4: Different Lengths [1,2,3,4,5] and [1,3]")
    print("-" * 80)
    list4_a = create_linked_list([1, 2, 3, 4, 5])
    list4_b = create_linked_list([1, 3])
    print_linked_list(list4_a, "List 1")
    print_linked_list(list4_b, "List 2")
    
    merged4 = merge_two_lists_iterative(
        create_linked_list([1, 2, 3, 4, 5]),
        create_linked_list([1, 3])
    )
    print_linked_list(merged4, "Iterative Result")
    
    expected4 = [1, 1, 2, 3, 3, 4, 5]
    result4 = linked_list_to_list(merged4)
    print(f"Expected: {expected4}")
    print(f"Status: {'✓ PASS' if result4 == expected4 else '✗ FAIL'}")
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
│ Iterative ⭐     │    O(n + m)      │      O(1)       │ BEST CHOICE     │
│ (Recommended)   │                  │   (Constant)    │ Most efficient  │
├─────────────────┼──────────────────┼─────────────────┼─────────────────┤
│ Recursive       │    O(n + m)      │    O(n + m)     │ Asked in        │
│                 │                  │   (Call stack)  │ follow-up       │
└─────────────────┴──────────────────┴─────────────────┴─────────────────┘

Iterative is more space-efficient!
"""


# =============================================================================
# INTERVIEW TIPS
# =============================================================================
"""
HOW TO ACE THIS IN AN INTERVIEW:

1. CLARIFY (30 seconds)
   • "Are both lists sorted?" → Yes
   • "Can I modify the original lists?" → Yes
   • "What if one list is empty?" → Return the other

2. EXPLAIN DUMMY NODE PATTERN (Important!)
   • "I'll use a dummy node to simplify code"
   • "Helps avoid special cases for head"
   • "Common pattern in linked list problems"

3. EXPLAIN APPROACH (2 minutes)
   • "Compare values from both lists"
   • "Always attach the smaller one"
   • "Move pointers forward"
   • "Attach remaining nodes at end"

4. CODE (5 minutes)
   • Write iterative solution with dummy node
   • Show clear pointer manipulation
   • Handle both lists becoming empty

5. WALK THROUGH (2 minutes)
   Use [1,2,4] and [1,3,4]:
   • Show dummy node creation
   • Step through comparisons
   • Show how current moves
   • Verify final result

COMMON MISTAKES:
❌ Not handling empty lists
❌ Forgetting to attach remaining nodes
❌ Returning dummy instead of dummy.next
❌ Losing reference to list heads

BONUS POINTS:
✓ Explaining dummy node pattern
✓ Mentioning recursive solution
✓ Discussing space complexity difference
✓ Showing clean pointer manipulation

KEY PHRASES:
- "Dummy node pattern"
- "Two-pointer technique"
- "In-place merging"
- "Linear time complexity"
"""


# =============================================================================
# RUN TESTS
# =============================================================================
if __name__ == "__main__":
    run_all_tests()