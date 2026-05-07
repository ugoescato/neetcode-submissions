class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return False if sorted([i for i in set(nums)]) == sorted(nums) else True