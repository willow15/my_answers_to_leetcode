class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 0:
            return []
        elif n == 1:
            return [nums]

        results = []
        for i in xrange(n):
            if i != 0:
                tmp = nums[0]
                nums[0] = nums[i]
                nums[i] = tmp
            sub_results = self.permute(nums[1:])
            if sub_results:
                for sub_result in sub_results:
                    results.append([nums[0]] + sub_result)
            else:
                results.append([nums[0]])
        return results


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    solution = Solution()
    print solution.permute(nums)
