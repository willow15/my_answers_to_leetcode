# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        result_node = None
        pre_pre_node = None
        pre_node = head
        cur_node = head.next
        while cur_node is not None:
            if pre_node.val == cur_node.val:
                cur_node = cur_node.next
            else:
                if pre_node.next != cur_node:
                    pre_node = cur_node
                    cur_node = cur_node.next
                else:
                    if result_node is None:
                        result_node = pre_node
                        pre_pre_node = pre_node
                    else:
                        pre_pre_node.next = pre_node
                        pre_pre_node = pre_pre_node.next
                    pre_node = cur_node
                    cur_node = cur_node.next
        if pre_node.next != cur_node:
            if pre_pre_node is not None:
                pre_pre_node.next = None
        else:
            if result_node is None:
                result_node = pre_node
            else:
                pre_pre_node.next = pre_node

        return result_node


if __name__ == '__main__':
    vals = [1, 2, 3, 3, 4, 4, 5]
    head = ListNode(vals[0])
    pre_node = head
    for i in xrange(1, len(vals)):
        cur_node = ListNode(vals[i])
        pre_node.next = cur_node
        pre_node = cur_node

    solution = Solution()
    result_node = solution.deleteDuplicates(head)
    while result_node:
        print result_node.val
        result_node = result_node.next
