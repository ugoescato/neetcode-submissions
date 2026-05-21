class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0

        while r <=len(t)-1:
            if l == len(s):
                return True
            elif s[l] == t[r]:
                l += 1
                r += 1
            else:
                r += 1
        return True if l == len(s) else False