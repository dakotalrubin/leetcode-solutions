# Time: O(n+m), where n and m are the lengths of list1 and list2 respectively,
# since we need to iterate through every element in both lists
# Space: O(1) since no extra memory is needed
#
# Here's the definition for a singly-linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # Base case for recursion: check if each head node is null
    if not list1:
      return list2
    if not list2:
      return list1

    # Check which head node has a smaller value
    if list1.val < list2.val:
      # Set the next node of list1 as the result of a nested mergeTwoLists() call
      list1.next = self.mergeTwoLists(list1.next, list2)

      # Use the current head node of list1 as the head of the merged list
      return list1
    else:
      # Set the next node of list2 as the result of a nested mergeTwoLists() call
      list2.next = self.mergeTwoLists(list1, list2.next)

      # Use the current head node of list2 as the head of the merged list
      return list2