# Link to the problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
        for p in prices:
            hold, notHold, notHold_cooldown = max(hold, notHold - p), max(notHold, notHold_cooldown), hold + p
        return max(notHold, notHold_cooldown)
