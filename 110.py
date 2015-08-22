# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.high(root) == -1:
            return False
        return True

    def high(self, root):
        if root == None: return 0
        hl = self.high(root.left) + 1
        hr = self.high(root.right) + 1
        if hl == 0 or hr == 0 or abs(hl-hr)>1:
            return -1
        return hl if hl>hr else hr


root = TreeNode(1)
print Solution().isBalanced(root)
root.left = TreeNode(2)
print Solution().isBalanced(root)
root.left.left = TreeNode(3)
print Solution().isBalanced(root)
root.right = TreeNode(3)
print Solution().isBalanced(root)