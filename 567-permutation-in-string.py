# Time: O(n) since we need to iterate through string s2 using the sliding window
# approach with two pointers
# Space: O(52) since we need two hashmaps, which might have to store every
# character in each string as a unique entry
class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    # Make sure string s2 has enough characters to support a permutation of
    # string s1
    if len(s2) < len(s1):
      return False

    # Create a hashmap to store char:frequency pairs for string s1, and
    # create another hashmap to store char:frequency pairs for string s2
    # in the current window
    s1Count, s2Count = {}, {}

    # Store every char:frequency pair from string s1 in s1Count
    for char in s1:
      if char in s1Count:
        s1Count[char] += 1
      else:
        s1Count[char] = 1

    # Store every char:frequency pair from string s2 for the first window
    for i in range(len(s1)):
      if s2[i] in s2Count:
        s2Count[s2[i]] += 1
      else:
        s2Count[s2[i]] = 1

    # Create left and right pointers for the sliding window
    # The window size will always be the length of string s1
    left, right = 0, len(s1) - 1

    # Check pointer bounds
    while right < len(s2):
      # Check whether the current window contains a permutation of string s1
      if s1Count == s2Count:
        return True

      # Decrement the leftmost character in the current window from s2Count
      s2Count[s2[left]] -= 1

      # If the count of the leftmost character in the current window is zero,
      # pop the char:frequency pair from s2Count
      if s2Count[s2[left]] == 0:
        s2Count.pop(s2[left])

      # Increment the left and right pointers to shift the window
      left += 1
      right += 1

      # Check pointer bounds
      if right < len(s2):
        # Store the rightmost character in the new window in s2Count
        if s2[right] in s2Count:
          s2Count[s2[right]] += 1
        else:
          s2Count[s2[right]] = 1

    # String s2 doesn't contain a permutation of string s1
    return False