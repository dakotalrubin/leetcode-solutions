# Time: O(n) because you might need to iterate through every element in the
# input array
# Space: O(n) because you need to create a set, which might need to store every
# element in the input array
class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
    # Create a set of seen elements
    seen = set()

    # Iterate through the input array and check if each element has been seen
    for num in nums:
      # If the input array contains a duplicate
      if num in seen:
        return True

      # Else add the element to the set of seen elements
      else:
        seen.add(num)

    # The input array doesn't contain duplicates
    return False