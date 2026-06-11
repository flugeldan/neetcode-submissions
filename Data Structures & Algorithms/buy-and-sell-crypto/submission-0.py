class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_stock=prices[0]
        for price in prices:
            if price<min_stock:
                min_stock=price
            elif price-min_stock >max_profit:
                max_profit=price-min_stock
        return max_profit
