# Time: O(nlog(n)) for sorting the input array, plus O(n^2) for using a nested
# loop to iterate through the input array and check number combinations using
# the two-pointer approach, so the time complexity is O(n^2) overall
# Space: O(n) since we need Python's sort() method
class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    # Create a list that will contain unique triplets
    triplets = []

    # Sort the input array
    nums.sort()

    # Loop through the input array and only consider unique elements
    for index, num in enumerate(nums):
      # If the current element isn't unique, skip it
      # The first element in the input array is exempt from this check
      if num == nums[index - 1] and index > 0:
        continue

      # Create left and right pointers
      left, right = index + 1, len(nums) - 1

      # Check pointer bounds
      while left < right:
        # Calculate the sum of the current elements
        sum = num + nums[left] + nums[right]

        # Adjust pointers depending on how sum compares to zero
        if sum > 0:
          right -= 1
        elif sum < 0:
          left += 1
        else:
          # Three unique elements that add up to zero have been found
          triplets.append([num, nums[left], nums[right]])

          # Increment the left pointer to look for new unique triplets
          left += 1

          # While the new left pointer element isn't unique, skip it
          while left < right and nums[left] == nums[left - 1]:
            left += 1

    return triplets