# Solution is O(n) time complexity because you might have to iterate through
# the entire input array, and O(n) space complexity because you need to
# create a set to store array elements
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a set of seen numbers
        seen = set()

        # Iterate through nums array and check if each element has been seen
        for num in nums:

            # If nums array contains a duplicate
            if num in seen:
                return True

            # Else add the element to the set of seen numbers
            else:
                seen.add(num)

        # If the nums array doesn't contain any duplicates
        return False