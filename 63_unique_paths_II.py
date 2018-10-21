class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        path_count = [] # m * n matrix
        for i in xrange(n):
            row = []
            for j in xrange(m):
                row.append(0)
            path_count.append(row)
        if obstacleGrid[0][0] == 1 or obstacleGrid[n - 1][m - 1] == 1:
            return 0
        path_count[0][0] = 1
        for j in xrange(1, m):
            path_count[0][j] = 0 if obstacleGrid[0][j] == 1 else path_count[0][j - 1]
        for i in xrange(1, n):
            path_count[i][0] = 0 if obstacleGrid[i][0] == 1 else path_count[i - 1][0]
        for i in xrange(1, n):
            for j in xrange(1, m):
                count1 = 0 if obstacleGrid[i - 1][j] == 1 else path_count[i - 1][j]
                count2 = 0 if obstacleGrid[i][j - 1] == 1 else path_count[i][j - 1]
                path_count[i][j] = count1 + count2
        return path_count[n - 1][m - 1]


if __name__ == '__main__':
    solution = Solution()
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print solution.uniquePathsWithObstacles(obstacleGrid)
