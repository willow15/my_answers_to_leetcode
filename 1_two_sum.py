class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        another_number = {target - nums[0] : 0}  # another number we need : index
        for i in xrange(1, len(nums)):
            if nums[i] in another_number:
                return [another_number[nums[i]], i]
            else:
                another_number[target - nums[i]] = i


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print s.twoSum(nums, target)
