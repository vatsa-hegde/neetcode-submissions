class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0

        while right < len(prices):
            p = prices[right] - prices[left]
            if p > profit:
                profit = p
            if prices[left] > prices[right]:
                left = right
            right+=1
        return profit
        