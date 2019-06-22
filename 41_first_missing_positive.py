class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1

        n = len(nums)
        marks = [0] * n
        for num in nums:
            if num <= 0 or num > n:
                continue
            marks[num - 1] = 1
        for i in xrange(n):
            if marks[i] == 0:
                return i + 1
        return n + 1


if __name__ == '__main__':
    # [1, 2, 0] -> 3
    # [3, 4, -1, 1] -> 2
    # [7, 8, 9, 11, 12] -> 1
    nums = [1, 2, 3, 4, 5, 6]
    solution = Solution()
    print solution.firstMissingPositive(nums)
