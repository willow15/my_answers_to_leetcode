class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        mappings = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I',
                    10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q',
                    18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y',
                    26:'Z'}
        while n > 0:
            m = n % 26
            if m != 0:
                result = mappings[m] + result
                n = (n - m) / 26
            else:
                result = 'Z' + result
                n = (n - 26) / 26
        return result


if __name__ == '__main__':
    n = 54100  # 54100 = 3*26*26*26 + 1*26*26 + 26*26 + 20 = (((3*26)*26+1)*26+26)*26+20
    solution = Solution()
    print solution.convertToTitle(n)
