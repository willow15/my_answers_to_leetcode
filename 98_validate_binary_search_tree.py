# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_bst(root, None, None)

    def is_bst(self, root, left_max, right_min):
        # compare with its direct parent
        if root is None:
            return True
        if left_max is not None and root.val <= left_max:
            return False
        if right_min is not None and root.val >= right_min:
            return False
        return self.is_bst(root.left, left_max, root.val) and self.is_bst(root.right, root.val, right_min)


if __name__ == '__main__':
    # input = [5, 1, 4, None, None, 3, 6]
    input = [2, 1, 3]
    if input:
        root = TreeNode(input.pop(0))
        nodes = [root]
        while input:
            node = nodes.pop(0)
            left_val = input.pop(0)
            if left_val:
                left = TreeNode(left_val)
                nodes.append(left)
            right_val = input.pop(0)
            if right_val:
                right = TreeNode(right_val)
                nodes.append(right)
            node.left = left
            node.right = right
    else:
        root = None

    solution = Solution()
    print solution.isValidBST(root)
