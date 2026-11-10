from collections import deque 

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        queue = deque()

        for i, char in enumerate(s):
            if char not in count:
                count[char] = 1
                queue.append((i, char))
            else:
                count[char] += 1

        while queue:
            i, char = queue[0]
            if count[char] == 1:
                return i 
            else:
                queue.popleft()

        return -1 

        