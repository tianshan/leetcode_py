# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        now = head
        left, right = ListNode(0), ListNode(0)
        r_left, r_right = left, right
        while now:
            if now.val >= x:
                right.next = now
                right = now
            else:
                left.next = now
                left = now
            now = now.next
        left.next = r_right.next
        right.next = None
        return r_left.next


from common import *
data = ([1,4,3,2,5,2],3)
root = make_list(data[0])
# print_list(root)
print_list(Solution().partition(root, data[1]))