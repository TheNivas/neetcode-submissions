class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res  = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix  * nums[i]
            print(f"first loop: {prefix = } and {res = }")
            
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res [i] = postfix * res[i]
            postfix = postfix * nums[i]
            print(f"second loop: {postfix = } and {res = }")
            
        return res
            
        
      