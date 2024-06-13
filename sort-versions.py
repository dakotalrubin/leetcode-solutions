# Time: O(nlog(n)) since we need to iterate through the input array once and
# then use Python's sort() method, which is a comparison-based sort.
# Space: O(n) since Python's sort() method uses temporary storage space.
"""This method takes an unsorted list of software version strings and sorts them."""
def sortVersions(versions):
  # Create an array to hold the integer representations of all software
  # version strings
  integerVersions = []

  # For each software version string (ex. "1.7.3")
  for version in versions:
    # Split the software version string by the dot character
    splitVersion = version.split(".")

    # Convert each element in the splitVersion array from string to integer
    for i in range(3):
      splitVersion[i] = int(splitVersion[i])

    # Append each splitVersion array to the integerVersions array
    integerVersions.append(splitVersion)

  # Sort the integerVersions array, store in-place
  integerVersions.sort()

  # Create an array to hold the string representations of all software version
  # arrays
  stringVersions = []

  # For each software version array (ex. [1, 7, 3])
  for version in integerVersions:
    # Join each value in the software version array into a string separated by dots
    stringVersion = ".".join(str(value) for value in version)

    # Append the software version string to the stringVersions array
    stringVersions.append(stringVersion)

  # Return the final sorted list of software version strings
  return stringVersions

"""This method runs the main program."""
def main():
  # Create a list of unsorted software version strings
  versions = ["1.7.3", "1.2.1", "1.11.0", "1.3.4", "0.9.9", "1.2.10"]

  # Call sortVersions() to sort the list of software version strings
  sortedVersions = sortVersions(versions)

  # Display the sorted list of software version strings
  print(sortedVersions)

# This statement allows the user to run the main method as a script
if __name__ == "__main__":
  main()