class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        substring = list()
        for character in s:
            if character not in substring:
                substring.append(character)
            else:
                substring = substring[substring.index(character) + 1:]
                substring.append(character)
            sub_len = len(substring)
            if sub_len > max_len:
                max_len = sub_len
        return max_len


if __name__ == '__main__':
    solution = Solution()
    s = 'pwwkew'
    print solution.lengthOfLongestSubstring(s)
