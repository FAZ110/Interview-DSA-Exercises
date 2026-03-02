'''
You are given an array prerequisites where prerequisites[i] = [a, b] 
indicates that you must take course b first if you want to take course a.

The pair [0, 1], indicates that must take course 1 before taking course 0.

There are a total of numCourses courses you are required to take, labeled 
from 0 to numCourses - 1.

Return true if it is possible to finish all courses, otherwise return false.
'''

# EXAMPLES

# Input: numCourses = 2, prerequisites = [[0,1]]
# Output: true

# Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
# Output: false

# IDEA
'''
build adjacency list to represent a graph and track courses with no prerequisites,
initialize queue with these courses. Simulate the course take with available informations.
'''

from collections import deque

def canFinish(numCourses, prerequisites):
    adj = [[] for _ in range(numCourses)]

    indegree = [0] * numCourses

    for dest, src in prerequisites:
        adj[src].append(dest)
        indegree[dest] += 1
    
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])

    completed_count = 0

    while queue:
        current = queue.popleft()
        completed_count += 1

        for neighbour in adj[current]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
    
    return completed_count == numCourses
