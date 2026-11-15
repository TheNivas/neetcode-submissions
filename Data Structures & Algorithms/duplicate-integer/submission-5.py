class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums)) != len(nums)
        aSet = set()
        for num in nums:
            if num in aSet:
                return True
            aSet.add(num)
        return False
        