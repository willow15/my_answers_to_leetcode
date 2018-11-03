class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        end_index = len(nums) - 1
        if end_index == 0:
            return True
        cur_index = end_index - 1
        while cur_index >= 0:
            if cur_index + nums[cur_index] >= end_index:
                if cur_index == 0:
                    return True
                else:
                    end_index = cur_index
                    cur_index = end_index - 1
            else:
                cur_index = cur_index - 1
        return False


if __name__ == '__main__':
    nums = [3, 2, 1, 0, 4]
    solution = Solution()
    print solution.canJump(nums)
