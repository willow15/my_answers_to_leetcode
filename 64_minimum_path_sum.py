class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        path_sum = [[0] * n] * m
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j == 0:
                    path_sum[i][j] = grid[i][j]
                elif i == 0 and j >= 1:
                    path_sum[i][j] = path_sum[i][j - 1] + grid[i][j]
                elif i >= 1 and j == 0:
                    path_sum[i][j] = path_sum[i-1][j] + grid[i][j]
                else:
                    path_sum[i][j] = min(path_sum[i - 1][j], path_sum[i][j - 1]) + grid[i][j]
                print i, j, path_sum[i][j]
        return path_sum[m - 1][n - 1]

if __name__ == '__main__':
    solution = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print solution.minPathSum(grid)
