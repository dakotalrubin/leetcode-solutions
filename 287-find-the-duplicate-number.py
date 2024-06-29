# Time: O(n) since we iterate through the array using the "tortoise and hare"
# approach with two pointers
# Space: O(1) since we use constant memory
class Solution:
  def findDuplicate(self, nums: List[int]) -> int:
    # Create two variables for the "tortoise and hare" approach
    slow, fast = 0, 0

    # Iterate through the array until slow and fast overlap
    while True:
      slow, fast = nums[slow], nums[nums[fast]]

      # If slow and fast overlap, break the loop
      if slow == fast:
        break

    # Create another slow variable at the start of the array
    slow2 = 0

    # Iterate through the array until slow and slow2 overlap
    while True:
      slow, slow2 = nums[slow], nums[slow2]

      # If slow and slow2 overlap, return either of them
      if slow == slow2:
        return slow