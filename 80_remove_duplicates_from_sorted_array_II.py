class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_length = len(nums)
        result_length = 0
        i = 0
        nums_count = dict()
        while nums_length:
            if nums[i] not in nums_count:
                nums_count[nums[i]] = 1
                result_length += 1
                i += 1
            elif nums_count[nums[i]] < 2:
                nums_count[nums[i]] += 1
                result_length += 1
                i += 1
            else:
                nums.remove(nums[i])
            nums_length -= 1

        return result_length


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    s = Solution()
    print s.removeDuplicates(nums)
    print nums
