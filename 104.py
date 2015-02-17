# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

class Solution2:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        queue = [root]
        i,j,h = 0,1,0
        while root:
            while i<j:
                if queue[i].left:
                    queue.append(queue[i].left)
                if queue[i].right:
                    queue.append(queue[i].right)
                i += 1
            j,h = len(queue),h+1
            if j<=i:
                return h
        return h

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
s2 = Solution2()

data = [[3,9,20,'#','#',15,7], []]
for d in data:
    print s2.maxDepth(make_tree(d)) 


# import time 

# start = time.clock()
# for d in data:
#     s.maxDepth(make_tree(d))
# print time.clock()-start

# start = time.clock()
# for d in data:
#     s2.maxDepth(make_tree(d))
# print time.clock()-start