class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_hash = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key not in my_hash:
                my_hash[key] = []
            my_hash[key].append(word)

        return list(my_hash.values())