# Time: O(n) since you need to iterate through the input string using
# the sliding window approach with two pointers
# Space: O(n) since you might need to store every character from the
# input string in a hashset as a unique entry
class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    # Create a hashset to store seen characters from the current window
    seen = set()

    # Create a variable to track the length of the longest substring
    longest = 0

    # Create left and right pointers for the sliding window
    left = right = 0

    # Check pointer bounds
    while right < len(s):
      if s[right] not in seen:
        # Add an unseen character to the hashset
        seen.add(s[right])

        # Update the length of the longest substring
        longest = max(longest, right - left + 1)

        # Increase the window size
        right += 1
      else:
        # Shrink the window from the left until the seen character is removed
        while s[right] in seen:
          seen.remove(s[left])
          left += 1

    return longest