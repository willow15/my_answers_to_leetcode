# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        queue = list()
        if root.left is not None:
            queue.append(root.left)
        if root.right is not None:
            queue.append(root.right)
        count = 2
        while queue:
            new_queue = list()
            for node in queue:
                if node.left is None and node.right is None:
                    return count
                else:
                    if node.left is not None:
                        new_queue.append(node.left)
                    if node.right is not None:
                        new_queue.append(node.right)
            count += 1
            queue = new_queue


if __name__ == '__main__':
    nodes = [3, 9, 20, None, None, 15, 7]
    root = TreeNode(nodes[0])
    queue = [root]
    nodes_count = len(nodes)
    for i in xrange(1, nodes_count, 2):
        node = queue.pop(0)
        if nodes[i] != None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        if nodes[i + 1] != None:
            node.right = TreeNode(nodes[i + 1])
            queue.append(node.right)

    solution = Solution()
    print solution.minDepth(root)
