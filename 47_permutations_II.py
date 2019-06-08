class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 1:
            return [nums]
        elif n == 0:
            return []

        used = []
        results = []
        for i in xrange(n):
            if i != 0:
                if nums[i] not in used:
                    used.append(nums[i])
                    tmp = nums[0]
                    nums[0] = nums[i]
                    nums[i] = tmp
                    sub_results = self.permuteUnique(nums[1:])
                    if sub_results:
                        for sub_result in sub_results:
                            results.append([nums[0]] + sub_result)
                    else:
                        results.append([nums[0]])
            else:
                used.append(nums[0])
                sub_results = self.permuteUnique(nums[1:])
                if sub_results:
                    for sub_result in sub_results:
                        results.append([nums[0]] + sub_result)
                else:
                    results.append([nums[0]])

        return results


if __name__ == '__main__':
    # nums = [2, 2, 1, 1]
    nums = [1, 1, 2]
    solution = Solution()
    print solution.permuteUnique(nums)
