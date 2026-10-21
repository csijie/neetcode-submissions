class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        curr_price = prices[0]
        res = 0 
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            curr_price = prices[i]
            res = max(res, curr_price - minimum)
        return res 
            