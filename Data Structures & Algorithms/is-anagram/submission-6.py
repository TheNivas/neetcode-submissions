class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for char in s:
            seen[char] = seen.get(char, 0) + 1
        
        for char in t:
            s = seen.get(char, 0)
            if s == 0: return False
            else:
                seen[char] -= 1
        
        return True
        