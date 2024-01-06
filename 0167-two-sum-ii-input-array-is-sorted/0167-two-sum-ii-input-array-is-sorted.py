# The solution has a time complexity of O(n), because we need to iterate
# through the input array once, and a space complexity of O(1), because
# no extra memory is needed.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Create left and right pointers
        left, right = 0, len(numbers) - 1

        # Loop until the two pointers overlap
        while left < right:
            # Add the current pointer elements
            sum = numbers[left] + numbers[right]

            # Sum above target, need to decrement right pointer
            if sum > target:
                right -= 1
            # Sum below target, need to increment left pointer
            elif sum < target:
                left += 1
            # Return the indices of the pointer elements
            else:
                return [left + 1, right + 1]