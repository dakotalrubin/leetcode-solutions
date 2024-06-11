# Time: O(m+n), where m is the length of string s and n is the length of string t,
# since we need to iterate through each string once, using the sliding window
# approach with two pointers for string s
# Space: O(52*2), since we need two hashmaps, which might need to store the
# uppercase and lowercase English letters in each string as unique entries
class Solution:
  def minWindow(self, s: str, t: str) -> str:
    # Create a variable to hold the minimum window substring
    # Create another variable that contains its length (default: infinity)
    minSubstring = ""
    minSubstringLength = float("infinity")

    # Check to make sure string t isn't the empty string, and ensure string s
    # has enough characters to support string t as a substring
    if t == "" or len(s) < len(t):
      return minSubstring

    # Create a hashmap to store all the characters from string t, and create
    # another to store all the characters from string s in the current window
    tCount, sCount = {}, {}

    # Store all the characters from string t in tCount
    for char in t:
      if char in tCount:
        tCount[char] += 1
      else:
        tCount[char] = 1

    # "have" is the number of characters in the current window that also belong
    # to tCount in the proper quantity, and "need" is the length of tCount
    have, need = 0, len(tCount)

    # Create left and right pointers for the sliding window
    left = right = 0

    # Check pointer bounds
    while right < len(s):
      # Add the rightmost char in the current window to sCount
      if s[right] in sCount:
        sCount[s[right]] += 1
      else:
        sCount[s[right]] = 1

      # Update "have" if the rightmost char in the current window also belongs
      # to tCount in the proper quantity
      if s[right] in tCount and sCount[s[right]] == tCount[s[right]]:
        have += 1

      # While the current window contains a valid minimum window substring
      while have == need:
        # Update the minimum window substring and its length
        if (right - left + 1) < minSubstringLength:
          minSubstring = s[left:(right + 1)]
          minSubstringLength = len(minSubstring)

        # Decrement the leftmost char in the current window from sCount
        sCount[s[left]] -= 1

        # Update "have" if the leftmost char in the current window also belongs
        # to tCount in a smaller quantity
        if s[left] in tCount and sCount[s[left]] < tCount[s[left]]:
          have -= 1

        # Increment the left pointer to shrink the window size
        left += 1

      # Increment the right pointer to expand the window size
      right += 1

    return minSubstring