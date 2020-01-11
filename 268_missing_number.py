class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_length = len(nums)
        total = (1 + nums_length) * nums_length / 2
        for num in nums:
            total -= num
        return total


if __name__ == '__main__':
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    solution = Solution()
    print solution.missingNumber(nums)
