class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_hash = {}
        res = []

        for i in nums:
            if i not in my_hash:
                my_hash[i] = 1
            else:
                my_hash[i] += 1
        
        freq = [(key, val) for key,val in my_hash.items()]
        freq.sort(key=lambda x: x[1], reverse=True)

        i = 0
        while i < k:
            res.append(freq[i][0])
            i += 1

        return res
