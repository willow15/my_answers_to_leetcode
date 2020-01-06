class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum_value = numbers[left] + numbers[right]
            if sum_value < target:
                left += 1
            elif sum_value > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return []


if __name__ == '__main__':
    numbers = [-1, 0]
    target = -1
    solution = Solution()
    print solution.twoSum(numbers, target)
