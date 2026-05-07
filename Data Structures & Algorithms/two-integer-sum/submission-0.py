class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        arr = []

        for i, val in enumerate(nums):
            res = target - val
            if res not in seen:
                seen[val] = i
            else:
                arr.append(seen[res])
                arr.append(i)

        return arr
