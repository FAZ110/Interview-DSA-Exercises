'''
You are given an array prerequisites where prerequisites[i] = [a, b] indicates
that you must take course b first if you want to take course a.

    For example, the pair [0, 1], indicates that to take course 0 you 
    have to first take course 1.

There are a total of numCourses courses you are required to take, labeled 
from 0 to numCourses - 1.

Return a valid ordering of courses you can take to finish all courses. If 
there are many valid answers, return any of them. If it's not possible to 
finish all courses, return an empty array.
'''

# EXAMPLES

# Input: numCourses = 3, prerequisites = [[1,0]]
# Output: [0,1,2]

# Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]
# Output: []

'''
Same as courseSchedule but we keep track of courses order (pop order) in a queue.
'''

from collections import deque

def findOrder(numCourses, prerequisites):
    adj = [[] for _ in range(numCourses)]

    indegree = [0] * numCourses

    for dest, src in prerequisites:
        adj[src].append(dest)
        indegree[dest] += 1
    
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])

    completed_count = 0

    path = []

    while queue:
        current = queue.popleft()
        completed_count += 1
        path.append(current)

        for neighbour in adj[current]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
    
    return path if completed_count == numCourses else []


numCourses = 3
prerequisites = [[1,0]]
print(findOrder(numCourses, prerequisites))


