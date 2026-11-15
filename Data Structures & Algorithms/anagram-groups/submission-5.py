class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for str1 in strs:
            sortedStr = "".join(sorted(str1))
            if sortedStr in seen:
                seen[sortedStr].append(str1)
            else:
                seen[sortedStr] = [str1]
        
        return list(seen.values())
        