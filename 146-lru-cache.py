# Time: Each operation runs in O(1) average time complexity
#
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class Node:
  """This method initializes a Node in a doubly-linked list."""
  def __init__(self, key, value):
    # Store the key and value arguments
    self.key, self.value = key, value

    # Initialize prev and next pointers to null
    self.prev = self.next = None

class LRUCache:
  """This method initializes an LRU cache with the given capacity."""
  def __init__(self, capacity: int):
    # Store the capacity argument
    self.capacity = capacity

    # Create a hashmap, where each key is the provided key and each value is
    # a pointer to a Node in a doubly-linked list
    self.cache = {}

    # Create two pointers, which are dummy nodes with default keys and values
    self.left, self.right = Node(0, 0), Node(0, 0)

    # Connect the dummy nodes ("left" is the least recently used side of the list,
    # "right" is the most recently used side of the list)
    self.left.next = self.right
    self.right.prev = self.left

  """This method removes a Node from a doubly-linked list."""
  def remove(self, Node):
    # Save the current Node's prev and next pointers
    prev, next = Node.prev, Node.next

    # Set the previous Node's next pointer to the Node after the current Node,
    # and set the next Node's prev pointer to the Node before the current Node
    prev.next, next.prev = next, prev

  """This method inserts a Node at the rightmost position in a doubly-linked
  list."""
  def insert(self, Node):
    # Get ready to insert the Node between the rightmost Node and the dummy Node
    prev, next = self.right.prev, self.right

    # Insert the new Node by updating the previous and next Nodes' pointers
    prev.next = next.prev = Node

    # Update the new Node's prev and next pointers
    Node.prev, Node.next = prev, next

  """This method will return an existing key's value, otherwise return -1."""
  def get(self, key: int) -> int:
    if key in self.cache:
      # Update the most recently used Node by removing this Node from the list
      # and inserting it at the end if the key already exists
      self.remove(self.cache[key])
      self.insert(self.cache[key])

      # Access the Node that the key points to and return its value attribute
      return self.cache[key].value
    else:
      # Else the key doesn't exist in the cache
      return -1

  """This method updates an existing key's value, or inserts a new Node and
  key-value pair."""
  def put(self, key: int, value: int) -> None:
    if key in self.cache:
      # Remove the associated Node from the list if the key already exists
      self.remove(self.cache[key])

    # Insert a new Node into the cache as a value
    self.cache[key] = Node(key, value)

    # Insert the new Node into the list
    self.insert(self.cache[key])

    # If the length of the cache exceeds its capacity
    if len(self.cache) > self.capacity:
      # Store the least recently used Node in the list
      lruNode = self.left.next

      # Remove the least recently used Node from the list
      self.remove(lruNode)

      # Pop the least recently used key-value pair from the cache
      self.cache.pop(lruNode.key)