class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0 #Buy
        j = 1 #Sell
        profit = 0
        while j < len(prices):
            cprofit = prices[j] - prices[i] #our current Profit
            if prices[i] < prices[j]:
                profit =max(cprofit,profit)
            else:
                i = j
            j += 1
        return profit