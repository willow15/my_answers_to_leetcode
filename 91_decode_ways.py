class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        for i in xrange(2, n + 1):
            if s[i - 1:i] != '0':
                dp[i] += dp[i - 1]
            if s[i - 2:i] >= '10' and s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]

        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    # s = "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
    s = '01'
    print solution.numDecodings(s)
