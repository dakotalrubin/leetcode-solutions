# Time: O(n) since we iterate through the linked list using the "tortoise and
# hare" approach with two pointers. It will take a maximum of n steps for the
# fast pointer to catch up to the slow pointer if a cycle exists, where n is
# the length of the linked list
# Space: O(1) since no extra memory is needed
#
# Here's the definition for a singly-linked list:
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    # Create two pointers for the "tortoise and hare" approach
    slow = fast = head

    # While the upcoming node isn't null, update the pointers: "slow" moves one
    # step at a time, "fast" moves two steps at a time
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

      # If the two pointers are equal at some point, the list contains a cycle
      if slow == fast:
        return True

    # The list doesn't contain a cycle
    return False