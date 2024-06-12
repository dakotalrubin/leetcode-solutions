class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    """Perform a depth-first search."""
    def backtrack(openingN, closingN, path):
      # All opening and closing parentheses have been used
      if openingN == closingN == n:
        paths.append(path)
        return

      # Add an opening parenthesis to the path
      if openingN < n:
        backtrack(openingN + 1, closingN, path + "(")

      # Add a closing parenthesis to the path
      if closingN < openingN:
        backtrack(openingN, closingN + 1, path + ")")

    # Create variables to track the current number of opening and closing
    # parentheses
    openingN = closingN = 0

    # Create a path variable to represent one possible combination of valid
    # parentheses
    path = ""

    # Create a paths array that contains all possible combinations of valid
    # parentheses
    paths = []

    # Perform a depth-first search to generate all possible combinations of
    # valid parentheses
    backtrack(openingN, closingN, path)

    return paths