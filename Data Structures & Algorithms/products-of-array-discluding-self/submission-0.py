class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        res = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            elif i == 1:
                prefix.append(nums[i-1])
            else:
                prefix.append(nums[i-1] * prefix[i-1])
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                suffix.append(1)
            elif i == len(nums)-2:
                suffix.append(nums[i+1])
            else:
                suffix.append(nums[i+1] * suffix[len(nums)-i-2])
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[len(nums)-1-i])

        return res 
        


