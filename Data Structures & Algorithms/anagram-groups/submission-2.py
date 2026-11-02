class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dicts = {}
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str in dicts:
                dicts[sorted_str].append(string)
            else:
                dicts[sorted_str] = [string]
        return list(dicts.values())