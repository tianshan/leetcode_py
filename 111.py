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
        if root==None: return 0
        hl = self.minDepth(root.left) + 1
        hr = self.minDepth(root.right) + 1
        if hl == 1: return hr 
        if hr == 1: return hl
        return hl if hl<hr else hr


root = TreeNode(1)
print Solution().minDepth(root)
root.left = TreeNode(2)
print Solution().minDepth(root)
root.left.left = TreeNode(3)
print Solution().minDepth(root)
root.right = TreeNode(3)
print Solution().minDepth(root)