# The solution has a time complexity of O(n), since you need to iterate
# through the input string once using the sliding window approach with two
# pointers. The space complexity is O(1), since you need to create a hashmap
# that could potentially store up to 26 unique uppercase English chars.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Create a hash map that contains char-frequency pairs of all
        # chars in the current window
        count = {}

        # Create a variable to track the length of the longest valid substring
        longest = 0

        # Create left and right pointers for the sliding window
        left = right = 0

        while right < len(s):
            # Increment the count of the right pointer element
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1

            # Check to make sure the current window size minus the
            # count of the most frequent char is within the given
            # k number of chars allowed to be replaced
            while ((right - left + 1) - max(count.values())) > k:
                # Decrement the count of the left pointer element and
                # increment the left pointer
                count[s[left]] -= 1
                left += 1

            # Update the longest valid substring using the current longest
            # valid substring and the current window size
            longest = max(longest, (right - left + 1))

            # Increase the size of the sliding window
            right += 1

        return longest