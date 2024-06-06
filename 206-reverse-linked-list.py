# Time: O(n) because we need to traverse the linked list once
# Space: O(1) because no extra memory is needed
#
# NOTE: Here's the definition for a singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # There is no previous node to the first node in the linked list
    prevNode = None

    # The first node in the linked list is the head
    currentNode = head

    # Check node bounds in the linked list
    while currentNode != None:
      # Save the connection that the current node has with the next node
      nextNode = currentNode.next

      # Set the current node to point to the previous node
      currentNode.next = prevNode

      # Increment the previous node and the current node
      prevNode = currentNode
      currentNode = nextNode

    # prevNode is now the final node in the original linked list
    return prevNode