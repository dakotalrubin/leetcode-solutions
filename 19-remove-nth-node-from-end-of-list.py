# Time: O(n) since we need to make one pass through the list using two pointers
# Space: O(1) since we only need to create a dummy node
#
# Here's the definition for a singly-linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # Create a dummy node and insert before the head
    dummy = ListNode(0, head)

    # Create a left pointer at the dummy node and a right pointer at the head
    left, right = dummy, head

    # Shift the right pointer n times
    while n > 0 and right:
      right = right.next
      n -= 1

    # Increment the left and right pointers until the end of the list
    while right:
      left, right = left.next, right.next

    # Set the left pointer's "next" attribute to the node after the next
    left.next = left.next.next

    # Return the head of the updated list
    return dummy.next