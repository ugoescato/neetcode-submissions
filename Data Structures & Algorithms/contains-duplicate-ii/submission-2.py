class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_hash = {}

        for idx, val in enumerate(nums):
            if val not in my_hash:
                my_hash[val] = idx
            elif abs(my_hash[val] - idx) <= k:
                return True
            else:
                my_hash[val] = idx
        return False 