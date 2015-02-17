# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        ans = []
        queue = [root]
        i,j = 0,1
        while root:
            temp = []
            while i<j:
                temp.append(queue[i].val)
                if queue[i].left:
                    queue.append(queue[i].left)
                if queue[i].right:
                    queue.append(queue[i].right)
                i += 1
            j = len(queue)
            if len(temp)>0:
                ans.append(temp)
            else:
                return ans
        return ans


def make_tree(data):
    n = len(data)
    if n==0:
        return None
    queue = [TreeNode(data[0])]
    i = 0
    j = 1
    while j<n:
        while i<j:
            if i*2+1<n and data[i*2+1]!='#':
                queue[i].left = TreeNode(data[i*2+1])
            if i*2+2<n and data[i*2+2]!='#':
                queue[i].right = TreeNode(data[i*2+2])
            if queue[i]:
                queue.append(queue[i].left)
                queue.append(queue[i].right)
            else:
                queue += [None, None]
            i += 1
        j = j*2+1
    return queue[0]

s = Solution()
data = [[3,9,20,'#','#',15,7], []]
for d in data:
    print s.levelOrder(make_tree(d))