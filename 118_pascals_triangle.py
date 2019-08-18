class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            result = [[1], [1, 1]]
            for num_row in xrange(2, numRows):
                row = [1]
                last_row = num_row - 1
                for i in xrange(len(result[last_row]) - 1):
                    row.append(result[last_row][i] + result[last_row][i + 1])
                row.append(1)
                result.append(row)
            return result


if __name__ == '__main__':
    numRows = 5
    solution = Solution()
    print solution.generate(numRows)
