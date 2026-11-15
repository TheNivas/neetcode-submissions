class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for _ in range(len(nums)+1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for kk, v in count.items():
            freq[v].append(kk)

        res = []
        for i in range(len(freq)-1, -1, -1):
            for item in freq[i]:
                res.append(item)

                if len(res) == k:
                    return res

        