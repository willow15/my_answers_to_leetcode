# Solution 1
# class Solution(object):
#     def getBianryNumbers(self, n):
#         if n == 0:
#             return ['0']
#         if n == 1:
#             return ['0', '1']
#
#         binary_numbers = []
#         sub_binary_numbers = self.getBianryNumbers(n - 1)
#         sub_binary_numbers_count = len(sub_binary_numbers)
#
#         for i in xrange(sub_binary_numbers_count):
#             binary_numbers.append('0' + sub_binary_numbers[i])
#
#         for i in xrange(sub_binary_numbers_count - 1, -1, -1):
#             binary_numbers.append('1' + sub_binary_numbers[i])
#
#         return binary_numbers
#
#     def grayCode(self, n):
#         """
#         :type n: int
#         :rtype: List[int]
#         """
#         binary_numbers = self.getBianryNumbers(n)
#         return [int(number, 2) for number in binary_numbers]


# Solution 2
class Solution(object):
    def grayCode(self, n):
        result = []
        for i in xrange(1<<n):
            result.append((i>>1)^i)
        return result


if __name__ == '__main__':
    # 000
    # 001
    #
    # 011
    # 010
    #
    # 110
    # 111
    #
    # 101
    # 100
    n = 3
    solution = Solution()
    print solution.grayCode(n)
