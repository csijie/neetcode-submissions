class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for i in s:
            s_dict[i] = s_dict.get(i, 0) + 1
        for i in t:
            if i not in s_dict:
                return False 
            if i in s_dict:
                s_dict[i] -= 1
        if all(value == 0 for value in s_dict.values()):
            return True 
        else:
            return False 
        
            
