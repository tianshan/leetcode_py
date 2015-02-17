# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        self.queue = [root]
        i = 0
        j = 1
        isNext = root
        while isNext:
            isNext = False
            while i<j:
                if self.queue[i]:
                    self.queue.append(self.queue[i].left)
                    self.queue.append(self.queue[i].right)
                    isNext = True
                i += 1
            j = len(self.queue)
            if not self.check(i, j-1):
                return False
        return True

    def check(self, i, j):
        while i<j:
            if (not self.queue[i] and not self.queue[j]) or \
                (self.queue[i] and self.queue[j] and \
                    self.queue[i].val==self.queue[j].val):
                i += 1 
                j -= 1
            else:
                return False
        return True

class Solution2:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        def isSym(L,R):
            if not L and not R: return True
            if L and R and L.val == R.val: 
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False
        return isSym(root, root)

class Solution3:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        left = [root]
        right = [root]
        i = 0
        j = 1 
        isNext = root
        while isNext:
            isNext = False
            while i<j:
                if not left[i] and not right[i]:
                    i += 1 
                    continue
                elif left[i] and right[i] and left[i].val==right[i].val:
                    left += [left[i].left, left[i].right]
                    right += [right[i].right, right[i].left]
                    isNext = True
                else:
                    return False
                i += 1 
            j = len(left)
        return True


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
s2 = Solution3()

data = ['1223443', '122#3#3', '']
# for d in data:
#     print s.isSymmetric(make_tree(d))

import time

start = time.clock()
for d in data:
    s.isSymmetric(make_tree(d))
print time.clock()-start

start = time.clock()
for d in data:
    s2.isSymmetric(make_tree(d))
print time.clock()-start