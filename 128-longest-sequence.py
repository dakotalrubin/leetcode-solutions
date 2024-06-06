# Time: O(n) because we need to iterate through the input array once to build
# a hashset and once more to check if each element is the start of a
# consecutive sequence
# Space: O(n) because we need to store every element from the input array in a
# hashset for O(1) lookup
class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    # Create a hashset that contains every element in the input array
    numsSet = set(nums)

    # Create a variable to track the length of the longest consecutive sequence
    longestLength = 0

    for num in nums:
      # Initialize the length of the current consecutive sequence
      currentLength = 1

      # Ignore elements that aren't the start of a consecutive sequence
      if (num - 1) in numsSet:
        continue
      else:
        # Increment the length of the current consecutive sequence if the
        # current element has a right neighbor (the sequence continues)
        while (num + currentLength) in numsSet:
          currentLength += 1

        # Update the length of the longest consecutive sequence
        longestLength = max(longestLength, currentLength)

    return longestLength