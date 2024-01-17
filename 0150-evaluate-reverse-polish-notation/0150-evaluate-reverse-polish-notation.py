# The solution has a time complexity of O(n), since you need to iterate
# through the input array once. The space complexity is O(n), since I'm
# using a stack to store expressions.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Create a stack to push and pop expressions from the input array
        stack = []

        for token in tokens:
            if token == "+":
                # Add the two most recent expressions
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                # Subtract the two most recent expressions in the order
                # they were pushed onto the stack
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == "*":
                # Multiply the two most recent expressions
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                # Divide the two most recent expressions in the order
                # they were pushed onto the stack
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                # Push an expression onto the stack
                stack.append(int(token))

        # Return the evaluated expression
        return stack.pop()
