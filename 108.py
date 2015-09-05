# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.nums = nums
        return self.do(0, len(nums)-1)

    def do(self, l, r):
        if l > r: return None
        mid = (l+r) / 2
        root = TreeNode(self.nums[mid])
        root.left = self.do(l, mid-1)
        root.right = self.do(mid+1, r)
        return root

from common import *
print_tree(Solution().sortedArrayToBST(range(3)))
print_tree3(Solution().sortedArrayToBST(range(3)))