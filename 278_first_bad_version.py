# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version >= 4:
        return True
    return False


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start <= end:
            mid = start + (end - start) / 2
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1

        return start


if __name__ == '__main__':
    n = 5
    solution = Solution()
    print solution.firstBadVersion(n)
