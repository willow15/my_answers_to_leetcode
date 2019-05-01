class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        max_right = len(nums) - 1
        for i in xrange(len(nums) - 3 + 1):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, max_right
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result = [nums[i], nums[left], nums[right]]
                    results.append(result)
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1]:
                        left += 1
                        if left > right:
                            break
                    while nums[right] == nums[right + 1]:
                        right -= 1
                        if left > right:
                            break
                elif total < 0:
                    left += 1
                    while nums[left] == nums[left - 1]:
                        left += 1
                        if left > right:
                            break
                else:
                    right -= 1
                    while nums[right] == nums[right + 1]:
                        right -= 1
                        if left > right:
                            break

        return results

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = []
    solution = Solution()
    print solution.threeSum(nums)
