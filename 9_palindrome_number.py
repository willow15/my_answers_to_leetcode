class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        origin_x = x
        if x < 0:
            return False
        y = 0
        while x > 0:
            y = y * 10 + x % 10
            x = x / 10
        return origin_x == y


if __name__ == '__main__':
    s = Solution()
    x = 1
    print s.isPalindrome(x)
