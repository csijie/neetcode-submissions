class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            curr = nums[i]
            compl = -curr
            l = i + 1
            r = len(nums) - 1 
            while l < r:
                if nums[l] + nums[r] == compl:
                    if [curr, nums[l], nums[r]] not in res:
                        res.append([curr, nums[l], nums[r]])
                    l += 1
                    r -= 1
                if nums[l] + nums[r] < compl:
                    l += 1
                if nums[l] + nums[r] > compl:
                    r -= 1

        return res 
        


            

   
            


        
        