class Solution:
    def findMin(self, nums: List[int]) -> int:
        # On
        # mins = nums[0]

        # for num in nums:
        #     mins = min(num, mins)
        # return mins
        # O logn
        l, r = 0 , len(nums) -1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]




        