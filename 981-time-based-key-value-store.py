# Time: O(1) for the __init__() method since we need to create a hashmap, O(1)
# for the set() method since we only ever append a [value, timestamp] pair to
# the hashmap, and O(log(n)) for the get() method since we need to use binary
# search to find a specific [value, timestamp] pair in the hashmap
# Space: O(n) since we might need to store every element from the input in the
# hashmap as a unique entry
#
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
class TimeMap:
  def __init__(self):
    # Create a hashmap where keys are strings and values are lists of
    # [value, timestamp] pairs
    self.store = defaultdict(list)

  def set(self, key: str, value: str, timestamp: int) -> None:
    # Append a [value, timestamp] pair to the list stored at the given key
    self.store[key].append([value, timestamp])

  def get(self, key: str, timestamp: int) -> str:
    # Create a variable that will hold the value retrieved from the hashmap
    value = ""

    # Store the list of [value, timestamp] pairs at the given key
    values = self.store[key]

    # Create left and right pointers that maximize the search area
    left, right = 0, len(values) - 1

    # Perform binary search
    while left <= right:
      # Find the middle index
      middle = (left + right) // 2

      # If the current timestamp is less than or equal to the given timestamp
      if values[middle][1] <= timestamp:
        # Update the value using the current [value, timestamp] pair
        value = values[middle][0]

        # Search the right portion of the search area
        left = middle + 1
      else:
        # Search the left portion of the search area
        right = middle - 1

    # Return the value at the given timestamp (or the most recent value)
    return value