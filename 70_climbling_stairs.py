class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        stair = [0] * (n + 1)
        stair[1] = 1
        stair[2] = 2
        for i in xrange(3, n + 1):
            stair[i] = stair[i - 1] + stair[i - 2]
        return stair[n]


if __name__ == '__main__':
    n = 2
    solution = Solution()
    print solution.climbStairs(n)
