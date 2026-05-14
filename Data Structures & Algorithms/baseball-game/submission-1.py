class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ops = ['+', 'C', 'D']
        res = 0

        for i in operations:
            if i not in ops:
                stack.append(int(i))
            elif i == '+':
                res = stack[-1] + stack[-2]
                stack.append(res)
                res = 0
            elif i =='C':
                stack.pop()
            elif i == 'D':
                res = stack[-1] * 2
                stack.append(res)
                res = 0
        return sum(stack)