class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums)//2
        my_hash = {}

        for i in nums:
            if i not in my_hash:
                my_hash[i] = 1
            else:
                my_hash[i] += 1
        
        for key, val in my_hash.items():
            if val > majority:
                return key
