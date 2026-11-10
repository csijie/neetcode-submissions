class MinStack:

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        if not self.data:
            current_min = val 
        else:
            current_min = min(val, self.data[-1][1])
        self.data.append((val, current_min))

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]
        
