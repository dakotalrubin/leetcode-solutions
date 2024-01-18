class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Perform a depth-first search to find all possible
        # combinations of well-formed parentheses
        def backtrack(openN, closedN, path):
            # The max numbers of opening and closing parentheses
            # have been used
            if openN == closedN == n:
                paths.append(path)
                return

            # Add an opening parenthesis to the path
            if openN < n:
                backtrack(openN + 1, closedN, path + "(")

            # Add a closed parenthesis to the path
            if closedN < openN:
                backtrack(openN, closedN + 1, path + ")")

        # Create variables to track the current number of opening
        # and closing parentheses
        openN = closedN = 0

        # Create a path variable to represent one possible combination
        # of well-formed parentheses
        path = ""

        # Create an array that contains all possible combinations of
        # well-formed parentheses
        paths = []

        # Make a recursive call to perform a depth-first search
        backtrack(openN, closedN, path)

        return paths