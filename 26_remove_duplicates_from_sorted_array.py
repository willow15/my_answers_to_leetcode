class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_length = len(nums)
        unique_length = 0
        i = 0
        num = None
        while nums_length:
            if nums[i] != num:
                num = nums[i]
                unique_length += 1
                i += 1
            else:
                nums.remove(nums[i])
            nums_length -= 1

        return unique_length


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    s = Solution()
    print s.removeDuplicates(nums)
    print nums
