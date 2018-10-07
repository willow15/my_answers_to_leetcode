# coding=utf-8


class KMP(object):
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern

    def compute_overlap(self):
        # overlap of two strings x and y: the longest word that's a suffix of x and a prefix of y
        # overlap for 'aabaaa' is [0, 1, 0, 1, 2, 2]
        self.overlap = [-1] + [0] * len(self.pattern)
        for i in xrange(len(self.pattern)):
            self.overlap[i + 1] = self.overlap[i]  + 1
            while self.overlap[i + 1] >= 1 and self.pattern[i] != self.pattern[self.overlap[i + 1] - 1]:
                self.overlap[i + 1] = self.overlap[self.overlap[i + 1] - 1] + 1

        print self.overlap

    def find_pattern(self):
        self.compute_overlap()

        match_start = None
        i = 0
        j = 0
        while i < len(self.text):
            print i, self.text[i], j, self.pattern[j]
            if self.text[i] == self.pattern[j]:
                i += 1
                j += 1
                if j == len(self.pattern):
                    match_start = i - len(self.pattern)
                    break
            elif j == 0:
                i += 1
            else:
                j = self.overlap[j]

        print match_start


if __name__ == '__main__':
    text = 'abcdaabaacaabaaad'
    pattern = 'aabaaa'
    kmp = KMP(text, pattern)
    kmp.find_pattern()
