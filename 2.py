# import numpy
# import theano.tensor as T
# from theano import *

# rnd = numpy.random
# feats = 10

# D = (rnd.randn(10, 2), rnd.randint(size=10,low=0,high=2))

# from theano import pp
# x = T.dscalar('x')
# y = x**2
# gy = T.grad(y,x)
# f =function([x],gy)

# print T.arange(10)

# b=1
# prim_ploy=023
# nwm1=(1<<4)-1
# nw=1<<4

# log_table = [nwm1]*nw 
# ilog_table = [0]*nw*3

# for j in range(nwm1):
#     log_table[b] = j
#     ilog_table[j] = b
#     b = b<<1
#     if b&nw:
#         b = (b^prim_ploy) & nwm1

# for j in range(len(log_table)):
#     print j,log_table[j],ilog_table[j]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        r = 0
        head = ListNode(0)
        tmphead = head
        while l1!=None or l2!=None or r!=0:
            if l1!=None:
                r += l1.val
                l1 = l1.next
            if l2!=None:
                r += l2.val
                l2 = l2.next
            newL = ListNode(r%10)
            tmphead.next = newL
            tmphead = newL
            r /= 10
        return head.next
    
    def printNum(self, l):
        while l != None:
            print l.val,
            l = l.next
        print ''

    def getNum(self, l):
        head = ListNode(l[0])
        tmphead = head
        for i in range(1, len(l)):
            newL = ListNode(l[i])
            tmphead.next = newL
            tmphead = newL
        return head


if __name__=='__main__':

    ans = Solution()
    l1 = ans.getNum([0,0,0,1])
    l2 = ans.getNum([2])
    ans.printNum(l1)
    ans.printNum(l2)
    re = ans.addTwoNumbers(l1, l2)
    ans.printNum(re)
    # ans.addTwoNumbers()