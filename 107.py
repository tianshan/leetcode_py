# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, nodes = [], [root]
        while len(nodes)>0:
            tmp, next = [], []
            for n in nodes:
                if n is None: continue
                tmp.append(n.val)
                if n.left is not None:
                    next.append(n.left)
                if n.right is not None:
                    next.append(n.right)
            nodes = next
            if len(tmp) != 0:
                res = [tmp] + res
        return res


from common import *

data = [[3,9,20,'#','#',15,7], [], [1,2]]
for d in data:
    print Solution().levelOrderBottom(make_tree(d))

        