class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        output, l = 0, 0
        stack = []

        for r in range(len(arr)+1):
            if r - l + 1 > k:
                if sum(stack) >= threshold * k:
                    output += 1
                stack.pop(0)
                l += 1
            if r != len(arr):
                stack.append(arr[r])
        return output
            