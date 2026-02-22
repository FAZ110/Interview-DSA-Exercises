'''
There are n gas stations along a circular route. You are given two 
integer arrays gas and cost where:

    gas[i] is the amount of gas at the ith station.
    cost[i] is the amount of gas needed to travel from the ith 
    station to the (i + 1)th station. (The last station is connected 
    to the first station)

You have a car that can store an unlimited amount of gas, but you 
begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index such that you can travel 
around the circuit once in the clockwise direction. If it's 
impossible, then return -1.

It's guaranteed that at most one solution exists.
'''


# EXAMPLES

# Input: gas = [1,2,3,4], cost = [2,2,4,1]
# Output: 3

# Input: gas = [1,2,3], cost = [2,3,2]
# Output: -1


def canCompleteCircuit(gas, cost):
    n = len(gas)

    for i in range(n):

        gas_left = 0

        for j in range(i, n+i+1):
            temp = j    # temp for end condition
            j = j%n     # for circular idx
            gas_left += gas[j]

            if gas_left < cost[j]:  # if we do not have enough gas break
                break
            else:
                gas_left -= cost[j]
            

            if temp == n+i and gas_left >= 0:   # end condition
                return i
    
    return -1


gas = [1,2,3,4]
cost = [2,2,4,1]


gas = [1,2,3]
cost = [2,3,2]
print(canCompleteCircuit(gas, cost))