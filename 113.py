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
        self.res = []
        self.do(root, sum, [])
        return self.res

    def do(self, root, sum, path):
        if root is None:
            return
        sum -= root.val
        path += [root.val]
        if root.left is None and root.right is None and sum == 0:
            self.res.append(path[:])
        if root.left:
            self.do(root.left, sum, path)
        if root.right:
            self.do(root.right, sum, path)
        del path[-1]

from common import *
# data = ([5,4,8,11,'#',13,4,7,2,'#','#','#','#',5,1], 22)
data = ([-2, '#', -3], -5)
print Solution().pathSum(make_tree(data[0]), data[1])