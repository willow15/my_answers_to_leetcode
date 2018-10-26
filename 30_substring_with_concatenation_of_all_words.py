class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # by using hash table
        if not s or not words:
            return []
        result = []
        s_length = len(s)
        words_length = len(words)
        word_length = len(words[0])
        bound = s_length - word_length * words_length + 1
        counts = {}
        for word in words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
        for i in xrange(bound):
            met = {}
            for key, value in counts.items():
                met[key] = value
            for j in xrange(i, s_length, word_length):
                substring = s[j : j + word_length]
                if substring in met:
                    met[substring] -= 1
                    if met[substring] == 0:
                        del met[substring]
                    if not met:
                        result.append(i)
                        break
                else:
                    break
        return result


if __name__ == '__main__':
    solution = Solution()
    s = 'barfoofoobarthefoobarman'
    words = ['bar', 'foo', 'the']
    print solution.findSubstring(s, words)
