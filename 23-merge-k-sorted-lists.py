# Time: O(nlog(k)), where n is the length of each linked list and k is the number
# of linked lists, since we need log k number of steps to run mergesort, and
# each step runs in O(n) time
# Space: O(log(k)) since we need to store half the number of linked lists at
# each step during the merging process
#
# Here's the definition for a singly-linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  """This method takes two lists sorted in ascending order and merges them."""
  def mergeTwoLists(self, list1, list2):
    # Base case for recursion: check if each head node is null
    if not list1:
      return list2
    if not list2:
      return list1

    # Check which head node has a smaller value
    if list1.val < list2.val:
      # Set the next node of list1 as the result of a nested mergeTwoLists() call
      list1.next = self.mergeTwoLists(list1.next, list2)

      # Use the head node of list1 as the head of the merged list
      return list1
    else:
      # Set the next node of list2 as the result of a nested mergeTwoLists() call
      list2.next = self.mergeTwoLists(list1, list2.next)

      # Use the head node of list2 as the head of the merged list
      return list2

  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # If lists is null or its length is zero, return null
    if not lists or len(lists) == 0:
      return None

    # Keep merging lists until only one remains
    while len(lists) > 1:
      # Create a list that will contain this iteration of merged lists
      mergedLists = []

      # Each for loop will involve 2 lists
      for i in range(0, len(lists), 2):
        # Store the first list
        list1 = lists[i]

        # Store the second list if "i" is within bounds, otherwise null
        list2 = lists[i + 1] if (i + 1) < len(lists) else None

        # Append the merged list to mergedLists
        mergedLists.append(self.mergeTwoLists(list1, list2))

      # Update lists to be the result of this iteration of merged lists
      lists = mergedLists

    # Return the final merged list
    return lists[0]