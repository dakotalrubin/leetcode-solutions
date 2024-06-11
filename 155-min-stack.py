# Time: O(1) since each stack operation is performed in constant time
# Space: O(1) since two stacks are needed to implement a min stack
#
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class MinStack:

  """Initialize the min stack object."""
  def __init__(self):
    # Create a normal stack and a min stack that tracks the minimum value added
    # to the normal stack so far
    self.stack, self.minStack = [], []

  """Push a value to both stacks."""
  def push(self, val: int) -> None:
    # Always push the value to the normal stack
    self.stack.append(val)

    # If minStack is empty, push the value to minStack
    if not self.minStack:
      self.minStack.append(val)
    else:
      # If minStack isn't empty, update and push the minimum value by comparing
      # the current minimum value with the argument "val"
      minValue = min(self.minStack[-1], val)
      self.minStack.append(minValue)

  """Pop the top of both stacks."""
  def pop(self) -> None:
    self.stack.pop()
    self.minStack.pop()

  """Get the top of the normal stack."""
  def top(self) -> int:
    return self.stack[-1]

  """Get the top of the min stack."""
  def getMin(self) -> int:
    return self.minStack[-1]