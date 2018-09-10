# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = 0
        count1 = 1
        while l1:
            n1 = n1 + l1.val * count1
            count1 = count1 * 10
            l1 = l1.next
        n2 = 0
        count2 = 1
        while l2:
            n2 = n2 + l2.val * count2
            count2 = count2 * 10
            l2 = l2.next
        n3 = n1 + n2
        l3 = ListNode(n3 % 10)
        previous = l3
        n3 = n3 / 10
        while n3:
            node = ListNode(n3 % 10)
            previous.next = node
            previous = node
            n3 = n3 / 10
        return l3


if __name__ == '__main__':
    n1 = 342
    l1 = ListNode(n1 % 10)
    previous = l1
    n1 = n1 / 10
    while n1:
        node = ListNode(n1 % 10)
        previous.next = node
        previous = node
        n1 = n1 / 10
    n2 = 465
    l2 = ListNode(n2 % 10)
    previous = l2
    n2 = n2 / 10
    while n2:
        node = ListNode(n2 % 10)
        previous.next = node
        previous = node
        n2 = n2 / 10
    s = Solution()
    s.addTwoNumbers(l1, l2)
