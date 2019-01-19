class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = []
        if not S:
            return [S]
        if S[0].isdigit():
            for sub_result in self.letterCasePermutation(S[1:]):
                result.append(S[0] + sub_result)
        else:
            for sub_result in self.letterCasePermutation(S[1:]):
                result.append(S[0].lower() + sub_result)
                result.append(S[0].upper() + sub_result)
        return result

if __name__ == '__main__':
    S = 'a1b2'
    solution = Solution()
    print solution.letterCasePermutation(S)
