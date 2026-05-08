class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for idx, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                stack_t, stack_idx = stack.pop()
                output[stack_idx] = (idx - stack_idx)
            stack.append([val, idx])
        
        return output


        

                
                
