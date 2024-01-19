# The solution has a time complexity of O(n), since we iterate through
# the input array once. The space complexity is O(n), since we use a
# stack to store indices of temperatures from the input array.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Create a stack to store indices of temperatures from the
        # input array
        stack = []

        # Create an array to store the number of days it takes to reach
        # a higher temperature after a given temperature in the input
        # array (default: 0, meaning there's no future day with a higher
        # temperature)
        answer = [0 for i in range(len(temperatures))]

        for index, temperature in enumerate(temperatures):
            # While the current temperature is greater than the
            # temperature at the top of the stack
            while stack and temperature > temperatures[stack[-1]]:
                # Pop the top index from the stack
                previousIndex = stack.pop()

                # Set the proper index in the answer array to be
                # the number of days it takes to reach a higher
                # temperature
                answer[previousIndex] = index - previousIndex

            # Append the index of the current temperature
            stack.append(index)

        return answer