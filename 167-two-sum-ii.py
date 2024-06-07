# Time: O(n) since we need to iterate through the input array once using the
# two-pointer approach
# Space: O(1) since no extra memory is needed
class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    # Create left and right pointers
    left, right = 0, len(numbers) - 1

    # Check pointer bounds
    while left < right:
      # Add the current pointer elements
      sum = numbers[left] + numbers[right]

      # Adjust pointers depending on how the sum compares to the target
      if sum > target:
        right -= 1
      elif sum < target:
        left += 1
      else:
        # Return pointers adjusted for 1-indexing
        return [left + 1, right + 1]