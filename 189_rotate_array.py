class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n != 0:
            k = k % n
            for count in xrange(k):
                num = nums.pop(-1)
                nums.insert(0, num)
        print nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solution = Solution()
    solution.rotate(nums, k)
