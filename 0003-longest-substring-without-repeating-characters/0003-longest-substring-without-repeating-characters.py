# The solution has a time complexity of O(n), since you need to iterate
# through the string once using the sliding window approach with two
# pointers. The space complexity is O(n), since you might need to store
# every character from the string in a set.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create a variable to track the longest size of the sliding window
        longest = 0

        # Create a set that contains all characters in the sliding window
        char_set = set()

        # Create left and right pointers for the sliding window
        left = right = 0

        while right < len(s):
            # If the right pointer element is a duplicate, increment the
            # left pointer past the first instance of that element and
            # remove all previous elements from the set
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add the right pointer element to the set
            char_set.add(s[right])

            # Update the longest size of the sliding window
            longest = max(longest, right - left + 1)

            # Increase the size of the sliding window
            right += 1

        return longest