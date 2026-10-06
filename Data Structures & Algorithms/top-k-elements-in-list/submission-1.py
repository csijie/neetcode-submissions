class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # Create n buckets 
        freq = [[] for _ in range(len(nums) + 1)]

        # Index of subarray represents frequency 
        for num, count in counts.items():
            freq[count].append(num)

        res = []

        # Starting from the highest frequency  
        for i in range(len(freq) - 1, 0, -1):

            # Iterates through the subarray until k 
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res 
                

        
            



