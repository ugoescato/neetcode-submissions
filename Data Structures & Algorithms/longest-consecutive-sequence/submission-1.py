class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted([i for i in set(nums)])
        counter, max_counter = 1, 1

        if len(nums) == 0:
            return 0

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                counter += 1
            elif counter > max_counter:
                max_counter = counter
                counter = 1
            else:
                counter = 1
        
        return max(max_counter, counter)

