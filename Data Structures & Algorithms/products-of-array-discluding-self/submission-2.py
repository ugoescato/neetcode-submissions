class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = []
        suffix_prod = []
        output = []
        
        total = 1
        for i in nums:
            total *= i
            prefix_prod.append(total)
        
        total = 1
        for j in nums[::-1]:
            total *= j
            suffix_prod.append(total)
        suffix_prod = suffix_prod[::-1]

        for k in range(len(nums)):
            left = prefix_prod[k-1] if k != 0 else 1
            right = suffix_prod[k+1] if k != len(nums)-1 else 1  
            res = left * right
            output.append(res)
            res = 0

        return output