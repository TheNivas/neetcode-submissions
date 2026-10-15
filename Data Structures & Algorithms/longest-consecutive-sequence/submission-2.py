class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longestcount = 0

        for num in num_set:
            if num -1 not in num_set:
                curr_num = num
                curr_count = 1

                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_count += 1
                
                longestcount = max(curr_count, longestcount)

        return longestcount
        