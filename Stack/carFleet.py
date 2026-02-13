'''
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

    position[i] is the position of the ith car (in miles)
    speed[i] is the speed of the ith car (in miles per hour)

The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

Return the number of different car fleets that will arrive at the destination.
'''


# EXAMPLES

# Input: target = 10, position = [1,4], speed = [3,2]
# Output: 1

# Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
# Output: 3


# MAIN IDEA

'''
We calculate the time in which each car will reach the target 
then we iterate backwards from the car that is the closest to target.
If the time of the previous(to the left) car is smaller than current then it makes 
a fleet with the current "main fleet" car, if it is bigger then it makes 
new fleet and becomes a "main fleet" car. Each time in the stack at the end
represents the time of a "main fleet" car.
'''

# main fleet car is the car that starts the fleet

def carFleet(target, position, speed):
    n = len(position)

    comb = [(position[i], speed[i]) for i in range(n)]
    comb.sort() # Have to sort to iterate from the closest car, sort by idx 0

    time = [0 for _ in range(n)]
    
    for i in range(n):
        time[i] = (target - comb[i][0])/comb[i][1]  # time that the car reaches the target (float)
    
    stack = [time[-1]]  # the closest car to the target is the first "main fleet" car
    for i in range(n-2, -1, -1):
        if time[i] > stack[-1]: # new "main fleet" car
            stack.append(time[i])
        
    
    return len(stack)



target = 10
position = [4,1,0,7]
speed = [2,2,1,1]


target = 10
position = [1,4]
speed = [3,2]


target=12
position=[10,8,0,5,3]
speed=[2,4,1,1,3]

target=10
position=[8,3,7,4,6,5]
speed=[4,4,4,4,4,4]

print(carFleet(target, position, speed))