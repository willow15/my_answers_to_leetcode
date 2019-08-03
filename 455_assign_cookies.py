class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        count = 0
        child_index = 0
        child_num = len(g)
        for size in s:
            if child_index == child_num:
                break
            if size >= g[child_index]:
                count += 1
                child_index += 1
        return count


if __name__ == '__main__':
    g = [1, 2, 3]
    s = [1, 1]
    solution = Solution()
    print solution.findContentChildren(g, s)
