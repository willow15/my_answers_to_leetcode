class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = True if x < 0 else False
        x = abs(x)
        result = 0
        while x:
            result = result * 10 + x % 10
            x = x / 10
        if is_negative:
            result = -result
        if result > 2 ** 31 -1 or result < 0 - 2 ** 31:
            return 0
        else:
            return result


if __name__ == '__main__':
    solution = Solution()
    x = -1
    print solution.reverse(x)
