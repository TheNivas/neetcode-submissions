class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        bucket = [[] for _ in range(len(nums)+1)]

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for kk, v in freq.items():
            bucket[v].append(kk)

        res = []
        for i in range(len(bucket)-1, 0, -1):
            for item in bucket[i]:
                res.append(item)

            if len(res) == k:
                return res


            
