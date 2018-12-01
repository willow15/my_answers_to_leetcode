class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_int_mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        max_i = len(s)
        result = 0
        while i < max_i:
            if i + 1 < max_i:
                if roman_int_mapping[s[i]] >= roman_int_mapping[s[i + 1]]:
                    result += roman_int_mapping[s[i]]
                    i += 1
                else:
                    result += roman_int_mapping[s[i + 1]] - roman_int_mapping[s[i]]
                    i += 2
            else:
                result += roman_int_mapping[s[i]]
                i += 1
        return result


if __name__ == '__main__':
    s = 'MCMXCIV'
    solution = Solution()
    print solution.romanToInt(s)
