class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1_max_index = len(nums1) - 1
        i = 0
        for j in xrange(n):
            if i - j != m:
                if nums2[j] < nums1[i]:
                    for k in xrange(nums1_max_index, i, -1):
                        nums1[k] = nums1[k - 1]
                    nums1[i] = nums2[j]
                    i += 1
                else:
                    while nums2[j] >= nums1[i]:
                        i += 1
                        if i - j == m:
                            break
                    if i - j == m:
                        nums1[i] = nums2[j]
                    else:
                        for k in xrange(nums1_max_index, i, -1):
                            nums1[k] = nums1[k - 1]
                        nums1[i] = nums2[j]
                    i += 1
            else:
                nums1[i] = nums2[j]
                i += 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print nums1
