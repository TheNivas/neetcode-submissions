class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
           if i == 0 or num != nums[i-1]:
                l, r = i+1, len(nums)-1
                while l < r:
                    sum = nums[l] + nums[r]
                    if sum == -num:
                        res.append([num, nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]: l += 1
                        while l < r and nums[r] == nums[r+1]: r -= 1
                    elif sum > -num:
                        r -= 1
                    else:
                        l += 1
        return res

                
        