class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Initiate res containing element 1 repeated n times  
        res = [1] * n

        for i in range(1, n):
            res[i] = nums[i-1] * res[i-1]
        
        # Update suffix_prod
        suffix_prod = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix_prod
            suffix_prod *= nums[i]

        return res 
         