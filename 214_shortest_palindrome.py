class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # by using kmp
        s_and_reverse = s + '_' + s[::-1]
        overlap = [-1] + [0] * len(s_and_reverse)
        for i in xrange(len(s_and_reverse)):
            overlap[i + 1] = overlap[i] + 1
            while overlap[i + 1] >= 1 and s_and_reverse[i] != s_and_reverse[overlap[i + 1] - 1]:
                overlap[i + 1] = overlap[overlap[i + 1] - 1] + 1
        start_index = overlap[-1]
        result = s[:start_index - 1:-1] + s
        return result


if __name__ == '__main__':
    solution = Solution()
    # s = 'abcd'
    s = 'aabba'
    print solution.shortestPalindrome(s)
