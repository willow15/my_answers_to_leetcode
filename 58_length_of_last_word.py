class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        start_index = None
        end_index = None
        for i in xrange(len(s) - 1, -1, -1):
            if start_index is None:
                if s[i] != ' ':
                    start_index = i
            else:
                if s[i] == ' ':
                    end_index = i
                    break
        if start_index is not None:
            if end_index is not None:
                return start_index - end_index
            else:
                return start_index + 1
        else:
            return 0


if __name__ == '__main__':
    s = 'hello'
    solution = Solution()
    print solution.lengthOfLastWord(s)
