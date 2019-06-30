class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        num = len(prices)
        if num < 2:
            return 0

        buy_price = prices[0]
        max_profit = 0
        current_profit = 0
        for i in xrange(1, num):
            if prices[i] < prices[i - 1]:
                buy_price = prices[i]
                max_profit += current_profit
                current_profit = 0
                continue
            if prices[i] < buy_price:
                buy_price = prices[i]
            else:
                current_profit = max(prices[i] - buy_price, current_profit)
        max_profit += current_profit

        return max_profit


if __name__ == '__main__':
    # prices = [7, 1, 5, 3, 4, 6]
    # prices = [1, 2, 3, 4, 5]
    prices = [7, 6, 4, 3, 1]
    solution = Solution()
    print solution.maxProfit(prices)
