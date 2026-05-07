class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        output = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    total *= nums[j]
            output.append(total)
            total = 1
        return output
            