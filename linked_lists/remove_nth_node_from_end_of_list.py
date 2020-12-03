# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode

        Given the head of a linked list, remove the nth node from the end of the list and return its head.

        1. Find the length of linked list
        2. Find the index of the node to be deleted by doing length-n
        3. Link previous node of delete_node to delete_node.next
        """
        tmp = head
        length = 0

        while(tmp is not None):
            tmp = tmp.next
            length+=1

        length = length - n
        prev = None
        current = head

        while(length!=0):
            prev = current
            current = current.next
            length-=1

        if prev is None:
            return head.next
        else:
            prev.next = current.next
            current = None
            return head
