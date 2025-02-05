class Solution:
    def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        initial = sorted(s)
        final = sorted(t)

        print(initial, final)

        if initial == final:
            return True
        return False
    
    print(isAnagram("anagram", "nagaram"))