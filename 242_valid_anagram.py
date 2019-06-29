class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (not s and t) or (s and not t):
            return False

        count = dict()
        for letter in s:
            if letter not in count:
                count[letter] = 1
            else:
                count[letter] += 1

        for letter in t:
            if letter in count:
                if count[letter] == 0:
                    return False
                else:
                    count[letter] -= 1
            else:
                return False

        for letter in count:
            if count[letter] != 0:
                return False

        return True


if __name__ == '__main__':
    # s = 'anagram'
    # t = 'nagaram'
    s = 'ab'
    t = 'a'
    solution = Solution()
    print solution.isAnagram(s, t)
