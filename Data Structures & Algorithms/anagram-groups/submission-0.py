class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            count = [0] * 26
            for i in string:
                count[ord(i) - ord("a")] += 1 
            key = tuple(count)
            if key not in groups:
                groups[key] = []
            groups[key].append(string)
        return list(groups.values())