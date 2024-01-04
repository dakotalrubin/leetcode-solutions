# The solution has a time complexity of O(n), because it's necessary to
# iterate through the input array once to check if each element is the start
# of a consecutive sequence. The space complexity is O(n), since we have to
# store every element of the input array in a set for O(1) lookup.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a set that contains every element in nums
        nums_set = set(nums)

        # Create a variable to track the longest sequence
        longest = 0
        
        for num in nums:
            # Initialize the length of this sequence
            length = 0

            # Check if num is the start of a sequence
            if (num - 1) not in nums_set:

                # Begin counting the length of this sequence
                while (num + length) in nums_set:
                    length += 1

                # Update the length of the longest sequence
                longest = max(longest, length)

        return longest