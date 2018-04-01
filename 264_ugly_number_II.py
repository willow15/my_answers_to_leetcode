class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly_numbers = list()
        ugly_numbers.append(1)
        index2 = 0
        index3 = 0
        index5 = 0
        for i in xrange(n - 1):
            number2 = ugly_numbers[index2] * 2
            number3 = ugly_numbers[index3] * 3
            number5 = ugly_numbers[index5] * 5
            min_number = min(number2, number3, number5)
            ugly_numbers.append(min_number)
            if min_number == number2:
                index2 += 1
            if min_number == number3:
                index3 += 1
            if min_number == number5:
                index5 += 1
        return ugly_numbers[n - 1]

if __name__ == '__main__':
    solution = Solution()
    print solution.nthUglyNumber(10)
