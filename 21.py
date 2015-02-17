# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        s = ListNode(0)
        temp = s
        while l1!=None or l2!=None:
            if l1==None or (l1!=None and l2!=None and l2.val<l1.val):
                temp.next = l2
                temp = l2
                l2 = l2.next
            else:
                temp.next = l1
                temp = l1
                l1 = l1.next
        temp.next = None
        return s.next

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
    data = [([1,3,5],[2,4]), ([],[]), ([1,2,3],[])]
    for d in data:
        l1 = s.getNum(d[0])
        l2 = s.getNum(d[1])
        head = s.mergeTwoLists(l1,l2)
        print d,
        s.printNum(head)