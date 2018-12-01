class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        int_roman_mapping = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C',
                             500: 'D', 1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL',
                             90: 'XC', 400: 'CD', 900: 'CM'}
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ''
        i = 0
        while num > 0:
            tmp_num = num - numbers[i]
            if tmp_num >= 0:
                result += int_roman_mapping[numbers[i]]
                num = tmp_num
            else:
                i += 1
        return result


if __name__ == '__main__':
    num = 1994
    solution = Solution()
    print solution.intToRoman(num)
