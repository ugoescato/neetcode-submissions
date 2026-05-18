class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_w = strs[0]
        stack = []
        res = []

        for i in strs:
            if len(i) < len(shortest_w):
                shortest_w = i

        l = 0
        
        while l <= len(shortest_w)-1:
            for i in strs:
                stack.append(i[l])
            
            for j in range(len(stack)):
                if stack[j] == stack[j-1]:
                    continue
                else:
                    return ''.join(res)
            res.append(stack[j])    
            stack.clear()
            l += 1
        return ''.join(res)