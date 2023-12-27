class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a set of seen integers (O(1) lookup)
        seen = set()

        # Iterate through nums array and check if each element has been seen
        for num in nums:

            # If nums array contains a duplicate
            if num in seen:
                return True

            # Else add the element to the set of seen integers
            else:
                seen.add(num)

        # If the nums array doesn't contain any duplicates
        return False