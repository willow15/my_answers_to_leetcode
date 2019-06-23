# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        depth = 0
        queue = [root]
        while queue:
            depth += 1
            new_queue = []
            for node in queue:
                if node.left is not None:
                    new_queue.append(node.left)
                if node.right is not None:
                    new_queue.append(node.right)
            queue = new_queue

        return depth


if __name__ == '__main__':
    # [3,9,20,null,null,15,7] -> 3
    pass
