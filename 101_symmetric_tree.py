# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        left_children = [root.left]
        right_children = [root.right]
        while sum(child is not None for child in left_children) > 0 or sum(child is not None for child in right_children) > 0:
            children_num = len(left_children)
            while children_num > 0:
                left_child = left_children.pop(0)
                right_child = right_children.pop(0)
                if left_child is not None and right_child is not None:
                    if left_child.val != right_child.val:
                        return False
                    left_children.extend([left_child.left, left_child.right])
                    right_children.extend([right_child.right, right_child.left])
                elif (left_child is None and right_child is not None) or (left_child is not None and right_child is None):
                    return False
                children_num -= 1

        return True


if __name__ == '__main__':
    inputs = [1, 2, 2, 3, 4, 4, 3]
    root = TreeNode(inputs[0])
    nodes = [root]
    index = 1
    max_index = len(inputs) - 1
    while nodes:
        node = nodes.pop(0)
        node.left = TreeNode(inputs[index])
        nodes.append(node.left)
        node.right = TreeNode(inputs[index + 1])
        nodes.append(node.right)
        index += 2
        if index > max_index:
            break
    solution = Solution()
    print solution.isSymmetric(root)
