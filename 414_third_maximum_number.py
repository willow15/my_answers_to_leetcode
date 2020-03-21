class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = [nums[0]]  # sort in descending order
        nums_count = len(nums)
        for i in xrange(1, nums_count):
            if nums[i] in result:
                continue
            result_count = len(result)
            if result_count == 3:
                for j in xrange(result_count):
                    if nums[i] > result[j]:
                        for k in xrange(result_count - 1, j, -1):
                            result[k] = result[k - 1]
                        result[j] = nums[i]
                        break
            elif nums[i] < result[-1]:
                result.append(nums[i])
            else:
                for j in xrange(result_count):
                    if nums[i] > result[j]:
                        result.insert(j, nums[i])
                        break

        if len(result) == 3:
            return result[-1]
        else:
            return result[0]


if __name__ == '__main__':
    nums = [1, 2]
    solution = Solution()
    print solution.thirdMax(nums)
