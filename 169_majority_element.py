class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) / 2
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
            if count[num] > n:
                return num


if __name__ == '__main__':
    # nums = [2, 2, 1, 1, 1, 2, 2]
    nums = [1]
    solution = Solution()
    print solution.majorityElement(nums)
