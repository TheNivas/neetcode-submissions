class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        x = 1

        for i in range(len(nums)):
            res[i] = x
            x *= nums[i]

        x = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= x
            x *= nums[i]

        return res
        