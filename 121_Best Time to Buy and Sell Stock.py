# 121 Best Time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
        """
        Fully recursive solution without loops to find max profit.
        """

        def helper(index, min_price, max_profit):
            # Base case: if we've gone past the last day
            if index == len(prices):
                return max_profit

            # Update minimum price seen so far
            min_price = min(min_price, prices[index])
            # Calculate profit if we sell today
            profit = prices[index] - min_price
            # Update max profit
            max_profit = max(max_profit, profit)

            # Recurse to the next day
            return helper(index + 1, min_price, max_profit)

        if not prices:
            return 0

        # Start recursion from index 0
        return helper(0, prices[0], 0)




# ---------------- Example Usage ----------------
sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))  # Output: 5 (buy at 1, sell at 6)
