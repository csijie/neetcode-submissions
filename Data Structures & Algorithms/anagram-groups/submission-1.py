class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key not in anagrams:
                anagrams[key] = [strs[i]]
            else:
                anagrams[key].append(strs[i])

        return list(anagrams.values())