class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        check_common = set()

        length = float("inf")
        for string in strs:
            if len(string) < length:
                length = len(string)

        for i in range(length): 
            for string in strs:
                check_common.add(string[i])
            if len(check_common) == 1:
                res += string[i]
            else: 
                break
            check_common = set()

        return res 