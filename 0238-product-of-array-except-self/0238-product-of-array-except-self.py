# The solution has a time complexity of O(n) and a space complexity of O(1),
# because the output array doesn't count as extra space (from the constraints)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create the output array using list comprehension
        answer = [1 for i in range(len(nums))]

        # Initialize prefix and postfix values
        prefix = postfix = 1

        # Compute the prefix multiplication for each index in the output array
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        # Compute the postfix multiplication for each index in the output array
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer