class Solution(object):
    def __init__(self):
        self.number = None

    def findKthSmallest(self, nums, k):
        key = nums[-1]
        i = - 1
        for j in xrange(len(nums) - 1):
            if nums[j] <= key:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[-1] = nums[-1], nums[i + 1]
        middle = i + 1
        print 'aaa', middle, k, nums
        if middle == k:
            print 'bbb', nums[middle], type(nums[middle])
            self.number = nums[middle]
            # return nums[middle]
        elif middle < k:
            self.findKthSmallest(nums[middle:], k - middle)
        else:
            self.findKthSmallest(nums[:middle], k)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k
        self.findKthSmallest(nums, k)
        return self.number

if __name__ == '__main__':
    solution = Solution()
    # nums = [3, 2, 1, 5, 6, 4]
    # nums = [1, 2]
    nums = [2, 1]
    print solution.findKthLargest(nums, 1)
