class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 
        max_profit = 0 

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r # Close sliding window 
            r += 1 # Always move right pointer forward to look for higher profit with price[l] as buying price 

        return max_profit
        