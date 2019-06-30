class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        num = len(prices)
        if num < 2:
            return 0

        max_profit = 0
        buy_price = prices[0]
        for i in xrange(1, num):
            if prices[i] < buy_price:
                buy_price = prices[i]
            else:
                profit = prices[i] - buy_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    # prices = [7, 6, 4, 3, 1]
    solution = Solution()
    print solution.maxProfit(prices)
