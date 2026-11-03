class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l, r = 0, 1
        # maxx = 0

        # while (r < len(prices)):
        #     if (prices[l] < prices[r]):
        #         profit = prices[r] - prices[l]
        #         maxx = max(profit, maxx)
        #     else:
        #         l = r
        #     r += 1
        # return maxx

        # DP
        minBuy = prices[0]
        maxx = 0
        for sale in prices:
            maxx = max(maxx, sale - minBuy)
            minBuy = min(minBuy, sale)
        
        return maxx

        