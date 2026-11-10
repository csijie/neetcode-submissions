from collections import deque 

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(tickets)
        pos = k 
        time = 0 
        while queue:
            if pos == 0 and queue[0] == 1:   
                time += 1 
                return time 
            elif pos == 0:
                queue[0] -= 1
                queue.append(queue.popleft())
                time += 1 
                pos = len(queue) - 1 
            elif queue[0] == 1:
                queue.popleft() 
                time += 1
                pos -= 1
            else:
                queue[0] -= 1
                queue.append(queue.popleft())
                time += 1 
                pos -= 1 
