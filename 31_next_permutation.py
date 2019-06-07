class Solution(object):
    def bubble_sort(self, nums, start, end):
        n = end - start + 1
        for i in xrange(n - 1):
            for j in xrange(start, start + n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j + 1] = nums[j] + nums[j + 1]
                    nums[j] = nums[j + 1] - nums[j]
                    nums[j + 1] = nums[j + 1] - nums[j]


    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        swap_index = None
        last_index = len(nums) - 1
        i = last_index - 1
        while i >= 0:
            for j in xrange(last_index, i, -1):
                if nums[i] < nums[j]:
                    swap_index = j
                    break
            if swap_index:
                break
            i -= 1
        if swap_index:
            nums[swap_index] = nums[i] + nums[swap_index]
            nums[i] = nums[swap_index] - nums[i]
            nums[swap_index] = nums[swap_index] - nums[i]
            if i + 1 < last_index:
                self.bubble_sort(nums, i + 1, last_index)
        else:
            self.bubble_sort(nums, 0, last_index)


if __name__ == '__main__':
    nums = [5, 1, 1]
    solution = Solution()
    solution.nextPermutation(nums)
    print nums
