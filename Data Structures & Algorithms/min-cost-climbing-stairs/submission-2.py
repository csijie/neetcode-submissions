class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        n = len(cost)

        def minCost(cost, n):
            if n == 0:
                return cost[0]
            if n == 1:
                return cost[1]
            if n not in cache:
                cache[n] = cost[n] + min(minCost(cost, n-1), minCost(cost, n-2))
            return cache[n] 

        return min(minCost(cost, n-1), minCost(cost, n-2))

        

        