class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        l = 0 
        max_len = 0 

        # Increment r 
        for r in range(len(s)):
            if s[r] in chars:
                l = max(chars[s[r]] + 1, l)
            chars[s[r]] = r
            max_len = max(max_len, r - l + 1)
        
        return max_len

         