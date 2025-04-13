class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        last_price = prices[0]
        for i in range(len(prices)):
            if prices[i] - last_price > 0:
                max_profit += prices[i] - last_price
            last_price = prices[i]
        return max_profit


test_array = [7, 1, 5, 3, 6, 4]
print(max(test_array))
print(test_array)
solution = Solution()
print(solution.maxProfit(test_array))