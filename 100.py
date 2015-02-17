# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        return self.check(p, q)

    def check(self, p, q):
        if p==None and q==None:
            return True
        if p!=None and q!=None and p.val==q.val:
            ans = self.check(p.left, q.left)
            ans = ans and self.check(p.right, q.right)
            return ans 
        return False

class Solution2:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        queue = [(p,q)]
        while len(queue)>0:
            t = queue.pop(0)
            if t[0]==None and t[1]==None:
                continue 
            if t[0]!=None and t[1]!=None and t[0].val==t[1].val:
                queue.append((t[0].left, t[1].left))
                queue.append((t[0].right, t[1].right))
            else:
                return False
        return True

s = Solution()
