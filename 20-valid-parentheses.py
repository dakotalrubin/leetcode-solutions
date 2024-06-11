# Time: O(n) since we need to iterate through the input string once using
# a stack and perform one push or pop operation per char in the input string
# Space: O(n) since we might need to push every char from the input string
# to the stack (ex. the input string contains only opening parentheses)
class Solution:
  def isValid(self, s: str) -> bool:
    # Create a stack to hold opening chars (top == end of the array)
    stack = []

    # Create a hashmap that contains (closing char : opening char) pairs
    matches = {")" : "(", "]" : "[", "}" : "{"}

    for char in s:
      if char in matches.values():
        # Append an opening char to the stack
        stack.append(char)
      elif char in matches.keys():
        # For a closing char, check the stack for the matching opening char
        if stack and stack[-1] == matches[char]:
          # Pop the matching opening char from the stack
          stack.pop()
        else:
          # The closing char doesn't have a matching opening char
          return False
      else:
        # The char isn't an opening or closing char
        return False

    # The input string is only valid if the stack is empty by the end
    if stack:
      return False
    else:
      return True