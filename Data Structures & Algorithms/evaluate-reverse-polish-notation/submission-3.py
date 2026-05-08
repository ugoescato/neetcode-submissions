class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import math
        operations = ['+', '-', '*', '/']
        stack = []
        res = 0

        for i in tokens:
            if i not in operations:
                stack.append(int(i))
            else:
                first_num = stack.pop(-2)
                second_num = stack.pop(-1)
                if i == '+':
                    res = first_num + second_num
                elif i == '-':
                    res = first_num - second_num
                elif i == '*':
                    res = first_num * second_num
                else:
                    res = math.trunc(first_num / second_num)
            
                stack.append(int(res))
        
        return stack[-1]
        

        
            
