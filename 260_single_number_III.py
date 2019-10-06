class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hash_table = {}
        for num in nums:
            try:
                hash_table.pop(num)
            except:
                hash_table[num] = 1
        return hash_table.keys()


if __name__ == '__main__':
    nums = [1, 2, 1, 3, 2, 5]
    solution = Solution()
    print solution.singleNumber(nums)
