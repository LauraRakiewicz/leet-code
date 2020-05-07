# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        output = []
        if root:
            output.append(root.val)
            output += self.preorderTraversal(root.left)
            output += self.preorderTraversal(root.right)
        return output