from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        stock = defaultdict(int)
        for num in nums:
            stock[num] += 1
        
        print(stock)
        lst = sorted(list(stock.values()), reverse=True)
        print(lst)
        res = []
        for key, value in stock.items():
            if value in lst[:k]:
                res.append(key)
        return res 