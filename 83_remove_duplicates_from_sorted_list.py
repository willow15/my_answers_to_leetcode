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

        vals = [head.val]
        result_node = head
        pre_node = head
        cur_node = head.next
        while cur_node is not None:
            if cur_node.val in vals:
                pre_node.next = cur_node.next
                cur_node = cur_node.next
            else:
                vals.append(cur_node.val)
                pre_node = cur_node
                cur_node = cur_node.next

        return result_node


if __name__ == '__main__':
    vals = [1, 1, 2, 3, 3]
    head = ListNode(vals[0])
    pre_node = head
    for i in xrange(1, len(vals)):
        cur_node = ListNode(vals[i])
        pre_node.next = cur_node
        pre_node = cur_node

    solution = Solution()
    result_node = solution.deleteDuplicates(head)
    while result_node is not None:
        print result_node.val
        result_node = result_node.next
