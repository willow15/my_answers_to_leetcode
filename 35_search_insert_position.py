class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        low = 0
        high = len(nums) - 1
        if target < nums[low]:
            return low
        if target > nums[high]:
            return high + 1

        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low


if __name__ == '__main__':
    nums = [1, 3, 5, 7]
    solution = Solution()
    for target in [1, 3, 5, 7, 0, 8, 2, 4, 6]:
        print solution.searchInsert(nums, target)
