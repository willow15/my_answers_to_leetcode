class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        water = 0
        while left < right:
            water = max(water, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return water

if __name__ == '__main__':
    height = [1, 1]
    solution = Solution()
    print solution.maxArea(height)
