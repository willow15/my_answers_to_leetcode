class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_len = len(s)
        if s_len % 2 != 0:
            return False

        parenthes_index = []
        bracket_index = []
        braces_index = []
        for i in xrange(len(s)):
            if s[i] == '(':
                parenthes_index.append(i)
            elif s[i] == ')':
                if parenthes_index:
                    last_index = parenthes_index.pop(-1)
                    if (i - last_index) % 2 != 1:
                        return False
                else:
                    return False
            elif s[i] == '[':
                bracket_index.append(i)
            elif s[i] == ']':
                if bracket_index:
                    last_index = bracket_index.pop(-1)
                    if (i - last_index) % 2 != 1:
                        return False
                else:
                    return False
            elif s[i] == '{':
                braces_index.append(i)
            else:
                if braces_index:
                    last_index = braces_index.pop(-1)
                    if (i - last_index) % 2 != 1:
                        return False
                else:
                    return False

        if parenthes_index or bracket_index or braces_index:
            return False
        return True


if __name__ == '__main__':
    s = '(()'
    solution = Solution()
    print solution.isValid(s)
