# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# NOTE: TIME LIMIT EXCEEDED
# Last executed input: [37,-34,-48,null,-100,-100,48,null,null,null,null,-54,null,-71,-22,null,null,null,8]
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        previous_node = {}
        next_node = {}
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node is None:
                continue
            if node.left is not None:
                val1 = node.left.val
                val2 = node.val
                if val1 in next_node:
                    tmp = next_node[val1]
                    next_node[val2] = tmp
                    previous_node[tmp] = val2
                    next_node[val1] = val2
                    previous_node[val2] = val1
                elif val2 in previous_node:
                    tmp = previous_node[val2]
                    next_node[tmp] = val1
                    previous_node[val1] = tmp
                    next_node[val1] = val2
                    previous_node[val2] = val1
                else:
                    next_node[val1] = val2
                    previous_node[val2] = val1
                queue.append(node.left)
            if node.right is not None:
                val1 = node.val
                val2 = node.right.val
                if val1 in next_node:
                    tmp = next_node[val1]
                    next_node[val2] = tmp
                    previous_node[tmp] = val2
                    next_node[val1] = val2
                    previous_node[val2] = val1
                elif val2 in previous_node:
                    tmp = previous_node[val2]
                    next_node[tmp] = val1
                    previous_node[val1] = tmp
                    next_node[val1] = val2
                    previous_node[val2] = val1
                else:
                    next_node[val1] = val2
                    previous_node[val2] = val1
                queue.append(node.right)
            if node.val not in next_node and node.left is None and node.right is None:
                next_node[node.val] = None

        start = list(set(next_node.keys()) - set(next_node.values()))
        if start:
            print start
            print next_node
            print previous_node
            start = start[0]
            result = [start]
            while start in next_node and next_node[start] is not None:
                result.append(next_node[start])
                start = next_node[start]
            return result
        else:
            return []


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.right.left = TreeNode(7)
    root.right.right.left.left = TreeNode(8)
    root.right.right.left.right = TreeNode(9)
    root.right.right.left.right.right = TreeNode(10)
    solution = Solution()
    print solution.inorderTraversal(root)
