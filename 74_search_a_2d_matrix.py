class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # find the row in which the target may locate
        if not matrix or not matrix[0]:
            return False
        starts = [row[0] for row in matrix]
        row_index = self.find_range(starts, target, 0, len(starts) - 1)
        if row_index == -1:
            return False
        if matrix[row_index][0] == target:
            return True
        # find the location of target in the row
        column_index = self.find_target(matrix[row_index], target, 0, len(matrix[row_index]) - 1)
        if column_index == -1:
            return False
        else:
            return True


    def find_range(self, row, target, low, high):
        if target < row[low]:
            return -1
        if target >= row[high]:
            return high
        mid = (low + high) / 2
        if target == row[mid]:
            return mid
        if low == high and target > row[low]:
            return low
        if low == high - 1 and target > row[low] and target < row[high]:
            return low
        if target < row[mid]:
            high = mid
        else:
            low = mid
        if low <= high:
            return self.find_range(row, target, low, high)
        else:
            return -1


    def find_target(self, row, target, low, high):
        mid = (low + high) / 2
        if target == row[mid]:
            return mid
        if target < row[mid]:
            high = mid - 1
        else:
            low = mid + 1
        if low <= high:
            return self.find_target(row, target, low, high)
        else:
            return -1


if __name__ == '__main__':
    # matrix = [[1,  3,  5,  7],
    #           [10, 11, 16, 20],
    #           [23, 30, 34, 50]]
    # target = 51
    matrix = [[]]
    target = 1
    solution = Solution()
    print solution.searchMatrix(matrix, target)
