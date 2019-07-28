# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is not None and l2 is not None:
            if l1.val < l2.val:
                result = ListNode(l1.val)
                l1 = l1.next
            else:
                result = ListNode(l2.val)
                l2 = l2.next
            p_result = result
            while l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    p_result.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    p_result.next = ListNode(l2.val)
                    l2 = l2.next
                p_result = p_result.next
            if l1 is not None and l2 is None:
                p_result.next = l1
            elif l1 is None and l2 is not None:
                p_result.next = l2
            return result
        elif l1 is not None and l2 is None:
            return l1
        elif l1 is None and l2 is not None:
            return l2
        else:
            return None


if __name__ == '__main__':
    l1_list = [1, 2, 4]
    l2_list = [1, 3, 4]
    l1 = ListNode(l1_list[0])
    p1 = l1
    for i in xrange(1, len(l1_list)):
        p1.next = ListNode(l1_list[i])
        p1 = p1.next
    l2 = ListNode(l2_list[0])
    p2 = l2
    for i in xrange(1, len(l2_list)):
        p2.next = ListNode(l2_list[i])
        p2 = p2.next

    solution = Solution()
    result = solution.mergeTwoLists(l1, l2)
    while result is not None:
        print result.val
        result = result.next
