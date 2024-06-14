# Time: O(n) since we need to iterate through the input array once
# Space: O(n) since we need to store indices of temperatures from the input
# array in a stack
class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    # Create an array to store the number of days it takes to reach a higher
    # temperature from a given temperature from the input array
    # (default: 0 days)
    answer = [0 for i in range(len(temperatures))]

    # Create a stack to store indices of temperatures from the input array
    stack = []

    for index, temperature in enumerate(temperatures):
      # While the stack is not empty and the current temperature is greater
      # than the temperature at the top of the stack
      while stack and temperature > temperatures[stack[-1]]:
        # Pop the index at the top of the stack, store as poppedIndex
        poppedIndex = stack.pop()

        # Calculate the number of days between the current index and poppedIndex
        # Store in the answer array on the day indicated by poppedIndex
        answer[poppedIndex] = index - poppedIndex

      # Append the index of the current temperature to the stack
      stack.append(index)

    return answer