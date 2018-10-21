class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # function: path_count[m][n] = path_count[m - 1][n] + path_count[m][n - 1]
        # because we can only move in right or down direction
        if n == 1 or m == 1:
            return 1
        path_count = [[1] * m] * n
        for i in xrange(1, n):
            for j in xrange(1, m):
                path_count[i][j] = path_count[i - 1][j] + path_count[i][j - 1]
        return path_count[n - 1][m - 1]


if __name__ == '__main__':
    solution = Solution()
    m = 3
    n = 3
    print solution.uniquePaths(m, n)
