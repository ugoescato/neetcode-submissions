class Solution:
    def isValid(self, s: str) -> bool:
        my_hash = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        stack = []

        if len(s) == 1:
            return False

        for i in s:
            if i not in my_hash:
                stack.append(i)
            elif len(stack) == 0:
                return False
            elif my_hash[i] == stack[-1]:
                stack.pop()
            else:
                return False
        return True if not stack else False