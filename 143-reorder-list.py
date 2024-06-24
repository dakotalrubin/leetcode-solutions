# Time: O(n) since we need one pass through the linked list to find the middle,
# one pass to reverse the second half, and one pass to merge the two halves
# Space: O(1) since we rearrange the nodes in-place and don't need extra memory
#
# Here's the definition for a singly-linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  """This method rearranges the nodes of the linked list in-place."""
  def reorderList(self, head: Optional[ListNode]) -> None:
    # Find the middle node using "tortoise and hare" pointers
    slow, fast = head, head.next

    # While upcoming nodes aren't null, update the pointers: "slow" moves one
    # step at a time, "fast" moves two steps at a time
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    # Create two pointers: "prev" is null, "current" is the node after the
    # middle node "slow"
    prev, current = None, slow.next

    # Break the connection between the first and second halves of the list
    # using the node at the middle ("slow")
    # (ex. one possible list: 1->2->3 4->5->6)
    slow.next = None

    # Reverse the second half of the list while the current node isn't null
    while current:
      # Save the connection the current node has with the next node
      next = current.next

      # Set the current node's "next" node to the previous node
      current.next = prev

      # Increment the previous and current nodes using the saved connection
      prev, current = current, next

    # After the while loop, "prev" is now the last node in the list
    # The nodes in the second half now progress backwards
    # (ex. one possible list: 1->2->3 4<-5<-6)
    first, second = head, prev

    # Merge the two halves of the list
    while second:
      # Save the first and second node connections
      firstNext, secondNext = first.next, second.next

      # Set the first node's "next" node to the second node
      first.next = second

      # Set the second node's "next" node to the saved first node connection
      second.next = firstNext

      # Increment the first and second nodes using the saved connections
      first, second = firstNext, secondNext