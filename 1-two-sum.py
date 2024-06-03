# Time: O(n) because you might need to iterate through the entire input array
# Space: O(n) because you need to create a hashmap to store seen elements
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Create a hashmap of seen elements, where keys are input array elements
    # and values are their indices
    seen = {}

    # Iterate through each input array element and its index
    for index, num in enumerate(nums):
      # Calculate the value that adds up to the target with the current element
      complement = target - num

      # If you've seen two elements that add up to the target, return
      # their indices
      if complement in seen:
        return [seen[complement], index]
      else:
        # Else add the current element and its index to the hashmap
        seen[num] = index