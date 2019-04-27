class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mappings = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6,
                    'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13,
                    'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
                    'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

        result = {}
        for word in strs:
            counter = [0] * 26
            for character in word:
                counter[mappings[character]] += 1
            code = ''
            for i in counter:
                code += str(i)
            if code not in result:
                result[code] = [word]
            else:
                result[code].append(word)

        return result.values()


if __name__ == '__main__':
    # strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    strs = ['cab', 'tin', 'pew', 'duh', 'may', 'ill', 'buy', 'bar', 'max', 'doc']
    solution = Solution()
    print solution.groupAnagrams(strs)
