# Time: O(n) since you need to make two passes through the original list
# Space: O(n) since you need to store every node from the original list inside 
# a hashmap
#
# Here's the definition for a Node:
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
class Solution:
  def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    # Create a hashmap that will contain mappings of old nodes to copied nodes
    # If an old node's "next" or "random" attributes point to null, the hashmap
    # should return None
    oldToCopy = { None : None }

    # Create a variable that tracks the current node in the list
    current = head

    # First pass through the list will copy nodes
    while current:
      # Create a copy of the current node (without "next" or "random" attributes)
      copy = Node(current.val)

      # Add an entry to the hashmap for this (old node : copied node) mapping
      oldToCopy[current] = copy

      # Increment the current node
      current = current.next

    # Reset the variable that tracks the current node in the list
    current = head

    # Second pass through the list will set pointers
    while current:
      # Get the copy of the current node
      copy = oldToCopy[current]

      # Set the copy node's "next" attribute
      copy.next = oldToCopy[current.next]

      # Set the copy node's "random" attribute
      copy.random = oldToCopy[current.random]

      # Increment the current node
      current = current.next

    # Take the head of the original list and return the head of the copied list
    return oldToCopy[head]