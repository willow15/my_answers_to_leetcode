class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.combinationSum_(candidates, target, 0)

    def combinationSum_(self, candidates, target, start_index):
        result = []
        if target < candidates[0]:
            return []
        for i in xrange(len(candidates)):
            remainder = target - candidates[i]
            if remainder == 0:
                result.append([candidates[i]])
            else:
                for sub_result in self.combinationSum_(candidates[i:], remainder, i):
                    result.append([candidates[i]] + sub_result)
        return result


if __name__ == '__main__':
    candidates = [8, 7, 4, 3]
    target = 11
    solution = Solution()
    print solution.combinationSum(candidates, target)
