class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) / 3
        count = {}
        result = []
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        for key, value in count.items():
            if value > n:
                result.append(key)
        return result


if __name__ == '__main__':
    # nums = [3, 2, 3]
    # nums = [1, 1, 1, 3, 3, 2, 2, 2]
    nums = [1]
    solution = Solution()
    print solution.majorityElement(nums)
