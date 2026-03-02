'''
You are given a network of n directed nodes, labeled from 1 to n. 
You are also given times, a list of directed edges where times[i] = (ui, vi, ti).

    ui is the source node (an integer from 1 to n)
    vi is the target node (an integer from 1 to n)
    ti is the time it takes for a signal to travel from the source 
    to the target node (an integer greater than or equal to 0).

You are also given an integer k, representing the node that we will 
send a signal from.

Return the minimum time it takes for all of the n nodes to receive the 
signal. If it is impossible for all the nodes to receive the signal, 
return -1 instead.
'''

# EXAMPLES

# Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1
# Output: 3

# Input: times = [[1,2,1],[2,3,1]], n = 3, k = 2
# Output: -1

# IDEA

'''
We use Dijkstra's algorithm. Firstly we build adjacency list (with 0-indexing for convenience),
initialize distance array (D) with infinities and starting node with 0, the we use heap
to simulate the algorithm, if we found a shorter path to a node we update the cost and
push it to the heap.
'''

import heapq
def networkDelayTime(times, n, k):

    adj = [[] for _ in range(n)]

    for ui, vi, ti in times:
        adj[ui-1].append((vi-1, ti))
    
    D = [float('inf') for _ in range(n)]
    D[k-1] = 0

    heap = [(0, k-1)]

    while heap:
        time, node = heapq.heappop(heap)

        if D[node] < time:  # We have a shorter path
            continue

        for neighbour, weight in adj[node]: # for every neighbour
            if D[node] + weight < D[neighbour]:
                D[neighbour] = D[node] + weight
                heapq.heappush(heap, (D[neighbour], neighbour))
    
    ans = max(D)
    return ans if ans < float('inf') else -1


times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]]
n = 4
k = 1

print(networkDelayTime(times, n, k))




     