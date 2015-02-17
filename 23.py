# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#O(nlogk)
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        while len(lists)>1:
            temp = []
            for i in range(0, len(lists), 2):
                if i+1==len(lists):
                    temp.append(lists[i])
                else:
                    l = self.mergeTwoLists(lists[i], lists[i+1])
                    temp.append(l)
            lists = temp
        if len(lists)==0:
            return None
        return lists[0]

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
    data = [([1,3,5],[2,4],[-1,2,3],[-1,2,3],[]), ([],[]), ([1,2,3],[])]
    for d in data:
        temp = []
        for l in d:
            temp.append(s.getNum(l))
        head = s.mergeKLists(temp)
        print d,
        s.printNum(head)