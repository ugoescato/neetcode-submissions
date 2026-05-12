class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
        count = {}

        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
            
            if count[i] > majority:
                return i