class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums_count = len(nums)
        now_index = 0
        result_count = 0
        while nums_count > 0:
            if nums[now_index] == val:
                nums.remove(nums[now_index])
            else:
                result_count += 1
                now_index += 1
            nums_count -= 1
        return result_count


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    solution = Solution()
    print solution.removeElement(nums, val)
    print nums
