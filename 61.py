# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head==None:
            return None
        last = ListNode(0)
        last.next = head
        head1 = last
        head2 = last
        n = 0
        for i in range(k):
            head1 = head1.next
            if head1==None:
                n = i
                break
        if n>0:
            k = k%n
            head1 = last
            for i in range(k):
                head1 = head1.next
        if head1.next==None:
            return head
        while head1.next!=None:
            head1 = head1.next
            head2 = head2.next
        head1.next = head
        head = head2.next
        head2.next = None
        return head

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

s = Solution()
for k in range(7):
    head = s.getNum([1,2,3,4,5])
    head = s.rotateRight(head, k)
    print k,'\t',
    s.printNum(head)