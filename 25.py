# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if head==None:
            return None
        last = ListNode(0)
        last.next = head
        temp = last
        while temp.next!=None:
            temp = self.reverse(temp, k)
        return last.next

    def reverse(self, last, k):
        start = last.next
        stop = last.next
        while k>1 and stop.next!=None:
            last.next = stop.next
            stop.next = stop.next.next
            last.next.next = start
            start = last.next
            k -= 1
        if k>1:
            start = last.next
            stop = last.next
            while stop.next!=None:
                last.next = stop.next
                stop.next = stop.next.next
                last.next.next = start
                start = last.next
        return stop

    def printNum(self, l):
        while l != None:
            print l.val,
            l = l.next
        print ''

    def getNum(self, l):
        if len(l)==0:
            return None
        head = ListNode(l[0])
        tmphead = head
        for i in range(1, len(l)):
            newL = ListNode(l[i])
            tmphead.next = newL
            tmphead = newL
        return head

if __name__=='__main__':
    s = Solution()
    data = [([1,2,3,4,5],1),([1,2,3,4,5],2),([1,2,3,4,5],3),([1,2,3,4,5],4)]
    for d in data:
        head = s.getNum(d[0])
        head = s.reverseKGroup(head, d[1])
        s.printNum(head)
