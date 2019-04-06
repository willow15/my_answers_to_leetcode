class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs_len = len(strs)
        if strs_len == 0:
            return ''
        if strs_len == 1:
            return strs[0]

        s = min(strs, key=len)
        strs = set(strs) - set([s])
        prefix = ''
        s_len = len(s)
        for i in xrange(s_len):
            for word in strs:
                if word[i] != s[i]:
                    return prefix
            prefix += s[i]
        return prefix


if __name__ == '__main__':
    s = Solution()
    strs = []
    print s.longestCommonPrefix(strs)
