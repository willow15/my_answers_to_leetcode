class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        n = len(digits)
        i = n - 1
        while i >= 0:
            if digits[i] < 9:
                break
            else:
                i -= 1
        if i < 0:
            result.append(1)
            for j in xrange(n):
                result.append(0)
        else:
            for j in xrange(i):
                result.append(digits[j])
            result.append(digits[i] + 1)
            for j in xrange(i + 1, n):
                result.append(0)
        return result


if __name__ == '__main__':
    digits = [9, 9, 0]
    solution = Solution()
    print solution.plusOne(digits)
