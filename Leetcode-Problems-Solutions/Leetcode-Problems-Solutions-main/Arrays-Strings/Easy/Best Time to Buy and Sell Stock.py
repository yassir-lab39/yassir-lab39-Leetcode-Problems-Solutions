class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        mini = prices[0]
        n = len(prices)
        for i in range(n):
            mini = min(mini, prices[i])
            maxi = max(maxi, prices[i]-mini)
        return maxi    
        
