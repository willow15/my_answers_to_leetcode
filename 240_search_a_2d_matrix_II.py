class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        while True:
            if target < matrix[0][0] or target > matrix[-1][-1]:
                return False

            # narrow search space first
            min_row_index = 0
            min_column_index = 0
            max_row_index = len(matrix) - 1
            max_column_index = len(matrix[0]) - 1
            if target <= matrix[-1][0]:
                find_it, max_row_index = self.find_position([row[0] for row in matrix], target)
                if find_it:
                    return True
            else:
                find_it, min_column_index = self.find_position(matrix[-1], target)
                if find_it:
                    return True
                min_column_index += 1
            if target <= matrix[0][-1]:
                find_it, max_column_index = self.find_position(matrix[0], target)
                if find_it:
                    return True
            else:
                find_it, min_row_index = self.find_position([row[-1] for row in matrix], target)
                if find_it:
                    return True
                min_row_index += 1

            if max_column_index < min_column_index:
                return False
            if max_row_index < min_row_index:
                return False

            new_matrix = []
            for row_index in xrange(min_row_index, max_row_index + 1):
                new_matrix.append(matrix[row_index][min_column_index:max_column_index + 1])
            matrix = new_matrix


    def find_position(self, numbers, target):
        low = 0
        high = len(numbers) - 1

        if target > numbers[high]:
            return False, high

        while True:
            middle = (low + high) / 2
            if target == numbers[middle]:
                return True, middle
            elif target > numbers[middle] and target < numbers[middle + 1]:
                return False, middle
            elif target < numbers[middle]:
                high = middle - 1
            else:
                low = middle + 1



if __name__ == '__main__':
    # matrix = [
    #   [1,   4,  7, 11, 15],
    #   [2,   5,  8, 12, 19],
    #   [3,   6,  9, 16, 22],
    #   [10, 13, 14, 17, 24],
    #   [18, 21, 23, 26, 30]
    # ]
    matrix = [[]]
    target = 12
    solution = Solution()
    print solution.searchMatrix(matrix, target)
