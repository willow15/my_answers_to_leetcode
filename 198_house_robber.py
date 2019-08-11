class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max_amounts[n] = max(nums[n] + max_amounts[n - 2], max_amounts[n - 1])
        if not nums:
            return 0

        house_count = len(nums)
        max_amounts = [nums[0]]
        if house_count > 1:
            max_amounts.append(max(nums[0], nums[1]))
        for i in xrange(2, house_count):
            max_amounts.append(max(nums[i] + max_amounts[i - 2], max_amounts[i - 1]))

        return max_amounts[-1]


if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]
    solution = Solution()
    print solution.rob(nums)
