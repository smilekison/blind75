from collections import defaultdict


class Solution:
    def groupAnagrams(strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)

        return res.values()





    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))