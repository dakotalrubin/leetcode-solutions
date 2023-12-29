# Solution is O(n) time complexity since you only need to iterate
# through the nums array once, and O(n) space complexity because
# you need to create a dictionary, with O(1) insert and O(1) lookup
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary of seen numbers:
        # Elements are keys and indices are values
        seen = {}

        # Create a variable to track the current nums index
        index = 0

        for num in nums:
            # Calculate the number that adds up to target with num
            diff = target - num

            # If the difference is in the dictionary, return a list
            # of the indices of both numbers
            if diff in seen:
                return [seen[diff], index]

            # Add the seen number to the dictionary
            seen[num] = index
            index += 1