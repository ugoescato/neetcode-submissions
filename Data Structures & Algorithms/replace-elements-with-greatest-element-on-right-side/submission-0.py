class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []

        for i in range(len(arr)):
            if i != len(arr)-1:
                maxi = max(arr[i+1:])
                res.append(maxi)
            else:
                res.append(-1)
        
        return res
            