# The time complexity for each stack operation is O(1).
class MinStack:

    def __init__(self):
        # Create a normal stack and a min stack that will track
        # the minimum value added to the normal stack so far
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # Always push the value onto the normal stack
        self.stack.append(val)

        # If minStack is empty, push the value onto minStack
        if not self.minStack:
            self.minStack.append(val)
        # If minStack isn't empty, push the mimumum value
        # (the current minimum value vs. the new value being pushed)
        else:
            val = min(val, self.minStack[-1])
            self.minStack.append(val)

    def pop(self) -> None:
        # Pop the top value from both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Get the top value from the normal stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Get the top value from the min stack
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()