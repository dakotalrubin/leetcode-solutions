# The solution has a time complexity of O(n), since you need to iterate
# through the input string once and perform one pop or push operation per
# char in the input string. The space complexity is also O(n), since you
# might need to push every char from the input string to the stack (the
# input string might contain only opening parentheses, for example).
class Solution:
    def isValid(self, s: str) -> bool:
        # Create a stack that contains opening chars (top == end)
        stack = []

        # Create a hashmap that contains (closing char : opening char) pairs
        matches = {")" : "(", "]" : "[", "}" : "{"}

        for char in s:
            # Push an opening char to the stack
            if char in matches.values():
                stack.append(char)
            # For a closing char, check the stack for a matching opening char
            elif char in matches.keys():
                # If there's a match, pop the opening char from the stack
                # (as long as the stack isn't empty)
                if stack and stack[-1] == matches[char]:
                    stack.pop()
                # If there's no match, a closing char wasn't opened properly
                else:
                    return False
            else:
                # Only parentheses, brackets and braces are allowed as chars
                return False

        # The input string is valid if the stack is empty by the end
        if stack:
            return False
        else:
            return True