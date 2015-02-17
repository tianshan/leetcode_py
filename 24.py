# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head==None or head.next == None:
            return head
        last = ListNode(0)
        last.next = head
        head = head.next
        while last.next!=None and last.next.next!=None:
            temp = last.next
            last.next = temp.next
            temp.next = temp.next.next
            last.next.next = temp
            last = temp
        return head

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
    s = Solution()
    data = [[1,2,3,4],[1,2,3],[1,2],[1], [1,2,3,4,5],[1,2,3,4,5,6]]
    for d in data:
        head = s.getNum(d)
        head = s.swapPairs(head)
        print d
        s.printNum(head)