class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n <= 2:
            return 0

        water = 0
        # find max left height and right height for ith bar
        left_max_heights = [0] * n
        right_max_heights = [0] * n
        j = n - 2
        for i in xrange(1, n):
            left_max_heights[i] = max(left_max_heights[i - 1], height[i - 1])
            right_max_heights[j] = max(right_max_heights[j + 1], height[j + 1])
            j -= 1
        for i in xrange(n):
            volume = min(left_max_heights[i], right_max_heights[i]) - height[i]
            if volume > 0:
                water += volume

        return water


if __name__ == '__main__':
    # height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    height = [5, 2, 1, 2, 1, 5]
    # height = [5, 4, 1, 2]
    # height = [2, 0, 2]
    solution = Solution()
    print solution.trap(height)
