class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tup = Counter(nums).most_common(k)
        output = []
        for i in tup:
            output.append(i[0])
        return output