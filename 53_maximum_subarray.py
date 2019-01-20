class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        # cross the middle
        nums_length = len(nums)
        mid = (nums_length) / 2
        mid_sum1 = nums[mid]
        sub_sum1 = nums[mid]
        for i in xrange(mid - 1, -1, -1):
            sub_sum1 += nums[i]
            if sub_sum1 > mid_sum1:
                mid_sum1 = sub_sum1
        mid_sum2 = nums[mid]
        sub_sum2 = nums[mid]
        for i in xrange(mid + 1, nums_length):
            sub_sum2 += nums[i]
            if sub_sum2 > mid_sum2:
                mid_sum2 = sub_sum2
        mid_sum = mid_sum1 + mid_sum2 - nums[mid]
        # left
        left_sum = self.maxSubArray(nums[:mid])
        # right
        right_sum = self.maxSubArray(nums[mid + 1:])

        max_sum = max(mid_sum, left_sum, right_sum)
        return max_sum


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    print solution.maxSubArray(nums)
