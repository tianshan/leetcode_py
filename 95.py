# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        left = [[TreeNode(1)]
        for i in xrange(2, n):
            for j in xrange(0, n):
                for 

class Solution2(object):
    def generateTrees(self, n):
        def node(val, left, right):
            node = TreeNode(val)
            node.left = left
            node.right = right
            return node
        def trees(first, last):
            return [node(root, left, right)
                    for root in range(first, last+1)
                    for left in trees(first, root-1)
                    for right in trees(root+1, last)] or [None]
        return trees(1, n)

from common import *
for r in Solution2().generateTrees(3):
    print_tree(r)