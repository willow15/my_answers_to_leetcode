# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = list()
        node_stack = [root]
        value_stack = [sum - root.val]
        visited_stack = list()
        while node_stack:
            node = node_stack[-1]
            if len(visited_stack) < len(node_stack):
                if node.left is not None:
                    node_stack.append(node.left)
                    value_stack.append(value_stack[-1] - node.left.val)
                    visited_stack.append('left')
                elif node.right is not None:
                    node_stack.append(node.right)
                    value_stack.append(value_stack[-1] - node.right.val)
                    visited_stack.append('right')
                else:
                    if value_stack[-1] == 0:
                        result.append([n.val for n in node_stack])
                    node_stack.pop(-1)
                    value_stack.pop(-1)
            else:
                if visited_stack[-1] == 'left':
                    if node.right is not None:
                        node_stack.append(node.right)
                        value_stack.append(value_stack[-1] - node.right.val)
                        visited_stack[-1] = 'right'
                    else:
                        node_stack.pop(-1)
                        value_stack.pop(-1)
                        visited_stack.pop(-1)
                else:
                    node_stack.pop(-1)
                    value_stack.pop(-1)
                    visited_stack.pop(-1)

        return result


if __name__ == '__main__':
    input = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
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

    sum = 22
    solution = Solution()
    print solution.pathSum(root, sum)
