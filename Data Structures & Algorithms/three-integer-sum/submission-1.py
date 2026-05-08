class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        output = []
        

        for i in range(len(nums)):
            triplet = []
            j = i+1
            k = len(nums)-1

            while j < k: 
                if -nums[i] == nums[j] + nums[k]:
                    triplet = [nums[i], nums[j], nums[k]]
                    if triplet not in output:
                        output.append(triplet)
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1

        return output