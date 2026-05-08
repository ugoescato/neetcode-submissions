class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen, output = {}, []

        for idx, val in enumerate(numbers):
            if target - val not in seen:
                seen[val] = idx
            else:
                output.append(seen[target-val])
                output.append(idx)
        return [i+1 for i in output]

