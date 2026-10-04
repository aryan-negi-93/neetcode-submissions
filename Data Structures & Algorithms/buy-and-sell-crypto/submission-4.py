class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        min_price = prices[0]
        mx_profit = 0

        for price in prices:
            min_price = min(price , min_price)
            profit = price - min_price
            mx_profit = max(mx_profit , profit )

        return mx_profit






        
        