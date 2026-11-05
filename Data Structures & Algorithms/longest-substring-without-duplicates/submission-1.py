class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx = 0
        l = bestL = 0
        aSet = set()

        for r, char in enumerate(s):
            while(char in aSet):
                aSet.remove(s[l])
                l += 1

            aSet.add(char)
            cLen = r -l + 1
            if cLen > maxx:
                maxx = cLen
                bestL = l
        return maxx