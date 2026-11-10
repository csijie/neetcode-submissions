import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        # Create an empty hash map 'adj'
        adj = {}

        # For each vertex, assign [] as value of index 
        for i in range(n):
            adj[i] = []

        # Append [d, w] to vertex s in 'adj'
        for s, d, w in edges:
            adj[s].append([d, w])

        # Create an empty hash map 'shortest'
        shortest = {}

        # Create a minHeap starting at [0, src]
        minHeap = [[0, src]]

        while minHeap:
            # Pop the smallest value 
            w1, n1 = heapq.heappop(minHeap)

            # If this distance has been found, continue 
            if n1 in shortest:
                continue 

            # Assign w1 as value of n1 
            shortest[n1] = w1

            # Coninue checking the 'adj' of n1
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])

        # Create the default variables 
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest 