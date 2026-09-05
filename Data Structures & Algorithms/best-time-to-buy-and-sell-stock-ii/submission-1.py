class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        low_price = prices[0]
        high_price = 0

        mx_profit = 0

        for price in prices:
            low_price = min(low_price , price)
            high_profit = max(high_price , price - low_price)

            if high_profit:
                mx_profit += high_profit
                low_price = price
                profit = 0

        return mx_profit

            

            

            
            


            

        