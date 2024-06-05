# Time: O(n) because you need to iterate through the input array once going
# forward and then once going backward
# Space: O(1) because the output array doesn't count as extra memory used
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    # Create an output array that will contain each product (default values: 1)
    answer = [1 for i in range(len(nums))]

    # Initialize default prefix and postfix values
    prefix = postfix = 1

    # Compute the prefix for each index in the output array
    for i in range(len(nums)):
      # The new output array value is the prefix
      answer[i] = prefix

      # The new prefix is the prefix times the current input array value
      prefix *= nums[i]

    # Compute the postfix for each index in the output array
    # The "stop" parameter in range() needs to be -1 to operate on index 0
    for i in range(len(nums) - 1, -1, -1):
      # The new output array value is the current output array value times
      # the postfix
      answer[i] *= postfix

      # The new postfix is the postfix times the current input array value
      postfix *= nums[i]

    return answer