class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for char in tokens:
            if char not in ["+", "-", "*", "/"]:
                stack.append(int(char))
            else:
                second = stack.pop()
                first = stack.pop()
                if char == "+":
                    res = first + second
                elif char == "-":
                    res = first - second
                elif char == "*":
                    res = first * second
                else:
                    res = int(first / second)
                stack.append(res)
                
        return stack[0] 