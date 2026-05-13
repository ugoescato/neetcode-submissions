class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        output,l  = 0, 0
        length = 99999

        for r in range(len(nums)):
            output += nums[r]

            while output >= target:
                length = min(r-l+1, length)
                output -= nums[l]
                l += 1
        return 0 if length == 99999 else length
