class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        my_set = set()

        if prices == sorted(prices, reverse=True):
            return 0
        
        for i in prices:
            if not my_set:
                my_set.add(i)
            elif i - min(my_set) > output:
                output = i - min(my_set)
            my_set.add(i)
        return output

        
                

