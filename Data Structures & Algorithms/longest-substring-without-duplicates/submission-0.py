class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenMap = {}
        l = bestL = maxL = 0

        for r, char in enumerate(s):
            if char in seenMap:
                l = max(l, seenMap[char] + 1)
            
            seenMap[char] = r
            currL = r - l + 1
            if currL > maxL:
                maxL = currL
                bestL = l
        print(s[bestL : bestL+maxL])
        return maxL