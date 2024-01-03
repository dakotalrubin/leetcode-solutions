# The solution has a time complexity of O(n), where n is the total
# number of chars in the input array. The space complexity is O(n),
# because the encoded string has the same number of chars as the
# input array, plus the length of each word with a delimiter.
class Solution:
    # Add each word in the input array to an encoded string
    def encode(self, strs: List[str]) -> str:
        # Create an encoded string
        s = ""

        # Encode the length of each word, a delimiter, and the word
        for str in strs:
            s += f"{len(str)}#{str}"

        return s

    # Separate an encoded string into an array of words
    def decode(self, s: str) -> List[str]:
        # Create an array of words and a variable to track
        # the index when scanning an encoded string
        words = []
        index = 0

        # Scan through an encoded string and separate words
        while index < len(s):
            # Scan ahead from the current index
            scanner = index

            # Scan the length of the upcoming word
            while s[scanner] != "#":
                scanner += 1

            # Convert length of upcoming word into an integer
            word_length = int(s[index:scanner])

            # Scan past the delimiter character
            scanner += 1

            # Append the upcoming word to the array of words
            words.append(s[scanner:(scanner + word_length)])
            index = scanner + word_length # Update the index

        return words
