# Time: O(n) because we need to iterate through the entire input string using
# the two-pointer approach
# Space: O(n) because no extra memory is needed
class Solution:
  def isPalindrome(self, s: str) -> bool:
    # Create two pointers to iterate through the input string
    left, right = 0, len(s) - 1

    # Check left and right pointer bounds
    while left < right:
      # Scan past non-alphanumeric left and right pointer characters
      while left < right and not self.isAlnum(s[left]):
        left += 1
      while left < right and not self.isAlnum(s[right]):
        right -= 1

      # Return False if the lowercase characters aren't equal
      if s[left].lower() != s[right].lower():
        return False

      # Increment left pointer, decrement right pointer
      left += 1
      right -= 1

    # The string is a palindrome
    return True

  def isAlnum(self, char: str) -> bool:
    # Return whether the argument is an alphanumeric character
    return ((ord("A") <= ord(char) <= ord("Z")) or
      (ord("a") <= ord(char) <= ord("z")) or
      (ord("0") <= ord(char) <= ord("9")))