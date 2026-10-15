class Solution:
    def climbStairs(self, n: int, cache : dict = {}) -> int:
        
        if n == 1:
            return 1
        if n == 2:
            return 2 

        if n not in cache:
            cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return cache[n]


        
        