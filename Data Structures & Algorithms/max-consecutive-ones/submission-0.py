class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_counter = 0

        for i in nums:
            if i == 1:
                counter += 1
            else:
                if counter > max_counter:
                    max_counter = counter
                    counter = 0
                else:
                    counter = 0
        
        return max_counter if max_counter > counter else counter