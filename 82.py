# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        last_node = ListNode(0)
        last_node.next = head
        last = last_node
        temp = head
        while temp!=None:
            if temp.next==None or temp.val!=temp.next.val:
                last.next = temp
                last = temp
                temp = temp.next
            else:
                while temp!=None and temp.val==last.next.val:
                    temp = temp.next
                last.next = temp
        return last_node.next


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
data = [[1,2,3,3,4,4,5],[1,1],[1,1,2],[],[1,1,1,2,3]]
for d in data:
    head = s.getNum(d)
    head = s.deleteDuplicates(head)
    s.printNum(head)