# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        Given the root of a binary tree, return the preorder traversal of its nodes' values.

        Algorithm:
        1. Traverse tree for left and right nodes in pre order, recursively
        2. Append node values to node list
        3. Return node list
        """
        return self.answer([], root)

    def answer(self, nodes, root):
        if root is None:
            # this node is null, so exit this function and go to its parent node
            return

        # pre-order traversal
        nodes.append(root.val)
        self.answer(nodes, root.left)
        # in-order traversal
        # nodes.append(root.val)
        self.answer(nodes, root.right)
        # post-order traversal
        # nodes.append(root.val)

        return nodes
