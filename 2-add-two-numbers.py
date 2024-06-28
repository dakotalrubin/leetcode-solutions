# Time: O(n) since we iterate through both lists to compute each sum digit
# Space: O(n) since we create a new list to contain the sum of both lists
#
# Here's the definition for a singly-linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # Create a dummy node to avoid edge cases with inserting into a linked list
    dummy = ListNode()

    # Create a variable that tracks the current node in the sum list
    current = dummy

    # Create a variable that tracks the current carry value (default: 0)
    carry = 0

    # Add digits while at least one list isn't null or there's a carry
    while l1 or l2 or carry:
      # Get the current digit from each list (default: 0 if no digit)
      l1Digit = l1.val if l1 else 0
      l2Digit = l2.val if l2 else 0

      # Add the two digits
      newDigit = l1Digit + l2Digit + carry

      # Calculate the new carry value
      carry = newDigit // 10

      # Only use the ones-place digit from newDigit
      newDigit = newDigit % 10

      # Insert a new node into the sum list with a value of newDigit
      current.next = ListNode(newDigit)

      # Increment the current node in the sum list
      current = current.next

      # Increment the current node in each list if neither is null
      l1 = l1.next if l1 else None
      l2 = l2.next if l2 else None

    # Return the first valid node in the sum list
    return dummy.next