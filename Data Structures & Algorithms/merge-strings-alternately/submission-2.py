class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        r = 0
        
        if len(word1) >= len(word2):
            longest_w = word1
            shortest_w = word2
        else:
            longest_w = word2
            shortest_w = word1

        for l in range(len(shortest_w)):
            res += word1[l]
            res += word2[r]
            r += 1
        
        res += longest_w[r:]
        
        return res