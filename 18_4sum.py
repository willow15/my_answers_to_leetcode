class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = self.nSum(nums, target, 4)
        return result

    def nSum(self, nums, target, n):
        if n == 2:
            results = list()
            left, right = 0, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    results.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            return results
        else:
            final_results = list()
            for i in xrange(len(nums) - n + 1):
                if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                    results = self.nSum(nums[i + 1:], target - nums[i], n - 1)
                    for j in xrange(len(results)):
                        result = [nums[i]] + results[j]
                        if result not in final_results:
                            final_results.append(result)
            return final_results



if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    solution = Solution()
    print solution.fourSum(nums, target)
