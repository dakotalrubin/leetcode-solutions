# Time: O(n) since we need to iterate through the input string once using
# the sliding window approach with two pointers
# Space: O(26) since we might need to store every character from the input
# string in a hashmap as a unique entry
class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    # Create a hashmap to hold char:frequency pairs for every character in the
    # current window
    count = {}

    # Create a variable to track the length of the longest valid substring
    longest = 0

    # Create left and right pointers for the sliding window
    left = right = 0

    # Check pointer bounds
    while right < len(s):
      # Increment the count of the right pointer element
      if s[right] in count:
        count[s[right]] += 1
      else:
        count[s[right]] = 1

      # Make sure the current window size minus the count of the most frequent
      # character is within the k number of characters allowed to be replaced
      while ((right - left + 1) - max(count.values())) > k:
        # Decrement the count of the left pointer element
        count[s[left]] -= 1

        # Shrink the window size
        left += 1

      # Update the length of the longest valid substring
      longest = max(longest, right - left + 1)

      # Increase the window size
      right += 1

    return longest