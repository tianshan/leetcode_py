 # Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        i, left = 1, ListNode(0)
        left.next = head
        head = left
        while i<m: 
            left = left.next
            i += 1
        # print left.val
        p = left.next 
        while i<n:
            tmp = left.next
            left.next = p.next
            p.next = p.next.next
            left.next.next = tmp
            i += 1
        return head.next


from common import *
# data = ([1,2,3,4,5],2,4)
data = ([3,5],1,2)
root = make_list(data[0])
print_list(Solution().reverseBetween(root, data[1], data[2]))