class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        left_count = (len1 + len2 + 1) / 2
        right_count = len1 + len2 - left_count

        for count1 in xrange(len1 + 1):
            count2 = left_count - count1
            if count2 < 0 or count2 > len2:
                continue

            index1 = count1 - 1
            index2 = count2 - 1
            print 'count1:', count1
            print 'count2:', count2
            print 'index1:', index1
            print 'index2:', index2

            if count1 > 0 and count1 < len1 and count2 > 0 and count2 < len2:
                if nums1[index1] <= nums2[count2] and nums2[index2] <= nums1[count1]:
                    if left_count > right_count:
                        return float(max(nums1[index1], nums2[index2]))
                    elif left_count < right_count:
                        return float(min(nums1[count1], nums2[count2]))
                    else:
                        return (max(nums1[index1], nums2[index2]) + min(nums2[count2], nums1[count1])) / 2.0

            elif count1 == 0:
                if len1 == 0:
                    if left_count == right_count:
                        return (nums2[index2] + nums2[count2]) / 2.0
                    elif left_count > right_count:
                        return float(nums2[index2])
                    else:
                        return float(nums2[count2])
                elif nums2[index2] <= nums1[0]:
                    if left_count > right_count:
                        return float(nums2[index2])
                    elif left_count < right_count:
                        if count2 < len2:
                            return float(min(nums1[0], nums2[count2]))
                        else:
                            return float(nums1[0])
                    else:
                        if count2 < len2:
                            return (nums2[index2] + min(nums1[0], nums2[count2])) / 2.0
                        else:
                            return (nums2[index2] + nums1[0]) / 2.0

            elif count1 == len1:
                if count2 == 0:
                    if left_count > right_count:
                        return float(nums1[-1])
                    elif left_count < right_count:
                        return float(nums2[0])
                    else:
                        return (nums1[-1] + nums2[0]) / 2.0
                elif count2 < len2 and nums1[-1] <= nums2[count2]:
                    if left_count > right_count:
                        if index2 >= 0:
                            return float(max(nums1[-1], nums2[index2]))
                        else:
                            return float(nums1[-1])
                    elif left_count < right_count:
                        return float(nums2[count2])
                    else:
                        if index2 >= 0:
                            return (max(nums1[-1], nums2[index2]) + nums2[count2]) / 2.0
                        else:
                            return (nums1[-1] + nums2[count2]) / 2.0

            elif count2 == 0:
                if len2 == 0:
                    if left_count == right_count:
                        return (nums1[index1] + nums1[count1]) / 2.0
                    elif left_count > right_count:
                        return float(nums1[index1])
                    else:
                        return float(nums1[count1])
                elif nums1[index1] <= nums2[0]:
                    if left_count > right_count:
                        return float(nums1[index1])
                    elif left_count < right_count:
                        if count1 < len1:
                            return float(min(nums1[count1], nums2[0]))
                        else:
                            return float(nums2[0])
                    else:
                        if count1 < len1:
                            return (nums1[index1] + min(nums1[count1], nums2[0])) / 2.0
                        else:
                            return (nums1[index1] + nums2[0]) / 2.0

            elif count2 == len2:
                if count1 == 0:
                    if left_count > right_count:
                        return float(nums2[-1])
                    elif left < right_count:
                        return float(nums1[0])
                    else:
                        return (nums2[-1] + nums1[0]) / 2.0
                elif count1 < len1 and nums2[-1] <= nums1[count1]:
                    if left_count > right_count:
                        if index1 >= 0:
                            return float(max(nums1[index1], nums2[-1]))
                        else:
                            return float(nums2[-1])
                    elif left_count < right_count:
                        return float(nums1[count1])
                    else:
                        if index1 >= 0:
                            return (max(nums1[index1], nums2[-1]) + nums1[count1]) / 2.0
                        else:
                            return (nums2[-1] + nums1[count1]) / 2.0


if __name__ == '__main__':
    s = Solution()
    nums1 = []
    nums2 = [1]
    print s.findMedianSortedArrays(nums1, nums2)
