class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:   
        my_set = set()
        l, max_length = 0, 0

        if not s:
            return 0

        for r in range(len(s)):
            while s[r] in my_set:
                my_set.discard(s[l])
                l += 1
            my_set.add(s[r])
            max_length = max(max_length, r - l + 1)

        return max_length