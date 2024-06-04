# Time: O(n) because you need to iterate through every character in
# the input array of strings once for encoding and once for decoding
# Space: O(n) because the encoded string has the same number of
# characters as the original input array of strings plus the length
# of each string followed by a delimiter character
class Solution:
  def encode(self, strs: List[str]) -> str:
    # Create an encoded string that will contain the entire input array
    encodedString = ""

    for str in strs:
      # Add the length of each string, a delimiter and the string itself
      encodedString += f"{len(str)}#{str}"

    return encodedString

  def decode(self, s: str) -> List[str]:
    # Create an array that will contain decoded strings
    decodedStrings = []

    # Create a variable to track the index when scanning the encoded string
    index = 0

    # Scan through the encoded string and separate the individual strings
    while index < len(s):
      # Scan ahead starting from the current index
      scanner = index

      # Scan through the number of characters that defines the 
      # length of the upcoming string
      while s[scanner] != "#":
        scanner += 1

      # Convert the length of the upcoming string to an integer
      stringLength = int(s[index:scanner])

      # Set the scanner to the starting position of the upcoming string
      scanner += 1

      # Append the upcoming string to the array of decoded strings
      string = s[scanner:(scanner + stringLength)]
      decodedStrings.append(string)

      # Set the index to the position after the string
      index = scanner + stringLength

    return decodedStrings