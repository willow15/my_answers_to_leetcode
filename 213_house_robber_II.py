class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_amounts1 = [nums[0]]  # with first house
        max_amounts2 = [0]  # without first house
        house_count = len(nums)
        if house_count > 1:
            max_amounts1.append(max(nums[0], nums[1]))
            max_amounts2.append(nums[1])

        for i in xrange(2, house_count):
            max_amounts1.append(max(nums[i] + max_amounts1[i - 2], max_amounts1[i - 1]))
            max_amounts2.append(max(nums[i] + max_amounts2[i - 2], max_amounts2[i - 1]))

        if house_count > 2:
            return max(nums[house_count - 1] + max_amounts2[house_count - 3], max_amounts1[house_count - 2])
        else:
            return max_amounts1[-1]


if __name__ == '__main__':
    # nums = [2, 3, 2]
    nums = [1, 2, 3, 1]
    solution = Solution()
    print solution.rob(nums)
