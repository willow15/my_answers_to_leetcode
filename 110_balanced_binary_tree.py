# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or root.val is None:
            return True

        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        if left_depth is False or right_depth is False:
            return False
        if abs(left_depth - right_depth) > 1:
            return False

        return True

    def get_depth(self, node):
        if node is None or node.val is None:
            return 0

        left_depth = self.get_depth(node.left)
        right_depth = self.get_depth(node.right)
        if left_depth is False or right_depth is False:
            return False
        if abs(left_depth - right_depth) > 1:
            return False

        return max(left_depth, right_depth) + 1


if __name__ == '__main__':
    # nodes = [1, 2, 2, 3, 3, None, None, 4, 4]
    # nodes = [3, 9, 20, None, None, 15, 7]
    # nodes = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]
    root = TreeNode(nodes[0])
    queue = [root]
    nodes_count = len(nodes)
    i = 1
    while i < nodes_count:
        node = queue.pop(0)
        left = TreeNode(nodes[i])
        right = TreeNode(nodes[i + 1])
        node.left = left
        node.right = right
        i += 2
        if left is not None:
            queue.append(left)
        if right is not None:
            queue.append(right)

    solution = Solution()
    print solution.isBalanced(root)
