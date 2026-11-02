class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a_set = set()
        for num in nums:
            if num in a_set:
                return True
            a_set.add(num)
        return False

        # return len(set(nums)) != len(nums)
        