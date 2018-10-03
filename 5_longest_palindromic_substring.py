class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start_index = 0
        result_length = 0
        max_right_index = len(s) - 1
        # aba
        for mid in xrange(len(s)):
            left_index = mid
            right_index = mid
            while left_index >= 0 and right_index <= max_right_index and s[left_index] == s[right_index]:
                left_index -= 1
                right_index += 1
            tmp_length = right_index - left_index - 1
            if tmp_length >= result_length:
                start_index = left_index + 1
                result_length = tmp_length
        # abba
        for mid in xrange(1, len(s)):
            left_index = mid - 1
            right_index = mid
            while left_index >= 0 and right_index <= max_right_index and s[left_index] == s[right_index]:
                left_index -= 1
                right_index += 1
            tmp_length = right_index - left_index - 1
            if tmp_length >= result_length:
                start_index = left_index + 1
                result_length = tmp_length

        return s[start_index:start_index + result_length]


if __name__ == '__main__':
    solution = Solution()
    s = 'a'
    print solution.longestPalindrome(s)
