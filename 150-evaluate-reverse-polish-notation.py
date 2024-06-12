# Time: O(n) since we need to iterate through the input array once
# Space: O(n) since we need a stack to store expressions from the input array
class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    # Create a stack to push and pop expressions from the input array
    stack = []

    # Create a hashmap of operators for O(1) lookup
    operators = {"+" : None, "-" : None, "*" : None, "/" : None}

    for token in tokens:
      # If we find an operator, pop the two most recent expressions
      if token in operators:
        a, b = int(stack.pop()), int(stack.pop())

      if token == "+":
        # Add the two most recent expressions
        stack.append(a + b)
      elif token == "-":
        # Subtract the two most recent expressions in the order they were pushed
        stack.append(b - a)
      elif token == "*":
        # Multiply the two most recent expressions
        stack.append(a * b)
      elif token == "/":
        # Divide the two most recent expressions in the order they were pushed
        stack.append(int(b / a))
      else:
        # Push the expression
        stack.append(token)

    # Return the final value of the expression
    return int(stack.pop())