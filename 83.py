# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        last = None
        last_node = ListNode(0)
        temp = head
        while temp!=None:
            if last!=None and temp.val==last:
                temp = temp.next
            else:
                last = temp.val
                last_node.next = temp
                last_node = temp
                temp = temp.next
        last_node.next = None
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
data = [[1,1,2], [1,1,2,3,3], [], [1],[1,1,1]]
for d in data:
    head = s.getNum(d)
    head = s.deleteDuplicates(head)
    s.printNum(head)
