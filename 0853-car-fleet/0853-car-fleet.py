# The solution has a time complexity of O(nlog(n)), since I iterate through
# each car's (position : speed) pair in linear time, and I sort these pairs
# in reverse order, hence an overall runtime of O(nlog(n)). The space
# complexity is O(n), since I'm using a stack and a dictionary to store
# (position : speed) pairs.
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a dictionary that stores car (position : speed) pairs
        car_dict = {}

        # Populate the dictionary using the car position and speed arrays
        for i in range(len(position)):
            car_dict[position[i]] = speed[i]

        # Sort the dictionary in reverse order
        sorted_car_dict = dict(sorted(car_dict.items(), reverse=True))

        # Create a stack that stores the time it takes for the leading car
        # in each car fleet to reach the target
        stack = []

        for position, speed in sorted_car_dict.items():
            # (distance / speed) = time
            # Push the time it takes for each car to reach the target
            stack.append((target - position) / speed)

            # If a car behind the leading car will reach the target faster
            # than the leading car, pop it from the stack. This car behind
            # the leading car is now part of a car fleet.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        # The length of the stack is the number of car fleets
        return len(stack)