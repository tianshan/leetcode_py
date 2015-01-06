# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if n==0:
            return head
        temp1 = head
        temp2 = head
        last = None
        for i in range(n):
            temp1 = temp1.next
        while temp1!=None:
            last = temp2
            temp1 = temp1.next
            temp2 = temp2.next
        if last==None:
            return temp2.next
        else:
            last.next = temp2.next
        return head

    def getNum(self, l):
        head = ListNode(l[0])
        tmphead = head
        for i in range(1, len(l)):
            newL = ListNode(l[i])
            tmphead.next = newL
            tmphead = newL
        return head

    def printNum(self, l):
        while l != None:
            print l.val,
            l = l.next
        print ''

if __name__=='__main__':
    s = Solution()
    data = [([1,2,3,4,5],2), (([1,2,3,4,5],0))]
    for d in data:
        head = s.getNum(d[0])
        head = s.removeNthFromEnd(head, d[1])
        s.printNum(head)


