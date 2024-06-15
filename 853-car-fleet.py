# Time: O(nlog(n)) since we need to iterate through the position and speed
# arrays in linear time to build an array of (position, speed) pairs, then use
# Python's sorted() method to sort this new array in O(nlog(n)) time
# Space: O(n) since we need to create an array of (position, speed) pairs
class Solution:
  def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    # Create an array that holds a (position, speed) pair for each car
    pairs = [(position[i], speed[i]) for i in range(len(position))]

    # Create variables to track the number of car fleets and the current time
    fleets = currentTime = 0

    # Sort the (position, speed) pairs in reverse order and iterate through them
    for position, speed in sorted(pairs, reverse=True):
      # (speed = distance / time) => (time = distance / speed)
      destinationTime = (target - position) / speed

      # If the destination time occurs in the future
      if currentTime < destinationTime:
        # Increment the number of arriving fleets
        fleets += 1

        # Update the current time as the destination time of the arriving fleet
        currentTime = destinationTime

    return fleets