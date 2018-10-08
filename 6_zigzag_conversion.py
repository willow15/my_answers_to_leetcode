class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        zigzag = [[]] * numRows
        index = 0
        direction = 0
        for character in s:
            if zigzag[index]:
                zigzag[index].append(character)
            else:
                zigzag[index] = [character]
            if numRows > 1:
                if index == 0:
                    direction = 1
                elif index == numRows - 1:
                    direction = -1
            index += direction
        print zigzag
        result = reduce(lambda x, y: x + y, zigzag)
        result = ''.join(result)
        return result


if __name__ == '__main__':
    solution = Solution()
    s = 'AB'
    numRows = 1
    print solution.convert(s, numRows)
