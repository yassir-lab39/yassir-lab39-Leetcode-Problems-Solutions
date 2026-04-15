class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        nb = 0
        for j in range(0,len(prices)-1):
            if prices[j] < prices[j+1]:
                nb += 1
                if j+1 == len(prices)-1:
                    profit = profit - prices[j+1-nb] + prices[j+1]
            else :
                profit = profit - prices[j-nb] + prices[j]
                nb = 0
        return profit
