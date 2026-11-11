class Solution:
    def findMin(self, nums: List[int]) -> int:
        mins = nums[0]

        for num in nums:
            mins = min(num, mins)
        return mins



        