class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}

        for i in s:
            if i not in hash_s:
                hash_s[i] = 1
            else:
                hash_s[i] += 1
        
        for j in t:
            if j not in hash_t:
                hash_t[j] = 1
            else:
                hash_t[j] += 1

        for key, val in hash_s.items():
            if key not in hash_t or len(hash_s) != len(hash_t):
                return False
            if val != hash_t[key]:
                return False
            else:
                continue
        return True