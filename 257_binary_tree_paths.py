# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        result = []
        def dfs(node, path):
            if node.left:
                dfs(node.left, path + '->' + str(node.left.val))
            if node.right:
                dfs(node.right, path + '->' + str(node.right.val))
            if not node.left and not node.right:
                result.append(path)

        dfs(root, str(root.val))
        return result


if __name__ == '__main__':
    # input = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    input = [1]
    if input:
        root = TreeNode(input.pop(0))
        nodes = [root]
        while input:
            node = nodes.pop(0)
            left_val = input.pop(0)
            if left_val:
                left = TreeNode(left_val)
                nodes.append(left)
                node.left = left
            right_val = input.pop(0)
            if right_val:
                right = TreeNode(right_val)
                nodes.append(right)
                node.right = right
    else:
        root = None

    solution = Solution()
    print solution.binaryTreePaths(root)
