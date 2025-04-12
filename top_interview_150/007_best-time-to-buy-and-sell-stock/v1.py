# My first solution was super lazy and recursive, so i got out of time error.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        current_lowest = prices[0]
        for i in range(len(prices)):
            if prices[i] > current_lowest:
                if prices[i] - current_lowest > max_profit:
                    max_profit = prices[i] - current_lowest
            elif prices[i] < current_lowest:
                current_lowest = prices[i]
        return max_profit


test_array = [7, 1, 5, 3, 6, 4]
print(max(test_array))
print(test_array)
solution = Solution()
print(solution.maxProfit(test_array))
