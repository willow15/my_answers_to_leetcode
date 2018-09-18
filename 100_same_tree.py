# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p_queue = [p]
        q_queue = [q]
        while p_queue and q_queue:
            p_node = p_queue.pop(0)
            q_node = q_queue.pop(0)
            if p_node is not None and q_node is not None:
                if p_node.val == q_node.val:
                    p_queue.append(p_node.left)
                    p_queue.append(p_node.right)
                    q_queue.append(q_node.left)
                    q_queue.append(q_node.right)
                else:
                    return False
            elif p_node is None and q_node is None:
                pass
            else:
                return False
        return True


if __name__ == '__main__':
    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(1)
    p2 = TreeNode(1)
    p2.left = TreeNode(2)
    p2.right = TreeNode(1)
    p2.right.right = TreeNode(3)

    s = Solution()
    print s.isSameTree(p1, p2)
