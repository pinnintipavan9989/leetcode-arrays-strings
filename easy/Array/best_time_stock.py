from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices =  float('inf')
        max_profit= 0

        for price in prices:
            if price < min_prices:
               min_prices= price
            else:
                max_profit = max(max_profit, price - min_prices)

        return max_profit 
           
if __name__ == "__main__":
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    result = sol.maxProfit(prices)
    print(result)
