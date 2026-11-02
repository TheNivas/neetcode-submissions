class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # map = dict()
        # for  char in s:
        #     map[char] = map.get(char, 0) + 1
        
        # for char in t:
        #     if char not in map or map[char] == 0:
        #         return False
        #     map[char] -= 1
        
        # return True
        s_map = {}
        t_map = {}
        for s_char, t_char in zip(s,t):
            s_map[s_char] = s_map.get(s_char, 0) +1
            t_map[t_char] = t_map.get(t_char, 0) +1
        
        # return s_map == t_map

        from collections import Counter
        return Counter(s) == Counter(t)
        