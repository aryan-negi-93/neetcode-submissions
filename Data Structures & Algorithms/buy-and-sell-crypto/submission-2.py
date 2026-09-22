class Solution:
    def maxProfit(self, prices: List[int]) -> int:

    
        min_price = prices[0]
        mx_profit  = 0
        for price in prices:
            min_price = min(min_price , price)
            mx_profit = max(mx_profit , price - min_price)

        return mx_profit

                                                                        