class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(len(nums)):
            value = i + 1
            while nums[i] != value:
                if nums[i] == nums[nums[i] - 1]:
                    return nums[i]
                tmp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    solution = Solution()
    print solution.findDuplicate(nums)
