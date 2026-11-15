class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxx = 0
        numSet = set(nums)

        for num in numSet:
            if num-1 not in numSet:
                curr = num
                currL = 1

                while curr + 1 in numSet:
                    curr += 1
                    currL += 1
                maxx = max(maxx, currL)
        
        return maxx